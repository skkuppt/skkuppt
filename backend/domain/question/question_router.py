
from fastapi import APIRouter  # , Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

# from database import get_db
from domain.question import question_schema
from domain.util.PPTmaker import gpt_pptmaker
from fastapi.responses import JSONResponse

# 라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위를 말한다.

router = APIRouter(
    # prefix 속성은 요청 URL에 항상 포함되어야 하는 값이다.
    prefix="/api/question",
)


@router.post("/create")
# async를 붙여줘야 합니다.
async def question_create(_question_create: question_schema.QuestionCreate):

    answer = gpt_pptmaker(_question_create.topic, _question_create.details)
    # 응답은 JSON으로 하는게 일반적입니다.
    return JSONResponse(content={"answer": answer})
