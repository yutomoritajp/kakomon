from sqlmodel import SQLModel, Field
from sqlalchemy import UniqueConstraint, Index, text

class Quiz(SQLModel, table=True):
    __tablename__ = "quizzes"
    id: int | None = Field(default=None, primary_key=True)
    exam_id: int = Field(foreign_key="exams.id")
    number: int = Field(sa_column_kwargs={"comment": "問題番号"})
    content: str = Field(sa_column_kwargs={"comment": "Markdown形式の問題文テキスト"})

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

class Option(SQLModel, table=True):
    __tablename__ = "options"
    __table_args__ = (
        UniqueConstraint("quiz_id", "sort_order", name="uq_options_quiz_id_sort_order"),
        Index("uq_options_quiz_id_correct", "quiz_id", unique=True, postgresql_where=text("correct_flag=true"))
    )
    id: int | None = Field(default=None, primary_key=True)
    quiz_id: int = Field(foreign_key="quizzes.id")
    sort_order: int = Field(sa_column_kwargs={"comment": "選択肢の順序（1=ア, 2=イ, 3=ウ, 4=エ）"})
    correct_flag: bool = Field(sa_column_kwargs={"comment": "正解フラグ（true: 正解, false: 不正解）"})

class Commentary(SQLModel, table=True):
    __tablename__ = "commentaries"
    id: int | None = Field(default=None, primary_key=True)
    quiz_id: int = Field(foreign_key="quizzes.id", unique=True)
    content: str = Field(sa_column_kwargs={"comment": "Markdown形式の解説テキスト"})

metadata = SQLModel.metadata