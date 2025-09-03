from pydantic import BaseModel
from enum import Enum


class TaskStatusChoices(str, Enum):

    created = "Создано"
    processed = "В работе"
    closed = "Завершено"


class TaskSchema(BaseModel):

    uuid: str
    title: str
    description: str | None
    status: TaskStatusChoices


class TaskCreateSchema(BaseModel):

    title: str
    description: str | None
    status: TaskStatusChoices = TaskStatusChoices.created
