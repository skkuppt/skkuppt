
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.question import question_schema, question_crud
from domain.user.user_router import get_current_user
from models import User
from domain.util.PPTmaker import gpt_pptmaker

# 라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위를 말한다.

router = APIRouter(
    #prefix 속성은 요청 URL에 항상 포함되어야 하는 값이다.
    prefix="/api/question",
)


@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db)):
    total, _question_list = question_crud.get_question_list(db=db)
    return {
        'question_list': _question_list
    }


@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db,question_id=question_id)
    return question

@router.post("/create")
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    
    answer = gpt_pptmaker(_question_create.topic, _question_create.content, _question_create.apikey )

    return answer
    

@router.put("/update/{question_id}",status_code=status.HTTP_204_NO_CONTENT)
def question_update(_question_update: question_schema.QuestionUpdate, 
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db,question_id=_question_update.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을 수 없습니다.")
    
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    
    question_crud.update_question(db=db, db_question=db_question, question_update=_question_update)
                    

@router.delete("/delete/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def question_delete(_question_delete: question_schema.QuestionDelete,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = question_crud.get_question(db,question_id=_question_delete.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을 수 없습니다.")
    
    if current_user.id != db_question.user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    
    question_crud.delete_question(db=db, db_question=db_question)
    