#!/usr/bin/env python3
"""Generate README as PDF (short version)."""
from fpdf import FPDF

FONT_PATH = r'C:\Windows\Fonts\ARIALUNI.ttf'

pdf = FPDF()
pdf.add_font('A', '', FONT_PATH)
pdf.add_font('A', 'B', FONT_PATH)
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.add_page()

# Title
pdf.set_font('A', 'B', 22)
pdf.set_text_color(50, 35, 15)
pdf.cell(0, 12, 'КВЕСТ МАЙНКРАФТ + ROBLOX', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('A', '', 14)
pdf.set_text_color(100, 70, 50)
pdf.cell(0, 9, 'День рождения двойняшек', new_x='LMARGIN', new_y='NEXT')
pdf.ln(5)

# Table of materials
pdf.set_font('A', 'B', 12)
pdf.set_text_color(50, 35, 15)
pdf.cell(0, 8, 'Файлы для печати (materials/)', new_x='LMARGIN', new_y='NEXT')
pdf.ln(2)

pdf.set_font('A', '', 9)
pdf.set_text_color(40, 40, 40)
files_table = [
    ('01-zapiski-all.svg', '5 записок с заданиями', '1 лист'),
    ('02-diamonds.svg', '6 алмазов', '1 лист'),
    ('03-diamond-sword.svg', 'Алмазный клинок', '2 листа'),
    ('04-lava-blocks.svg', '12 лавовых блоков', '1 лист'),
    ('05-hp-hearts.svg', '12 сердечек HP', '1 лист'),
    ('06-flame-endurance.svg', 'Пламя выносливости', '1 лист'),
    ('07-mob-tear.svg', 'Наклейки Слеза моба', '1 лист'),
    ('08-dragon-mask.svg', 'Рога + накидка', '2 листа'),
    ('09-chest-labels.svg', 'Этикетки сундуков', '1 лист'),
    ('10-craft-grid.svg', 'Крафт-станция 3x3', '1 лист'),
    ('11-progress-map.svg', 'Карта прогресса', '1 лист'),
    ('12-scp-obby-signs.svg', 'SCP, obby, портал', '2 листа'),
    ('13-obby-floor-signs.svg', 'Номера этажей', '1 лист'),
    ('14-chest-wrap.svg', 'Обклейка под дерево', '4+ листа'),
]
for fname, desc, sheets in files_table:
    pdf.cell(55, 5, fname, 0, 0)
    pdf.cell(75, 5, desc, 0, 0)
    pdf.cell(0, 5, sheets, 0, 1, 'R')

pdf.ln(3)

# Previews
pdf.set_font('A', 'B', 12)
pdf.set_text_color(50, 35, 15)
pdf.cell(0, 8, 'Превью материалов', new_x='LMARGIN', new_y='NEXT')
pdf.ln(2)

pdf.set_font('A', '', 9)
pdf.set_text_color(40, 40, 40)
previews = [
    'Записки — 5 карточек, коричневый фон, зелёная пиксельная рамка',
    'Алмазы — 6 голубых кристаллов сложной огранки со звездой',
    'Клинок — меч на весь А4: голубое лезвие, 65 см',
    'Лава — 12 оранжево-красных квадратов, подпись «НЕ НАСТУПАТЬ!»',
    'HP сердца — 12 красных сердечек с бликом, подпись ❤ HP',
    'Пламя — 2 языка пламени для мишуры',
    'Слеза моба — 8 этикеток с голубой каплей',
    'Маска — 2 листа: рога для каски + выкройка накидки',
    'Сундуки — 4 наклейки с замками и металлическими полосами',
    'Крафт — сетка 3x3: слоты для алмазов в верхнем ряду',
    'Карта — пергамент с 4 ресурсами, порталом, стикерами',
    'SCP/obby — серые SCP-таблички, зелёные obby, портал',
    'Этажи — 5 зелёных табличек с цифрами 1-5',
    'Обклейка — узор под дерево, 4+ листа',
]
for p in previews:
    pdf.cell(5, 6, '•', 0, 0)
    pdf.multi_cell(0, 6, p)
    pdf.ln(0.5)

# SVG info
pdf.ln(3)
pdf.set_font('A', 'B', 12)
pdf.set_text_color(50, 35, 15)
pdf.cell(0, 8, 'Как открыть SVG', new_x='LMARGIN', new_y='NEXT')
pdf.ln(2)
pdf.set_font('A', '', 9)
pdf.set_text_color(40, 40, 40)
pdf.multi_cell(0, 5,
    'SVG открывается любым браузером (Chrome, Edge, Яндекс). '
    'Перетащить файл в окно, Ctrl+P, печать. '
    'Ориентация книжная, масштаб 95-100%, цветная печать. '
    'Вырезать по серому пунктиру.\n\n'
    'Полная инструкция: instructions.md / instructions.pdf\n'
    'Репозиторий: github.com/RuslanStrogov/quest-minecraft-roblox')

output = r'C:\Users\Ruslan\quest-minecraft-rob\README.pdf'
pdf.output(output)
print(f'PDF: {output} ({pdf.page_no()} стр)')