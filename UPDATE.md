# 手动更新指南（v2.1.0）

网站是单页静态站：`index.html`（外壳 + 交互）+ `content/`（四支柱内容，全部 Markdown/JSON）。更新不用懂代码，按下面分类操作。

## 目录结构

| 支柱 | 文件 | 改什么 |
|---|---|---|
| 一 · 数学前备库 | `content/math.md` | M01–M56 条目；难懂公式可加「补充」块 |
| 二 · 概论 | `content/overview.md` | 叙事长文；公式只给编号 `[Fxxx](#graph?f=Fxxx)` |
| 三 · 公式图谱 | `content/formulas.json` + `content/formulas-proofs.json` | 节点（公式）/ 边（推导关系）/ 推导打卡 |
| 四 · 例题精解 | `content/manifest.json` + `content/problems/*.md` | 模块清单 + 每题解答 |

## 支柱一：数学库加「补充」

每条目 = 编号标题 + 要点 + 公式 + 用途。若某条难懂，在条目末尾（`用：…` 的下一行）加：

```markdown
<details class="sup"><summary>补充</summary>

**通俗解释**：……
$$公式$$
</details>
```

- 补充块内部是完整 Markdown，公式照常写 LaTeX（`$…$` 行内、`$$…$$` 独立行）；
- 页面渲染为条目旁的「补充」小徽标，点击展开/收起；
- 已有 9 条示例：M03、M06、M09、M13、M17、M23、M25、M32、M55。

## 支柱三：图谱推导打卡

- 图谱的一条边 = 一条推导关系，基础数据在 `content/formulas.json` 的 `edges` 数组，形如 `{"from":"F101","to":"F102"}`。
- 推导状态与推导记录独立存放在 `content/formulas-proofs.json`（key 为 `"Fxxx->Fyyy"`，与边的 from/to 一致）：

```json
{
  "F101->F102": {
    "proved": true,
    "proof": "**已知**：…\n\n**推导**：\n1. …\n$$公式$$"
  }
}
```

- `proved: true` → 图上该边变绿加粗（灰细线 = 还没推过）；`proof` 是该推导的完整记录（Markdown + LaTeX，建议按「已知 / 要求推出 / 推导 / 物理结论」写，点击绿色边可回看）。
- 想新增一条推导关系：往 `formulas.json` 的 `edges` 加 `{"from":"Fxxx","to":"Fyyy"}`（两个节点必须已存在于 `nodes`），推导记录再照上面格式写进 `formulas-proofs.json`。

## 支柱四：新增例题

1. 新建 `content/problems/模块N-名称.md`，格式照现有 `模块4-一维束缚态.md`：先列「应用公式」链接清单（`[Fxxx](#graph?f=Fxxx)`），再按严谨答题规范分步求解；
2. 在 `content/manifest.json` 的 `modules` 数组里给该模块补 `"problem": "problems/模块N-名称.md"`。

## 升版本号（每次发布新功能时）

打开 `index.html`，四处一起改：

1. `var VERSION = "x.y.z";`
2. 页脚 `v<span id="footVer">x.y.z</span>`；
3. `CHANGELOG` 数组头部加 `["x.y.z","本次更新说明"]`；
4. 关于页文案（`v-about` 视图）。

## 本地预览与发布

```bash
python -m http.server 8000
# 浏览器打开 http://localhost:8000
```

`file://` 双击打不开（浏览器禁止本地读取数据文件），必须走本地服务器。

确认无误后提交推送：

```bash
git add -A && git commit -m "v2.1.0 更新说明" && git push
```

GitHub Pages 自动发布，约 1 分钟内生效。线上地址：https://kinghihido.github.io/quantum-mechanics-notes/
