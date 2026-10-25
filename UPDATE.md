# 手动更新指南（v2.0.0 · 四支柱）

网站内容全部是 Markdown / JSON，更新不用懂代码。四支柱各自独立维护：

## 支柱① 数学前备库（content/math.md）

- 单文件，条目编号 M01–M56，按大类（A 线性代数 / B 微积分 / C 常微分 / D 偏微分 / E 傅里叶 / F 复变 / G 特殊函数 / H 概率统计 / I 数值方法）排列。
- 新条目在对应大类末尾追加，编号顺延；改动公式用 LaTeX（行内 `$…$`、独立行 `$$…$$`）。

## 支柱② 量子力学概论（content/overview.md）

- 十章叙事长文，公式一律不推导，只用编号链接 `[F121](#graph?f=F121)` 指到图谱；编号必须对应 formulas.json 中真实存在的节点。
- 改文字不影响其他支柱；新增公式时先在图谱登记编号，再回来引用。

## 支柱③ 公式图谱（content/formulas.json）

- 结构：`nodes`（id=编号、name、formula、module、note、app、pre）与 `edges`（source→target）。
- 新增公式：在 nodes 追加一条（编号 F 段内顺延），在 edges 补上前置依赖边，再在 overview.md 里引用。
- `app: true` 表示应用公式（图谱里标「应用」、不再给推导）；`note` 可写用途说明。
- 校验：节点/边格式必须自洽（无悬空引用、无自环），改完建议本地开 `python -m http.server` 实测蛛网。

## 支柱④ 例题精解（content/problems/ + content/manifest.json）

- 每个模块一个文件，如 `content/problems/模块4-一维束缚态.md`。
- 例题格式固定：题号 + **应用公式**（`[F145](#graph?f=F145)` 链接清单）→ 已知/求 → 严谨分步解（含 ⚠️ 易错标注、全程带单位）。
- 新模块：写例题文件后，在 `content/manifest.json` 里把对应模块的 `problem` 字段填上文件路径。

## 提交与发布

```bash
git add -A
git commit -m "更新：…"
git push
```

GitHub Pages 每次推送自动发布，约 1 分钟生效。

## 本地预览

```bash
python -m http.server 8000
# 浏览器打开 http://localhost:8000
```

## 常见问题

- **公式乱码**：检查 LaTeX 里是否含 `<`、`>`、`*` 等字符——渲染管线已对公式做 HTML 转义保护，但写法上尽量用 `\langle`/`\rangle`、`\ast` 等转义符更稳。
- **蛛网空白**：多为 CDN 加载失败；确认能访问 jsDelivr（fastly.jsdelivr.net），刷新重试。
- **链接跳转后不在顶部**：网址带 `#/graph?f=Fxxx` 直达弹卡属正常设计；普通章节跳转会回到页面顶部。
