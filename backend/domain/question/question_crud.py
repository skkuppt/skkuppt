from datetime import datetime
from sqlalchemy import and_

from domain.question.question_schema import QuestionCreate, QuestionUpdate, QuestionDelete
from models import Question, User
from sqlalchemy.orm import Session

def get_question_list(db : Session):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list

def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db: Session, question_create: QuestionCreate, user: User):
    db_question = Question(topic = question_create.topic,
                           content=question_create.content,
                           create_date=datetime.now(),
                           user=user)
    db.add(db_question)
    db.commit()


def update_question(db: Session, db_question : Question,
                    question_update: QuestionUpdate):
    db_question.content = question_update.content
    db.add(db_question)
    db.commit()

def delete_question(db: Session, db_question : Question):
    db.delete(db_question)
    db.commit()

