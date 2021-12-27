import uvicorn

from src.application import app

uvicorn.run(app, host="0.0.0.0", port=8001)
