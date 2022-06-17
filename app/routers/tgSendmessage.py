from fastapi import APIRouter
from loguru import logger as log 
from tele.dto import sendMessage
from config import TG_URL
import requests

router = APIRouter()


# @router.post(f"{TG_URL}/sendMessage")
# async def send_message(d: sendMessage):
#     return {"Status": "OK"}

# async def send_message(text: str):
#     method = TG_URL + "/sendMessage"
#     response = requests.post(method, s = sendMessage)   

