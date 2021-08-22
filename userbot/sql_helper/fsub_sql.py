from sqlalchemy import Column, String

from . import BASE, SESSION


class Fsub(BASE):
    __tablename__ = "fsub"
    chat_id = Column(String(14), primary_key=True)
    usrname = Column(String(14), primary_key=True)

    def __init__(self, chat_id, usrname):
        self.chat_id = str(chat_id)
        self.usrname = str(usrname)


Fsub.__table__.create(checkfirst=True)


def is_fsub(chat_id):
    try:
        return SESSION.query(Fsub).filter(Fsub.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def add_fsub(chat_id, usrname):
    adder = Fsub(str(chat_id), str(usrname))
    SESSION.add(adder)
    SESSION.commit()


def rem_fsub(chat_id):
    rem = SESSION.query(Fsub).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def all_fsub():
    rem = SESSION.query(Fsub).all()
    SESSION.close()
    return rem
