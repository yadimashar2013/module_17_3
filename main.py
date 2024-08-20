from fastapi import FastAPI
from routers import task, user


app = FastAPI()


@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

# uvicorn app:app --reload
# python -m uvicorn main:app