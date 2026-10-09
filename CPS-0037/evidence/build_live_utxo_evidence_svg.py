#!/usr/bin/env python3
"""Build the exact-count historical figure used by the scoped CPS Evidence section."""

from __future__ import annotations

import csv
from datetime import datetime
from html import escape
from pathlib import Path


EVIDENCE_DIR = Path(__file__).resolve().parent
CPS_DIR = EVIDENCE_DIR.parent
COUNTS = EVIDENCE_DIR / "utxo-count-by-epoch.csv"
DATES = EVIDENCE_DIR / "epoch-dates.csv"
OUTPUT = CPS_DIR / "images/09-live-utxo-history.svg"

FIRST_SHELLEY_EPOCH = 208
RECENT_START_EPOCH = 503
LAST_COMPLETE_EPOCH = 648

WIDTH = 1400
HEIGHT = 860
PLOT_LEFT = 125
PLOT_RIGHT = 1335
PLOT_WIDTH = PLOT_RIGHT - PLOT_LEFT
STOCK_TOP = 170
STOCK_HEIGHT = 240
FLOW_TOP = 535
FLOW_HEIGHT = 205

COLORS = {
    "background": "#f8faf8",
    "panel": "#ffffff",
    "ink": "#17201d",
    "muted": "#5d6964",
    "grid": "#d9ded9",
    "frame": "#c8d0cc",
    "stock": "#4f6fb4",
    "created": "#397c74",
    "consumed": "#c0644f",
    "window": "#e8eef9",
    "window_text": "#405a8f",
}


def number(row: dict[str, str], key: str) -> float:
    value = row.get(key, "")
    return float(value) if value else 0.0


with DATES.open(newline="", encoding="utf-8") as handle:
    dates_by_epoch = {
        int(row["epoch_no"]): row for row in csv.DictReader(handle)
    }

with COUNTS.open(newline="", encoding="utf-8") as handle:
    all_rows = []
    for row in csv.DictReader(handle):
        epoch_no = int(row["epoch_no"])
        if epoch_no > LAST_COMPLETE_EPOCH:
            continue
        row.update(dates_by_epoch[epoch_no])
        all_rows.append(row)

rows_by_epoch = {int(row["epoch_no"]): row for row in all_rows}
stock_rows = [
    row for row in all_rows if int(row["epoch_no"]) >= FIRST_SHELLEY_EPOCH
]
flow_rows = [
    row for row in all_rows if int(row["epoch_no"]) >= RECENT_START_EPOCH
]

stock_dates = [datetime.fromisoformat(row["end_time"]) for row in stock_rows]
stock_values = [number(row, "utxo_count_end") / 1_000_000 for row in stock_rows]
flow_epochs = [int(row["epoch_no"]) for row in flow_rows]
created_values = [number(row, "created") / 1_000_000 for row in flow_rows]
consumed_values = [number(row, "consumed") / 1_000_000 for row in flow_rows]

stock_date_min = stock_dates[0]
stock_date_max = stock_dates[-1]
recent_start_date = datetime.fromisoformat(rows_by_epoch[RECENT_START_EPOCH - 1]["end_time"])

peak_row = max(stock_rows, key=lambda row: int(row["utxo_count_end"]))
peak_date = datetime.fromisoformat(peak_row["end_time"])
peak_value = number(peak_row, "utxo_count_end") / 1_000_000
latest_row = rows_by_epoch[LAST_COMPLETE_EPOCH]
latest_date = datetime.fromisoformat(latest_row["end_time"])
latest_value = number(latest_row, "utxo_count_end") / 1_000_000

created_total = sum(int(row["created"]) for row in flow_rows)
consumed_total = sum(int(row["consumed"]) for row in flow_rows)
gross_total = created_total + consumed_total
net_change = sum(int(row["net_change"]) for row in flow_rows)
start_stock = int(rows_by_epoch[RECENT_START_EPOCH - 1]["utxo_count_end"])
net_change_pct = 100 * net_change / start_stock


def sx_stock(value: datetime) -> float:
    ratio = (value - stock_date_min).total_seconds() / (
        stock_date_max - stock_date_min
    ).total_seconds()
    return PLOT_LEFT + ratio * PLOT_WIDTH


def sx_flow(value: int) -> float:
    ratio = (value - RECENT_START_EPOCH) / (
        LAST_COMPLETE_EPOCH - RECENT_START_EPOCH
    )
    return PLOT_LEFT + ratio * PLOT_WIDTH


def sy(value: float, top: float, height: float, maximum: float) -> float:
    return top + height - (value / maximum) * height


def path_for(xs: list[float], values: list[float], top: float, height: float, maximum: float) -> str:
    points = [
        f"{x:.2f},{sy(value, top, height, maximum):.2f}"
        for x, value in zip(xs, values)
    ]
    return "M" + " L".join(points)


