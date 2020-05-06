from blog.base import BaseModel


def user_directory_path(instance: BaseModel, filename: str) -> str:
    return f'uploads/{filename}'