from fastapi import FastAPI

from tasks.celery_tasks import my_task

app = FastAPI()


@app.get("/run")
def handle_run():
    task_response = my_task.delay(5, 6)
    return {"message": "Task execution started"}


if __name__ == '__main__':
    uvicorn.run(app, port=8080)
