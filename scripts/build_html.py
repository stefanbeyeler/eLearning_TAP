#!/usr/bin/env python3
"""
Generate complete eLearning.html from content/content.md
"""
import re

# HTML template header
HTML_HEADER = '''<!DOCTYPE html>
<!-- Generiert aus content/content.md am 2025-10-25 -->
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ambulantes Gesamt-Tarifsystem - Basiswissen für Anwender:innen</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Typ 1451 LL', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #666;
            background: #fff;
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
            text-align: center;
        }

        h1, h2, h3 {
            font-family: 'DTL Documenta WT', Georgia, 'Times New Roman', serif;
            font-weight: 700;
        }

        h1 {
            color: #667eea;
            font-size: 60px;
            line-height: 1.2em;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #666;
            font-size: 1.2em;
        }

        .progress-bar {
            width: 100%;
            height: 8px;
            background: #e0e0e0;
            border-radius: 10px;
            margin: 20px 0;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            width: 0%;
            transition: width 0.3s ease;
        }

        nav {
            background: white;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .nav-buttons {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .nav-btn {
            padding: 12px 24px;
            background: #f5f5f5;
            color: #666;
            border: 1px solid #ccc;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 0.95em;
            font-weight: 500;
        }

        .nav-btn:hover {
            background: #eaeaea;
            color: #444;
            border-color: #bbb;
        }

        .nav-btn.active {
            background: #e0e0e0;
            color: #222;
            border-color: #aaa;
            font-weight: 600;
        }

        .content {
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            min-height: 500px;
        }

        .chapter {
            display: none;
        }

        .chapter.active {
            display: block;
            animation: fadeIn 0.5s;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h2 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 36px;
            line-height: 1.2em;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }

        h3 {
            color: #764ba2;
            margin-top: 25px;
            margin-bottom: 15px;
            font-size: 24px;
            line-height: 1.2em;
        }

        h4, h5, h6 {
            font-family: 'Typ 1451 LL', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        h4 {
            font-size: 18px;
            line-height: 1.4em;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        h5 {
            font-size: 20px;
            line-height: 1.5em;
            margin-top: 15px;
            margin-bottom: 10px;
        }

        h6 {
            font-size: 14px;
            line-height: 1.3em;
            margin-top: 10px;
            margin-bottom: 8px;
        }

        a {
            color: #2A64B0;
            text-decoration: underline;
            transition: color 0.3s ease;
        }

        a:hover {
            color: #282828;
        }

        .image-container {
            text-align: center;
            margin: 30px 0;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
        }

        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .info-box {
            background: #e8f4f8;
            border-left: 5px solid #667eea;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }

        .info-box.warning {
            background: #fff3cd;
            border-left-color: #ffc107;
        }

        .info-box.success {
            background: #d4edda;
            border-left-color: #28a745;
        }

        .info-box h4 {
            color: #667eea;
            margin-top: 0;
            margin-bottom: 10px;
        }

        .info-box.warning h4 {
            color: #856404;
        }

        .info-box.success h4 {
            color: #155724;
        }

        .accordion {
            margin: 20px 0;
        }

        .accordion-item {
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 10px;
            overflow: hidden;
        }

        .accordion-header {
            background: #f8f9fa;
            padding: 15px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background 0.3s;
            font-weight: 600;
        }

        .accordion-header:hover {
            background: #e9ecef;
        }

        .accordion-header::after {
            content: '▼';
            transition: transform 0.3s;
        }

        .accordion-header.active::after {
            transform: rotate(180deg);
        }

        .accordion-content {
            display: none;
            padding: 15px;
            background: white;
        }

        .accordion-content.active {
            display: block;
        }

        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .comparison-table th {
            background: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
        }

        .comparison-table td {
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }

        .comparison-table tr:nth-child(even) {
            background: #f8f9fa;
        }

        .code-example {
            background: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 15px;
            margin: 15px 0;
            font-family: 'Courier New', monospace;
            font-size: 0.95em;
            white-space: pre-wrap;
        }

        .quiz-section {
            margin-top: 40px;
            padding: 30px;
            background: #f8f9fa;
            border-radius: 10px;
        }

        .quiz-question {
            margin-bottom: 30px;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .question-text {
            color: #667eea;
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 15px;
        }

        .answers {
            margin: 15px 0;
        }

        .answers label {
            display: block;
            padding: 12px;
            margin: 8px 0;
            background: #f8f9fa;
            border: 2px solid #ddd;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .answers label:hover {
            border-color: #667eea;
            background: #e8f4f8;
        }

        .answers input[type="radio"] {
            margin-right: 10px;
            cursor: pointer;
        }

        .feedback {
            display: none;
            margin-top: 15px;
            padding: 15px;
            border-radius: 5px;
        }

        .feedback.correct {
            display: block;
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }

        .feedback.incorrect {
            display: block;
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }

        .check-btn {
            background: #28a745;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            font-size: 1.1em;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 20px;
        }

        .check-btn:hover {
            background: #218838;
            transform: translateY(-2px);
        }

        .navigation-footer {
            display: flex;
            justify-content: space-between;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 2px solid #ddd;
        }

        .nav-footer-btn {
            padding: 12px 25px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 1em;
        }

        .nav-footer-btn:hover {
            background: #764ba2;
        }

        .nav-footer-btn:disabled {
            background: #ccc;
            cursor: not-allowed;
        }

        ul, ol {
            margin-left: 20px;
            padding-left: 20px;
        }

        li {
            margin-bottom: 8px;
        }

        p {
            margin-bottom: 15px;
        }

        strong {
            font-weight: 600;
        }

        em {
            font-style: italic;
        }

        /* Responsive Typography */
        @media (min-width: 1025px) and (max-width: 1440px) {
            h1 { font-size: 48px; }
            h2 { font-size: 28px; }
            h3 { font-size: 24px; }
        }

        @media (min-width: 431px) and (max-width: 1024px) {
            h1 { font-size: 36px; }
            h2 { font-size: 24px; }
            h3 { font-size: 21px; }
        }

        @media (max-width: 430px) {
            h1 { font-size: 28px; }
            h2 { font-size: 21px; }
            h3 { font-size: 21px; }
            .content { padding: 15px; }
            .nav-buttons { flex-direction: column; }
        }

        @media (max-width: 768px) {
            .content { padding: 20px; }
            .nav-buttons { flex-direction: column; }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Ambulantes Gesamt-Tarifsystem</h1>
            <p class="subtitle">Basiswissen für Anwender:innen</p>
            <div class="progress-bar">
                <div class="progress-fill" id="progressBar"></div>
            </div>
            <button onclick="resetTraining()" style="margin-top: 15px; padding: 8px 16px; background: #6c757d; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 0.9em;">
                🔄 Schulung zurücksetzen
            </button>
        </header>

        <nav>
            <div class="nav-buttons">
                <button class="nav-btn active" onclick="showChapter(0)">Vorwort</button>
                <button class="nav-btn" onclick="showChapter(1)">Kapitel 1: Einführung</button>
                <button class="nav-btn" onclick="showChapter(2)">Kapitel 2: Diagnosen ICD-10</button>
                <button class="nav-btn" onclick="showChapter(3)">Kapitel 3: Dignitäten</button>
                <button class="nav-btn" onclick="showChapter(4)">Kapitel 4: Ambulante Behandlung</button>
                <button class="nav-btn" onclick="showChapter(5)">Kapitel 5: LKAAT</button>
                <button class="nav-btn" onclick="showChapter(6)">Kapitel 6: ICD-10-GM</button>
                <button class="nav-btn" onclick="showChapter(7)">Kapitel 7: TARDOC</button>
                <button class="nav-btn" onclick="showChapter(8)">Kapitel 8: Ambulante Pauschalen</button>
                <button class="nav-btn" onclick="showChapter(9)">Kapitel 9: Vergleich</button>
                <button class="nav-btn" onclick="showChapter(10)">Kapitel 10: Praxisanwendung</button>
                <button class="nav-btn" onclick="showChapter(11)">Abschlusstest</button>
                <button class="nav-btn" onclick="showChapter(12)">FAQ</button>
            </div>
        </nav>

        <div class="content">
'''

