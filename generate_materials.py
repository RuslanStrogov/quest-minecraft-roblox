#!/usr/bin/env python3
"""Generate all 14 SVG files for the quest - SIMPLE & ROCK SOLID.
Uses viewBox 0 0 800 1131 (A4 ratio) and standard px font sizes.
"""
import os

BASE = r"C:\Users\Ruslan\quest-minecraft-rob\materials"
os.makedirs(BASE, exist_ok=True)

W, H = 800, 1131  # viewBox dimensions (A4 ratio)

def svg(title):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#ffffff"/>
<rect x="0" y="0" width="{W}" height="24" fill="#4a7b2a"/>
<text x="20" y="17" font-size="16" fill="#ffffff" font-family="Arial,sans-serif">{title}</text>
'''

def end():
    return '</svg>\n'

def box(x, y, w, h, fill="#f0e8d8", stroke="#8b6914", sw=2, rx=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def cut(x, y, w, h):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#888" stroke-width="1" stroke-dasharray="6,4"/>'

def txt(x, y, s, size=18, color="#333", align="start", bold="normal"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-family="Arial,sans-serif" text-anchor="{align}" font-weight="{bold}">{s}</text>'

def wb(x, y, w, h, colors=("#3d6b1e","#5a8c3a"), size=4):
    """Pixel border"""
    p = []
    for i in range(int(w/size)):
        p.append(f'<rect x="{x+i*size}" y="{y}" width="{size}" height="{size}" fill="{colors[i%2]}"/>')
        p.append(f'<rect x="{x+i*size}" y="{y+h-size}" width="{size}" height="{size}" fill="{colors[(i+1)%2]}"/>')
    for i in range(int(h/size)):
        p.append(f'<rect x="{x}" y="{y+i*size}" width="{size}" height="{size}" fill="{colors[i%2]}"/>')
        p.append(f'<rect x="{x+w-size}" y="{y+i*size}" width="{size}" height="{size}" fill="{colors[(i+1)%2]}"/>')
    return '\n'.join(p)


# ─── 1. NOTES ─────────────────────────────────────────────────
def gen_notes():
    s = [svg("Записки — распечатай и вырежи")]
    cards = [
        ("Записка №1", "Ресурс №1 — КРИСТАЛЛЫ ГЛУБИН", [
            "Игроки заспавнились!",
            "Нужно собрать 4 легендарных ресурса,",
            "чтобы открыть портал в Энд.",
            "",
            "Ресурс №1 — КРИСТАЛЛЫ ГЛУБИН",
            "Ищи там, где земля встречается",
            "с камнем. Подсказка: у бордюра,",
            "где любит сидеть кот.",
        ]),
        ("Записка №2", "Ресурс №2 — ПЛАМЯ ВЫНОСЛИВОСТИ", [
            "Крафт активирован!",
            "Положи 3 кристалла в ячейки —",
            "получишь Алмазный клинок.",
            "",
            "--- Новое задание ---",
            "Преодолей лавовый трек, не",
            "наступив на красное. Там, где",
            "ветки становятся мостом.",
        ]),
        ("Записка №3", "Ресурс №3 — СЛЁЗЫ МОБА", [
            "Паркур пройден! Ты получил",
            "ПЛАМЯ ВЫНОСЛИВОСТИ.",
            "",
            "--- Новое задание ---",
            "Иди туда, где живёт Зомби.",
            "Победи его 3 мячами —",
            "он выронит слезу.",
        ]),
        ("Записка №4", "Ресурс №4 — ПЕРВОРОДНАЯ ПЫЛЬ", [
            "Моб повержен! СЛЁЗЫ МОБА",
            "твои!",
            "",
            "--- Новое задание ---",
            "Ищи в самом неожиданном месте:",
            "туда, куда ты обычно не",
            "смотришь.",
        ]),
        ("Записка №5", "ФИНАЛ — ЭНДЕР-ДРАКОН", [
            "Ресурс №5 уже у тебя — это",
            "СИЛА ДВОИХ (вы в команде!)",
            "",
            "Неси ВСЕ 4 ресурса к",
            "фиолетовому порталу.",
            "Когда все на месте —",
            "появится ЭНДЕР-ДРАКОН!",
        ]),
    ]
    positions = [(20, 30), (280, 30), (540, 30), (20, 600), (280, 600)]
    cw, ch = 240, 500
    for (num, title, lines), (cx, cy) in zip(cards, positions):
        s.append(cut(cx-5, cy-5, cw+10, ch+10))
        s.append(box(cx, cy, cw, ch, "#f5e6c8", "#8b6914"))
        s.append(wb(cx+5, cy+5, cw-10, ch-10, ("#4a7b2a","#5a8c3a"), 3))
        s.append(txt(cx+cw/2, cy+20, num, 16, "#5a3a1a", "middle", "bold"))
        s.append(txt(cx+cw/2, cy+40, title, 14, "#3d2b0a", "middle", "bold"))
        for i, line in enumerate(lines):
            s.append(txt(cx+15, cy+80+i*24, line, 12, "#3d2b0a"))
    s.append(txt(400, 1100, "Вырежи по пунктиру", 14, "#999", "middle"))
    with open(os.path.join(BASE, "01-zapiski-all.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  01-zapiski-all.svg")


# ─── 2. DIAMONDS ──────────────────────────────────────────────
def gen_diamonds():
    s = [svg("Алмазы — вырежи, обведи на картоне, раскрась голубым")]
    positions = [(90, 80), (400, 80), (90, 410), (400, 410), (90, 740), (400, 740)]
    dw, dh = 200, 280
    for cx, cy in positions:
        s.append(cut(cx-5, cy-5, dw+10, dh+10))
        s.append(box(cx, cy, dw, dh, "#b8e8f8", "#4a8ab8", 3, 12))
        # Diamond shape
        pts = f'{cx+dw/2},{cy+60} {cx+dw/2+60},{cy+100} {cx+dw/2+80},{cy+130} {cx+dw/2},{cy+220} {cx+dw/2-80},{cy+130} {cx+dw/2-60},{cy+100}'
        s.append(f'<polygon points="{pts}" fill="#c8e8f8" stroke="#4a8ab8" stroke-width="3"/>')
        s.append(f'<line x1="{cx+dw/2}" y1="{cy+60}" x2="{cx+dw/2}" y2="{cy+220}" stroke="#6aadd8" stroke-width="2" opacity="0.5"/>')
        s.append(f'<polygon points="{cx+dw/2-20},{cy+65} {cx+dw/2+20},{cy+65} {cx+dw/2+10},{cy+80}" fill="white" opacity="0.6"/>')
        s.append(txt(cx+dw/2, cy+260, "✦ АЛМАЗ ✦", 22, "#4a8ab8", "middle", "bold"))
        s.append(txt(cx+dw/2, cy+280, "Кристалл Глубины", 14, "#6aadd8", "middle"))
    s.append(txt(400, 1100, "Вырежи → обведи на картоне → раскрась голубым акрилом", 14, "#999", "middle"))
    with open(os.path.join(BASE, "02-diamonds.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  02-diamonds.svg")


# ─── 3. SWORD ─────────────────────────────────────────────────
def gen_sword():
    s = [svg("Алмазный клинок — шаблон (печатать 2 копии, склеить, на картон, в фольгу)")]
    cx, cy = 400, 400
    # Blade
    s.append(f'<polygon points="{cx-45},{cy+50} {cx},{cy-250} {cx+45},{cy+50}" fill="#b0d8f0" stroke="#4a8ab8" stroke-width="4"/>')
    s.append(f'<polygon points="{cx},{cy-250} {cx+30},{cy+50} {cx+45},{cy+50}" fill="#8abce0" opacity="0.6"/>')
    s.append(f'<line x1="{cx}" y1="{cy-250}" x2="{cx}" y2="{cy+60}" stroke="white" stroke-width="4" opacity="0.4"/>')
    s.append(f'<polygon points="{cx-25},{cy-220} {cx+25},{cy-220} {cx+15},{cy-230}" fill="white" opacity="0.7"/>')
    # Guard
    s.append(f'<rect x="{cx-120}" y="{cy+55}" width="240" height="40" rx="6" fill="#5a3a1a" stroke="#3a2510" stroke-width="3"/>')
    s.append(f'<circle cx="{cx}" cy="{cy+75}" r="12" fill="#d4a84a"/>')
    # Handle
    s.append(f'<rect x="{cx-30}" y="{cy+95}" width="60" height="140" rx="8" fill="#3a2510" stroke="#2a1a08" stroke-width="3"/>')
    for i in range(6):
        gy = cy + 105 + i * 22
        s.append(f'<line x1="{cx-20}" y1="{gy}" x2="{cx+20}" y2="{gy}" stroke="#8b6914" stroke-width="3"/>')
    # Pommel
    s.append(f'<circle cx="{cx}" cy="{cy+250}" r="30" fill="#4a8ab8" stroke="#3a6a98" stroke-width="3"/>')
    s.append(f'<circle cx="{cx}" cy="{cy+250}" r="12" fill="#8ad4f0"/>')
    # Cut outline
    s.append(f'<rect x="{cx-140}" y="{cy-270}" width="280" height="540" fill="none" stroke="#888" stroke-width="1.5" stroke-dasharray="8,6"/>')
    # Size
    s.append(txt(400, 1100, "Длина ~65 см | Распечатай 2 копии → склей → на картон → обклей фольгой", 16, "#666", "middle"))
    with open(os.path.join(BASE, "03-diamond-sword.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  03-diamond-sword.svg")


# ─── 4. LAVA BLOCKS ───────────────────────────────────────────
def gen_lava():
    s = [svg("Лавовые блоки — для паркура (заламинировать)")]
    colors = ["#e84420","#e86020","#d43010","#f05030","#e84018","#f06020",
              "#cc3a18","#e85525","#f04820","#d44020","#e87030","#cc3010"]
    pos = [(60,60),(260,60),(460,60),(660,60),
           (60,240),(260,240),(460,240),(660,240),
           (60,420),(260,420),(460,420),(660,420)]
    bw, bh = 160, 160
    for idx, (x, y) in enumerate(pos):
        c = colors[idx]
        s.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="4" fill="{c}" stroke="#aa2a10" stroke-width="3"/>')
        s.append(f'<ellipse cx="{x+bw/2}" cy="{y+bh/2}" rx="{bw/3}" ry="{bh/3}" fill="#ff8800" opacity="0.3"/>')
        # cracks
        s.append(f'<line x1="{x+30}" y1="{y+30}" x2="{x+110}" y2="{y+100}" stroke="#ffcc00" stroke-width="4" opacity="0.6"/>')
        s.append(f'<line x1="{x+100}" y1="{y+20}" x2="{x+40}" y2="{y+120}" stroke="#ffcc00" stroke-width="3" opacity="0.5"/>')
        s.append(f'<line x1="{x+120}" y1="{y+110}" x2="{x+50}" y2="{y+40}" stroke="#ff8800" stroke-width="2" opacity="0.5"/>')
        s.append(txt(x+bw/2, y+bh/2+8, "НЕ НАСТУПАТЬ!", 18, "#ffdd66", "middle", "bold"))
    s.append(txt(400, 1100, "Разложить на земле — наступать нельзя! Заламинировать от дождя.", 16, "#cc3300", "middle", "bold"))
    with open(os.path.join(BASE, "04-lava-blocks.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  04-lava-blocks.svg")


# ─── 5. HEARTS ────────────────────────────────────────────────
def gen_hearts():
    s = [svg("Сердечки HP — по 5 на каждого игрока")]
    for row in range(3):
        for col in range(4):
            cx, cy = 80 + col * 180, 80 + row * 320
            s.append(cut(cx-10, cy-10, 160, 280))
            # Heart shape
            s.append(f'<circle cx="{cx+50}" cy="{cy+55}" r="45" fill="#e83030" stroke="#aa1010" stroke-width="4"/>')
            s.append(f'<circle cx="{cx+110}" cy="{cy+55}" r="45" fill="#e83030" stroke="#aa1010" stroke-width="4"/>')
            s.append(f'<polygon points="{cx+20},{cy+100} {cx+140},{cy+100} {cx+80},{cy+160}" fill="#e83030" stroke="#aa1010" stroke-width="4"/>')
            s.append(f'<circle cx="{cx+60}" cy="{cy+30}" r="14" fill="white" opacity="0.4"/>')
            s.append(txt(cx+80, cy+200, "❤ HP", 28, "#aa1010", "middle", "bold"))
    s.append(txt(400, 1100, "10 сердечек — по 5 каждому игроку. Выдать перед финалом.", 14, "#999", "middle"))
    with open(os.path.join(BASE, "05-hp-hearts.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  05-hp-hearts.svg")


# ─── 6. FLAME ─────────────────────────────────────────────────
def gen_flame():
    s = [svg("Пламя выносливости — вырежи, прикрепи к мишуре")]
    for i, (cx, cy) in enumerate([(200, 200), (600, 200)]):
        s.append(cut(cx-100, cy-100, 200, 320))
        # Outer flame
        pts = f'{cx},{cy+120} {cx+30},{cy+60} {cx+60},{cy+10} {cx+90},{cy-30} {cx+60},{cy-60} {cx+20},{cy-30} {cx-20},{cy+10} {cx-30},{cy+60} {cx},{cy+120}'
        s.append(f'<polygon points="{pts}" fill="#ff6600" stroke="#cc4400" stroke-width="3"/>')
        # Inner flame
        pts2 = f'{cx+5},{cy+100} {cx+25},{cy+55} {cx+45},{cy+15} {cx+65},{cy-20} {cx+45},{cy-45} {cx+15},{cy-20} {cx-5},{cy+15} {cx-15},{cy+55} {cx+5},{cy+100}'
        s.append(f'<polygon points="{pts2}" fill="#ffcc00"/>')
        # Core
        pts3 = f'{cx+12},{cy+70} {cx+25},{cy+40} {cx+35},{cy+10} {cx+25},{cy-15} {cx+12},{cy+5} {cx+5},{cy+30} {cx+12},{cy+70}'
        s.append(f'<polygon points="{pts3}" fill="#ffee88"/>')
        s.append(txt(cx, cy-60, "ПЛАМЯ", 24, "#ff6600", "middle", "bold"))
        s.append(txt(cx, cy-35, "ВЫНОСЛИВОСТИ", 14, "#ff6600", "middle"))
    s.append(txt(400, 700, "Маленькие пламена (запасные)", 14, "#666", "middle"))
    for cx, cy in [(100, 760), (300, 760), (500, 760), (700, 760)]:
        s.append(f'<polygon points="{cx},{cy} {cx+15},{cy-30} {cx+30},{cy-55} {cx+20},{cy-70} {cx+5},{cy-50} {cx-5},{cy-30} {cx},{cy}" fill="#ff6600"/>')
        s.append(f'<polygon points="{cx+5},{cy-5} {cx+12},{cy-28} {cx+20},{cy-48} {cx+15},{cy-60} {cx+5},{cy-40} {cx-2},{cy-25} {cx+5},{cy-5}" fill="#ffcc00"/>')
    s.append(txt(400, 1100, "Вырежи 2 больших + запасные. Прикрепи к жёлтой мишуре.", 14, "#666", "middle"))
    with open(os.path.join(BASE, "06-flame-endurance.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  06-flame-endurance.svg")


# ─── 7. TEAR ──────────────────────────────────────────────────
def gen_tear():
    s = [svg("Слеза моба — этикетки для бусин (вырежи, наклей)")]
    for idx in range(8):
        col, row = idx % 4, idx // 4
        cx, cy = 40 + col * 180, 40 + row * 260
        s.append(cut(cx-5, cy-5, 160, 230))
        s.append(box(cx, cy, 150, 220, "#e8e0f8", "#7a5a9a", 3, 10))
        # Tear
        tx, ty = cx + 75, cy + 60
        s.append(f'<circle cx="{tx}" cy="{ty}" r="30" fill="#6088c8" stroke="#4060a0" stroke-width="3"/>')
        s.append(f'<polygon points="{tx-15},{ty+30} {tx+15},{ty+30} {tx},{ty+60}" fill="#6088c8" stroke="#4060a0" stroke-width="3"/>')
        s.append(f'<circle cx="{tx-10}" cy="{ty-10}" r="10" fill="white" opacity="0.4"/>')
        s.append(txt(cx+75, cy+130, "СЛЕЗА МОБА", 18, "#4060a0", "middle", "bold"))
        s.append(txt(cx+75, cy+160, "💧", 30, "#4060a0", "middle"))
    s.append(txt(400, 1100, "Вырежи, наклей на синюю бусину или камешек", 14, "#666", "middle"))
    with open(os.path.join(BASE, "07-mob-tear.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  07-mob-tear.svg")


# ─── 8. DRAGON MASK ───────────────────────────────────────────
def gen_dragon():
    s = [svg("Маска дракона — рога (стр.1) + накидка (стр.2) — вырежи из картона и ткани")]
    # Page 1: Horns
    s.append(txt(400, 40, "=== СТРАНИЦА 1: РОГА ===", 20, "#333", "middle", "bold"))
    s.append(txt(400, 65, "Вырежи из картона, согни по линии, приклей скотчем к каске", 14, "#666", "middle"))
    for i, (cx, cy) in enumerate([(200, 250), (600, 250)]):
        s.append(cut(cx-130, cy-130, 260, 380))
        hp = f'M{cx-60},{cy+120} L{cx-30},{cy+60} L{cx+10},{cy-10} L{cx},{cy-60} L{cx-20},{cy-90} L{cx+20},{cy-110} L{cx+80},{cy-130} Z'
        s.append(f'<path d="{hp}" fill="#4a2a10" stroke="#3a1a08" stroke-width="4"/>')
        for t in range(6):
            ty2 = cy + 100 - t * 35
            s.append(f'<line x1="{cx-50+t*5}" y1="{ty2}" x2="{cx-30+t*10}" y2="{ty2-10}" stroke="#6a3a18" stroke-width="2" opacity="0.5"/>')
        s.append(txt(cx, cy-150, f'{"ЛЕВЫЙ" if i==0 else "ПРАВЫЙ"} РОГ', 18, "#333", "middle", "bold"))
        s.append(f'<line x1="{cx-60}" y1="{cy+120}" x2="{cx+80}" y2="{cy+120}" stroke="#999" stroke-width="2" stroke-dasharray="6,4"/>')
        s.append(txt(cx, cy+150, "Согни по линии", 12, "#999", "middle"))
    s.append(txt(400, 510, "=== СТРАНИЦА 2: НАКИДКА ===", 20, "#333", "middle", "bold"))
    s.append(txt(400, 535, "Вырежи из чёрной/фиолетовой ткани. Пришей завязки.", 14, "#666", "middle"))
    # Cape
    s.append(cut(40, 560, 720, 520))
    s.append(f'<path d="M160,590 L80,1040 L720,1040 L640,590" fill="#3a1a5a" stroke="#5a2a7a" stroke-width="3" opacity="0.5"/>')
    # scalloped bottom
    for i in range(8):
        sx = 80 + i * 80
        s.append(f'<path d="M{sx},{1040} Q{sx+20},{1020} {sx+40},{1050}" fill="#3a1a5a" stroke="#5a2a7a" stroke-width="2" opacity="0.5"/>')
    s.append(txt(400, 1080, "Пришей/приклей завязки по краям", 12, "#666", "middle"))
    with open(os.path.join(BASE, "08-dragon-mask.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  08-dragon-mask.svg")


# ─── 9. CHEST LABELS ──────────────────────────────────────────
def gen_chests():
    s = [svg("Этикетки для сундуков — вырежи, наклей на коробки")]
    chests = [
        (30, 30, "★ СУНДУК ★", "(внутри ресурсы)"),
        (430, 30, "ГЛАВНЫЙ СУНДУК", "(подарки!)"),
        (30, 600, "СУНДУК РЕСУРСОВ", ""),
        (430, 600, "ТАЙНИК", ""),
    ]
    for cx, cy, title, sub in chests:
        s.append(cut(cx-5, cy-5, 340, 500))
        s.append(box(cx, cy, 330, 490, "#b8956a", "#6b4f2e", 3, 10))
        # Brick pattern
        for row in range(10):
            for col in range(6):
                bx = cx + 15 + col * 50 + (row % 2) * 25
                by = cy + 20 + row * 46
                s.append(f'<rect x="{bx}" y="{by}" width="45" height="38" rx="3" fill="#8b6914" opacity="0.6"/>')
        # Iron bands
        s.append(f'<rect x="{cx+15}" y="{cy+140}" width="300" height="20" rx="4" fill="#888" stroke="#555" stroke-width="2"/>')
        s.append(f'<rect x="{cx+15}" y="{cy+320}" width="300" height="20" rx="4" fill="#888" stroke="#555" stroke-width="2"/>')
        # Lock
        s.append(f'<rect x="{cx+120}" y="{cy+220}" width="80" height="60" rx="8" fill="#c8a830" stroke="#a08820" stroke-width="3"/>')
        s.append(f'<circle cx="{cx+160}" cy="{cy+250}" r="12" fill="#a08820"/>')
        s.append(txt(cx+165, cy+460, title, 32, "#3d2b0a", "middle", "bold"))
        if sub:
            s.append(txt(cx+165, cy+490, sub, 16, "#3d2b0a", "middle"))
    s.append(txt(400, 1100, "Наклей на картонные коробки, обклеенные коричневой бумагой", 14, "#666", "middle"))
    with open(os.path.join(BASE, "09-chest-labels.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  09-chest-labels.svg")


# ─── 10. CRAFT GRID ───────────────────────────────────────────
def gen_craft():
    s = [svg("Крафт-станция 3×3 — для стола")]
    s.append(box(50, 50, 700, 500, "#f0e8d8", "#8b6914", 4, 15))
    s.append(txt(400, 30, "КРАФТ-СТАНОК 3×3", 28, "#6b4f2e", "middle", "bold"))
    cs = 200
    gx, gy = 100, 80
    for row in range(3):
        for col in range(3):
            x, y = gx + col * (cs+20), gy + row * (cs+20)
            s.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="#e0d4b8" stroke="#6b4f2e" stroke-width="3"/>')
            if row == 0:
                # Diamond slot
                cx2, cy2 = x + cs/2, y + cs/2
                pts = f'{cx2},{cy2-40} {cx2+30},{cy2-15} {cx2+45},{cy2+20} {cx2},{cy2+40} {cx2-45},{cy2+20} {cx2-30},{cy2-15}'
                s.append(f'<polygon points="{pts}" fill="#c8e8f8" stroke="#4a8ab8" stroke-width="2" opacity="0.8"/>')
                s.append(txt(cx2, cy2+30, "✦", 24, "#4a8ab8", "middle"))
            else:
                s.append(f'<line x1="{x+30}" y1="{y+30}" x2="{x+cs-30}" y2="{y+cs-30}" stroke="#a09070" stroke-width="2" opacity="0.4"/>')
                s.append(f'<line x1="{x+cs-30}" y1="{y+30}" x2="{x+30}" y2="{y+cs-30}" stroke="#a09070" stroke-width="2" opacity="0.4"/>')
    # Instruction box
    s.append(box(50, 600, 700, 420, "#f5e6c8", "#8b6914", 3, 12))
    s.append(txt(400, 635, "КАК РАБОТАЕТ КРАФТ", 22, "#6b4f2e", "middle", "bold"))
    lines = [
        "1. Игроки кладут 3 КРИСТАЛЛА ГЛУБИНЫ в верхние ячейки (ряд с алмазами ✦).",
        "2. Ведущий (мама/помощник) проверяет — ВСЁ ВЕРНО!",
        "3. Вручает АЛМАЗНЫЙ КЛИНОК (картонный меч, обклеенный фольгой).",
        "",
        "★ Рецепт: 3 × Кристалл Глубины = Алмазный Клинок +1 ★",
    ]
    for i, line in enumerate(lines):
        s.append(txt(70, 680+i*36, line, 16, "#3d2b0a"))
    with open(os.path.join(BASE, "10-craft-grid.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  10-craft-grid.svg")


# ─── 11. PROGRESS MAP ─────────────────────────────────────────
def gen_map():
    s = [svg("Карта прогресса — наклей собранные ресурсы (заламинировать)")]
    s.append(box(10, 10, 780, 1110, "#f0e0c8", "#8b6914", 4, 20))
    s.append(txt(400, 45, "🗺 КАРТА ПРОГРЕССА", 36, "#3d2b0a", "middle", "bold"))
    # 4 resource slots
    sw, sh = 140, 160
    sy = 80
    colors = ["#4a8ab8", "#ff8800", "#6088c8", "#a070d0"]
    labels = ["Кристаллы\nГлубины", "Пламя\nВыносливости", "Слёзы\nМоба", "Первородная\nПыль"]
    icons = ["💎", "🔥", "💧", "✨"]
    for i in range(4):
        sx = 50 + i * 180
        s.append(box(sx, sy, sw, sh, "#e8dcc8", colors[i], 3, 10))
        s.append(txt(sx+sw/2, sy+35, icons[i], 30, colors[i], "middle"))
        for li, l in enumerate(labels[i].split('\n')):
            s.append(txt(sx+sw/2, sy+70+li*28, l, 16, "#3d2b0a", "middle"))
        s.append(f'<circle cx="{sx+sw/2}" cy="{sy+sh-20}" r="16" fill="white" stroke="#666" stroke-width="2" stroke-dasharray="4,3"/>')
        s.append(txt(sx+sw/2, sy+sh-16, "✓", 16, "#999", "middle"))
    # Portal
    px2, py2 = 400, 300
    s.append(f'<ellipse cx="{px2}" cy="{py2}" rx="120" ry="90" fill="none" stroke="#8844bb" stroke-width="6"/>')
    s.append(f'<ellipse cx="{px2}" cy="{py2}" rx="100" ry="70" fill="#6a30a0" opacity="0.3"/>')
    s.append(f'<ellipse cx="{px2}" cy="{py2}" rx="80" ry="50" fill="#9955cc" opacity="0.3"/>')
    s.append(txt(px2, py2-10, "ПОРТАЛ", 28, "#cc88ff", "middle", "bold"))
    s.append(txt(px2, py2+15, "В ЭНД", 20, "#cc88ff", "middle"))
    # Players
    ty = 500
    s.append(box(20, ty, 760, 120, "#e0d4b8", "#8b6914", 3, 12))
    s.append(txt(400, ty+30, "🏃 ИГРОКИ НА ТРОПЕ", 24, "#6b4f2e", "middle", "bold"))
    for i in range(2):
        ax = 50 + i * 380
        s.append(f'<circle cx="{ax+100}" cy="{ty+80}" r="30" fill="#4a7b2a"/>')
        s.append(txt(ax, ty+85, f"Игрок {i+1}: ______", 18, "#3d2b0a"))
    # Stickers
    sty = 660
    s.append(box(10, sty, 780, 180, "#f5ecc8", "#8b6914", 3, 15))
    s.append(txt(400, sty+30, "📋 НАКЛЕЙКИ (вырежи отдельно)", 22, "#6b4f2e", "middle", "bold"))
    for i, (ic, co) in enumerate([("💎","#4a8ab8"),("🔥","#ff8800"),("💧","#6088c8"),("✨","#a070d0")]):
        sx2 = 50 + i * 180
        s.append(f'<circle cx="{sx2+80}" cy="{sty+100}" r="35" fill="none" stroke="#888" stroke-width="1.5" stroke-dasharray="6,4"/>')
        s.append(f'<circle cx="{sx2+80}" cy="{sty+100}" r="30" fill="{co}" opacity="0.3"/>')
        s.append(txt(sx2+80, sty+105, ic, 28, co, "middle"))
        s.append(txt(sx2+80, sty+150, f"Ресурс {i+1}", 14, "#666", "middle"))
    # Info
    s.append(txt(400, 1100, "По ходу квеста дети наклеивают стикеры на собранные ресурсы. Заламинировать!", 14, "#666", "middle"))
    with open(os.path.join(BASE, "11-progress-map.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  11-progress-map.svg")


# ─── 12. SIGNS ────────────────────────────────────────────────
def gen_signs():
    s = [svg("Таблички — SCP, obby, портал (вырежи, повесь)")]
    # SCP signs
    for i, (cx, cy) in enumerate([(30, 30), (430, 30)]):
        s.append(cut(cx-5, cy-5, 340, 300))
        s.append(box(cx, cy, 330, 290, "#d8d8d8", "#666", 3, 8))
        s.append(f'<rect x="{cx}" y="{cy}" width="330" height="50" rx="8" fill="#cc2222"/>')
        s.append(txt(cx+165, cy+30, "⚠ SCP ОБЪЕКТ ⚠", 24, "white", "middle", "bold"))
        s.append(f'<circle cx="{cx+165}" cy="{cy+160}" r="50" fill="none" stroke="#333" stroke-width="6"/>')
        s.append(f'<circle cx="{cx+165}" cy="{cy+160}" r="25" fill="none" stroke="#333" stroke-width="4"/>')
        s.append(txt(cx+165, cy+250, "ЗОМБИ-МОБ", 22, "#333", "middle", "bold"))
        s.append(txt(cx+165, cy+280, "Победи 3 мячами!", 14, "#666", "middle"))
    # obby signs
    for i, (cx, cy) in enumerate([(30, 380), (430, 380)]):
        s.append(cut(cx-5, cy-5, 340, 300))
        s.append(box(cx, cy, 330, 290, "#e8f0e8", "#4a8a3a", 3, 8))
        s.append(f'<rect x="{cx}" y="{cy}" width="330" height="50" rx="8" fill="#4a8a3a"/>')
        s.append(txt(cx+165, cy+30, "obby", 28, "white", "middle", "bold"))
        s.append(txt(cx+165, cy+130, f"ЭТАЖ {i+1}", 60, "#4a8a3a", "middle", "bold"))
        s.append(f'<rect x="{cx+110}" y="{cy+180}" width="40" height="70" fill="#cc4444" rx="4"/>')
        s.append(f'<rect x="{cx+110}" y="{cy+170}" width="40" height="15" fill="#888" rx="2"/>')
        s.append(txt(cx+165, cy+260, "ПРЕОДОЛЕЙ ЛАВУ!", 16, "#4a8a3a", "middle"))
        s.append(txt(cx+165, cy+280, "Не наступай на красное", 12, "#666", "middle"))
    # Portal sign
    s.append(txt(400, 700, "=== ПОРТАЛ В ЭНД (большая табличка) ===", 22, "#7733aa", "middle", "bold"))
    s.append(cut(30, 730, 740, 320))
    s.append(box(30, 730, 740, 320, "#d8b0f0", "#7733aa", 4, 15))
    s.append(f'<ellipse cx="400" cy="840" rx="180" ry="100" fill="#9955cc" opacity="0.3"/>')
    s.append(f'<ellipse cx="400" cy="840" rx="140" ry="70" fill="#bb77ee" opacity="0.3"/>')
    s.append(txt(400, 785, "🌀 ПОРТАЛ В ЭНД", 42, "#aa44dd", "middle", "bold"))
    s.append(txt(400, 825, "THE VOID", 24, "#cc66ff", "middle", "bold"))
    s.append(txt(400, 940, "Собери все 4 ресурса и возвращайся сюда!", 20, "#7733aa", "middle"))
    s.append(txt(400, 975, "Когда все на месте — появится ЭНДЕР-ДРАКОН 🐉", 20, "#7733aa", "middle"))
    with open(os.path.join(BASE, "12-scp-obby-signs.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  12-scp-obby-signs.svg")


# ─── 13. OBBY FLOOR SIGNS ─────────────────────────────────────
def gen_obby():
    s = [svg("Obby — номера этажей для паркура")]
    pos = [(80, 80), (400, 80), (80, 420), (400, 420), (240, 760)]
    for i, (cx, cy) in enumerate(pos):
        s.append(cut(cx-10, cy-10, 280, 310))
        s.append(box(cx, cy, 260, 290, "#d8f0d8", "#3a7a2a", 3, 10))
        s.append(f'<rect x="{cx}" y="{cy}" width="260" height="55" rx="10" fill="#3a7a2a"/>')
        s.append(txt(cx+130, cy+33, "obby", 26, "white", "middle", "bold"))
        s.append(txt(cx+130, cy+190, f"{i+1}", 90, "#3a7a2a", "middle", "bold"))
        s.append(f'<rect x="{cx+190}" y="{cy+220}" width="30" height="60" fill="#44aa44" rx="4"/>')
        s.append(txt(cx+130, cy+270, "ЧЕКПОИНТ", 16, "#3a7a2a", "middle"))
    with open(os.path.join(BASE, "13-obby-floor-signs.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  13-obby-floor-signs.svg")


# ─── 14. CHEST WRAP ───────────────────────────────────────────
def gen_wrap():
    s = [svg("Обклейка для сундуков — текстура под дерево (печатать 4+ листов)")]
    bw, bh, gap = 100, 50, 6
    for row in range(18):
        for col in range(7):
            bx = 8 + col * (bw + gap) + (row % 2) * ((bw + gap) / 2)
            by = 30 + row * (bh + gap)
            if bx + bw > 790:
                continue
            shade = ["#b8956a","#c8a070","#a08050","#b89060","#c0a068","#b08858","#c8a870"][(row+col)%7]
            s.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="4" fill="{shade}" stroke="#8b6914" stroke-width="2"/>')
            if (row+col)%3 == 0:
                s.append(f'<line x1="{bx+20}" y1="{by+12}" x2="{bx+bw-20}" y2="{by+bh-12}" stroke="#7a5a30" stroke-width="2" opacity="0.4"/>')
    s.append(txt(400, 1100, "Обклей коробки — получатся сундуки", 16, "#6b4f2e", "middle", "bold"))
    with open(os.path.join(BASE, "14-chest-wrap.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(s))
    print("  14-chest-wrap.svg")


# ─── MAIN ─────────────────────────────────────────────────────
if __name__ == "__main__":
    os.makedirs(BASE, exist_ok=True)
    print("Генерация SVG (viewBox 800x1131, px-шрифты)...")
    gen_notes()
    gen_diamonds()
    gen_sword()
    gen_lava()
    gen_hearts()
    gen_flame()
    gen_tear()
    gen_dragon()
    gen_chests()
    gen_craft()
    gen_map()
    gen_signs()
    gen_obby()
    gen_wrap()
    print("Готово! 14 SVG-файлов в materials/")