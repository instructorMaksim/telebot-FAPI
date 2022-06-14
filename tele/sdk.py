import requests

from app.config import TG_URL, APP_HOST


async def setWebhook(APP_HOST) -> bool:
    json_params = {
        "url": APP_HOST,
        "allowed_updates": ["message", "edited_message", "callback_query"]
    }
    endpoint = TG_URL + "setWebhook"
    result = requests.post(endpoint, json=json_params)
    js = result.json()
    return js.get("ok", False)


async def deleteWebhook() -> bool:
    pass


async def getWebhookInfo() -> dict:
    pass


async def sendMessage(chat: int, msg: str) -> dict:
    pass
