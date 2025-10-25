#!/usr/bin/env python3
"""
Script to generate eLearning.html from content/content.md
"""

import re
import sys

def parse_markdown_to_html(md_content):
    """Parse markdown content and convert to HTML chapters"""

    # Split content by main headers
    sections = re.split(r'^## ', md_content, flags=re.MULTILINE)

    chapters = []
    chapter_titles = []

    for section in sections[1:]:  # Skip first empty section
        if not section.strip():
            continue

        # Get chapter title (first line)
        lines = section.split('\n', 1)
        title = lines[0].strip()
        content = lines[1] if len(lines) > 1 else ""

        # Skip metadata sections
        if title.startswith('Hinweise zur Nutzung') or title.startswith('Ende der Content-Datei'):
            continue

        chapters.append({
            'title': title,
            'content': content
        })
        chapter_titles.append(title)

    return chapters, chapter_titles

def convert_md_section_to_html(md_text):
    """Convert markdown section to HTML"""
    html = ""
    lines = md_text.split('\n')

    in_info_box = False
    in_accordion = False
    in_accordion_item = False
    in_quiz = False
    in_table = False
    in_code_block = False
    current_list = []
    accordion_items = []
    quiz_questions = []
    table_rows = []

    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        # Handle code blocks
        if line.startswith('```'):
            if not in_code_block:
                in_code_block = True
                html += '<div class="code-example">'
                i += 1
                continue
            else:
                in_code_block = False
                html += '</div>\n'
                i += 1
                continue

        if in_code_block:
            html += line + '\n'
            i += 1
            continue

        # Handle INFO-BOX
        if line.startswith('**INFO-BOX'):
            # Close any previous list
            if current_list:
                html += '</ul>\n'
                current_list = []

            # Determine box type
            if 'WARNUNG' in line:
                box_class = 'warning'
            elif 'SUCCESS' in line:
                box_class = 'success'
            else:
                box_class = ''

            # Extract title
            title_match = re.search(r'\*\*INFO-BOX[^:]*:\s*(.+?)\*\*', line)
            title = title_match.group(1) if title_match else "Information"

            html += f'<div class="info-box{" " + box_class if box_class else ""}">\n'
            html += f'    <h4>{title}</h4>\n'
            in_info_box = True
            i += 1
            continue

        # Close INFO-BOX when we hit a blank line followed by non-list content
        if in_info_box and line == '' and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if next_line and not next_line.startswith('*') and not next_line.startswith('-'):
                if current_list:
                    html += '</ul>\n'
                    current_list = []
                html += '</div>\n\n'
                in_info_box = False

        # Handle ACCORDION
        if line.startswith('**ACCORDION:**') or line == '**ACCORDION:**':
            if current_list:
                html += '</ul>\n'
                current_list = []
            in_accordion = True
            accordion_items = []
            i += 1
            continue

        # Handle accordion items (bold headers within accordion)
        if in_accordion and line.startswith('**') and line.endswith('**') and len(line) > 4:
            # This is an accordion header
            header_title = line.strip('*').strip()

            # Find content until next header or end of accordion
            content_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i].rstrip()
                if next_line.startswith('**') and next_line.endswith('**') and len(next_line) > 4:
                    # Next accordion item
                    break
                if next_line.startswith('###') or next_line.startswith('**INFO-BOX') or next_line.startswith('**QUIZ'):
                    # End of accordion
                    in_accordion = False
                    break
                if next_line == '' and i + 1 < len(lines) and lines[i + 1].startswith('###'):
                    # Blank line before next section
                    in_accordion = False
                    break
                content_lines.append(next_line)
                i += 1

            # Convert content lines to HTML
            item_content = '\n'.join(content_lines).strip()
            item_html = convert_simple_md_to_html(item_content)

            accordion_items.append({
                'header': header_title,
                'content': item_html
            })

            # Check if accordion ended
            if not in_accordion:
                # Output all accordion items
                html += '<div class="accordion">\n'
                for item in accordion_items:
                    html += '    <div class="accordion-item" onclick="toggleAccordion(this)">\n'
                    html += f'        <div class="accordion-header">{item["header"]}</div>\n'
                    html += f'        <div class="accordion-content">\n{item["content"]}\n        </div>\n'
                    html += '    </div>\n'
                html += '</div>\n\n'
                accordion_items = []
            continue

        # Handle TABELLE (tables)
        if line.startswith('**TABELLE:'):
            if current_list:
                html += '</ul>\n'
                current_list = []
            title = line.replace('**TABELLE:', '').replace('**', '').strip()
            html += f'<h4>{title}</h4>\n'
            i += 1
            continue

        # Handle markdown tables
        if '|' in line and not in_table:
            if current_list:
                html += '</ul>\n'
                current_list = []
            in_table = True
            table_rows = []

        if in_table:
            if '|' in line:
                # Clean up table row
                cells = [cell.strip() for cell in line.split('|')]
                cells = [c for c in cells if c]  # Remove empty cells

                # Check if it's a separator row
                if all(re.match(r'^-+$', cell) or cell == '---' for cell in cells):
                    i += 1
                    continue

                table_rows.append(cells)
                i += 1
                continue
            else:
                # End of table
                if table_rows:
                    html += '<table class="comparison-table">\n'
                    # First row is header
                    if table_rows:
                        html += '    <tr>\n'
                        for cell in table_rows[0]:
                            html += f'        <th>{cell}</th>\n'
                        html += '    </tr>\n'
                    # Rest are data rows
                    for row in table_rows[1:]:
                        html += '    <tr>\n'
                        for cell in row:
                            html += f'        <td>{cell}</td>\n'
                        html += '    </tr>\n'
                    html += '</table>\n\n'
                in_table = False
                table_rows = []
                continue

        # Handle QUIZ sections
        if line.startswith('### QUIZ'):
            if current_list:
                html += '</ul>\n'
                current_list = []
            html += '<div class="quiz-section">\n    <h3>Quiz</h3>\n'
            in_quiz = True
            quiz_questions = []
            i += 1
            continue

        # Handle quiz questions
        if in_quiz and line.startswith('**Frage'):
            # Extract question
            question_match = re.match(r'\*\*Frage (\d+):\s*(.+?)\*\*', line)
            if question_match:
                q_num = question_match.group(1)
                q_text = question_match.group(2)

                # Find answers
                answers = []
                correct_answer = 'a'
                i += 1
                while i < len(lines):
                    ans_line = lines[i].strip()
                    if ans_line.startswith('*   '):
                        ans_line = ans_line[4:].strip()
                        # Check for correct answer marker
                        if '✓' in ans_line:
                            ans_line = ans_line.replace('✓', '').strip()
                            correct_answer = ans_line[0].lower()
                        answers.append(ans_line)
                        i += 1
                    elif ans_line.startswith('**Frage') or ans_line.startswith('---') or ans_line.startswith('##'):
                        break
                    elif ans_line == '':
                        i += 1
                        if i < len(lines) and (lines[i].startswith('**Frage') or lines[i].startswith('---') or lines[i].startswith('##')):
                            break
                    else:
                        i += 1

                quiz_questions.append({
                    'num': q_num,
                    'text': q_text,
                    'answers': answers,
                    'correct': correct_answer
                })

                # Check if quiz section ended
                if i < len(lines) and (lines[i].startswith('---') or lines[i].startswith('##')):
                    in_quiz = False
                    # Output all quiz questions
                    for q in quiz_questions:
                        html += f'    <div class="quiz-question">\n'
                        html += f'        <div class="question-text">Frage {q["num"]}: {q["text"]}</div>\n'
                        html += f'        <div class="answers">\n'
                        for ans in q["answers"]:
                            ans_value = ans[0].lower()
                            html += f'            <label><input type="radio" name="q_X_{q["num"]}" value="{ans_value}"> {ans}</label>\n'
                        html += f'        </div>\n'
                        html += f'        <button class="check-btn" onclick="checkAnswer(99, {q["num"]}, \'{q["correct"]}\')">Antwort überprüfen</button>\n'
                        html += f'        <div class="feedback" id="feedback99_{q["num"]}"></div>\n'
                        html += f'    </div>\n'
                    html += '</div>\n\n'
                    quiz_questions = []
                continue

        # Handle headings
        if line.startswith('### '):
            if current_list:
                html += '</ul>\n'
                current_list = []
            if in_info_box:
                html += '</div>\n\n'
                in_info_box = False
            heading = line[4:].strip()
            html += f'<h3>{heading}</h3>\n'
            i += 1
            continue

        if line.startswith('#### '):
            if current_list:
                html += '</ul>\n'
                current_list = []
            heading = line[5:].strip()
            html += f'<h4>{heading}</h4>\n'
            i += 1
            continue

        # Handle lists
        if line.startswith('*   ') or line.startswith('- '):
            item = line[4:].strip() if line.startswith('*   ') else line[2:].strip()
            item = convert_inline_md(item)
            if not current_list:
                html += '<ul>\n'
            current_list.append(item)
            html += f'    <li>{item}</li>\n'
            i += 1
            continue

        # Close list if we hit non-list content
        if current_list and line and not line.startswith('*') and not line.startswith('-'):
            html += '</ul>\n'
            current_list = []
            if in_info_box and not line.startswith('<'):
                html += '</div>\n\n'
                in_info_box = False

        # Handle paragraphs
        if line.strip() and not line.startswith('#'):
            para = convert_inline_md(line)
            # Check if it's emphasis
            if line.startswith('*') and line.endswith('*') and not line.startswith('**'):
                html += f'<p><em>{para[1:-1]}</em></p>\n'
            else:
                html += f'<p>{para}</p>\n'
        elif line.strip() == '':
            html += '\n'

        i += 1

    # Close any remaining open tags
    if current_list:
        html += '</ul>\n'
    if in_info_box:
        html += '</div>\n'
    if in_quiz:
        html += '</div>\n'
    if in_table and table_rows:
        html += '<table class="comparison-table">\n'
        if table_rows:
            html += '    <tr>\n'
            for cell in table_rows[0]:
                html += f'        <th>{cell}</th>\n'
            html += '    </tr>\n'
        for row in table_rows[1:]:
            html += '    <tr>\n'
            for cell in row:
                html += f'        <td>{cell}</td>\n'
            html += '    </tr>\n'
        html += '</table>\n'

    return html

def convert_simple_md_to_html(md_text):
    """Convert simple markdown to HTML (for accordion content, etc.)"""
    html = ""
    lines = md_text.split('\n')
    in_list = False

    for line in lines:
        line = line.strip()
        if not line:
            if in_list:
                html += '</ul>\n'
                in_list = False
            continue

        # Lists
        if line.startswith('*   ') or line.startswith('- '):
            if not in_list:
                html += '<ul>\n'
                in_list = True
            item = line[4:] if line.startswith('*   ') else line[2:]
            html += f'    <li>{convert_inline_md(item)}</li>\n'
        else:
            if in_list:
                html += '</ul>\n'
                in_list = False
            html += f'<p>{convert_inline_md(line)}</p>\n'

    if in_list:
        html += '</ul>\n'

    return html

def convert_inline_md(text):
    """Convert inline markdown (bold, italic, etc.)"""
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text

def generate_full_html(chapters):
    """Generate the complete HTML file"""

    # ... (HTML template code here - truncated for brevity)
    # This would include the full HTML structure
    pass

# Main execution
if __name__ == '__main__':
    print("This script needs to be completed. Use Claude to finish it.")
