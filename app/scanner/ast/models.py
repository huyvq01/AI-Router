from pydantic import BaseModel, Field


class FunctionNode(BaseModel):
    name: str

    line: int


class ClassNode(BaseModel):
    name: str

    line: int

    methods: list[FunctionNode] = Field(default_factory=list)


class ModuleNode(BaseModel):
    path: str

    classes: list[ClassNode] = Field(default_factory=list)

    functions: list[FunctionNode] = Field(default_factory=list)

    imports: list[str] = Field(default_factory=list)
