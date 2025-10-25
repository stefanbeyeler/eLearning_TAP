#!/usr/bin/env python3
"""
Konvertiert content.md zu HTML und aktualisiert eLearning.html

Dieses Skript:
1. Liest content.md und extrahiert alle Kapitel
2. Konvertiert Markdown zu HTML mit speziellen Konventionen
3. Aktualisiert die Kapitel-Inhalte in eLearning.html
4. Aktualisiert Quiz-Antworten im JavaScript
"""

import re
import sys
from typing import List, Dict, Tuple

class MarkdownToHTMLConverter:
    def __init__(self):
        self.quiz_counter = 0
        self.quiz_answers = {}  # Speichert Quiz-Antworten pro Kapitel

    def convert_chapter(self, markdown_text: str, chapter_num: int) -> str:
        """Konvertiert ein Kapitel von Markdown zu HTML"""
        html_parts = []
        lines = markdown_text.split('\n')
        i = 0

        self.quiz_counter = 0  # Reset für jedes Kapitel
        self.quiz_answers[chapter_num] = []

        while i < len(lines):
            line = lines[i].strip()  # Strip entfernt Einrückung und trailing whitespace

            # INFO-BOX Konvertierung
            if line.startswith('**INFO-BOX'):
                html, new_i = self._convert_info_box(lines, i)
                html_parts.append(html)
                i = new_i
                continue

            # ACCORDION Konvertierung
            if line.startswith('**ACCORDION:**'):
                html, new_i = self._convert_accordion(lines, i)
                html_parts.append(html)
                i = new_i
                continue

            # TABELLE Konvertierung
            if line.startswith('**TABELLE:**'):
                html, new_i = self._convert_table(lines, i)
                html_parts.append(html)
                i = new_i
                continue

            # QUIZ Konvertierung
            if line.startswith('### QUIZ') or line.startswith('## QUIZ'):
                html, new_i = self._convert_quiz(lines, i, chapter_num)
                html_parts.append(html)
                i = new_i
                continue

            # Überschriften
            if line.startswith('### '):
                html_parts.append(f'<h3>{line[4:]}</h3>')
                i += 1
                continue

            if line.startswith('## ') and not line.startswith('## KAPITEL'):
                html_parts.append(f'<h2>{line[3:]}</h2>')
                i += 1
                continue

            # Listen (mit - oder * beginnend)
            if line.startswith('- ') or line.startswith('* '):
                html, new_i = self._convert_list(lines, i)
                html_parts.append(html)
                i = new_i
                continue

            # Nummerierte Listen
            if re.match(r'^\d+\.\s', line):
                html, new_i = self._convert_numbered_list(lines, i)
                html_parts.append(html)
                i = new_i
                continue

            # Fett formatierter Text (aber nicht INFO-BOX, ACCORDION, etc.)
            if line.startswith('**') and not any(line.startswith(x) for x in ['**INFO-BOX', '**ACCORDION', '**TABELLE', '**Frage']):
                # Extrahiere den fetten Text
                match = re.match(r'\*\*(.*?)\*\*(.*)', line)
                if match:
                    html_parts.append(f'<p><strong>{match.group(1)}</strong>{match.group(2)}</p>')
                    i += 1
                    continue

            # Horizontale Linie (--- in Markdown)
            if line == '---':
                # Ignoriere horizontale Linien (werden nicht benötigt)
                i += 1
                continue

            # Normaler Paragraph
            if line and not line.startswith('#'):
                # Konvertiere Inline-Markdown
                line = self._convert_inline_markdown(line)
                html_parts.append(f'<p>{line}</p>')
            elif line == '':
                # Leere Zeile ignorieren, aber nur wenn es nicht mehrere hintereinander sind
                pass

            i += 1

        return '\n'.join(html_parts)

    def _convert_inline_markdown(self, text: str) -> str:
        """Konvertiert Inline-Markdown wie **bold**, *italic*, etc."""
        # Fetter Text
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        # Kursiver Text
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        # Code
        text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
        return text

    def _convert_info_box(self, lines: List[str], start_i: int) -> Tuple[str, int]:
        """Konvertiert INFO-BOX zu HTML"""
        line = lines[start_i].strip()

        # Typ bestimmen
        box_class = 'info-box'
        if 'WARNUNG:' in line:
            box_class = 'info-box warning'
            title = line.replace('**INFO-BOX WARNUNG:', '').replace('**', '').strip()
        elif 'SUCCESS:' in line:
            box_class = 'info-box success'
            title = line.replace('**INFO-BOX SUCCESS:', '').replace('**', '').strip()
        else:
            title = line.replace('**INFO-BOX:', '').replace('**', '').strip()

        html = f'<div class="{box_class}">\n'
        if title:
            html += f'    <h4>{title}</h4>\n'

        i = start_i + 1
        content_lines = []

        # Skip initial empty lines
        while i < len(lines) and not lines[i].strip():
            i += 1

        # Sammle Content bis zur nächsten leeren Zeile oder nächsten Markdown-Element
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                # Bei leerer Zeile: prüfe ob danach noch Content kommt
                if i + 1 < len(lines) and lines[i + 1].strip():
                    i += 1
                    continue
                else:
                    i += 1
                    break
            if line.startswith('**') and not line.startswith('**-'):
                break
            if line.startswith('###') or line.startswith('##'):
                break
            content_lines.append(line)
            i += 1

        # Konvertiere Content (gemischter Content: Paragraphen + Listen)
        if content_lines:
            i = 0
            while i < len(content_lines):
                line = content_lines[i]

                # Prüfe ob es eine Liste ist (mit - oder * beginnend)
                if line.startswith('- ') or line.startswith('* '):
                    # Sammle alle aufeinanderfolgenden Listen-Einträge
                    html += '    <ul>\n'
                    while i < len(content_lines) and (content_lines[i].startswith('- ') or content_lines[i].startswith('* ')):
                        item_text = content_lines[i][2:].strip()
                        item = self._convert_inline_markdown(item_text)
                        html += f'        <li>{item}</li>\n'
                        i += 1
                    html += '    </ul>\n'
                else:
                    # Normaler Paragraph
                    line = self._convert_inline_markdown(line)
                    html += f'    <p>{line}</p>\n'
                    i += 1

        html += '</div>'
        return html, i

    def _convert_accordion(self, lines: List[str], start_i: int) -> Tuple[str, int]:
        """Konvertiert ACCORDION zu HTML"""
        html_parts = []
        i = start_i + 1  # Skip **ACCORDION:**

        # Skip empty lines
        while i < len(lines) and not lines[i].strip():
            i += 1

        current_header = None
        current_content = []

        while i < len(lines):
            line = lines[i].strip()

            # Ende des Accordions
            if not line and current_header is None:
                i += 1
                continue
            if line.startswith('###') or line.startswith('## ') and not current_header:
                break
            if line.startswith('**INFO-BOX') or line.startswith('**TABELLE') or line.startswith('**QUIZ'):
                break

            # Neuer Accordion-Header (fett formatiert)
            if line.startswith('**') and line.endswith('**') and len(line) > 4:
                # Speichere vorherigen Accordion
                if current_header:
                    html_parts.append(self._create_accordion_item(current_header, current_content))
                    current_content = []

                current_header = line.strip('*')
                i += 1
                continue

            # Content sammeln
            if current_header and line:
                current_content.append(line)

            i += 1

        # Letzter Accordion
        if current_header:
            html_parts.append(self._create_accordion_item(current_header, current_content))

        return '\n'.join(html_parts), i

    def _create_accordion_item(self, header: str, content_lines: List[str]) -> str:
        """Erstellt ein einzelnes Accordion-Element"""
        html = '<div class="accordion" onclick="toggleAccordion(this)">\n'
        html += f'    <div class="accordion-header">{header}</div>\n'
        html += '    <div class="accordion-content">\n'

        i = 0
        while i < len(content_lines):
            line = content_lines[i]

            # Prüfe ob es eine Liste ist (mit - oder * beginnend)
            if line.startswith('- ') or line.startswith('* '):
                # Sammle alle aufeinanderfolgenden Listen-Einträge
                html += '        <ul>\n'
                while i < len(content_lines) and (content_lines[i].startswith('- ') or content_lines[i].startswith('* ')):
                    item_text = content_lines[i][2:].strip()
                    item = self._convert_inline_markdown(item_text)
                    html += f'            <li>{item}</li>\n'
                    i += 1
                html += '        </ul>\n'
            else:
                # Normaler Paragraph
                line = self._convert_inline_markdown(line)
                html += f'        <p>{line}</p>\n'
                i += 1

        html += '    </div>\n'
        html += '</div>'
        return html

    def _convert_table(self, lines: List[str], start_i: int) -> Tuple[str, int]:
        """Konvertiert TABELLE zu HTML"""
        i = start_i + 1  # Skip **TABELLE:**

        # Skip empty lines
        while i < len(lines) and not lines[i].strip():
            i += 1

        # Sammle Tabellenzeilen
        table_lines = []
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                break
            if line.startswith('|'):
                table_lines.append(line)
            i += 1

        if not table_lines:
            return '', i

        # Konvertiere zu HTML
        html = '<table class="comparison-table">\n'

        # Header (erste Zeile)
        if table_lines:
            headers = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]
            html += '    <thead>\n        <tr>\n'
            for header in headers:
                html += f'            <th>{header}</th>\n'
            html += '        </tr>\n    </thead>\n'

        # Skip separator line (z.B. |---|---|)
        start_row = 2 if len(table_lines) > 1 and '---' in table_lines[1] else 1

        # Body
        html += '    <tbody>\n'
        for row_line in table_lines[start_row:]:
            cells = [cell.strip() for cell in row_line.split('|')[1:-1]]
            html += '        <tr>\n'
            for cell in cells:
                cell = self._convert_inline_markdown(cell)
                html += f'            <td>{cell}</td>\n'
            html += '        </tr>\n'
        html += '    </tbody>\n'

        html += '</table>'
        return html, i

    def _convert_quiz(self, lines: List[str], start_i: int, chapter_num: int) -> Tuple[str, int]:
        """Konvertiert QUIZ zu HTML"""
        html_parts = []
        i = start_i + 1  # Skip ### QUIZ

        # Skip empty lines
        while i < len(lines) and not lines[i].strip():
            i += 1

        question_count = 0
        while i < len(lines):
            line = lines[i].strip()

            # Ende des Quiz
            if line.startswith('###') or line.startswith('## KAPITEL'):
                break
            if line.startswith('**INFO-BOX') or line.startswith('**ACCORDION') or line.startswith('**TABELLE'):
                break
            if line == '---':  # Markdown separator
                break

            # Neue Frage
            if line.startswith('**Frage'):
                question_count += 1
                question_html, new_i, received_correct_answer = self._convert_quiz_question(lines, i, chapter_num)
                html_parts.append(question_html)
                if received_correct_answer:
                    self.quiz_answers[chapter_num].append(received_correct_answer)
                i = new_i
                continue

            i += 1

        return '\n'.join(html_parts), i

    def _convert_quiz_question(self, lines: List[str], start_i: int, chapter_num: int) -> Tuple[str, int, str]:
        """Konvertiert eine einzelne Quiz-Frage"""
        question_line = lines[start_i].strip()
        question_text = question_line.replace('**Frage', 'Frage').replace('**', '').strip()

        question_id = self.quiz_counter
        self.quiz_counter += 1

        html = '<div class="quiz-question">\n'
        html += f'    <p class="question-text">{question_text}</p>\n'
        html += '    <div class="answers">\n'

        i = start_i + 1
        answers = []
        correct_answer = None

        # Sammle Antworten
        answer_count = 0
        while i < len(lines):
            line = lines[i].strip()

            if not line:
                i += 1
                if answer_count > 0:  # Wenn wir schon Antworten haben, brechen wir bei leerer Zeile ab
                    break
                continue
            if line.startswith('**Frage'):
                break
            if line.startswith('###') or line.startswith('##'):
                break
            if line == '---':  # Markdown separator
                break

            # Antwort-Zeile (z.B. "* a) Text ✓" oder "- a) Text ✓")
            if line.startswith('* ') or line.startswith('- '):
                answer_count += 1
                answer_text = line[2:].strip()
                is_correct = '✓' in answer_text
                answer_text = answer_text.replace('✓', '').strip()

                # Extrahiere Buchstaben (a, b, c, d)
                match = re.match(r'^([a-d])\)\s*(.*)', answer_text)
                if match:
                    letter = match.group(1)
                    text = match.group(2)
                    answers.append((letter, text))

                    if is_correct:
                        correct_answer = letter

            i += 1

        # Erstelle HTML für Antworten
        for letter, text in answers:
            text = self._convert_inline_markdown(text)
            html += f'        <label><input type="radio" name="q{chapter_num}_{question_id}" value="{letter}"> {letter}) {text}</label>\n'

        html += '    </div>\n'
        html += f'    <button class="check-btn" onclick="checkAnswer({chapter_num}, {question_id}, \'{correct_answer}\')">Antwort prüfen</button>\n'
        html += f'    <div class="feedback" id="feedback{chapter_num}_{question_id}"></div>\n'
        html += '</div>'

        return html, i, correct_answer

    def _convert_list(self, lines: List[str], start_i: int) -> Tuple[str, int]:
        """Konvertiert eine ungeordnete Liste"""
        html = '<ul>\n'
        i = start_i

        while i < len(lines):
            line = lines[i].strip()
            # Unterstütze sowohl '- ' als auch '* ' für Listen
            if not (line.startswith('- ') or line.startswith('* ')):
                break

            # Entferne das Listen-Präfix und zusätzliche Whitespaces
            item_text = line[2:].strip()
            item = self._convert_inline_markdown(item_text)
            html += f'    <li>{item}</li>\n'
            i += 1

        html += '</ul>'
        return html, i

    def _convert_numbered_list(self, lines: List[str], start_i: int) -> Tuple[str, int]:
        """Konvertiert eine nummerierte Liste"""
        html = '<ol>\n'
        i = start_i

        while i < len(lines):
            line = lines[i].strip()
            if not re.match(r'^\d+\.\s', line):
                break

            item = re.sub(r'^\d+\.\s', '', line)
            item = self._convert_inline_markdown(item)
            html += f'    <li>{item}</li>\n'
            i += 1

        html += '</ol>'
        return html, i


