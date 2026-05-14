from fastapi import FastAPI

app = FastAPI()


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