def text(
    x: float,
    y: float,
    value: str,
    css_class: str,
    anchor: str = "start",
) -> str:
    return (
        f'<text class="{css_class}" x="{x:.1f}" y="{y:.1f}" '
        f'text-anchor="{anchor}">{escape(value)}</text>'
    )


def line_legend(x: float, y: float, label: str, color: str, dashed: bool = False) -> list[str]:
    dash = ' stroke-dasharray="8 5"' if dashed else ""
    return [
        f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x + 30:.1f}" y2="{y:.1f}" '
        f'stroke="{color}" stroke-width="3"{dash}/>',
        text(x + 39, y + 4, label, "small muted"),
    ]


stock_xs = [sx_stock(value) for value in stock_dates]
flow_xs = [sx_flow(value) for value in flow_epochs]
recent_x = sx_stock(recent_start_date)
peak_x = sx_stock(peak_date)
peak_y = sy(peak_value, STOCK_TOP, STOCK_HEIGHT, 12.0)
latest_x = sx_stock(latest_date)
latest_y = sy(latest_value, STOCK_TOP, STOCK_HEIGHT, 12.0)

svg: list[str] = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
    '  <title id="title">Cardano mainnet live UTxO count and output turnover</title>',
    '  <desc id="desc">Two panels show the exact live UTxO count from Shelley epoch 208 through epoch 648 and exact output creation and consumption during epochs 503 through 648. The live count plateaued in the recent window while creation and consumption remained high and closely balanced.</desc>',
    "  <defs>",
    "    <style>",
    "      .bg{fill:#f8faf8}.panel{fill:#fff;stroke:#c8d0cc;stroke-width:1.2}.ink{fill:#17201d}.muted{fill:#5d6964}.window-label{fill:#405a8f}.title{font:700 31px system-ui,sans-serif}.subtitle{font:16px system-ui,sans-serif}.panel-title{font:700 19px system-ui,sans-serif}.eyebrow{font:700 13px ui-monospace,monospace;letter-spacing:1.15px}.body{font:15px system-ui,sans-serif}.body-strong{font:700 15px system-ui,sans-serif}.small{font:13px system-ui,sans-serif}.small-strong{font:700 13px system-ui,sans-serif}.axis{font:12px system-ui,sans-serif}.axis-title{font:650 12px system-ui,sans-serif}.grid{stroke:#d9ded9;stroke-width:1}.series{fill:none;stroke-linecap:round;stroke-linejoin:round}",
    "    </style>",
    "  </defs>",
    f'  <rect class="bg" width="{WIDTH}" height="{HEIGHT}" rx="12"/>',
    text(64, 42, "MAINNET EVIDENCE · EXACT DB-SYNC COUNTS", "eyebrow muted"),
    text(64, 80, "Live UTxO growth slowed while output turnover continued", "title ink"),
    text(64, 108, "Historical stock above; creation and consumption during the highlighted two-year window below.", "subtitle muted"),
    text(64, 151, "Live UTxO stock", "panel-title ink"),
    text(260, 151, "exact · end-of-epoch count", "small muted"),
    f'  <rect class="panel" x="{PLOT_LEFT}" y="{STOCK_TOP}" width="{PLOT_WIDTH}" height="{STOCK_HEIGHT}" rx="4"/>',
]

# Stock-panel grid and highlighted recent window.
for tick in [0, 3, 6, 9, 12]:
    y = sy(float(tick), STOCK_TOP, STOCK_HEIGHT, 12.0)
    svg.append(f'  <line class="grid" x1="{PLOT_LEFT}" y1="{y:.2f}" x2="{PLOT_RIGHT}" y2="{y:.2f}"/>')
    svg.append(text(PLOT_LEFT - 10, y + 4, f"{tick}", "axis muted", "end"))

year_ticks = [datetime(year, 1, 1) for year in range(2021, 2027)]
for date in year_ticks:
    x = sx_stock(date)
    svg.append(f'  <line class="grid" x1="{x:.2f}" y1="{STOCK_TOP}" x2="{x:.2f}" y2="{STOCK_TOP + STOCK_HEIGHT}" opacity="0.55"/>')
    svg.append(text(x, STOCK_TOP + STOCK_HEIGHT + 25, str(date.year), "axis muted", "middle"))

