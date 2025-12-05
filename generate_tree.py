from pathlib import Path
import datetime
import random

OUTPUT = Path("tree.svg")

# Colors for leaves
COLORS = [
    "#2ecc71",  # green
    "#e74c3c",  # red
    "#f1c40f",  # yellow
    "#3498db",  # blue
    "#9b59b6",  # purple
    "#1abc9c",  # teal
]

# Characters for tree decoration
CHARS = ["*", "+", "o", "x", "▲", "◆", "●"]

def days_until_christmas():
    today = datetime.date.today()
    year = today.year
    christmas = datetime.date(year, 12, 25)

    # If Christmas already passed this year → countdown to next year's Christmas
    if today > christmas:
        christmas = datetime.date(year + 1, 12, 25)

    delta = (christmas - today).days
    return delta


def generate_colored_ascii():
    today = datetime.date.today()
    seed = today.timetuple().tm_yday
    random.seed(seed)

    height = 14
    lines = []

    for i in range(height):
        spaces = " " * (height - i - 1)
        leaves = ""

        # Assign random colored characters
        for _ in range(2 * i + 1):
            char = random.choice(CHARS)
            color = random.choice(COLORS)
            leaves += f'<tspan fill="{color}">{char}</tspan>'

        lines.append(spaces + leaves)

    # Tree trunk
    trunk_color = "#8e5a2b"
    trunk = " " * (height - 2) + "".join(
        f'<tspan fill="{trunk_color}">█</tspan>' for _ in range(3)
    )
    lines.append(trunk)
    lines.append(trunk)

    return lines


def build_svg():
    lines = generate_colored_ascii()
    today = datetime.date.today().isoformat()
    countdown = days_until_christmas()

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="380">',
        '<rect width="100%" height="100%" fill="#0b1020"/>',

        # Countdown text
        '<text x="20" y="40" font-family="monospace" font-size="22" fill="#f1c40f">',
        f"  {countdown} days until Christmas 🎄",
        "</text>",

        '<text x="20" y="70" font-family="monospace" font-size="18" fill="#ecf0f1">'
    ]

    y = 100
    for line in lines:
        svg.append(f'<tspan x="20" y="{y}">{line}</tspan>')
        y += 20

    svg.append(f'<tspan x="20" y="{y+20}" fill="#bdc3c7">Updated: {today}</tspan>')
    svg.append("</text></svg>")

    return "\n".join(svg)


def main():
    svg = build_svg()
    OUTPUT.write_text(svg, encoding="utf-8")
    print("Generated colorful tree.svg with countdown")


if __name__ == "__main__":
    main()