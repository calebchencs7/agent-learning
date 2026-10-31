# 金融文本分析页面

React 前端通过本地 HTTP 接口调用上一级目录中已有的 `classify_model`、`extract_model` 和 `match_model`。分别支持文本分类、金融信息抽取和两段文本的语义匹配。模型密钥只在 Python 后端使用。

## 启动

在原有 Python 环境中安装 `openai` 和 `python-dotenv`，并按原脚本的方式配置 `BAILIAN_API_KEY`（环境变量或 `.env`）。然后在本目录打开两个终端：

```bash
# 终端一：启动后端
python server.py
```

```bash
# 终端二：安装并启动前端
npm install
npm run dev
```

打开 Vite 输出的本地地址（通常是 http://localhost:5173）。开发服务器将 `/api` 请求转发到本地 8000 端口。启动后可在页面上切换三种功能，抽取会展示模型识别出的字段；匹配需要输入两段文本。分类模型可能在四个常见类别之外返回其他类别，与原有提示词行为一致。

此接口仅供本机开发使用，没有身份认证；请勿直接暴露到公网。
