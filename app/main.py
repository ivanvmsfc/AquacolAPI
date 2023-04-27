import uvicorn
from app.v1.api import app

app = app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8009)
