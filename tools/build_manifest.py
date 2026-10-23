# -*- coding: utf-8 -*-
"""为「量子力学学习网站」生成 content/manifest.json。

用法（在网站根目录执行）：
    python tools/build_manifest.py

扫描 content/modules、content/notes、content/qa 下的 Markdown，
按文件名自然序生成模块/知识点/笔记/答疑清单。新增或重命名文件后
重跑一次即可（GitHub Pages 会自动使用新清单）。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
MODULES_DIR = CONTENT / "modules"
NOTES_DIR = CONTENT / "notes"
QA_DIR = CONTENT / "qa"

# 模块状态与所属章节（1-5），以笔记库实际文件夹为准
MODULE_META = {
    "模块1-旧量子论与诞生": ("done", 1),
    "模块2-波函数与统计诠释": ("done", 1),
    "模块3-薛定谔方程与概率守恒": ("done", 1),
    "模块4-一维束缚态": ("done", 2),
    "模块5-散射与隧穿": ("done", 2),
    "模块7-周期势与能带": ("todo", 2),
    "模块8-态矢量与表象": ("done", 3),
    "模块9-厄米算符与本征值问题": ("done", 3),
    "模块10-对易与相容观测量": ("done", 4),
    "模块11-时间演化与守恒量": ("done", 4),
    "模块12-对称守恒律": ("partial", 4),
    "模块13-角动量代数": ("todo", 4),
    "模块14-自旋与Zeeman": ("partial", 4),
    "模块15-谐振子代数解法与相干态": ("done", 4),
    "模块16-全同粒子": ("todo", 5),
}


def natural_key(text: str):
    """自然排序：把文件名里的数字按数值参与排序。"""
    parts = re.split(r"(\d+)", text)
    return [int(p) if p.isdigit() else p for p in parts]


def strip_title(filename: str):
    """去掉文件名前缀编号（如 1.1- / 08- / 2026-10-22-），得到展示标题。"""
    name = Path(filename).stem
    m = re.match(r"^\d+(\.\d+)?\s*[-.]?\s*(.+)$", name)
    if m:
        return m.group(2).strip()
    return name


def module_display(folder: str):
    """模块展示名：模块1 · 旧量子论与诞生。"""
    m = re.match(r"^(模块\d+)-(.*)$", folder)
    if m:
        return m.group(1) + " · " + m.group(2)
    return folder


def collect_points(folder: str):
    """递归收集模块下的知识点，返回 (file, title, path) 列表。"""
    out = []
    for p in sorted(MODULES_DIR.joinpath(folder).rglob("*.md"), key=lambda x: natural_key(x.name)):
        if p.name == "README.md":
            continue
        title = strip_title(p.name)
        parent = p.parent.name
        # 嵌套目录（如 8.6-自旋1\2态空间.md）→ 标题带上父级
        if p.parent.name != folder and re.match(r"^\d+\.\d+", parent):
            pt = strip_title(parent)
            title = "%s（%s）" % (title, pt)
        out.append({
            "file": p.name,
            "title": title,
            "path": p.relative_to(CONTENT).as_posix(),
        })
    return out


def main():
    modules, point_key = [], 0
    for folder in sorted(
        [d.name for d in MODULES_DIR.iterdir() if d.is_dir()],
        key=lambda x: (int(re.match(r"模块(\d+)", x).group(1)), x),
    ):
        status, chapter = MODULE_META.get(folder, ("todo", 1))
        points = []
        for item in collect_points(folder):
            points.append({"key": "p%d" % point_key, "file": item["file"],
                           "title": item["title"], "path": item["path"]})
            point_key += 1
        modules.append({
            "id": "m%d" % len(modules),
            "folder": folder,
            "name": module_display(folder),
            "status": status,
            "chapter": chapter,
            "points": points,
        })

    notes = []
    for p in sorted(NOTES_DIR.glob("*.md"), key=lambda x: natural_key(x.name)):
        notes.append({
            "key": "n%d" % len(notes),
            "file": p.name,
            "title": strip_title(p.name),
            "path": p.relative_to(CONTENT).as_posix(),
        })

    qa = []
    for p in sorted(QA_DIR.glob("*.md"), key=lambda x: natural_key(x.name)):
        m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+)$", p.stem)
        date = m.group(1) if m else ""
        title = m.group(2).strip() if m else strip_title(p.name)
        qa.append({
            "key": "q%d" % len(qa),
            "file": p.name,
            "title": title,
            "date": date,
            "path": p.relative_to(CONTENT).as_posix(),
        })

    manifest = {
        "generated": "2026-10-23",
        "counts": {
            "points": sum(len(m["points"]) for m in modules),
            "modules": len(modules),
            "notes": len(notes),
            "qa": len(qa),
        },
        "aliases": {
            "00-学习进度/学习进度.md": "#/progress",
            "00-学习进度/量子力学体系总览.md": "#/framework",
        },
        "modules": modules,
        "notes": notes,
        "qa": qa,
    }

    out = CONTENT / "manifest.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("manifest.json 已生成：%d 个知识点 / %d 个模块 / %d 篇笔记 / %d 篇答疑"
          % (manifest["counts"]["points"], manifest["counts"]["modules"],
             manifest["counts"]["notes"], manifest["counts"]["qa"]))


if __name__ == "__main__":
    main()
