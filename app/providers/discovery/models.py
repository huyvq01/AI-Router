from pydantic import BaseModel


class OllamaModel(BaseModel):
    name: str
    context_window: int = 0
    family: str = ""
    parameter_size: str = ""
    quantization: str = ""