from database.database import SessionLocal
from models.models import TestModel
from ariadne import QueryType, MutationType

query = QueryType()
mutation = MutationType()

def resolve_hello(_, info):
    db = SessionLocal()
    result = db.query(TestModel).first()
    db.close()
    return result.message

def resolve_get_message(_, info, id):
    db = SessionLocal()
    result = db.query(TestModel).filter(TestModel.id == id).first()
    db.close()
    return result.message

def resolve_create_message(_, info, message):
    db = SessionLocal()
    test_model = TestModel(message=message)
    db.add(test_model)
    db.commit()
    db.refresh(test_model)
    db.close()
    return test_model

def resolve_update_message(_, info, id, message):
    db = SessionLocal()
    test_model = db.query(TestModel).filter(TestModel.id == id).first()
    test_model.message = message
    db.commit()
    db.refresh(test_model)
    db.close()
    return test_model

def resolve_delete_message(_, info, id):
    db = SessionLocal()
    test_model = db.query(TestModel).filter(TestModel.id == id).first()
    db.delete(test_model)
    db.commit()
    db.close()
    return True

query.set_field("hello", resolve_hello)
query.set_field("getMessage", resolve_get_message)
mutation.set_field("createMessage", resolve_create_message)
mutation.set_field("updateMessage", resolve_update_message)
mutation.set_field("deleteMessage", resolve_delete_message)