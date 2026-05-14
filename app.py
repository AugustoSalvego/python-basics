from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StudyItem(BaseModel):
    topic: str
    hours: int


@app.get("/")
def home():
    return {"message": "Backend is running."}


@app.get("/studies")
def studies():
    return {
        "current_focus": [
            "Python",
            "FastAPI",
            "Git",
            "Backend Development"
        ]
    }


@app.post("/studies")
def create_study(item: StudyItem):
    return {
        "topic": item.topic,
        "hours": item.hours,
        "status": "Study session created successfully"
    }