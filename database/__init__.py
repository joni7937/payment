from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Ссылка для нашего БД
SQLALCHEMY_DATABASE_URI = "sqlite:///pay.db"

# Подключения к базе данных
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Генерация сессий
SessionLocal = sessionmaker(bind=engine)

# Общий класс для моделей(models.py)
Base = declarative_base()

# Импорт моделей
from database import models


# Функция для генерации связей к базе данных
def get_db():
    db = SessionLocal
    try:
        yield db
    except Exception:
        db.rollback()
        raise

    finally:
        db.close()
