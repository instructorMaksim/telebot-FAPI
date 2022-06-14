from fastapi import APIRouter
from loguru import logger as log 
from tele.dto import UpdateTelegram, sendMessage
from config import TG_URL


router = APIRouter()


@router.post("/tg_wh")
async def tg_wh(r: UpdateTelegram):  # r: Request
    log.debug(r)
    return {"Status": "OK"}
    # json_request = await r.json()
    # js = json.dumps(r, ensure_ascii=False)
    # json_request["message"]["from"]["first_name"]
    #return {"Status": "OK"}


@router.post(f"{TG_URL}/post")
async def tg_wh(g: sendMessage):
    return {"Status": "OK"}