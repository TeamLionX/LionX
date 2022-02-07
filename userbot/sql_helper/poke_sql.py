from sqlalchemy import Column, String

from . import BASE, SESSION


class Pokemon(BASE):
    __tablename__ = "pokemon"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Pokemon.__table__.create(checkfirst=True)


def add_grp(chat_id: str):
    poke = Pokemon(str(chat_id))
    SESSION.add(poke)
    SESSION.commit()


def rm_grp(chat_id: str):
    poke = SESSION.query(Pokemon).get(str(chat_id))
    if poke:
        SESSION.delete(poke)
        SESSION.commit()


def get_all_grp():
    poke = SESSION.query(Pokemon).all()
    SESSION.close()
    return poke


def is_pokemon(chat_id: str):
    try:
        poke = SESSION.query(Pokemon).get(str(chat_id))
        if poke:
            return str(poke.chat_id)
    finally:
        SESSION.close()
