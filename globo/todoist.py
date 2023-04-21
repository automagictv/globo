from dataclasses import dataclass

from todoist_api_python.api import TodoistAPI


@dataclass
class Todoist:

    def __init__(self, api_token: str):
        self._api = TodoistAPI(api_token)
        self._inbox_id = None

        for project in self._api.get_projects():
            if project.is_inbox_project:
                self._inbox_id = project.id
                break

        return self

    def addTask(self, name: str, description: str):
        return self._api.add_task(content=name, description=description)
