from fastapi import FastAPI, Form
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


temp_data = {}


@app.get("/notification")
async def getNotification():
    return {"message": temp_data.get("noti")}

@app.post("/notification")
async def postNotification(text: str = Form(...)):
    temp_data["noti"] = text
    return {"message": "Data stored successfully"}