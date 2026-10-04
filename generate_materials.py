#!/usr/bin/env python3
"""Generate all printable materials for Minecraft+Roblox birthday quest."""
import os, math

BASE = r"C:\Users\Ruslan\quest-minecraft-rob\materials"

def svg_header(title):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">
<defs>
<style>
  @page {{ margin: 0; }}
  text {{ font-family: 'Segoe UI', 'Arial', sans-serif; }}
  .title {{ font-size: 7mm; font-weight: bold; }}
  .sub {{ font-size: 4.5mm; }}
  .body {{ font-size: 3.5mm; }}
  .small {{ font-size: 2.8mm; }}
  .cutline {{ stroke: #666; stroke-width: 0.3; stroke-dasharray: 3,2; fill: none; }}
  .foldline {{ stroke: #999; stroke-width: 0.2; stroke-dasharray: 1,3; fill: none; }}
</style>
</defs>
<rect width="210" height="297" fill="white"/>
<text x="15" y="12" class="title" fill="#333">{title}</text>
<line x1="15" y1="13.5" x2="195" y2="13.5" stroke="#ccc" stroke-width="0.3"/>
'''

def svg_footer():
    return '</svg>\n'

def rounded_rect(x, y, w, h, r=2, fill="#f5e6c8", stroke="#8b6914", sw=0.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def minecraft_border(x, y, w, h, colors=("#3d6b1e", "#5a8c3a")):
    parts = []
    size = 2
    cols = int(w / size)
    rows = int(h / size)
    for i in range(cols):
        parts.append(f'<rect x="{x+i*size}" y="{y}" width="{size}" height="{size}" fill="{colors[i%2]}"/>')
        parts.append(f'<rect x="{x+i*size}" y="{y+h-size}" width="{size}" height="{size}" fill="{colors[(i+1)%2]}"/>')
    for i in range(rows):
        parts.append(f'<rect x="{x}" y="{y+i*size}" width="{size}" height="{size}" fill="{colors[i%2]}"/>')
        parts.append(f'<rect x="{x+w-size}" y="{y+i*size}" width="{size}" height="{size}" fill="{colors[(i+1)%2]}"/>')
    return '\n'.join(parts)

def note_card(x, y, w, h, num, title_text, body_lines):
    parts = []
    parts.append(f'<rect x="{x+1}" y="{y+1}" width="{w}" height="{h}" rx="2" fill="rgba(0,0,0,0.15)"/>')
    parts.append(rounded_rect(x, y, w, h, 2, "#f5e6c8", "#8b6914"))
    bcolors = ["#4a7b2a", "#5a3a1a", "#7b3a1a", "#3a5a7b", "#5a2a7b"]
    parts.append(minecraft_border(x+2, y+2, w-4, h-4, (bcolors[num%5], bcolors[(num+1)%5])))
    parts.append(f'<circle cx="{x+w-8}" cy="{y+8}" r="4" fill="#d4c49a" stroke="#8b6914" stroke-width="0.3"/>')
    parts.append(f'<text x="{x+6}" y="{y+7}" class="sub" fill="#5a3a1a" font-weight="bold">Записка №{num}</text>')
    parts.append(f'<text x="{x+6}" y="{y+12}" class="body" fill="#3d2b0a" font-weight="bold">{title_text}</text>')
    cy = y + 17
    for line in body_lines:
        while len(line) > 38:
            parts.append(f'<text x="{x+6}" y="{cy}" class="small" fill="#3d2b0a">{line[:38]}</text>')
            line = "   " + line[38:]
            cy += 3.8
        parts.append(f'<text x="{x+6}" y="{cy}" class="small" fill="#3d2b0a">{line}</text>')
        cy += 3.8
    parts.append(f'<rect x="{x-0.5}" y="{y-0.5}" width="{w+1}" height="{h+1}" class="cutline"/>')
    return '\n'.join(parts)


def generate_notes():
    parts = [svg_header("Записки для квеста — распечатай и вырежи")]
    cards = [
        (1, "Ресурс №1 — КРИСТАЛЛЫ ГЛУБИН", [
            "Игроки заспавнились! Чтобы открыть", "портал в Энд и призвать дракона, нужно", "собрать 4 легендарных ресурса.", "",
            "Ресурс №1 — КРИСТАЛЛЫ ГЛУБИН", "Ищи там, где земля встречается с", "камнем, а трава шепчет: «копай здесь».", "",
            "Подсказка: у бордюра, где любит", "сидеть кот / где растёт самый", "высокий куст.",
        ]),
        (2, "Ресурс №2 — ПЛАМЯ ВЫНОСЛИВОСТИ", [
            "Крафт активирован! Положи 3", "кристалла в ячейки крафта —", "получишь Алмазный клинок.", "",
            "--- Новое задание ---",
            "Ресурс №2 — ПЛАМЯ ВЫНОСЛИВОСТИ",
            "Преодолей лавовый трек, не", "наступив на красное. Там, где", "ветки становятся мостом.",
        ]),
        (3, "Ресурс №3 — СЛЁЗЫ МОБА", [
            "Паркур пройден! Ты получил", "ПЛАМЯ ВЫНОСЛИВОСТИ", "",
            "--- Новое задание ---",
            "Ресурс №3 — СЛЁЗЫ МОБА",
            "Иди туда, где живёт Зомби",
            "(ориентир: дерево с лентой).",
            "Победи его 3 мячами — он", "выронит слезу.",
        ]),
        (4, "Ресурс №4 — ПЕРВОРОДНАЯ ПЫЛЬ", [
            "Моб повержен! СЛЁЗЫ МОБА твои!","",
            "--- Новое задание ---",
            "Ресурс №4 — ПЕРВОРОДНАЯ ПЫЛЬ",
            "Ищи в самом неожиданном месте:",
            "туда, куда ты обычно не смотришь.",
            "(почтовый ящик / тайник под",
            "крыльцом / коробка)",
        ]),
        (5, "ФИНАЛ — ЭНДЕР-ДРАКОН", [
            "Ресурс №5 уже у тебя — это", "СИЛА ДВОИХ (вы в команде!).", "",
            "Неси ВСЕ 4 ресурса к фиолетовому", "порталу. Когда все на месте —", "появится ЭНДЕР-ДРАКОН!", "",
            "Победи его и получишь ГЛАВНЫЙ", "СУНДУК с подарками!",
        ]),
    ]
    positions = [(8,12),(72,12),(136,12),(8,155),(72,155)]
    cw, ch = 62, 140
    for (num, title, body), (cx, cy) in zip(cards, positions):
        parts.append(note_card(cx, cy, cw, ch, num, title, body))
    parts.append(svg_footer())
    with open(os.path.join(BASE, "notes", "01-zapiski-all.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_diamonds():
    parts = [svg_header("Алмазы (Кристаллы Глубины) — вырежи и раскрась голубым")]
    positions = [(15, 15, 2), (80, 15, 2), (145, 15, 2), (15, 110, 2), (80, 110, 2), (145, 110, 2)]
    dw, dh = 55, 85
    for cx, cy, _ in positions:
        parts.append(f'<rect x="{cx-2}" y="{cy-2}" width="{dw+4}" height="{dh+4}" class="cutline"/>')
        mx, my = cx + dw/2, cy + dh/2
        pts = f'{mx},{my-30} {mx+15},{my-12} {mx+22},{my+5} {mx},{my+30} {mx-22},{my+5} {mx-15},{my-12}'
        parts.append(f'<polygon points="{pts}" fill="#b8e8f8" stroke="#4a8ab8" stroke-width="1.5"/>')
        parts.append(f'<line x1="{mx}" y1="{my-30}" x2="{mx}" y2="{my+30}" stroke="#6aadd8" stroke-width="0.5" opacity="0.5"/>')
        parts.append(f'<line x1="{mx-15}" y1="{my-12}" x2="{mx+15}" y2="{my-12}" stroke="#6aadd8" stroke-width="0.5" opacity="0.5"/>')
        parts.append(f'<polygon points="{mx-8},{my-28} {mx+8},{my-28} {mx+3},{my-22}" fill="white" opacity="0.6"/>')
        parts.append(f'<text x="{cx+dw/2}" y="{cy+dh-5}" class="body" fill="#4a8ab8" text-anchor="middle">★ Алмаз ★</text>')
        parts.append(f'<text x="{cx+dw/2}" y="{cy+dh+8}" class="small" fill="#666" text-anchor="middle">Вырежи, покрась голубым</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "templates", "02-diamonds.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_sword():
    parts = [svg_header("Алмазный клинок — шаблон для вырезания из картона")]
    cx, cy = 105, 80
    blade_h = 150
    # Blade
    parts.append(f'<polygon points="{cx-9},{cy} {cx},{cy-150} {cx+9},{cy}" fill="#b0d8f0" stroke="#4a8ab8" stroke-width="1.5"/>')
    parts.append(f'<polygon points="{cx},{cy-150} {cx+5},{cy} {cx+9},{cy}" fill="#8abce0" opacity="0.7"/>')
    parts.append(f'<line x1="{cx}" y1="{cy-150}" x2="{cx}" y2="{cy+5}" stroke="white" stroke-width="1.5" opacity="0.5"/>')
    parts.append(f'<polygon points="{cx-5},{cy-135} {cx+5},{cy-135} {cx+3},{cy-140}" fill="white" opacity="0.8"/>')
    # Guard
    parts.append(f'<rect x="{cx-30}" y="{cy+5}" width="60" height="10" rx="2" fill="#5a3a1a" stroke="#3a2510" stroke-width="1"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy+7}" r="3" fill="#d4a84a"/>')
    # Handle
    parts.append(f'<rect x="{cx-7}" y="{cy+15}" width="14" height="50" rx="2" fill="#3a2510" stroke="#2a1a08" stroke-width="1"/>')
    for i in range(5):
        gy = cy + 18 + i * 9
        parts.append(f'<line x1="{cx-5}" y1="{gy}" x2="{cx+5}" y2="{gy}" stroke="#8b6914" stroke-width="1"/>')
    # Pommel
    parts.append(f'<circle cx="{cx}" cy="{cy+73}" r="8" fill="#4a8ab8" stroke="#3a6a98" stroke-width="1"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy+73}" r="3" fill="#8ad4f0"/>')
    # Cut line
    parts.append(f'<rect x="{cx-38}" y="{cy-158}" width="76" height="240" class="cutline"/>')
    parts.append(f'<text x="105" y="290" class="body" fill="#666" text-anchor="middle">Длина: ~65 см | Вырежи из картона, обклей фольгой</text>')
    parts.append(f'<text x="10" y="270" class="small" fill="#666">1. Распечатай 2 копии на A4  2. Склей по центру  3. Вырежи по контуру</text>')
    parts.append(f'<text x="10" y="278" class="small" fill="#666">4. Приложи к картону, обведи  5. Вырежи из картона  6. Обклей фольгой</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "templates", "03-diamond-sword.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_lava():
    parts = [svg_header("Лавовые блоки — A4 для паркура (распечатай, заламинируй)")]
    bw, bh, gap = 60, 60, 5
    sx, sy = 10, 30
    colors = ["#e84420","#e86020","#d43010","#f05030","#e84018","#f06020",
              "#cc3a18","#e85525","#f04820","#d44020","#e87030","#cc3010"]
    for idx in range(12):
        col, row = idx % 3, idx // 3
        x = sx + col * (bw + gap)
        y = sy + row * (bh + gap)
        c = colors[idx]
        parts.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="1" fill="{c}" stroke="#aa2a10" stroke-width="1"/>')
        for _ in range(4):
            sx2 = x + 10 + (idx * 7 + _ * 13) % 40
            sy2 = y + 10 + (idx * 11 + _ * 17) % 40
            ex = sx2 + (-1 if _%2==0 else 1) * (10 + _ * 5)
            ey = sy2 + (-1 if _%3==0 else 1) * (10 + _ * 3)
            parts.append(f'<line x1="{sx2}" y1="{sy2}" x2="{ex}" y2="{ey}" stroke="#ffcc00" stroke-width="1.5" opacity="0.7"/>')
        parts.append(f'<ellipse cx="{x+bw/2}" cy="{y+bh/2}" rx="{bw/4}" ry="{bh/4}" fill="#ff8800" opacity="0.4"/>')
        parts.append(f'<text x="{x+bw/2}" y="{y+bh-5}" class="small" fill="#ffdd66" text-anchor="middle">НЕ НАСТУПАТЬ!</text>')
    parts.append(f'<text x="105" y="285" class="body" fill="#cc3300" text-anchor="middle">🔥 НАСТУПАТЬ НЕЛЬЗЯ — это лава! 🔥</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "a4-sheets", "04-lava-blocks.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_hearts():
    parts = [svg_header("Сердечки HP (здоровье) — по 5 на каждого игрока")]
    hw, hh, gap = 40, 35, 8
    sx, sy = 15, 30
    for idx in range(12):
        col, row = idx % 4, idx // 4
        cx = sx + col * (hw + gap) + hw/2
        cy = sy + row * (hh + gap) + hh/2
        parts.append(f'<rect x="{cx-hw/2-3}" y="{cy-hh/2-3}" width="{hw+6}" height="{hh+6}" class="cutline"/>')
        r = 10
        parts.append(f'<circle cx="{cx-6}" cy="{cy-5}" r="{r}" fill="#e83030" stroke="#aa1010" stroke-width="1.5"/>')
        parts.append(f'<circle cx="{cx+6}" cy="{cy-5}" r="{r}" fill="#e83030" stroke="#aa1010" stroke-width="1.5"/>')
        parts.append(f'<polygon points="{cx-13},{cy+3} {cx+13},{cy+3} {cx},{cy+15}" fill="#e83030" stroke="#aa1010" stroke-width="1.5"/>')
        parts.append(f'<circle cx="{cx-4}" cy="{cy-8}" r="3" fill="white" opacity="0.5"/>')
        parts.append(f'<text x="{cx}" y="{cy+hh/2-3}" class="small" fill="#aa1010" text-anchor="middle">❤ HP</text>')
    parts.append(f'<text x="105" y="285" class="body" fill="#cc0000" text-anchor="middle">Всего 10 сердечек (по 5 на каждого ребёнка)</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "templates", "05-hp-hearts.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_flame():
    parts = [svg_header("Пламя выносливости — шаблон для вырезания")]
    for cx, cy in [(55, 80), (160, 80)]:
        parts.append(f'<rect x="{cx-5}" y="{cy-5}" width="90" height="130" class="cutline"/>')
        parts.append(f'<polygon points="{cx+5},{cy+100} {cx+15},{cy+60} {cx+25},{cy+30} {cx+40},{cy+5} {cx+25},{cy-10} {cx+10},{cy+5} {cx},{cy+30} {cx-10},{cy+60} {cx+5},{cy+100}" fill="#ff8800" stroke="#ff6600" stroke-width="1"/>')
        parts.append(f'<polygon points="{cx+8},{cy+85} {cx+15},{cy+55} {cx+20},{cy+25} {cx+30},{cy+8} {cx+20},{cy-5} {cx+8},{cy+5} {cx-2},{cy+30} {cx-5},{cy+55} {cx+8},{cy+85}" fill="#ffcc00" stroke="#ffaa00" stroke-width="0.8"/>')
        parts.append(f'<polygon points="{cx+12},{cy+65} {cx+18},{cy+40} {cx+22},{cy+15} {cx+18},{cy+3} {cx+12},{cy+10} {cx+8},{cy+25} {cx+12},{cy+65}" fill="#ffee88" opacity="0.8"/>')
        parts.append(f'<text x="{cx+40}" y="{cy+15}" class="body" fill="#ff6600" text-anchor="middle">ПЛАМЯ</text>')
        parts.append(f'<text x="{cx+40}" y="{cy+23}" class="body" fill="#ff6600" text-anchor="middle">ВЫНОСЛИВОСТИ</text>')
    parts.append(f'<text x="105" y="215" class="body" fill="#666" text-anchor="middle">Вырежи 2 пламени, прикрепи к жёлтой мишуре</text>')
    parts.append(f'<text x="105" y="225" class="body" fill="#666" text-anchor="middle">или используй как шаблон из фетра/фоамирана</text>')
    for cx, cy in [(15, 235), (105, 235), (195, 235)]:
        parts.append(f'<polygon points="{cx},{cy} {cx+5},{cy-20} {cx+12},{cy-35} {cx+8},{cy-45} {cx+2},{cy-30} {cx-3},{cy-20} {cx},{cy}" fill="#ff8800" stroke="#ff6600" stroke-width="0.8"/>')
        parts.append(f'<polygon points="{cx+2},{cy-5} {cx+5},{cy-18} {cx+8},{cy-30} {cx+5},{cy-22} {cx+1},{cy-15} {cx-1},{cy-5} {cx+2},{cy-5}" fill="#ffcc00"/>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "templates", "06-flame-endurance.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_tear():
    parts = [svg_header("Слеза моба — этикетка для бусины/камешка")]
    for idx in range(8):
        col, row = idx % 4, idx // 4
        cx, cy = 25 + col * 48, 30 + row * 65
        parts.append(f'<rect x="{cx-3}" y="{cy-3}" width="44" height="58" class="cutline"/>')
        parts.append(rounded_rect(cx, cy, 40, 52, 3, "#e8e0f8", "#7a5a9a"))
        tx, ty = cx + 20, cy + 15
        parts.append(f'<circle cx="{tx}" cy="{ty}" r="8" fill="#6088c8" stroke="#4060a0" stroke-width="1"/>')
        parts.append(f'<polygon points="{tx-4},{ty+8} {tx+4},{ty+8} {tx},{ty+18}" fill="#6088c8" stroke="#4060a0" stroke-width="1"/>')
        parts.append(f'<circle cx="{tx-3}" cy="{ty-3}" r="2.5" fill="white" opacity="0.5"/>')
        parts.append(f'<text x="{cx+20}" y="{cy+44}" class="small" fill="#4060a0" text-anchor="middle">СЛЕЗА МОБА</text>')
    parts.append(f'<text x="105" y="285" class="body" fill="#4060a0" text-anchor="middle">💧 Вырежи, приклей на бусину или камешек</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "labels", "07-mob-tear.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_chest_labels():
    parts = [svg_header("Сундуки — этикетки для коробок")]
    for i, (cx, cy) in enumerate([(15, 15), (110, 15)]):
        parts.append(f'<rect x="{cx}" y="{cy}" width="90" height="120" class="cutline"/>')
        parts.append(rounded_rect(cx+2, cy+2, 86, 116, 3, "#b8956a", "#6b4f2e"))
        for row in range(8):
            for col in range(5):
                bx = cx + 5 + col * 17 + (row % 2) * 8.5
                by = cy + 10 + row * 14
                parts.append(f'<rect x="{bx}" y="{by}" width="15" height="12" fill="#8b6914" rx="1" opacity="0.6"/>')
        parts.append(f'<rect x="{cx+5}" y="{cy+30}" width="80" height="6" rx="1" fill="#888" stroke="#555" stroke-width="0.8"/>')
        parts.append(f'<rect x="{cx+5}" y="{cy+70}" width="80" height="6" rx="1" fill="#888" stroke="#555" stroke-width="0.8"/>')
        parts.append(f'<rect x="{cx+35}" y="{cy+50}" width="20" height="15" rx="2" fill="#c8a830" stroke="#a08820" stroke-width="1"/>')
        parts.append(f'<circle cx="{cx+45}" cy="{cy+57}" r="3" fill="#a08820"/>')
        if i == 0:
            parts.append(f'<text x="{cx+45}" y="{cy+105}" class="body" fill="#3d2b0a" text-anchor="middle">★ СУНДУК ★</text>')
            parts.append(f'<text x="{cx+45}" y="{cy+113}" class="small" fill="#3d2b0a" text-anchor="middle">(ресурсы)</text>')
        else:
            parts.append(f'<text x="{cx+45}" y="{cy+105}" class="body" fill="#3d2b0a" text-anchor="middle">ГЛАВНЫЙ СУНДУК</text>')
            parts.append(f'<text x="{cx+45}" y="{cy+113}" class="small" fill="#3d2b0a" text-anchor="middle">(подарки!)</text>')
    for i, (cx, cy) in enumerate([(15, 155), (110, 155)]):
        parts.append(f'<rect x="{cx}" y="{cy}" width="90" height="75" class="cutline"/>')
        parts.append(rounded_rect(cx+2, cy+2, 86, 71, 3, "#b8956a", "#6b4f2e"))
        for row in range(5):
            for col in range(5):
                bx = cx + 5 + col * 17 + (row % 2) * 8.5
                by = cy + 8 + row * 13
                parts.append(f'<rect x="{bx}" y="{by}" width="15" height="11" fill="#8b6914" rx="1" opacity="0.5"/>')
        parts.append(f'<rect x="{cx+35}" y="{cy+30}" width="20" height="12" rx="2" fill="#c8a830"/>')
        parts.append(f'<circle cx="{cx+45}" cy="{cy+36}" r="2.5" fill="#a08820"/>')
        items = ["СУНДУК РЕСУРСОВ", "ТАЙНИК"]
        parts.append(f'<text x="{cx+45}" y="{cy+62}" class="body" fill="#3d2b0a" text-anchor="middle">{items[i]}</text>')
    parts.append(f'<text x="105" y="285" class="body" fill="#666" text-anchor="middle">Вырежи, наклей на картонные коробки (обклеенные коричневой бумагой)</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "labels", "09-chest-labels.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_craft_grid():
    parts = [svg_header("Крафт-станция — сетка 3×3 (для стола)")]
    cs = 50
    gx, gy = 30, 40
    parts.append(f'<rect x="{gx-5}" y="{gy-5}" width="{cs*3+10}" height="{cs*3+10}" rx="3" fill="#f0e8d8" stroke="#8b6914" stroke-width="2"/>')
    for row in range(3):
        for col in range(3):
            x, y = gx + col * cs, gy + row * cs
            parts.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="#e0d4b8" stroke="#6b4f2e" stroke-width="1.5"/>')
            if row == 0:
                cx2, cy2 = x + cs/2, y + cs/2
                pts = f'{cx2},{cy2-12} {cx2+10},{cy2-5} {cx2+14},{cy2+5} {cx2},{cy2+12} {cx2-14},{cy2+5} {cx2-10},{cy2-5}'
                parts.append(f'<polygon points="{pts}" fill="#c8e8f8" stroke="#4a8ab8" opacity="0.7"/>')
                parts.append(f'<text x="{cx2}" y="{cy2+8}" class="small" fill="#4a8ab8" text-anchor="middle">✦</text>')
            else:
                parts.append(f'<line x1="{x+8}" y1="{y+8}" x2="{x+cs-8}" y2="{y+cs-8}" stroke="#a09070" stroke-width="0.8" opacity="0.4"/>')
                parts.append(f'<line x1="{x+cs-8}" y1="{y+8}" x2="{x+8}" y2="{y+cs-8}" stroke="#a09070" stroke-width="0.8" opacity="0.4"/>')
    parts.append(f'<text x="{gx+cs*1.5}" y="{gy-10}" class="body" fill="#6b4f2e" text-anchor="middle">КРАФТ-СТАНОК 3×3</text>')
    parts.append(f'<text x="{gx+cs*1.5}" y="{gy+cs*3+15}" class="sub" fill="#6b4f2e" text-anchor="middle">Положи 3 алмаза в верхний ряд → получи АЛМАЗНЫЙ КЛИНОК!</text>')
    cx2, cy2 = 30, 200
    parts.append(rounded_rect(cx2, cy2, 150, 70, 3, "#f5e6c8", "#8b6914"))
    lines = [
        "КАК РАБОТАЕТ КРАФТ:",
        "1. Игроки кладут 3 КРИСТАЛЛА ГЛУБИНЫ в верхние",
        "   ячейки крафт-станции (ряд ✦).",
        "2. Ведущий (мама/помощник) проверяет — ВСЁ ВЕРНО!",
        "3. Вручает АЛМАЗНЫЙ КЛИНОК (картонный меч в фольге).",
        "Рецепт: 3 × Кристалл Глубины = Алмазный Клинок +1",
    ]
    for li, line in enumerate(lines):
        parts.append(f'<text x="{cx2+8}" y="{cy2+10+li*6.5}" class="small" fill="#3d2b0a">{line}</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "a4-sheets", "10-craft-grid.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_progress_map():
    parts = [svg_header("Карта прогресса — наклей собранные ресурсы")]
    parts.append(rounded_rect(5, 10, 200, 275, 5, "#f0e0c8", "#8b6914", 1.5))
    # Title
    parts.append(rounded_rect(25, 15, 160, 20, 3, "#c8a060", "#6b4f2e"))
    parts.append(f'<text x="105" y="28" class="title" fill="#3d2b0a" text-anchor="middle" font-size="8mm">🗺 КАРТА ПРОГРЕССА</text>')
    # 4 resource slots
    sw, sh = 35, 45
    sy = 55
    colors = ["#4a8ab8", "#ff8800", "#6088c8", "#a070d0"]
    labels = ["Кристаллы\nГлубины", "Пламя\nВыносливости", "Слёзы\nМоба", "Первородная\nПыль"]
    icons = ["💎", "🔥", "💧", "✨"]
    for i in range(4):
        sx = 25 + i * 48
        parts.append(rounded_rect(sx, sy, sw, sh, 3, "#e8dcc8", colors[i], 1.2))
        parts.append(f'<text x="{sx+sw/2}" y="{sy+12}" class="body" fill="{colors[i]}" text-anchor="middle" font-size="6mm">{icons[i]}</text>')
        for li, l in enumerate(labels[i].split('\n')):
            parts.append(f'<text x="{sx+sw/2}" y="{sy+22+li*6}" class="small" fill="#3d2b0a" text-anchor="middle">{l}</text>')
        parts.append(f'<circle cx="{sx+sw/2}" cy="{sy+sh-7}" r="5" fill="white" stroke="#666" stroke-width="0.5" stroke-dasharray="2,2"/>')
        parts.append(f'<text x="{sx+sw/2}" y="{sy+sh-5}" class="small" fill="#999" text-anchor="middle">✓</text>')
    # Portal
    px2, py2 = 105, 125
    parts.append(f'<ellipse cx="{px2}" cy="{py2}" rx="40" ry="30" fill="none" stroke="#8844bb" stroke-width="3"/>')
    parts.append(f'<ellipse cx="{px2}" cy="{py2}" rx="35" ry="25" fill="#6a30a0" opacity="0.3"/>')
    parts.append(f'<ellipse cx="{px2}" cy="{py2}" rx="30" ry="20" fill="#9955cc" opacity="0.3"/>')
    for a in range(0, 360, 30):
        rad = math.radians(a)
        px3 = px2 + 20 * math.cos(rad)
        py3 = py2 + 12 * math.sin(rad)
        ro = 1.5 if a % 60 == 0 else 1.0
        parts.append(f'<circle cx="{px3}" cy="{py3}" r="{ro}" fill="#aa66dd" opacity="0.5"/>')
    parts.append(f'<text x="{px2}" y="{py2-3}" class="body" fill="#cc88ff" text-anchor="middle">ПОРТАЛ</text>')
    parts.append(f'<text x="{px2}" y="{py2+5}" class="small" fill="#cc88ff" text-anchor="middle">В ЭНД</text>')
    # Players
    ty = 175
    parts.append(rounded_rect(20, ty, 170, 40, 3, "#e0d4b8", "#8b6914"))
    parts.append(f'<text x="105" y="{ty+10}" class="body" fill="#6b4f2e" text-anchor="middle">🏃 ИГРОКИ НА ТРОПЕ</text>')
    for i in range(2):
        ax = 30 + i * 90
        parts.append(f'<circle cx="{ax+15}" cy="{ty+28}" r="7" fill="#4a7b2a"/>')
        parts.append(f'<text x="{ax}" y="{ty+28}" class="small" fill="#3d2b0a">Игрок {i+1}: ______</text>')
    # Stickers
    sty = 225
    parts.append(rounded_rect(10, sty, 190, 50, 3, "#f5ecc8", "#8b6914"))
    parts.append(f'<text x="105" y="{sty+8}" class="body" fill="#6b4f2e" text-anchor="middle">📋 НАКЛЕЙКИ-СТИКЕРЫ (вырежи отдельно)</text>')
    for i, (ic, co) in enumerate([("💎","#4a8ab8"),("🔥","#ff8800"),("💧","#6088c8"),("✨","#a070d0")]):
        sx2 = 20 + i * 45
        parts.append(f'<circle cx="{sx2+17}" cy="{sty+30}" r="8" class="cutline"/>')
        parts.append(f'<circle cx="{sx2+17}" cy="{sty+30}" r="7" fill="{co}" opacity="0.3"/>')
        parts.append(f'<text x="{sx2+17}" y="{sty+32}" class="body" fill="{co}" text-anchor="middle" font-size="5mm">{ic}</text>')
        parts.append(f'<text x="{sx2+17}" y="{sty+45}" class="small" fill="#666" text-anchor="middle">Ресурс {i+1}</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "map", "11-progress-map.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_signs():
    parts = [svg_header("Таблички: SCP-моб и obby-паркур — вырежи, повесь")]
    for i, (cx, cy) in enumerate([(8, 12), (110, 12)]):
        parts.append(f'<rect x="{cx-3}" y="{cy-3}" width="95" height="80" class="cutline"/>')
        parts.append(rounded_rect(cx, cy, 90, 75, 3, "#d8d8d8", "#666"))
        parts.append(f'<rect x="{cx}" y="{cy}" width="90" height="15" fill="#cc2222" rx="3"/>')
        parts.append(f'<text x="{cx+45}" y="{cy+10}" class="sub" fill="white" text-anchor="middle" font-weight="bold">⚠ SCP ОБЪЕКТ ⚠</text>')
        parts.append(f'<circle cx="{cx+45}" cy="{cy+42}" r="15" fill="none" stroke="#333" stroke-width="2"/>')
        parts.append(f'<circle cx="{cx+45}" cy="{cy+42}" r="8" fill="none" stroke="#333" stroke-width="1.5"/>')
        parts.append(f'<path d="M{cx+37},{cy+42} L{cx+45},{cy+32} L{cx+53},{cy+42}" fill="none" stroke="#333" stroke-width="1.5"/>')
        parts.append(f'<text x="{cx+45}" y="{cy+65}" class="sub" fill="#333" text-anchor="middle">ЗОМБИ-МОБ</text>')
        parts.append(f'<text x="{cx+45}" y="{cy+72}" class="small" fill="#666" text-anchor="middle">Победи 3 мячами!</text>')
    for i, (cx, cy) in enumerate([(8, 105), (110, 105)]):
        parts.append(f'<rect x="{cx-3}" y="{cy-3}" width="95" height="80" class="cutline"/>')
        parts.append(rounded_rect(cx, cy, 90, 75, 3, "#e8f0e8", "#4a8a3a"))
        parts.append(f'<rect x="{cx}" y="{cy}" width="90" height="15" rx="3" fill="#4a8a3a"/>')
        parts.append(f'<text x="{cx+45}" y="{cy+10}" class="sub" fill="white" text-anchor="middle" font-weight="bold">🎮 obby</text>')
        parts.append(f'<text x="{cx+45}" y="{cy+38}" class="title" fill="#4a8a3a" text-anchor="middle" font-size="10mm">ЭТАЖ {i+1}</text>')
        parts.append(f'<rect x="{cx+30}" y="{cy+48}" width="10" height="20" fill="#cc4444" rx="1"/>')
        parts.append(f'<rect x="{cx+30}" y="{cy+43}" width="10" height="5" fill="#888"/>')
        parts.append(f'<text x="{cx+45}" y="{cy+65}" class="body" fill="#4a8a3a" text-anchor="middle">ПРЕОДОЛЕЙ ЛАВУ!</text>')
        parts.append(f'<text x="{cx+45}" y="{cy+72}" class="small" fill="#666" text-anchor="middle">Не наступай на 🔴</text>')
    # Portal sign
    parts.append(f'<rect x="8" y="200" width="195" height="80" class="cutline"/>')
    parts.append(rounded_rect(10, 202, 190, 76, 4, "#d8b0f0", "#7733aa", 2))
    parts.append(f'<ellipse cx="105" cy="240" rx="50" ry="25" fill="#9955cc" opacity="0.3"/>')
    parts.append(f'<ellipse cx="105" cy="240" rx="40" ry="20" fill="#bb77ee" opacity="0.3"/>')
    parts.append(f'<path d="M60,280 Q105,220 150,280" fill="none" stroke="#aa44dd" stroke-width="3"/>')
    parts.append(f'<path d="M65,280 Q105,228 145,280" fill="none" stroke="#cc66ff" stroke-width="1.5" opacity="0.6"/>')
    parts.append(f'<text x="105" y="215" class="title" fill="#aa44dd" text-anchor="middle" font-size="8mm">🌀 ПОРТАЛ В ЭНД</text>')
    parts.append(f'<text x="105" y="228" class="sub" fill="#cc66ff" text-anchor="middle">THE VOID</text>')
    parts.append(f'<text x="105" y="255" class="body" fill="#7733aa" text-anchor="middle">Собери все 4 ресурса и возвращайся сюда!</text>')
    parts.append(f'<text x="105" y="265" class="body" fill="#7733aa" text-anchor="middle">Когда все на месте — появится ЭНДЕР-ДРАКОН 🐉</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "labels", "12-scp-obby-signs.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_dragon_mask():
    parts = [svg_header("Маска дракона — рога на каску + накидка")]
    for i, (cx, cy) in enumerate([(15, 15), (110, 15)]):
        w, h = 90, 120
        parts.append(f'<rect x="{cx-3}" y="{cy-3}" width="{w+6}" height="{h+6}" class="cutline"/>')
        parts.append(f'<text x="{cx+5}" y="{cy+8}" class="sub" fill="#333">{"ЛЕВЫЙ" if i==0 else "ПРАВЫЙ"} РОГ — вырежи 2 шт из картона</text>')
        hp = f'M{cx+5},{cy+h-15} L{cx+15},{cy+h-35} L{cx+20},{cy+h-55} L{cx+12},{cy+h-70} L{cx+5},{cy+h-85} L{cx+15},{cy+h-95} L{cx+35},{cy+h-105} Z'
        parts.append(f'<path d="{hp}" fill="#4a2a10" stroke="#3a1a08" stroke-width="1.5"/>')
        for t in range(6):
            ty2 = cy + h - 25 - t * 14
            parts.append(f'<line x1="{cx+8+t*2}" y1="{ty2}" x2="{cx+15+t*3}" y2="{ty2-5}" stroke="#6a3a18" stroke-width="0.8" opacity="0.5"/>')
        parts.append(f'<line x1="{cx+5}" y1="{cy+h-15}" x2="{cx+30}" y2="{cy+h-15}" class="foldline"/>')
        parts.append(f'<text x="{cx+40}" y="{cy+h-10}" class="small" fill="#666">Согни, приклей скотчем к каске</text>')
    # Cape
    cx2, cy2 = 10, 155
    parts.append(f'<rect x="{cx2-3}" y="{cy2-3}" width="190" height="130" class="cutline"/>')
    parts.append(f'<text x="105" y="{cy2+8}" class="sub" fill="#333" text-anchor="middle">НАКИДКА ДРАКОНА — вырежи из чёрной/фиолетовой ткани</text>')
    cw2, cw3, ch2 = 160, 200, 110
    cc = cx2 + 95
    ty2 = cy2 + 15
    by2 = ty2 + ch2
    parts.append(f'<path d="M{cc-cw2/2},{ty2} L{cc-cw3/2},{by2} L{cc+cw3/2},{by2} L{cc+cw2/2},{ty2} Z" fill="#3a1a5a" stroke="#5a2a7a" stroke-width="1.5" opacity="0.5"/>')
    for s in range(8):
        sx2 = cc - cw3/2 + s * (cw3/8)
        sy2 = by2 + 6 * (s % 2)
        parts.append(f'<path d="M{sx2},{by2} Q{sx2+6},{by2-10} {sx2+12},{by2+5}" fill="#3a1a5a" stroke="#5a2a7a" stroke-width="0.5" opacity="0.5"/>')
    parts.append(f'<text x="105" y="{by2+20}" class="small" fill="#666" text-anchor="middle">Пришей/приклей завязки по краям | Длина: ~110 см</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "templates", "08-dragon-mask.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_obby_numbers():
    parts = [svg_header("Obby — номера этажей для паркура")]
    for i in range(5):
        cx = 8 + (i % 3) * 68
        cy = 15 + (i // 3) * 95
        parts.append(f'<rect x="{cx-3}" y="{cy-3}" width="62" height="85" class="cutline"/>')
        parts.append(rounded_rect(cx, cy, 58, 80, 3, "#d8f0d8", "#3a7a2a"))
        parts.append(f'<rect x="{cx}" y="{cy}" width="58" height="18" rx="3" fill="#3a7a2a"/>')
        parts.append(f'<text x="{cx+29}" y="{cy+12}" class="sub" fill="white" text-anchor="middle">obby</text>')
        parts.append(f'<text x="{cx+29}" y="{cy+52}" class="title" fill="#3a7a2a" text-anchor="middle" font-size="18mm" font-weight="bold">{i+1}</text>')
        parts.append(f'<rect x="{cx+42}" y="{cy+60}" width="8" height="18" fill="#44aa44" rx="1"/>')
        parts.append(f'<text x="{cx+29}" y="{cy+75}" class="small" fill="#3a7a2a" text-anchor="middle">ЧЕКПОИНТ</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "labels", "13-obby-floor-signs.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


def generate_chest_wrap():
    parts = [svg_header("Обклейка для сундуков — коричневая текстура «под дерево» (4 листа)")]
    bw, bh, mort = 30, 14, 2
    for row in range(18):
        for col in range(7):
            bx = 3 + col * (bw + mort) + (row % 2) * ((bw + mort) / 2)
            by = 25 + row * (bh + mort)
            if bx + bw > 207:
                continue
            shade = ["#b8956a","#c8a070","#a08050","#b89060","#c0a068","#b08858","#c8a870"][(row+col)%7]
            parts.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="1" fill="{shade}" stroke="#8b6914" stroke-width="0.5"/>')
            if (row+col)%3 == 0:
                parts.append(f'<line x1="{bx+5}" y1="{by+3}" x2="{bx+bw-5}" y2="{by+bh-3}" stroke="#7a5a30" stroke-width="0.3" opacity="0.4"/>')
    parts.append(f'<text x="105" y="285" class="body" fill="#6b4f2e" text-anchor="middle">Распечатай 4+ листа, обклей коробки — получатся сундуки</text>')
    parts.append(svg_footer())
    with open(os.path.join(BASE, "a4-sheets", "14-chest-wrap.svg"), "w", encoding="utf-8") as f:
        f.write('\n'.join(parts))


if __name__ == "__main__":
    os.makedirs(BASE, exist_ok=True)
    for d in ("notes", "templates", "labels", "a4-sheets", "map"):
        os.makedirs(os.path.join(BASE, d), exist_ok=True)
    print("Генерация материалов квеста...")
    for name, fn in [("01-zapiski-all.svg", generate_notes),
                     ("02-diamonds.svg", generate_diamonds),
                     ("03-diamond-sword.svg", generate_sword),
                     ("04-lava-blocks.svg", generate_lava),
                     ("05-hp-hearts.svg", generate_hearts),
                     ("06-flame-endurance.svg", generate_flame),
                     ("07-mob-tear.svg", generate_tear),
                     ("08-dragon-mask.svg", generate_dragon_mask),
                     ("09-chest-labels.svg", generate_chest_labels),
                     ("10-craft-grid.svg", generate_craft_grid),
                     ("11-progress-map.svg", generate_progress_map),
                     ("12-scp-obby-signs.svg", generate_signs),
                     ("13-obby-floor-signs.svg", generate_obby_numbers),
                     ("14-chest-wrap.svg", generate_chest_wrap)]:
        fn()
        print(f"  ✓ {name}")
    print("\n✅ Готово! 14 файлов создано.")