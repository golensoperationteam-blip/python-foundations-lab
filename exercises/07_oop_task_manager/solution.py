import sys
from typing import Dict, List, Optional, Any


class TaskNotFoundError(Exception):
    """Raised when a requested task ID is not found."""
    pass


class Task:
    """Represents an individual agent task."""
    VALID_STATUSES = {"pending", "in_progress", "completed"}

    def __init__(self, task_id: str, title: str, priority: int = 1):
        if not task_id or not title:
            raise ValueError("task_id and title cannot be empty")
        self.task_id = str(task_id)
        self.title = str(title)
        self.priority = int(priority)
        self.status = "pending"

    def set_status(self, new_status: str) -> None:
        if new_status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status '{new_status}'. Allowed: {self.VALID_STATUSES}")
        self.status = new_status

    def mark_completed(self) -> None:
        self.set_status("completed")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        task = cls(task_id=data["task_id"], title=data["title"], priority=data.get("priority", 1))
        task.set_status(data.get("status", "pending"))
        return task

    def __repr__(self) -> str:
        return f"Task(id='{self.task_id}', title='{self.title}', status='{self.status}', priority={self.priority})"


class TaskManager:
    """Manages a collection of tasks using object composition."""
    def __init__(self):
        self._tasks: Dict[str, Task] = {}

    def add_task(self, task: Task) -> None:
        if task.task_id in self._tasks:
            raise ValueError(f"Task with ID '{task.task_id}' already exists")
        self._tasks[task.task_id] = task

    def get_task(self, task_id: str) -> Task:
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"Task '{task_id}' not found")
        return self._tasks[task_id]

    def list_tasks(self, status: Optional[str] = None) -> List[Task]:
        if status:
            return [t for t in self._tasks.values() if t.status == status]
        return list(self._tasks.values())

    def total_count(self) -> int:
        return len(self._tasks)


if __name__ == "__main__":
    manager = TaskManager()
    t1 = Task("T-01", "Inspect Model Registry", priority=1)
    t2 = Task("T-02", "Deploy Proxy Server", priority=2)
    manager.add_task(t1)
    manager.add_task(t2)
    t1.mark_completed()
    print(f"OOP Task Manager Initialized: {manager.total_count()} tasks tracked.")
    print(f"Completed Tasks: {[t.title for t in manager.list_tasks(status='completed')]}")
