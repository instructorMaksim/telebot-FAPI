from xmlrpc.client import Boolean
import requests

from app.config import TG_URL, APP_HOST
from dto import sendTheMessage


async def setWebhook() -> bool:
    json_params = {
        "url": APP_HOST,
        "allowed_updates": ["message", "edited_message", "callback_query"]
    }
    endpoint = TG_URL + "setWebhook"
    result = requests.post(endpoint, json=json_params)
    js = result.json()
    return js.get("ok", False)


async def deleteWebhook() -> bool:
    params = {
        "drop_pending_updates": True,
    }
    endpoint = TG_URL + "deleteWebhook"
    result = requests.post(endpoint, params=params)
    js = result.json()
    return js.get("ok", False)  #под вопросом
    #pass


async def WebhookInfo() -> dict:
    endpoint = TG_URL + "getWebhookinfo"
    result = requests.post(endpoint)
    js = result.json()
    return js.get("ok", False)  #ваще хз какой результат тут
    #pass


async def send_message(chat: int, msg: str) -> dict:
    method = TG_URL + "/sendMessage"
    response = requests.post(method, params = sendTheMessage) 
    #pass
    #вызов имени функции("text")