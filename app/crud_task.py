from sqlalchemy.orm import Session
from app.models import Task
from app.schemas import TaskSchema, TaskCreateSchema, TaskUpdateSchema


def get_task(db: Session, task_uuid: str) -> Task | None:
    return db.query(Task).filter(Task.uuid == task_uuid).first()


def get_task_list(db: Session) -> list[Task]:
    return db.query(Task).all()


def create_task(db: Session, task: TaskCreateSchema) -> Task:
    db_task = Task(
        title=task.title,
        description=task.description,
        status=task.status
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_uuid: str, task_update: TaskUpdateSchema) -> Task | None:
    db_task = get_task(db, task_uuid)
    if db_task:
        update_data = task_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_uuid: str) -> bool:
    db_task = get_task(db, task_uuid)
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False
