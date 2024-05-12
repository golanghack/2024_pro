from fastapi import FastAPI
import uvicorn
from src.web import explorer
from src.web import create

app = FastAPI()
app.include_router(explorer.router)
app.include_router(create.router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)