from pydantic import BaseModel


class RegistroCreate(BaseModel):
    titulo: str
    descricao: str | None = None
    ativo: bool = True


class RegistroResponse(RegistroCreate):
    id: int