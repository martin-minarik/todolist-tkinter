from flask_marshmallow import Marshmallow
from todo_record import TodoRecord

ma = Marshmallow()

class TodoRecordSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "status", "description", "last_edited", "created", "due_to")
        model = TodoRecord


todorecord_schema = TodoRecordSchema()
todorecord_list_schema = TodoRecordSchema(many=True)

