import requests
from client.config import API_URL
from client.model.todo_record import TodoRecord, todo_record_schema, todo_record_list_schema
import logging


def get_todo_records():
    logging.info("Fetching all records")
    response = requests.get(f"{API_URL}/todorecords")
    if response.ok and response.json:
        return todo_record_list_schema.load(response.json())
    raise RuntimeError("GET ALL request failed")


def search_todo_records(keyword: str):
    logging.info(f"Fetching records by keyword: {keyword}")
    response = requests.get(f"{API_URL}/todorecords", params={"search": keyword})
    if response.ok and response.json:
        return todo_record_list_schema.load(response.json())
    raise RuntimeError("GET ALL request failed")


def delete_todo_records():
    logging.info("Deleting all records")
    response = requests.delete(f"{API_URL}/todorecords")
    if response.ok:
        return
    raise RuntimeError("DELETE ALL request failed")


def create_todo_record(todo_record: TodoRecord):
    logging.info("Creating new record")
    response = requests.post(f"{API_URL}/todorecords", json=todo_record_schema.dump(todo_record))
    if response.ok and response.json:
        return
    raise RuntimeError("POST request failed")


def update_todo_record(todo_record: TodoRecord):
    logging.info("Updating record")

    response = requests.put(f"{API_URL}/todorecord/{todo_record.id}", json=todo_record_schema.dump(todo_record))
    if response.ok and response.json:
        return
    raise RuntimeError("PUT request failed")


def delete_todo_record(todo_record: TodoRecord):
    logging.info("Deleting record")
    response = requests.delete(f"{API_URL}/todorecord/{todo_record.id}")
    if response.ok and response.json:
        return
    raise RuntimeError("DELETE request failed")
