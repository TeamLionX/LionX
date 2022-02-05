from sqlalchemy import Column, String

from . import BASE, SESSION


class Harem(BASE):
    __tablename__ = "harem"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Harem.__table__.create(checkfirst=True)


def add_grp(chat_id: str):
    waifu = Harem(str(chat_id))
    SESSION.add(waifu)
    SESSION.commit()


def rm_grp(chat_id: str):
    waifu = SESSION.query(Harem).get(str(chat_id))
    if waifu:
        SESSION.delete(waifu)
        SESSION.commit()


def get_all_grp():
    waifu = SESSION.query(Harem).all()
    SESSION.close()
    return waifu


def is_harem(chat_id: str):
    try:
        waifu = SESSION.query(Harem).get(str(chat_id))
        if waifu:
            return str(waifu.chat_id)
    finally:
        SESSION.close()
