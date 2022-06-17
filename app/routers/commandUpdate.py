from fastapi import APIRouter
from loguru import logger as log 
from tele.dto import sendMessage
from config import TG_URL


router = APIRouter()

data = ['start', 'help']

#@router()
