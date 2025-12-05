from pathlib import Path
import datetime
import random

OUTPUT = Path("tree.svg")

# Colors for the stars
COLORS = [
    "#2ecc71",  # green
    "#e74c3c",  # red
    "#f1c40f",  # yellow
    "#3498db",  # blue
    "#9b59b6",  # purple
    "#1abc9c",  # teal
]


def days_until_christmas() -> int:
    today = datetime.date.today()
    year = today.year
    christmas = datetime.date(year, 12, 25)

    # If Christmas already passed this year → countdown to next year's Christmas
    if today > christmas:
        christmas = datetime.date(year + 1, 12, 25)

    return (christmas - today).days


def build_svg() -> str:
    today = datetime.date.today()
    seed = today.timetuple().tm_yday
    random.seed(seed)

    days_left = days_until_christmas()
    today_str = today.isoformat()

    # Smaller tree settings
    height = 9          # number of star rows (smaller than before)
    line_height = 18
    center_x = 200
    y_start = 110

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="320">',
        '<rect width="100%" height="100%" fill="#0b1020"/>',

        # Countdown text centered at top
        (
            f'<text x="{center_x}" y="40" '
            'font-family="monospace" font-size="22" '
            'fill="#f1c40f" text-anchor="middle">'
            f'{days_left} days until Christmas 🎄'
            '</text>'
        ),

        # Tree text block
        '<text font-family="monospace" font-size="16" fill="#ecf0f1">'
    ]

    y = y_start

    # Tree rows – all stars, multicolored, centered
    for i in range(height):
        count = 2 * i + 1  # 1, 3, 5, ...
        stars = []
        for _ in range(count):
            color = random.choice(COLORS)
            stars.append(f'<tspan fill="{color}">*</tspan>')

        row = "".join(stars)
        svg.append(
            f'<tspan x="{center_x}" y="{y}" text-anchor="middle">{row}</tspan>'
        )
        y += line_height

    # Trunk – 3 brown blocks, centered
    trunk_color = "#8e5a2b"
    trunk_chars = "".join(
        f'<tspan fill="{trunk_color}">█</tspan>' for _ in range(3)
    )
    svg.append(
        f'<tspan x="{center_x}" y="{y}" text-anchor="middle">{trunk_chars}</tspan>'
    )
    y += line_height

    # Updated date
    svg.append(
        f'<tspan x="{center_x}" y="{y + 10}" text-anchor="middle" '
        f'fill="#bdc3c7">Updated: {today_str}</tspan>'
    )

    svg.append("</text></svg>")

    return "\n".join(svg)


def main():
    svg = build_svg()
    OUTPUT.write_text(svg, encoding="utf-8")
    print("Generated centered, smaller star tree with countdown")


if __name__ == "__main__":
    main()