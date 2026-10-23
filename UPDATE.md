# 手动更新指南（三步）

网站内容全部是 Markdown，更新不用懂代码。每次更新只需三步。

## 第 1 步：放文件

| 想加的内容 | 放到哪里 | 命名要求 |
|---|---|---|
| 新知识点 | `content/modules/模块N-主题/` | `N.小节号-名称.md`（如 `4.10-量子隧穿应用.md`）；模块文件夹不存在就先建 |
| 课堂笔记 | `content/notes/` | `序号-标题.md`（如 `13-定态微扰引入.md`） |
| 答疑记录 | `content/qa/` | `YYYY-MM-DD-主题.md`（如 `2026-11-01-角动量对易答疑.md`） |
| 体系总览 / 学习进度 | `content/framework.md` / `content/progress.md` | 直接编辑覆盖 |

知识点文件建议沿用固定骨架：`# 编号　标题` → `> 模块与状态` → `## 速览` → `## 精要` → `## 相关知识点` → `## 例题` → `## 易错点` → `## 问答记录` → `## 留白`。

公式用 LaTeX：行内 `$E_n=\hbar\omega(n+\tfrac12)$`，独立行用 `$$…$$`。

## 第 2 步：更新清单

在网站根目录运行：

```bash
python tools/build_manifest.py
```

脚本会扫描三个 content 目录，自动重新生成 `content/manifest.json`（含每个知识点的标题、路径、模块状态与章节）。没有 Python 时，也可以手动按现有格式往 `manifest.json` 对应数组里补一条记录。

> 模块状态（已整理/部分覆盖/待补）与所属章节定义在 `tools/build_manifest.py` 顶部的 `MODULE_META` 字典里，改名或新建模块时改这里。

## 第 3 步：提交并发布

```bash
git add -A
git commit -m "更新：新增 xxx"
git push
```

仓库开启 GitHub Pages（Settings → Pages → Deploy from a branch → main / root）后，每次推送都会自动发布，约 1 分钟内生效。

## 本地预览

直接双击 `index.html` 打不开（浏览器禁止读取本地文件），用本地服务器：

```bash
python -m http.server 8000
# 浏览器打开 http://localhost:8000
```

## 常见问题

- **链接报"原文未收录"**：知识点里的旧链接指向笔记库其他位置（如 `01-课件/`），站点没有收录这些文件，会显示灰色占位；这是正常的。
- **改了文件名/移动文件**：重跑 `build_manifest.py`；旧链接失效会在页面上显示"原文未收录"。
