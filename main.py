from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v1/getAllTasks/{user_id}/")
def get_all_tasks_of_user(user_id: str):
    tasks = ["read the data from database",
             "check user access",
             "return only this users tasks"]
    return tasks