svg.extend(
    [
        f'  <rect x="{recent_x:.2f}" y="{STOCK_TOP + 1}" width="{PLOT_RIGHT - recent_x:.2f}" height="{STOCK_HEIGHT - 2}" fill="{COLORS["window"]}"/>',
        text(recent_x + 12, STOCK_TOP + STOCK_HEIGHT - 16, "AUG 2024–AUG 2026 · EPOCHS 503–648", "small-strong window-label"),
        f'  <path class="series" d="{path_for(stock_xs, stock_values, STOCK_TOP, STOCK_HEIGHT, 12.0)}" stroke="{COLORS["stock"]}" stroke-width="3.2"/>',
        f'  <circle cx="{peak_x:.2f}" cy="{peak_y:.2f}" r="5" fill="{COLORS["stock"]}"/>',
        f'  <circle cx="{latest_x:.2f}" cy="{latest_y:.2f}" r="5" fill="{COLORS["stock"]}"/>',
        f'  <line x1="{peak_x:.2f}" y1="{peak_y + 7:.2f}" x2="{peak_x:.2f}" y2="{peak_y + 42:.2f}" stroke="{COLORS["stock"]}" stroke-width="1.5"/>',
        text(peak_x + 9, peak_y + 31, "Peak · 11.246M", "small-strong ink"),
        text(peak_x + 9, peak_y + 49, "epoch 511 · Sep 2024", "small muted"),
        f'  <line x1="{latest_x - 2:.2f}" y1="{latest_y + 7:.2f}" x2="{latest_x - 42:.2f}" y2="{latest_y + 68:.2f}" stroke="{COLORS["stock"]}" stroke-width="1.5"/>',
        text(latest_x - 50, latest_y + 64, "Latest · 11.076M", "small-strong ink", "end"),
        text(latest_x - 50, latest_y + 82, "epoch 648 · Aug 2026", "small muted", "end"),
        f'  <text class="axis-title muted" x="28" y="{STOCK_TOP + STOCK_HEIGHT / 2:.1f}" text-anchor="middle" transform="rotate(-90 28 {STOCK_TOP + STOCK_HEIGHT / 2:.1f})">Live UTxOs (millions)</text>',
        text((PLOT_LEFT + PLOT_RIGHT) / 2, STOCK_TOP + STOCK_HEIGHT + 51, "Calendar time", "axis-title muted", "middle"),
    ]
)

# Flow-panel headings, totals, legend, frame, and grid.
svg.extend(
    [
        text(64, 473, "Output creation and consumption", "panel-title ink"),
        text(390, 473, "exact per-epoch counts · epochs 503–648", "small muted"),
        text(PLOT_LEFT, 509, f"{created_total / 1_000_000:.3f}M created · {consumed_total / 1_000_000:.3f}M consumed", "body-strong ink"),
        text(PLOT_LEFT + 365, 509, f"{gross_total / 1_000_000:.3f}M gross events · net −{abs(net_change):,} live outputs (−{abs(net_change_pct):.2f}% of opening stock)", "body ink"),
        f'  <rect class="panel" x="{PLOT_LEFT}" y="{FLOW_TOP}" width="{PLOT_WIDTH}" height="{FLOW_HEIGHT}" rx="4"/>',
    ]
)
svg.extend(line_legend(1035, 469, "created", COLORS["created"]))
svg.extend(line_legend(1168, 469, "consumed", COLORS["consumed"], dashed=True))

for tick in [0, 0.5, 1.0, 1.5, 2.0]:
    y = sy(tick, FLOW_TOP, FLOW_HEIGHT, 2.0)
    svg.append(f'  <line class="grid" x1="{PLOT_LEFT}" y1="{y:.2f}" x2="{PLOT_RIGHT}" y2="{y:.2f}"/>')
    label = "0" if tick == 0 else f"{tick:.1f}"
    svg.append(text(PLOT_LEFT - 10, y + 4, label, "axis muted", "end"))

for epoch in [503, 540, 580, 620, 648]:
    x = sx_flow(epoch)
    svg.append(f'  <line class="grid" x1="{x:.2f}" y1="{FLOW_TOP}" x2="{x:.2f}" y2="{FLOW_TOP + FLOW_HEIGHT}" opacity="0.55"/>')
    svg.append(text(x, FLOW_TOP + FLOW_HEIGHT + 24, str(epoch), "axis muted", "middle"))

svg.extend(
    [
        f'  <path class="series" d="{path_for(flow_xs, created_values, FLOW_TOP, FLOW_HEIGHT, 2.0)}" stroke="{COLORS["created"]}" stroke-width="2.4"/>',
        f'  <path class="series" d="{path_for(flow_xs, consumed_values, FLOW_TOP, FLOW_HEIGHT, 2.0)}" stroke="{COLORS["consumed"]}" stroke-width="2.4" stroke-dasharray="8 5"/>',
        f'  <text class="axis-title muted" x="28" y="{FLOW_TOP + FLOW_HEIGHT / 2:.1f}" text-anchor="middle" transform="rotate(-90 28 {FLOW_TOP + FLOW_HEIGHT / 2:.1f})">Outputs per epoch (millions)</text>',
        text((PLOT_LEFT + PLOT_RIGHT) / 2, FLOW_TOP + FLOW_HEIGHT + 51, "Epoch", "axis-title muted", "middle"),
        text(64, 830, "Exact accepted output counts and flows · live stock through epoch 648", "small muted"),
        "</svg>",
    ]
)

OUTPUT.write_text("\n".join(svg) + "\n", encoding="utf-8")
print(OUTPUT)
