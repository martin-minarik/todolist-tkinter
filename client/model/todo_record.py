from dataclasses import dataclass
from datetime import datetime
from marshmallow import Schema, fields, post_load
from typing import Optional


class TodoRecordSchema(Schema):
    id = fields.Integer()
    title = fields.Str()
    status = fields.Str()
    description = fields.Str()
    created = fields.DateTime()
    last_edited = fields.DateTime()
    due_to = fields.DateTime()

    @post_load
    def make_todo_record(self, data, **kwargs):
        return TodoRecord(**data)


todo_record_schema = TodoRecordSchema()
todo_record_list_schema = TodoRecordSchema(many=True)


@dataclass
class TodoRecord:
    id: Optional[int]
    title: str
    status: str
    description: Optional[str]
    created: Optional[datetime]
    last_edited: Optional[datetime]
    due_to: datetime
