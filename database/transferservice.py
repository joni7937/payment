#ДЗ!!!!
# Получить все переводы по карте get_card_transaction_db()
from datetime import datetime

from database.models import Transfer, UserCard
from database import get_db


def verification_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card


def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    checker_card_from = verification_card(card_from, db)
    checker_card_to = verification_card(card_to, db)

    if checker_card_from and checker_card_to:
        if checker_card_from.balance >= amount:
            checker_card_from.balance -= amount
            checker_card_to.balance += amount

            new_transaction = Transfer(card_from_id=card_from, card_to_id=card_to, amount=amount, transfers_date=datetime.now())

            db.add(new_transaction)
            db.commit()

            return 'Перевод успешно выполнен'
        else:
            return "Недостаточно средств на балансе"

    else:
        return "Одна из карт не существует"


def get_card_trasaction_db(card_from_id):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()

    return card_transaction

