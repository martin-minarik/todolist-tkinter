from flask import Flask, request
from flask_restful import Api, Resource, abort
from datetime import datetime
from database import db
from todo_record import TodoRecord
from marshmallow_schema import ma, todorecord_schema, todorecord_list_schema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # new

api = Api(app)
db.init_app(app)
ma.init_app(app)


class TodoRecordResource(Resource):
    def get(self, todo_record_id):
        todo_record = TodoRecord.query.get_or_404(todo_record_id)
        return todorecord_schema.dump(todo_record)

    def delete(self, todo_record_id):
        todo_record = TodoRecord.query.get_or_404(todo_record_id)
        db.session.delete(todo_record)
        db.session.commit()
        return '', 204

    def put(self, todo_record_id):
        todo_record = TodoRecord.query.get_or_404(todo_record_id)
        todo_record.title = request.json['title']
        todo_record.status = request.json['status']
        todo_record.description = request.json['description']
        todo_record.last_edited = datetime.now().replace(microsecond=0)
        todo_record.due_to = datetime.strptime(request.json['due_to'], "%Y-%m-%dT%H:%M:%S").replace(microsecond=0)
        db.session.commit()
        return '', 204


class TodoRecordListResource(Resource):
    def get(self):
        todo_records = TodoRecord.query.all()
        if keyword := (request.args.get('search', '')).lower():
            todo_records = [*filter(lambda item: keyword in item.title.lower(), todo_records)]

        return todorecord_list_schema.dump(todo_records)

    def post(self):
        todo_record = TodoRecord(
            title=request.json['title'],
            status=request.json['status'],
            description=request.json['description'],
            last_edited=datetime.now().replace(microsecond=0),
            created=datetime.now().replace(microsecond=0),
            due_to=datetime.strptime(request.json['due_to'], "%Y-%m-%dT%H:%M:%S"), )

        db.session.add(todo_record)
        db.session.commit()

        return '', 204

    def delete(self):
        try:
            db.session.query(TodoRecord).delete()
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(404, message='Failed to delete all rows')

        return '', 204


api.add_resource(TodoRecordResource, '/todorecord/<int:todo_record_id>')
api.add_resource(TodoRecordListResource, '/todorecords')

if __name__ == '__main__':
    app.run(debug=False)
