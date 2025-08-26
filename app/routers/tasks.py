from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas import TaskCreate, TaskRead, TaskUpdate
from ..models import Task, User
from ..deps import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("", response_model=TaskRead, status_code=201)
def create_task(payload: TaskCreate, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    task = Task(title=payload.title, description=payload.description, done=payload.done, owner_id=current.id)
    db.add(task); db.commit(); db.refresh(task)
    return task

@router.get("", response_model=List[TaskRead])
def list_tasks(db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    return db.query(Task).filter(Task.owner_id == current.id).order_by(Task.created_at.desc()).all()

@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(task, k, v)
    db.commit(); db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task); db.commit()
