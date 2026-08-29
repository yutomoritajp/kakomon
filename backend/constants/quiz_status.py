from enum import Enum


class QuizStatus(Enum):
    """
    QuizStatus（画像配置および画面確認状況）
    """
    ## 画像配置前
    DRAFT = "draft"
    
    ## レビュー中（画像配置済み）
    IN_REVIEW = "in_review"
    
    ## 公開中（画面確認済み）
    PUBLISHED = "published"
