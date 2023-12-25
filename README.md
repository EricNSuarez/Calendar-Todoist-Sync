# Calendar-Todoist-Sync

## Overview

TodoSync-Cal-Git is a Python project to synchorinize tasks between Todoist and Google Calendar. This tool allows you to manage your to-do list in Todoist while keeping your events organized in Google Calendar.

## Features

- Oneway synchronization from Todoist to Google Calendar.
- **Optional** bidirectional synchronization between Todoist and Google Calendar.
- Option to add a **Todoist** tag to the events created in Google Calendar. 
- Ability to
    - Choose in which calendar the tasks will be synchronized to. 
    - Omit synchronization of tasks without a given datetime. 
    - Delete completed tasks from the calendar. 
    - Add duration to the events created.
    - Set a default duration for tasks. 

### Prerequisites

- Python 3.x installed
- Todoist API key
- Google Calendar API credentials

### Installation

...

### Usage

1. Run the synchronization script:

    ```bash
    python sync.py
    ```

## License

This project is licensed under the [GNU General Public License (GPL)](LICENSE).