def extract_chapters_from_content_md(filepath: str) -> Dict[int, Dict[str, str]]:
    """Extrahiert alle Kapitel aus content.md"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    chapters = {}

    # Finde alle Abschnitte (Vorwort, Kapitel 1-8, Abschlusstest)
    sections = []

    # 1. Vorwort
    vorwort_match = re.search(r'## Vorwort\n', content)
    if vorwort_match:
        sections.append((0, 'Vorwort', vorwort_match.end()))

    # 2. Kapitel 1-8
    chapter_pattern = r'## KAPITEL (\d+): (.+?)\n'
    for match in re.finditer(chapter_pattern, content):
        chapter_num = int(match.group(1))
        chapter_title = match.group(2)
        sections.append((chapter_num, chapter_title, match.end()))

    # 3. Abschlusstest
    abschluss_match = re.search(r'## Abschlusstest\n', content)
    if abschluss_match:
        sections.append((9, 'Abschlusstest', abschluss_match.end()))

    # Sortiere nach Position
    sections.sort(key=lambda x: x[2])

    # Extrahiere Content für jeden Abschnitt
    for i, (num, title, start_pos) in enumerate(sections):
        end_pos = sections[i + 1][2] if i + 1 < len(sections) else len(content)

        # Suche Start-Position rückwärts bis zum "##"
        section_start = content.rfind('##', 0, start_pos)

        # Extrahiere Content (ohne die "##" Überschrift selbst)
        chapter_content = content[start_pos:end_pos].strip()

        chapters[num] = {
            'title': title,
            'content': chapter_content
        }

    return chapters


def add_new_chapter(html_content: str, chapter_num: int, chapter_data: Dict[str, str], chapter_html: str) -> str:
    """Fügt ein neues Kapitel zur HTML-Datei hinzu"""

    # Erstelle das neue Kapitel-div
    if chapter_num == 0:
        title = f'<h2>{chapter_data["title"]}</h2>'  # Nur Titel ohne "Kapitel 0:"
    elif chapter_num == 9:
        title = f'<h2>{chapter_data["title"]}</h2>'
    else:
        title = f'<h2>Kapitel {chapter_num}: {chapter_data["title"]}</h2>'

    # Finde das letzte </div> vor dem <script> Tag
    script_pos = html_content.find('    <script>')
    if script_pos == -1:
        print(f"    ✗ Konnte <script> Tag nicht finden!")
        return html_content

    # Finde die Position des letzten chapter-divs
    # Suche rückwärts von script_pos nach </div>\n        </div>\n    </div>
    search_area = html_content[:script_pos]
    last_closing_divs = search_area.rfind('            </div>\n        </div>\n    </div>')

    if last_closing_divs == -1:
        print(f"    ✗ Konnte letzte chapter-closing-divs nicht finden!")
        return html_content

    # Finde die Position nach den schließenden divs
    insert_pos = last_closing_divs + len('            </div>\n        </div>\n    </div>\n')

    # Erstelle das neue Kapitel
    new_chapter = f'''
            <!-- Kapitel {chapter_num}: {chapter_data["title"]} -->
            <div class="chapter" id="chapter{chapter_num}">
                {title}

                {chapter_html}

                <div class="navigation-footer">
                    <button class="nav-footer-btn" onclick="showChapter({chapter_num - 1})">◄ Vorheriges Kapitel</button>
                    <button class="nav-footer-btn" onclick="resetTraining()">Schulung neu starten</button>
                </div>
            </div>
'''

    # Füge das neue Kapitel ein
    html_content = html_content[:insert_pos] + new_chapter + html_content[insert_pos:]

    return html_content


def update_elearning_html(html_filepath: str, chapters: Dict[int, Dict[str, str]], converter: MarkdownToHTMLConverter):
    """Aktualisiert eLearning.html mit den neuen Kapitel-Inhalten"""
    with open(html_filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Backup erstellen
    with open(html_filepath + '.backup', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Backup erstellt: {html_filepath}.backup")

    # Aktualisiere jedes Kapitel
    for chapter_num in sorted(chapters.keys()):
        chapter_data = chapters[chapter_num]
        chapter_id = f'chapter{chapter_num}'

        print(f"\nKonvertiere Kapitel {chapter_num}: {chapter_data['title']}...")

        # Konvertiere Markdown zu HTML
        chapter_html = converter.convert_chapter(chapter_data['content'], chapter_num)

        # Finde das chapter-div und ersetze den Inhalt zwischen <h2> und <div class="navigation-footer">
        # Pattern: <div class="chapter" id="chapterX"> ... <h2>...</h2> [CONTENT TO REPLACE] <div class="navigation-footer">

        # Suche nach dem chapter-div
        chapter_start_pattern = rf'<div class="chapter(?:\s+active)?" id="{chapter_id}">'
        chapter_start = re.search(chapter_start_pattern, html_content)

        if not chapter_start:
            print(f"  ℹ Kapitel {chapter_num} nicht gefunden in HTML - wird hinzugefügt")
            # Neues Kapitel hinzufügen
            html_content = add_new_chapter(html_content, chapter_num, chapter_data, chapter_html)
            print(f"  ✓ Kapitel {chapter_num} hinzugefügt")
            continue

        # Finde die Position nach dem <div class="chapter...">
        search_start = chapter_start.end()

        # Finde das <h2> Tag und die navigation-footer
        h2_pattern = rf'<h2>.*?</h2>'
        nav_footer_pattern = r'<div class="navigation-footer">'

        h2_match = re.search(h2_pattern, html_content[search_start:], re.DOTALL)
        nav_footer_match = re.search(nav_footer_pattern, html_content[search_start:])

        if not h2_match or not nav_footer_match:
            print(f"  ✗ Kapitel {chapter_num}: H2 oder Navigation-Footer nicht gefunden")
            continue

        # Berechne absolute Positionen
        h2_end = search_start + h2_match.end()
        nav_footer_start = search_start + nav_footer_match.start()

        # Erstelle neuen Content mit richtigem Titel
        if chapter_num == 0:
            new_title = f'<h2>{chapter_data["title"]}</h2>'  # Nur Titel ohne "Kapitel 0:"
        elif chapter_num == 9:
            new_title = f'<h2>{chapter_data["title"]}</h2>'
        else:
            new_title = f'<h2>Kapitel {chapter_num}: {chapter_data["title"]}</h2>'

        new_content = f'{new_title}\n\n                {chapter_html}\n\n                '

        # Ersetze den Content
        html_content = html_content[:search_start] + new_content + html_content[nav_footer_start:]

        print(f"  ✓ Kapitel {chapter_num} aktualisiert")

    # Schreibe aktualisierte HTML-Datei
    with open(html_filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✓ {html_filepath} wurde aktualisiert")

    # Ausgabe der Quiz-Antworten für JavaScript-Update
    print("\n" + "="*60)
    print("QUIZ-ANTWORTEN FÜR JAVASCRIPT:")
    print("="*60)
    for chapter_num in sorted(converter.quiz_answers.keys()):
        answers = converter.quiz_answers[chapter_num]
        print(f"Kapitel {chapter_num}: {answers}")


def main():
    content_md_path = '/Users/sbeyeler/GIT/eLearning_TAP/content.md'
    elearning_html_path = '/Users/sbeyeler/GIT/eLearning_TAP/eLearning.html'

    print("="*60)
    print("content.md → eLearning.html Konvertierung")
    print("="*60)

    # Extrahiere Kapitel aus content.md
    print("\n1. Extrahiere Kapitel aus content.md...")
    chapters = extract_chapters_from_content_md(content_md_path)
    print(f"   ✓ {len(chapters)} Kapitel gefunden")

    # Konvertiere und aktualisiere
    print("\n2. Konvertiere Markdown zu HTML und aktualisiere eLearning.html...")
    converter = MarkdownToHTMLConverter()
    update_elearning_html(elearning_html_path, chapters, converter)

    print("\n" + "="*60)
    print("✓ KONVERTIERUNG ABGESCHLOSSEN")
    print("="*60)
    print(f"\nÜberprüfen Sie {elearning_html_path} im Browser.")
    print(f"Bei Problemen: Backup verfügbar unter {elearning_html_path}.backup")


if __name__ == '__main__':
    main()
