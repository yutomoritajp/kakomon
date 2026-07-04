from sqlmodel import SQLModel, Field
from sqlalchemy import CheckConstraint, UniqueConstraint

class Quiz(SQLModel, table=True):
    __tablename__ = "quizzes"
    __table_args__ = (
        CheckConstraint("correct_option between 0 and 3", name="check_correct_option"),
        CheckConstraint("status in ('draft', 'in_review', 'published')", name="check_status"),
    )
    id: int | None = Field(default=None, primary_key=True)
    exam_id: int = Field(foreign_key="exams.id")
    number: int = Field(sa_column_kwargs={"comment": "問題番号"})
    content: str = Field(sa_column_kwargs={"comment": "Markdown形式の問題文テキスト"})
    correct_option: int = Field(sa_column_kwargs={"comment": "正解の選択肢（0=ア, 1=イ, 2=ウ, 3=エ）"})
    status: str = Field(sa_column_kwargs={"comment": "draft=画像未配置, in_review=画像配置済み・レビュー待ち, published=公開中"})

class Exam(SQLModel, table=True):
    __tablename__ = "exams"
    __table_args__ = (
        UniqueConstraint("period_code", "section_code", name="uix_period_section"),
    )
    id: int | None = Field(default=None, primary_key=True)
    period_code: str = Field(foreign_key="periods.code")
    section_code: str = Field(foreign_key="sections.code")

class Period(SQLModel, table=True):
    __tablename__ = "periods"
    code: str = Field(primary_key=True, sa_column_kwargs={"comment": "試験回識別子（例：r7）"})
    name: str = Field(unique=True, sa_column_kwargs={"comment": "試験回表示名（例：令和7年度）"})
    sort_order: int = Field(unique=True, sa_column_kwargs={"comment": "並び順"})

class Section(SQLModel, table=True):
    __tablename__ = "sections"
    code: str = Field(primary_key=True, sa_column_kwargs={"comment": "試験区分識別子（例：am2）"})
    name: str = Field(unique=True, sa_column_kwargs={"comment": "試験区分表示名（例：午前Ⅱ）"})
    sort_order: int = Field(unique=True, sa_column_kwargs={"comment": "並び順"})

class Commentary(SQLModel, table=True):
    __tablename__ = "commentaries"
    id: int | None = Field(default=None, primary_key=True)
    quiz_id: int = Field(foreign_key="quizzes.id", unique=True)
    content: str = Field(sa_column_kwargs={"comment": "Markdown形式の解説テキスト"})

metadata = SQLModel.metadata