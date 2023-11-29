from datetime import datetime

from database import transferservice
from database import get_db
from database.models import UserCard, Transfer


# Добавления карты
def add_card_db(user_id, card_number, balance, card_name, exp_date):
    db = next(get_db())

    new_card = UserCard(user_id=user_id, card_number=card_number,
                        balance=balance, card_name=card_name,
                        exp_date=exp_date)
    db.add(new_card)
    db.commit()

    return 'Карта успешно добавлено'


# Вывести все карты определенного пользователя через user_id
def get_exact_user_cards_db(user_id):
    db = next(get_db())

    exact_user_card = db.query(UserCard).filter_by(user_id=user_id).all()

    return exact_user_card


# Проверка карты на наличия в БД
def check_card_db(card_number):
    db = next(get_db())

    checker = db.query(UserCard).filter_by(card_number=card_number).first()

    return checker


# Удаления карту
def delete_card_db(card_id):
    db = next(get_db())

    delete_card = db.query(UserCard).filter_by(card_id=card_id).first()

    if delete_card:
        db.delete(delete_card)
        db.commit()

        return 'Карта успешно удален'
    else:
        return 'Карта не найдено!'


# Vivesti opredelennuyu kartu
def get_exact_card_db(user_id, cart_id):
    db = next(get_db())

    exact_user_card = db.query(UserCard).filter_by(user_id=user_id, cart_id=cart_id).first()

    return exact_user_card


#
# def canceled_transfer_db(card_from, card_to, amount, transfer_id):
#     db = next(get_db())
#
#     canceled_transaction = db.query(Transfer).filter_by(transfer_id=transfer_id, card_to=card_to, card_from=card_from).first()
#
#     if canceled_transaction:
#         canceled_transaction.card_to -= amount
#

    # checker_card_from = verification_card(card_from, db)
    # checker_card_to = verification_card(card_to, db)
    #
    # if checker_card_from.balance >= amount:
    #     checker_card_from.balance -= amount
    #     checker_card_to.balance += amount
    #
    #     new_transaction = Transfer(card_from_id=card_from, card_to_id=card_to, amount=amount,
    #                                transfers_date=datetime.now())
    #
    #     db.add(new_transaction)
    #     db.commit()
