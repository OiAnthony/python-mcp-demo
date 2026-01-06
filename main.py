from logging import debug
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from services.mcp.tools import mcp


mcp_app = mcp.http_app(path="/")

app = FastAPI(title="FastAPI + FastMCP Demo", lifespan=mcp_app.lifespan)

app.mount("/mcp", mcp_app)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "fastapi-fastmcp-demo"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
