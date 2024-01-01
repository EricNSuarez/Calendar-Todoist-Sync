from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime, timedelta

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
    title: str
    description: str = ''
    duration: int = 15
    task_id: Optional[str] = None
    event_id: Optional[str] = None
    project_id: Optional[str] = None
    calendar_id: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    bidirectional_sync: bool = False

    def __post_init__(self):
        """
        Adjust task attributes according to the description and title.
        """
        self.datetime_end = self.datetime_start + timedelta(minutes=self.duration)

    def get_properties_from_description_excerpt(self) -> Dict|None:
        """
        Extracts sync properties data from the task excerpt delimited by marks on the description:

        Returns:
        -----------
            Dict or None:
                The extracted sync properties data, or None if markers are not found.

        Markers:
        -----------
            start:
                "-----[TODOIST TASK]-----"
            end: 
                "-------------------"
        """

        # Find text between markers
        start_marker = "-----[TODOIST TASK]-----"
        end_marker = "-------------------"

        start_idx = self.description.find(start_marker)
        end_idx = self.description.find(end_marker, start_idx)

        if start_idx == -1 or end_idx == -1:
            return None

        start_idx += len(start_marker)

        sync_properties = self.description[start_idx:end_idx].strip()

        # Iterate over excerpt to get relevant data
        result_dict = {'ID':None, 'DURATION': None, 'EVENT_ID': None}

        for line in sync_properties.splitlines():
            parts = line.split(':')
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                result_dict[key] = value
        
        return result_dict
