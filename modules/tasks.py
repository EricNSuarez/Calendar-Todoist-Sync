from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class Task:
    """
    Represents a task.

    Attributes:
    -----------
    id : int
        Unique identifier for the task.
    datetime_start : datetime
        Start time of the task.
    datetime_end : datetime
        End time of the task.
    title : str
        Title of the task.
    description : str, optional
        Description of the task. Default is an empty string.
    duration : int, optional
        Duration of the task in minutes. Default is 15.
    task_id : str, optional
        ID of the task. Default is None.
    event_id : str, optional
        ID of the event. Default is None.
    project_id : str, optional
        ID of the project. Default is None.
    calendar_id : str, optional
        ID of the calendar. Default is None.
    tags : List[str], optional
        List of tags associated with the task. Default is an empty list.
    bidirectional_sync : bool, optional
        Flag indicating whether the task is synced bidirectionally. Default is False.
    """
    id: int
    datetime_start: datetime
    datetime_end: datetime
    title: str
    description: str = ''
    duration: int = 15
    task_id: Optional[str] = None
    event_id: Optional[str] = None
    project_id: Optional[str] = None
    calendar_id: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    bidirectional_sync: bool = False