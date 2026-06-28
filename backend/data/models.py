from sqlmodel import SQLModel, Field
from sqlalchemy import CheckConstraint

class Quiz(SQLModel, table=True):
    __tablename__ = "quizzes"
    __table_args__ = (
        CheckConstraint("correct_option between 0 and 3", name="check_correct_option"),
    )
    id: int | None = Field(default=None, primary_key=True)
    exam_id: int = Field(foreign_key="exams.id")
    number: int = Field(sa_column_kwargs={"comment": "問題番号"})
    content: str = Field(sa_column_kwargs={"comment": "Markdown形式の問題文テキスト"})
    correct_option: int = Field(sa_column_kwargs={"comment": "正解の選択肢（0=ア, 1=イ, 2=ウ, 3=エ）"})

class Exam(SQLModel, table=True):
    __tablename__ = "exams"
    id: int | None = Field(default=None, primary_key=True)
    period_id: int = Field(foreign_key="periods.id")
    section_id: int = Field(foreign_key="sections.id")

class Period(SQLModel, table=True):
    __tablename__ = "periods"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, sa_column_kwargs={"comment": "試験回（例：令和7年秋）"})

class Section(SQLModel, table=True):
    __tablename__ = "sections"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, sa_column_kwargs={"comment": "試験区分（例：午前Ⅱ）"})

class Commentary(SQLModel, table=True):
    __tablename__ = "commentaries"
    id: int | None = Field(default=None, primary_key=True)
    quiz_id: int = Field(foreign_key="quizzes.id", unique=True)
    content: str = Field(sa_column_kwargs={"comment": "Markdown形式の解説テキスト"})

metadata = SQLModel.metadata