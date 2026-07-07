from fastapi import FastAPI
from src.api.routes import projects

app = FastAPI()
app.include_router(projects.router)

@app.get("/")
async def root():
    return {"message": "API rodando!"}