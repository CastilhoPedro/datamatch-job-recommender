from backend.database.models import *
from backend.database.connection import *


class Database:
    def __init__(self):
        Base.metadata.create_all(bind= engine)
        self.db = SessionLocal()

    @staticmethod
    def handle_db(func):
        def wrapper(self, **kwargs):
            new_row = func(**kwargs)
            
            self.db.add(new_row)
            self.db.commit()
        return wrapper




    # precisaremos fazer as funções para adicionar linhas e alrerar linhas (coluna 'processada' de false para true)
    @handle_db
    def add_rel_raw(self):
        return RelsRaw(
            
        )


if __name__ == '__main__':
    db = Database()