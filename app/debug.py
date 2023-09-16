import uvicorn

from test import app


if __name__ == "__main__":
    uvicorn.run("debug:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
