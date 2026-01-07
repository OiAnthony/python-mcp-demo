# Python MCP 演示

一个展示 FastMCP (Model Context Protocol) 与 FastAPI 集成的演示项目。

## 概览

本项目演示了如何使用 FastMCP 构建 MCP 服务器，并通过 FastAPI 应用程序将其公开。它包含一个基于 Web 的界面，用于与 MCP 工具进行交互。

## 功能特性

- **FastAPI 集成**：具有自动 API 文档功能的现代 Python Web 框架
- **MCP 工具**：展示 MCP 能力的三个示例工具
  - `greet`：个性化问候函数
  - `add_numbers`：简单的算术运算
  - `get_server_info`：服务器元数据检索
- **Web 界面**：用于测试 MCP 工具的交互式 HTML 界面
- **健康检查端点**：服务监控端点

## 环境要求

- Python >= 3.11

## 安装

```bash
# Clone the repository
git clone git@github.com:OiAnthony/python-mcp-demo.git
cd python-mcp-demo

# Create virtual environment (optional but recommended)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies using uv (recommended)
uv sync
```

## 使用方法

### 启动服务器

```bash
# Using uvicorn directly
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Or run the main script
python main.py
```

服务器将在 `http://localhost:8000` 启动

### 可用端点

- `GET /` - 用于 MCP 工具交互的 Web 界面
- `GET /health` - 健康检查端点
- `/mcp/*` - MCP 服务器端点（HTTP 传输）
- `/static/*` - 静态文件服务

### 访问 Web 界面

打开浏览器并访问：

```
http://localhost:8000
```

### API 文档

FastAPI 提供自动生成的交互式 API 文档：

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 项目结构

```
python-mcp-demo/
├── main.py                 # FastAPI application entry point
├── services/
│   └── mcp/
│       ├── __init__.py
│       └── tools.py        # MCP tools implementation
├── static/
│   └── index.html          # Web interface
├── pyproject.toml          # Project metadata and dependencies
└── README.md
```

## MCP 工具

### 1. greet(name: str)

按名字问候用户。

**参数：**

- `name`: 要问候的人的名字

**返回：** 一条问候消息

### 2. add_numbers(a: int, b: int)

将两个数字相加。

**参数：**

- `a`: 第一个数字
- `b`: 第二个数字

**返回：** a 和 b 的和

### 3. get_server_info()

获取 MCP 服务器的信息。

**返回：** 包含服务器信息的字典

## 开发

### 添加新的 MCP 工具

如需添加新工具，请编辑 `services/mcp/tools.py`：

```python
@mcp.tool()
def your_tool_name(param: str) -> str:
    """Your tool description.
    
    Args:
        param: Parameter description
    
    Returns:
        Return value description
    """
    # Your implementation
    return result
```

### 使用自动重载运行

开发服务器支持自动重载，以加快开发速度：

```bash
uvicorn main:app --reload
```

### 使用 MCP Inspector 进行调试

MCP Inspector 是一个强大的调试工具，可以用来测试和检查 MCP 服务器的功能。

#### 启动 MCP Inspector

在项目运行的情况下，打开新的终端窗口并运行：

```bash
npx @modelcontextprotocol/inspector
```

这将启动一个交互式调试界面，允许你：

- 列出 MCP 服务器公开的所有工具和资源
- 在 Web UI 中调用工具并查看结果
- 检查工具参数和返回值
- 测试工具的输入/输出
- 调试工具实现

#### 访问 Inspector Web 界面

运行上述命令后，Inspector 会在随机端口上启动 Web 界面。具体的访问地址会显示在命令行输出中，通常是 `http://localhost:<port>`，其中 `<port>` 是分配的端口号。查看终端输出找到正确的 URL。

#### 调试工作流

1. 启动开发服务器：`python main.py`
2. 在新终端中启动 Inspector：`npx @modelcontextprotocol/inspector`
3. 在 Inspector Web UI 中测试你的工具
4. 根据结果迭代开发

## 依赖项

- **fastapi**: 用于构建 API 的现代 Web 框架
- **fastmcp**: 用于 Model Context Protocol (模型上下文协议) 的 FastMCP 库
- **uvicorn**: 用于运行 FastAPI 应用程序的 ASGI 服务器
