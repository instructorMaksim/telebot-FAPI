from pydantic import BaseModel, Field


class FromUser(BaseModel):
    id: int
    is_bot: bool
    first_name: str = None
    last_name: str = None
    username: str = None
    language_code: str

class Message(BaseModel):
    from_user: FromUser = Field(alias="from")

class UpdateTelegram(BaseModel):
    update_id: int
    message: Message = None
    edited_message: Message = None


class sendMessage(BaseModel):
    id: int
    text: str = "it's an experiment"


class sendWeather(BaseModel):
    name: str = name
    temp: float 
    main: str
    wind: float 
    
# print(
#     ' city:', q['name'],'\n',
#     'temp:',  q['main']["temp"],"degrees\n",
#     'main:', q['weather'][0]['description'],"\n",
#     'wind:', q['wind']['speed'],'km/h'
# )