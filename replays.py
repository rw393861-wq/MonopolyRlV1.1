import json
import os
import shutil

from monopoly.board import BOARD

SHORT_NAMES = {
    1: "Mediterranean", 3: "Baltic", 5: "Reading RR", 6: "Oriental", 8: "Vermont",
    9: "Connecticut", 11: "St. Charles", 12: "Electric Co", 13: "States",
    14: "Virginia", 15: "Pennsylvania RR", 16: "St. James", 18: "Tennessee",
    19: "New York", 21: "Kentucky", 23: "Indiana", 24: "Illinois", 25: "B&O RR",
    26: "Atlantic", 27: "Ventnor", 28: "Water Works", 29: "Marvin Gardens",
    31: "Pacific", 32: "N. Carolina", 34: "Pennsylvania", 35: "Short Line",
    37: "Park Place", 39: "Boardwalk", 0: "GO", 2: "Chest", 4: "Income Tax",
    7: "Chance", 10: "Jail", 17: "Chest", 20: "Free Parking", 22: "Chance",
    30: "Go To Jail", 33: "Chest", 36: "Chance", 38: "Luxury Tax",
}


def board_data():
    return [{"n": SHORT_NAMES.get(sp.idx, sp.name), "k": sp.kind, "g": sp.group,
             "p": sp.price} for sp in BOARD]


def build_page(docs_dir="docs"):
    template = os.path.join(docs_dir, "viewer_template.html")
    with open(template, encoding="utf-8") as fh:
        html = fh.read()
    html = html.replace("__BOARD__", json.dumps(board_data(), separators=(",", ":")))
    out = os.path.join(docs_dir, "index.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    return out


def collect(log_root="logs", docs_dir="docs", keep=150, quiet=False):
    dest = os.path.join(docs_dir, "replays")
    os.makedirs(dest, exist_ok=True)
    copied = 0
    if os.path.isdir(log_root):
        for run in sorted(os.listdir(log_root)):
            src = os.path.join(log_root, run, "replays")
            if not os.path.isdir(src):
                continue
            for name in os.listdir(src):
                if name.endswith(".json"):
                    shutil.copy2(os.path.join(src, name), os.path.join(dest, name))
                    copied += 1

    entries = []
    for name in os.listdir(dest):
        if not name.endswith(".json") or name == "index.json":
            continue
        path = os.path.join(dest, name)
        try:
            with open(path, encoding="utf-8") as fh:
                d = json.load(fh)
        except (ValueError, OSError):
            continue
        entries.append({
            "id": d.get("id", name[:-5]),
            "winner": d["players"][d["winner"]],
            "rounds": d["rounds"],
            "reason": d["reason"],
            "run": d.get("run", ""),
            "events": len(d.get("events", [])),
            "_path": path,
            "_mtime": os.path.getmtime(path),
        })

    entries.sort(key=lambda e: -e["_mtime"])
    for stale in entries[keep:]:
        os.remove(stale["_path"])
    entries = entries[:keep]
    for e in entries:
        e.pop("_path")
        e.pop("_mtime")

    with open(os.path.join(dest, "index.json"), "w", encoding="utf-8") as fh:
        json.dump(entries, fh, separators=(",", ":"))

    page = build_page(docs_dir)
    if not quiet:
        print(f"copied {copied} replays, {len(entries)} available")
        print("viewer page:", os.path.abspath(page))
    return len(entries)
