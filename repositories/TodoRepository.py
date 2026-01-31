from typing import List
from entities.Todo import Todo

class TodoRepository():
    def __init__(self):
        self.data: List[Todo] = []  # type: ignore

    def get_all_todos(self) -> List[Todo]: # type: ignore
        return self.data

    def add_todo(self, new_todo: Todo):
        self.data.append(new_todo)

    def remove_todo(self, id: int) -> bool:
        # cari todo berdasarkan id
        target_todo = next((todo for todo in self.data if todo.id == id), None)
        if target_todo is None:
            return False
        self.data.remove(target_todo)
        return True

def update_todo(self, id: int, new_title: str = None, new_status: bool = None) -> bool:
    target_todo = next((todo for todo in self.data if todo.id == id), None)
    if target_todo is None:
        return False

    if new_title is not None:
        target_todo.title = new_title
    if new_status is not None:
        target_todo.is_finished = new_status

    return True

def search_todo(self, keyword: str):
    return [todo for todo in self.data if keyword.lower() in todo.title.lower()]

def sort_todo(self, key: str):
    if key == "title":
        self.data.sort(key=lambda todo: todo.title.lower())
    elif key == "status":
        self.data.sort(key=lambda todo: todo.is_finished)
    elif key == "id":
        self.data.sort(key=lambda todo: todo.id)