HTML_FOOTER = '''
        </div>
    </div>

    <script>
        let currentChapter = 0;
        const totalChapters = 13;

        function showChapter(index) {
            const chapters = document.querySelectorAll('.chapter');
            chapters.forEach(chapter => chapter.classList.remove('active'));
            document.getElementById('chapter' + index).classList.add('active');
            currentChapter = index;
            const navButtons = document.querySelectorAll('.nav-btn');
            navButtons.forEach((btn, i) => {
                btn.classList.toggle('active', i === index);
            });
            updateProgress();
            window.scrollTo(0, 0);
        }

        function updateProgress() {
            document.getElementById('progressBar').style.width = ((currentChapter + 1) / totalChapters * 100) + '%';
        }

        function toggleAccordion(element) {
            const header = element.querySelector('.accordion-header');
            const content = element.querySelector('.accordion-content');
            if (header && content) {
                header.classList.toggle('active');
                content.classList.toggle('active');
            }
        }

        function checkAnswer(chapter, questionNum, correctAnswer) {
            const feedbackId = `feedback${chapter}_${questionNum}`;
            const feedback = document.getElementById(feedbackId);
            const questionName = `q${chapter}_${questionNum}`;
            const selectedAnswer = document.querySelector(`input[name="${questionName}"]:checked`);

            if (!selectedAnswer) {
                feedback.className = 'feedback incorrect';
                feedback.textContent = 'Bitte wählen Sie eine Antwort aus.';
                return;
            }

            const isCorrect = selectedAnswer.value === correctAnswer;
            if (isCorrect) {
                feedback.className = 'feedback correct';
                feedback.textContent = '✓ Richtig! Sehr gut.';
            } else {
                feedback.className = 'feedback incorrect';
                feedback.textContent = '✗ Leider falsch. Die richtige Antwort ist: ' + correctAnswer + ')';
            }
        }

        function resetTraining() {
            if (confirm('Möchten Sie die Schulung wirklich zurücksetzen? Alle Ihre Antworten gehen verloren.')) {
                document.querySelectorAll('input[type="radio"]').forEach(radio => radio.checked = false);
                document.querySelectorAll('.feedback').forEach(feedback => {
                    feedback.style.display = 'none';
                    feedback.className = 'feedback';
                });
                showChapter(0);
                alert('Die Schulung wurde zurückgesetzt.');
            }
        }

        window.onload = function() {
            updateProgress();
        };
    </script>
</body>
</html>'''


