from pydantic import BaseModel
from typing import Union

class Post(BaseModel):

    title: Union[str, None] = None
    content: str
