import datetime

from pydantic import BaseModel, validator
from domain.user.user_schema import User

# BaseModel을 상속한 Question 클래스를 만들었다.
class Question(BaseModel):
    id: int
    topic : str
    content: str
    create_date: datetime.datetime
    user: User 

    # orm_mode 항목을 True로 설정하면 Question 모델의 항목들이 자동으로 Question 스키마로 매핑된다.
    class Config:
        orm_mode = True


class QuestionCreate(BaseModel):
    topic : str
    content: str
    apikey: str
    # subject와 content에는 빈 값을 허용하지 않도록 했다.
    @validator('content')
    def not_empty(cls,v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class QuestionList(BaseModel):
    question_list: list[Question] = []


# QuestionCreate 스키마에 이미 subject, content 항목이 있으므로 QuestionCreate 스키마를 상속하고 question_id 항목만 추가
class QuestionUpdate(QuestionCreate):
    question_id: int

class QuestionDelete(BaseModel):
    question_id: int

class QuestionAnswer(BaseModel):
    answer_list: list[str] = []