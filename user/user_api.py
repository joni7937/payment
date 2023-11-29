from fastapi import APIRouter

from datetime import datetime

from database.userservice import register_user_db, edit_user_db, delete_user_db, get_exact_user_db, check_user_email_db

from user import UserRegisterValidator, EditUserValidator


user_router = APIRouter(prefix='/user', tags=['Работа с пользователями'])


@user_router.post('/register')
async def register_user(data: UserRegisterValidator):
    new_user_data = data.model_dump()

    checker = check_user_email_db(data.email)

    if not checker:
        result = register_user_db(reg_date=datetime.now(), **new_user_data)

        return {'message': result}

    else:
        return {'message': 'Пользователь уже с таким email существует'}


@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого пользователя нет'}


@user_router.put('/edit-data')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()

    result = edit_user_db(**change_data)

    return {"message": result}


@user_router.delete('/delete_user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    return {'message': result}

