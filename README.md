# 量子力学学习笔记 · 公开版

一套把《材料中的量子与统计》课程（量子力学部分，18 学时五章节）学透的**公开学习笔记网站**。纯静态 HTML + Markdown，无需构建工具；内容全部可手动维护，GitHub Pages 一键发布。

> 课程：北京大学 ·《材料中的量子与统计》（量子部分）
> 教材：曾谨言《量子力学·卷Ⅰ》为主，Griffiths 辅

## 学习主线

```
实验反常（黑体/光电/光谱）
 → 波函数 + Born 统计诠释
 → Schrödinger 方程（定态 = 解能量本征方程）
 → 一维练手：束缚态 / 散射态 / 隧穿 / 周期势
 → 抽象成态矢量与表象（代数表示）
 → 对易 · 时间演化 · 对称性
 → 角动量 · 自旋
 → 全同粒子（Bose/Fermi、Pauli、费米气体/BEC）
```

## 站点内容

| 内容 | 位置 | 数量 |
|---|---|---|
| 知识点（速览 / 精要 / 例题 / 易错点） | `content/modules/` | 50 |
| 课堂笔记 | `content/notes/` | 12 |
| 答疑记录 | `content/qa/` | 9 |
| 体系总览（纲领） | `content/framework.md` | 1 |
| 学习进度 | `content/progress.md` | 1 |

- 每个知识点：**速览**（30 秒复习）、**精要**（公式逐符号讲解）、**例题**（完整推导 + 第一遍易错处 ⚠️）、**易错点**、**问答记录**、**留白**。
- 公式全程 KaTeX（LaTeX）渲染；知识点之间互相链接，可沿主线跳转。
- 模块编号沿用笔记库文件夹命名；与《体系总览》中教科书式编号略有出入处，以实际文件夹为准。

## 目录结构

```
quantum-mechanics-notes/
├── index.html              # 单页网站（全部样式与逻辑内联）
├── content/
│   ├── manifest.json       # 内容清单（由脚本生成）
│   ├── modules/模块N-主题/  # 知识点 Markdown
│   ├── notes/              # 课堂笔记
│   ├── qa/                 # 答疑记录
│   ├── framework.md        # 体系总览
│   └── progress.md         # 学习进度
├── tools/build_manifest.py # 重新生成 manifest.json
└── UPDATE.md               # 手动更新指南（三步）
```

## 如何更新

增删内容后运行一次：

```bash
python tools/build_manifest.py
```

提交推送，GitHub Pages 自动发布。详细步骤见 [UPDATE.md](UPDATE.md)。

## 许可

- 除特别注明外，本站笔记文本采用 **CC BY-NC-SA 4.0**（署名–非商业–相同方式共享）。
- 涉及课程讲义、作业题与教材的引用，版权归原权利人所有，仅作学习交流。