def convert_inline_md(text):
    """Convert inline markdown to HTML"""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    return text


def parse_content_md(content):
    """Parse content.md and extract chapters"""
    chapters = []

    # Split by ## headers
    sections = re.split(r'^## ', content, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue

        lines = section.split('\n')
        title = lines[0].strip()

        # Skip metadata sections
        if 'Hinweise zur Nutzung' in title or 'Ende der Content' in title:
            continue

        # Determine chapter number and clean title
        if title == 'Vorwort':
            ch_num = 0
            ch_title = 'Vorwort'
        elif title.startswith('KAPITEL'):
            # Parse chapter number and title
            match = re.match(r'KAPITEL \d+:\s*(.+)', title)
            if match:
                ch_title = match.group(1)
                # Determine actual chapter number based on content
                if 'Einführung' in ch_title:
                    ch_num = 1
                elif ch_title == 'Diagnosen als ICD-10 Code' and 'Warum ist' not in '\n'.join(lines):
                    ch_num = 2  # Short version
                elif 'Dignitäten' in ch_title:
                    ch_num = 3
                elif 'Ambulante Behandlung' in ch_title:
                    ch_num = 4
                elif 'LKAAT' in ch_title:
                    ch_num = 5
                elif 'ICD-10-GM' in ch_title or ('Diagnosen' in ch_title and 'Warum ist' in '\n'.join(lines)):
                    ch_num = 6  # Full version
                elif 'TARDOC' in ch_title and 'vs' not in ch_title:
                    ch_num = 7
                elif 'Ambulante Pauschalen' in ch_title and 'vs' not in ch_title:
                    ch_num = 8
                elif 'TARDOC vs' in ch_title or 'Vergleich' in ch_title:
                    ch_num = 9
                elif 'Praxisanwendung' in ch_title:
                    ch_num = 10
                else:
                    continue
            else:
                continue
        elif title == 'Abschlusstest':
            ch_num = 11
            ch_title = 'Abschlusstest'
        elif title.startswith('FAQ'):
            ch_num = 12
            ch_title = 'FAQ'
        else:
            continue

        content_text = '\n'.join(lines[1:])
        chapters.append((ch_num, ch_title, content_text))

    # Sort by chapter number
    chapters.sort(key=lambda x: x[0])
    return chapters


def process_markdown_content(md_text, chapter_num):
    """Convert markdown content to HTML"""
    html = ""
    lines = md_text.split('\n')
    i = 0
    in_list = False
    in_accordion = False
    in_quiz = False
    in_info_box = False
    accordion_items = []
    quiz_questions = []

    while i < len(lines):
        line = lines[i].rstrip()

        # Handle code blocks
        if line.startswith('```'):
            html += '<div class="code-example">'
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                html += lines[i] + '\n'
                i += 1
            html += '</div>\n\n'
            i += 1
            continue

        # Handle INFO-BOX
        if line.startswith('**INFO-BOX'):
            if in_list:
                html += '</ul>\n'
                in_list = False
            if in_info_box:
                html += '</div>\n\n'
                in_info_box = False

            box_class = ''
            if 'WARNUNG' in line:
                box_class = ' warning'
            elif 'SUCCESS' in line:
                box_class = ' success'

            title_match = re.search(r'\*\*INFO-BOX[^:]*:\s*(.+?)\*\*', line)
            title = title_match.group(1) if title_match else "Information"

            html += f'<div class="info-box{box_class}">\n    <h4>{title}</h4>\n'
            in_info_box = True
            i += 1
            continue

        # Close info box when we hit certain markers
        if in_info_box and (line.startswith('###') or line.startswith('**INFO-BOX') or
                           line.startswith('**ACCORDION') or line.startswith('**TABELLE') or
                           line == '---' or line.startswith('### QUIZ')):
            if in_list:
                html += '</ul>\n'
                in_list = False
            html += '</div>\n\n'
            in_info_box = False

        # Handle ACCORDION
        if line == '**ACCORDION:**':
            if in_list:
                html += '</ul>\n'
                in_list = False
            in_accordion = True
            accordion_items = []
            i += 1
            continue

        # Accordion items - improved detection
        if in_accordion and line.startswith('**') and line.endswith('**') and len(line) > 4:
            header_title = line.strip('*').strip()

            # Check if this looks like an accordion header (not a sub-heading within content)
            # Accordion headers typically are standalone concepts, not formatting within text
            is_accordion_header = (
                header_title.startswith('Schritt ') or
                header_title in ['Konsultationen und Untersuchungen', 'Diagnostische Verfahren',
                               'Therapeutische Eingriffe', 'Notfallbehandlungen',
                               'Flexibilität in der Abrechnung', 'Wirtschaftlichkeit und Transparenz',
                               'Anpassung an internationale Standards',
                               'Ebene 1: Kapitel (Buchstabe + 2 Ziffern)', 'Ebene 2: Kategorie (3-stellig)',
                               'Ebene 3: Unterkategorie (4-5-stellig)',
                               'Mehrere Leistungen in einer Sitzung', 'Fallbeispiel: Hausarztbesuch',
                               'Verdachtsdiagnosen', 'Symptomcodes', 'Akut vs. Chronisch',
                               'Erkrankungen nach medizinischen Maßnahmen',
                               'Kapitel A: Ärztliche Grundleistungen', 'Weitere Kapitel: Diagnostik und Therapie',
                               'AP-Gruppen und Klassifikation', 'Inkludierte Leistungen', 'Zusatzentgelte',
                               'Grundsätzlich: Keine Mischung im selben Fall',
                               'Ausnahme: Zwei Behandlungen am gleichen Tag', 'Ausnahme: Zusatzentgelte',
                               'Ausnahme: Komplikationen'] or
                'FAQ' in header_title or 'Fragen' in header_title
            )

            if is_accordion_header:
                content_lines = []
                i += 1
                while i < len(lines):
                    next_line = lines[i].rstrip()
                    # Check for next accordion header
                    if next_line.startswith('**') and next_line.endswith('**') and len(next_line) > 4:
                        next_title = next_line.strip('*').strip()
                        next_is_header = (
                            next_title.startswith('Schritt ') or
                            next_title in ['Konsultationen und Untersuchungen', 'Diagnostische Verfahren',
                                         'Therapeutische Eingriffe', 'Notfallbehandlungen',
                                         'Flexibilität in der Abrechnung', 'Wirtschaftlichkeit und Transparenz',
                                         'Anpassung an internationale Standards',
                                         'Ebene 1: Kapitel (Buchstabe + 2 Ziffern)', 'Ebene 2: Kategorie (3-stellig)',
                                         'Ebene 3: Unterkategorie (4-5-stellig)',
                                         'Mehrere Leistungen in einer Sitzung', 'Fallbeispiel: Hausarztbesuch',
                                         'Verdachtsdiagnosen', 'Symptomcodes', 'Akut vs. Chronisch',
                                         'Erkrankungen nach medizinischen Maßnahmen',
                                         'Kapitel A: Ärztliche Grundleistungen', 'Weitere Kapitel: Diagnostik und Therapie',
                                         'AP-Gruppen und Klassifikation', 'Inkludierte Leistungen', 'Zusatzentgelte',
                                         'Grundsätzlich: Keine Mischung im selben Fall',
                                         'Ausnahme: Zwei Behandlungen am gleichen Tag', 'Ausnahme: Zusatzentgelte',
                                         'Ausnahme: Komplikationen'] or
                            'FAQ' in next_title or 'Fragen' in next_title
                        )
                        if next_is_header:
                            break
                    if next_line.startswith('###') or next_line.startswith('**INFO-BOX') or \
                       next_line.startswith('**TABELLE') or next_line.startswith('**FRAGE') or \
                       next_line == '---':
                        break
                    content_lines.append(next_line)
                    i += 1

                item_content = process_accordion_content('\n'.join(content_lines))
                accordion_items.append((header_title, item_content))

                if i < len(lines) and (lines[i].startswith('###') or lines[i].startswith('**INFO-BOX') or
                                      lines[i].startswith('**TABELLE') or lines[i] == '---'):
                    # End of accordion
                    html += '<div class="accordion">\n'
                    for hdr, cnt in accordion_items:
                        html += '    <div class="accordion-item" onclick="toggleAccordion(this)">\n'
                        html += f'        <div class="accordion-header">{hdr}</div>\n'
                        html += f'        <div class="accordion-content">\n{cnt}\n        </div>\n'
                        html += '    </div>\n'
                    html += '</div>\n\n'
                    in_accordion = False
                    accordion_items = []
                continue
            else:
                # This is just bold text within accordion content, not a header
                # Skip it for now and let it be processed as part of content
                i += 1
                continue

        # Handle tables
        if '|' in line:
            table_lines = []
            while i < len(lines) and '|' in lines[i]:
                table_lines.append(lines[i])
                i += 1
            html += process_table(table_lines)
            continue

        # Handle QUIZ
        if line.startswith('### QUIZ') or line.startswith('**Frage'):
            if not in_quiz:
                html += '<div class="quiz-section">\n    <h3>Quiz</h3>\n'
                in_quiz = True

            if line.startswith('**Frage'):
                q_match = re.match(r'\*\*Frage (\d+):\s*(.+?)\*\*', line)
                if q_match:
                    q_num = q_match.group(1)
                    q_text = q_match.group(2)
                    answers = []
                    correct = 'a'
                    i += 1
                    while i < len(lines):
                        ans_line = lines[i].strip()
                        if ans_line.startswith('*   '):
                            ans_text = ans_line[4:].strip()
                            if '✓' in ans_text:
                                ans_text = ans_text.replace('✓', '').strip()
                                correct = ans_text[0].lower()
                            answers.append(ans_text)
                            i += 1
                        elif ans_line.startswith('**Frage') or ans_line == '---' or ans_line.startswith('##'):
                            break
                        else:
                            i += 1
                            if i < len(lines) and (lines[i].startswith('**Frage') or lines[i] == '---'):
                                break

                    html += f'    <div class="quiz-question">\n'
                    html += f'        <div class="question-text">Frage {q_num}: {q_text}</div>\n'
                    html += f'        <div class="answers">\n'
                    for ans in answers:
                        ans_val = ans[0].lower()
                        html += f'            <label><input type="radio" name="q{chapter_num}_{q_num}" value="{ans_val}"> {ans}</label>\n'
                    html += f'        </div>\n'
                    html += f'        <button class="check-btn" onclick="checkAnswer({chapter_num}, {q_num}, \'{correct}\')">Antwort überprüfen</button>\n'
                    html += f'        <div class="feedback" id="feedback{chapter_num}_{q_num}"></div>\n'
                    html += f'    </div>\n'
                    continue
            else:
                i += 1
                continue

        # Close quiz
        if in_quiz and line == '---':
            html += '</div>\n\n'
            in_quiz = False

        # Handle headings
        if line.startswith('### '):
            if in_list:
                html += '</ul>\n'
                in_list = False
            if in_info_box:
                html += '</div>\n\n'
                in_info_box = False
            heading = convert_inline_md(line[4:].strip())
            html += f'<h3>{heading}</h3>\n'
            i += 1
            continue

        if line.startswith('#### '):
            if in_list:
                html += '</ul>\n'
                in_list = False
            heading = convert_inline_md(line[5:].strip())
            html += f'<h4>{heading}</h4>\n'
            i += 1
            continue

        # Handle lists
        if line.startswith('*   ') or line.startswith('- '):
            if not in_list:
                html += '<ul>\n'
                in_list = True
            item = line[4:].strip() if line.startswith('*   ') else line[2:].strip()
            item = convert_inline_md(item)
            html += f'    <li>{item}</li>\n'
            i += 1
            continue

        # Close list
        if in_list and line and not line.startswith('*') and not line.startswith('-') and not line.strip() == '':
            html += '</ul>\n'
            in_list = False

        # Handle paragraphs
        if line.strip() and not line.startswith('#') and not line.startswith('---'):
            para = convert_inline_md(line)
            html += f'<p>{para}</p>\n'
        elif line.strip() == '':
            html += '\n'

        i += 1

    # Close any remaining tags
    if in_list:
        html += '</ul>\n'
    if in_info_box:
        html += '</div>\n\n'
    if in_quiz:
        html += '</div>\n'
    if in_accordion and accordion_items:
        html += '<div class="accordion">\n'
        for hdr, cnt in accordion_items:
            html += '    <div class="accordion-item" onclick="toggleAccordion(this)">\n'
            html += f'        <div class="accordion-header">{hdr}</div>\n'
            html += f'        <div class="accordion-content">\n{cnt}\n        </div>\n'
            html += '    </div>\n'
        html += '</div>\n\n'

    return html


def process_list_content(content):
    """Process content for lists (accordion, info-box, etc.)"""
    html = ""
    lines = content.split('\n')
    in_list = False

    for line in lines:
        line = line.strip()
        if not line:
            if in_list:
                html += '</ul>\n'
                in_list = False
            continue

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


def process_accordion_content(content):
    """Process content for accordion items with sub-headings"""
    html = ""
    lines = content.split('\n')
    in_list = False

    for line in lines:
        line = line.strip()
        if not line:
            if in_list:
                html += '</ul>\n'
                in_list = False
            html += '\n'
            continue

        # Check for bold sub-headings (but not standalone accordion headers)
        if line.startswith('**') and line.endswith('**') and len(line) > 4:
            if in_list:
                html += '</ul>\n'
                in_list = False
            heading = line.strip('*').strip()
            html += f'<p><strong>{heading}</strong></p>\n'
        elif line.startswith('*   ') or line.startswith('- '):
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


def process_table(lines):
    """Convert markdown table to HTML"""
    html = '<table class="comparison-table">\n'
    rows = []

    for line in lines:
        cells = [cell.strip() for cell in line.split('|')]
        cells = [c for c in cells if c]
        if cells and not all(re.match(r'^-+$', cell) for cell in cells):
            rows.append(cells)

    if rows:
        # Header
        html += '    <tr>\n'
        for cell in rows[0]:
            html += f'        <th>{convert_inline_md(cell)}</th>\n'
        html += '    </tr>\n'
        # Body
        for row in rows[1:]:
            html += '    <tr>\n'
            for cell in row:
                html += f'        <td>{convert_inline_md(cell)}</td>\n'
            html += '    </tr>\n'

    html += '</table>\n\n'
    return html


def generate_html(chapters):
    """Generate complete HTML file"""
    html = HTML_HEADER

    for ch_num, ch_title, ch_content in chapters:
        active = ' active' if ch_num == 0 else ''
        html += f'            <!-- {"VORWORT" if ch_num == 0 else ("KAPITEL " + str(ch_num) if ch_num <= 10 else ("Abschlusstest" if ch_num == 11 else "FAQ"))} -->\n'
        html += f'            <div class="chapter{active}" id="chapter{ch_num}">\n'
        html += f'                <h2>{ch_title}</h2>\n\n'
        html += process_markdown_content(ch_content, ch_num)

        # Navigation footer
        html += '\n                <div class="navigation-footer">\n'
        if ch_num == 0:
            html += '                    <button class="nav-footer-btn" disabled>◄ Vorheriges Kapitel</button>\n'
        else:
            html += f'                    <button class="nav-footer-btn" onclick="showChapter({ch_num - 1})">◄ Vorheriges Kapitel</button>\n'

        if ch_num == 12:
            html += '                    <button class="nav-footer-btn" disabled>Nächstes Kapitel ►</button>\n'
        else:
            html += f'                    <button class="nav-footer-btn" onclick="showChapter({ch_num + 1})">Nächstes Kapitel ►</button>\n'
        html += '                </div>\n'
        html += '            </div>\n\n'

    html += HTML_FOOTER
    return html


def main():
    print("Reading content.md...")
    with open('content/content.md', 'r', encoding='utf-8') as f:
        content = f.read()

    print("Parsing chapters...")
    chapters = parse_content_md(content)
    print(f"Found {len(chapters)} chapters")

    print("Generating HTML...")
    html = generate_html(chapters)

    print("Writing eLearning.html...")
    with open('eLearning.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("✅ eLearning.html generated successfully!")
    print(f"Total size: {len(html)} characters")


if __name__ == '__main__':
    main()
