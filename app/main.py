import json
import asyncio
from fastapi import FastAPI
from loguru import logger as log
from tele.sdk import setWebhook, deleteWebhook
from app.config import APP_HOST
# from tele.dto import UpdateTelegram
from .routers import tgUpdate

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(tgUpdate.router)

# @app.post("/tg_wh")
# async def tg_wh(r: UpdateTelegram):  # r: Request
#     log.debug(r)
#     # json_request = await r.json()
#     # js = json.dumps(r, ensure_ascii=False)
#     # json_request["message"]["from"]["first_name"]
#     return {"Status": "OK"}




@app.on_event("startup")
async def on_startup():
    log.success("APP start")
    log.debug("APP start")
    log.info("APP start")
    log.warning("APP start")
    log.error("APP start")
    log.critical("APP start")
    # 1. Получить getWebhookInfo
    # 2. Если вебхук отличается от нашего - то удалить через deleteWebhook
    # 3 и затем setWebhook
    # -- если не отличается -то не трогаем ничего
    url = f"{APP_HOST}/tg_wh"
    was_set = await setWebhook(url)
    if was_set:
        log.success("Webhook was set")
    else:
        log.warning("Webhook was not set")

    # Пример как можно одновременно собрать все запросы разом
    # await asyncio.gather(*[
    #     setWebhook(),
    #     setWebhook(),
    #     setWebhook()
    # ])

@app.on_event("shutdown")
async def on_shutdown():
    await deleteWebhook()
    log.debug("Webhook was deleted")




