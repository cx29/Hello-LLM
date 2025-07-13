# FastAPI 用于创建API应用实例
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 最小可运行的fastAPI
app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


tasks = []


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_tasks(task_id: int):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return {"msg": "Deleted"}
