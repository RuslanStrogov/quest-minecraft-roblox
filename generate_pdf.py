#!/usr/bin/env python3
"""Generate printable PDF instructions - LARGE FONT VERSION"""
import os
from fpdf import FPDF

FONT = r'C:\Windows\Fonts\ARIALUNI.ttf'

class QuestPDF(FPDF):
    def setup_fonts(self):
        self.add_font('A', '', FONT)
        self.add_font('A', 'B', FONT)
    
    def header(self):
        self.set_font('A', '', 8)
        self.set_text_color(180,180,180)
        self.cell(0, 4, 'КВЕСТ "МАЙНКРАФТ + ROBLOX" — инструкция', new_x='LMARGIN', new_y='NEXT')
    
    def footer(self):
        self.set_y(-12)
        self.set_font('A', '', 8)
        self.set_text_color(150,150,150)
        self.cell(0, 8, f'{self.page_no()}', 0, 0, 'C')

def write_pdf(output_path):
    pdf = QuestPDF()
    pdf.setup_fonts()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # ===== TITLE PAGE =====
    pdf.add_page()
    pdf.ln(40)
    pdf.set_font('A', 'B', 30)
    pdf.set_text_color(50, 35, 15)
    pdf.multi_cell(0, 14, 'КВЕСТ\n"МАЙНКРАФТ + ROBLOX"', 0, 'C')
    pdf.ln(8)
    pdf.set_font('A', '', 18)
    pdf.set_text_color(100, 70, 50)
    pdf.cell(0, 10, 'День рождения двойняшек', 0, 1, 'C')
    pdf.ln(15)
    pdf.set_font('A', '', 13)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 8, 'Уличный квест | ~40 минут | 4-8 лет', 0, 1, 'C')
    
    pdf.ln(40)
    pdf.set_font('A', 'B', 12)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(0, 7, 'Все материалы: github.com/RuslanStrogov/quest-minecraft-roblox', 0, 1, 'C')
    
    # ===== 1. WHAT IS THIS =====
    pdf.add_page()
    pdf.set_font('A', 'B', 22)
    pdf.set_text_color(50, 35, 15)
    pdf.cell(0, 12, '1. ЧТО ЭТО?', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(5)
    pdf.set_font('A', '', 14)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 8,
        'Дети — "игроки", которые "спавнятся" во дворе. Им нужно пройти 6 этапов, '
        'собрать 4 ресурса и в финале победить Эндер-дракона (папу). Каждый этап — '
        'отдельный "биом" из Minecraft с наградой.\n\n'
        'ВСЕ материалы готовы к печати — SVG-файлы открываются в браузере (Ctrl+P).')
    
    # ===== 2. WHAT TO BUY =====
    pdf.add_page()
    pdf.set_font('A', 'B', 22)
    pdf.set_text_color(50, 35, 15)
    pdf.cell(0, 12, '2. ЧТО НУЖНО КУПИТЬ / НАЙТИ', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(3)
    
    items = [
        '4-5 картонных коробок (магазин/посылки)',
        'Коричневая/крафтовая бумага 3-4 листа',
        'Голубая акриловая краска',
        'Фольга пищевая (1 рулон)',
        'Жёлтая мишура',
        '3-4 мячика (теннисные)',
        '6-8 синих бусин или камешков',
        'Верёвка 5 метров',
        'Красная+оранжевая бумага А4 (4-5 листов)',
        'Фиолетовая бумага (1-2 листа)',
        'Чёрный маркер, скотч прозрачный+малярный',
        'Каска (строительная или велосипедная)',
        'Чёрная/фиолетовая ткань 60x120 см',
    ]
    pdf.set_font('A', '', 13)
    pdf.set_text_color(50, 50, 50)
    for item in items:
        pdf.cell(10, 7, '', 0, 0)
        pdf.cell(5, 7, '•', 0, 0)
        pdf.multi_cell(0, 7, item, 0, 'L')
        pdf.ln(1)
    
    # ===== 3. WHAT TO PRINT =====
    pdf.add_page()
    pdf.set_font('A', 'B', 22)
    pdf.set_text_color(50, 35, 15)
    pdf.cell(0, 12, '3. ЧТО РАСПЕЧАТАТЬ', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(3)
    
    pdf.set_font('A', '', 12)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 7, 'Всего ~18-20 листов А4, цветная печать. Файлы SVG.', 0, 1, 'L')
    pdf.ln(3)
    
    prints = [
        ('01-zapiski-all.svg', '5 записок с заданиями', '1 лист'),
        ('02-diamonds.svg', '6 алмазов (вырезать+раскрасить)', '1 лист'),
        ('03-diamond-sword.svg', 'Алмазный клинок (2 копии)', '2 листа'),
        ('04-lava-blocks.svg', '12 лавовых блоков', '1 лист'),
        ('05-hp-hearts.svg', '12 сердечек HP', '1 лист'),
        ('06-flame-endurance.svg', 'Пламя выносливости', '1 лист'),
        ('07-mob-tear.svg', 'Наклейки "Слеза моба"', '1 лист'),
        ('08-dragon-mask.svg', 'Рога+накидка дракона', '2 листа'),
        ('09-chest-labels.svg', 'Этикетки для сундуков', '1 лист'),
        ('10-craft-grid.svg', 'Крафт-станция 3x3', '1 лист'),
        ('11-progress-map.svg', 'Карта прогресса+стикеры', '1 лист'),
        ('12-scp-obby-signs.svg', 'SCP-моб, obby, портал', '2 листа'),
        ('13-obby-floor-signs.svg', 'Номера этажей', '1 лист'),
        ('14-chest-wrap.svg', 'Обклейка "под дерево"', '4+ листа'),
    ]
    pdf.set_font('A', '', 11)
    pdf.set_text_color(50, 50, 50)
    for fname, desc, sheets in prints:
        pdf.cell(55, 6, fname, 0, 0)
        pdf.cell(75, 6, desc, 0, 0)
        pdf.cell(0, 6, sheets, 0, 1, 'R')
    
    # ===== 4. PROPS =====
    pdf.add_page()
    pdf.set_font('A', 'B', 22)
    pdf.set_text_color(50, 35, 15)
    pdf.cell(0, 12, '4. КАК СДЕЛАТЬ РЕКВИЗИТ', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(3)
    
    pdf.set_font('A', 'B', 14)
    pdf.set_text_color(80, 50, 30)
    pdf.cell(0, 8, 'Сундуки (4 шт.)', new_x='LMARGIN', new_y='NEXT')
    pdf.set_font('A', '', 13)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 7,
        '1. Обклей коробку коричневой бумагой\n'
        '2. Сверху наклей текстуру (14-chest-wrap.svg)\n'
        '3. Приклей полоски фольги поперёк\n'
        '4. Нарисуй чёрные точки-заклёпки\n'
        '5. Наклей этикетку (09-chest-labels.svg)\n'
        '6. Положи внутрь записку или алмазы')
    pdf.ln(2)
    
    pdf.set_font('A', 'B', 14)
    pdf.set_text_color(80, 50, 30)
    pdf.cell(0, 8, 'Алмазы (6 шт.)', new_x='LMARGIN', new_y='NEXT')
    pdf.set_font('A', '', 13)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 7,
        '1. Вырежи 6 фигур из 02-diamonds.svg\n'
        '2. Обведи на картоне, вырежи картон\n'
        '3. Покрась голубым акрилом с обеих сторон\n'
        '4. Дай высохнуть ~30 минут')
    pdf.ln(2)
    
    pdf.set_font('A', 'B', 14)
    pdf.set_text_color(80, 50, 30)
    pdf.cell(0, 8, 'Алмазный клинок', new_x='LMARGIN', new_y='NEXT')
    pdf.set_font('A', '', 13)
    pdf.multi_cell(0, 7,
        '1. Распечатай 03-diamond-sword.svg (2 копии)\n'
        '2. Вырежи обе, склей спинками\n'
        '3. Приложи к картону, обведи, вырежи\n'
        '4. Обклей фольгой')
    pdf.ln(2)
    
    pdf.set_font('A', 'B', 14)
    pdf.set_text_color(80, 50, 30)
    pdf.cell(0, 8, 'Остальное', new_x='LMARGIN', new_y='NEXT')
    pdf.set_font('A', '', 13)
    pdf.multi_cell(0, 7,
        '• Пламя: вырежи из 06-flame-endurance.svg, приклей к жёлтой мишуре\n'
        '• HP сердца: вырежи 10 шт. из 05-hp-hearts.svg\n'
        '• Слеза моба: наклей этикетку 07-mob-tear.svg на синюю бусину\n'
        '• Рога: вырежи из 08-dragon-mask.svg, согни, приклей к каске скотчем\n'
        '• Накидка: вырежи из чёрной/фиолетовой ткани по выкройке\n'
        '• Лава: вырежи 12 блоков из 04-lava-blocks.svg (лучше заламинировать)')
    
    # ===== 5. TIMELINE =====
    pdf.add_page()
    pdf.set_font('A', 'B', 22)
    pdf.set_text_color(50, 35, 15)
    pdf.cell(0, 12, '5. СЦЕНАРИЙ (40 МИНУТ)', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(3)
    
    timeline = [
        ('12:00', 'Спавн: дети находят сундук с Запиской №1. Задание — найти 3 алмаза'),
        ('12:10', 'Крафт: кладут 3 алмаза в сетку 3x3 → получают Алмазный клинок + Записка №2'),
        ('12:12', 'Паркур obby: верёвка между деревьями, лава на земле (наступать нельзя!), 5 этажей. Награда: Пламя выносливости + Записка №3'),
        ('12:25', 'Моб-арена: папа в маске "Зомби". Дети кидают 3 мяча. Папа падает. В сундуке: Слеза моба + Записка №4'),
        ('12:30', 'Тайник: Первородная пыль (почтовый ящик/под крыльцом). Записка №5'),
        ('12:35', 'Портал: несут 4 ресурса → появляется Эндер-дракон (папа в каске+накидке). "Победа" → Главный сундук с подарками!'),
        ('12:40+', 'Подарки и RUTUBE-съёмка'),
    ]
    pdf.set_font('A', 'B', 13)
    for t, d in timeline:
        pdf.set_text_color(120, 70, 30)
        pdf.cell(18, 7, t, 0, 0)
        pdf.set_text_color(40, 40, 40)
        pdf.set_font('A', '', 13)
        pdf.multi_cell(0, 7, d, 0, 'L')
        pdf.set_font('A', 'B', 13)
        pdf.ln(3)
    
    # ===== 6. STAGE DETAILS =====
    pdf.add_page()
    pdf.set_font('A', 'B', 22)
    pdf.set_text_color(50, 35, 15)
    pdf.cell(0, 12, '6. ДЕТАЛИ ПО ЭТАПАМ', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(3)
    
    stages = [
        ('Спавн', 'Во дворе на видном месте стоит сундук. Внутри Записка №1. Дети читают: "Вы заспавнились! Нужно собрать 4 ресурса..."'),
        ('Поиск алмазов', '3 алмаза спрятаны вдоль бордюров, в песке, под листьями, в горшках. Дети ищут 5-10 минут. Найденные несут к крафт-станции.'),
        ('Крафт', 'На столе сетка 3x3. Ведущий: "Положите 3 алмаза в верхний ряд!" Проверяет → вручает Алмазный клинок и Записку №2.'),
        ('Паркур (obby)', 'Между деревьями верёвка (h=20-30 см) — перепрыгнуть. На земле лавовые блоки — на них наступать нельзя! 5 этажей с табличками.'),
        ('Моб-арена', 'Папа в каске+рогах+накидке — "Зомби". Дети кидают мячи (3 попадания). Папа падает. Рядом сундук со Слезой моба.'),
        ('Тайник', 'Первородная пыль в неожиданном месте (почтовый ящик/под крыльцом/коробка).'),
        ('Финал', 'Дети несут 4 ресурса к фиолетовому порталу (арка с лентами). Появляется папа-дракон. "Победа" → Главный сундук с подарками.'),
    ]
    pdf.set_font('A', '', 13)
    pdf.set_text_color(40, 40, 40)
    for title, desc in stages:
        pdf.set_font('A', 'B', 14)
        pdf.set_text_color(80, 50, 30)
        pdf.cell(0, 8, title, new_x='LMARGIN', new_y='NEXT')
        pdf.set_font('A', '', 13)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 7, desc)
        pdf.ln(3)
    
    # ===== 7. PLAN B =====
    pdf.add_page()
    pdf.set_font('A', 'B', 22)
    pdf.set_text_color(50, 35, 15)
    pdf.cell(0, 12, '7. ПЛАН Б', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(3)
    pdf.set_font('A', '', 14)
    pdf.set_text_color(40, 40, 40)
    plans = [
        'Дождь → в подъезд/подвал/гараж. Паркур между комнатами, лава=подушки',
        'Грязь → алмазы не на земле, а в крупе/фасоли в контейнере',
        'Папа занят → нарисовать дракона на коробке, дети кидают в лицо',
        'Ветрено → лавовые блоки приклеить скотчем',
        'Нет красок → алмазы из цветного картона/пластилина',
    ]
    for p in plans:
        pdf.cell(7, 7, '•', 0, 0)
        pdf.multi_cell(0, 7, p)
        pdf.ln(2)
    
    # ===== 8. RUTUBE =====
    pdf.ln(5)
    pdf.set_font('A', 'B', 22)
    pdf.set_text_color(50, 35, 15)
    pdf.cell(0, 12, '8. СЪЁМКА ДЛЯ RUTUBE', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(3)
    pdf.set_font('A', '', 14)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 7,
        '0:00 — Интро: "Сегодня день рождения и Майнкрафт-квест в реальной жизни!"\n'
        '0:15 — Спавн и первая записка (крупный план)\n'
        '0:40 — Крафт (крупный план рук)\n'
        '1:00 — Паркур (смешные моменты, слоу-мо)\n'
        '1:30 — Битва с мобом (эффектное падение папы)\n'
        '2:00 — Финальная битва с драконом\n'
        '2:30 — Сундук с подарками и титры')
    
    # ===== 9. CHECKLIST =====
    pdf.add_page()
    pdf.set_font('A', 'B', 22)
    pdf.set_text_color(50, 35, 15)
    pdf.cell(0, 12, '9. ЧЕК-ЛИСТ НА ДЕНЬ КВЕСТА', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(3)
    
    checklist = [
        'Распечатаны все 14 файлов (18-20 листов А4)',
        'Сделаны 4 сундука (коробки обклеены)',
        'Сделан Алмазный клинок (картон+фольга)',
        'Покрашены 6 алмазов (высыхают)',
        'Вырезаны 12 лавовых блоков',
        'Вырезаны 10 сердечек HP',
        'Сделано Пламя (мишура+бумага)',
        'Сделана Слеза моба (бусина+наклейка)',
        'Сделана Первородная пыль',
        'Рога приклеены к каске',
        'Вырезана накидка дракона',
        'Разложена верёвка для паркура',
        'Спрятаны 3 алмаза',
        'Спрятана Первородная пыль',
        'Сделана арка портала',
        'Главный сундук с подарками',
        'Телефон заряжен для съёмки',
        '3 мячика готовы',
        'Карта прогресса на видном месте',
        'Записки разложены по сундукам',
    ]
    pdf.set_font('A', '', 13)
    pdf.set_text_color(40, 40, 40)
    for i, item in enumerate(checklist, 1):
        pdf.cell(8, 7, f'{i}.', 0, 0)
        pdf.cell(5, 7, '☐', 0, 0)
        pdf.multi_cell(0, 7, item)
        pdf.ln(1)
    
    pdf.output(output_path)
    print(f'PDF: {output_path} ({pdf.page_no()} стр)')

write_pdf(r'C:\Users\Ruslan\quest-minecraft-rob\instructions.pdf')