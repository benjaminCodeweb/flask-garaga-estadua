from pydantic import BaseModel
from typing import Optional

class AutoCreateSchema(BaseModel):
    modelo: str
    patente:  Optional[str] = None
    image_url: Optional[str] = None
    cant_horas: Optional[int] = None
    