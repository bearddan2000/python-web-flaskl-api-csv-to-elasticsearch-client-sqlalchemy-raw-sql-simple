from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from strategy.cls_raw import Raw
# from strategy.cls_chained import Chained

class Cluster():
    def __init__(self) -> None:
        self.hive = [
            Node("es1"),
            Node('es2'),
            Node('es3')
        ]

    def filter_by(self, id):
        result = []
        for node in self.hive:
            result.append(node.filter_by(id))
        return result
    
    def get_all(self):
        result = []
        for node in self.hive:
            result.append(node.get_all())
        return result
    
    def delete_by(self, id):
        result = []
        for node in self.hive:
            result.append(node.delete_by(id))
        return result
    
    def insert_entry(self, fld1, fld2):
        result = []
        for node in self.hive:
            result.append(node.insert_entry(fld1, fld2))
        return result
    
    def update_entry(self, id, fld1, fld2):
        result = []
        for node in self.hive:
            result.append(node.update_entry(id, fld1, fld2))
        return result

class Node():
    def __init__(self,server='elasticsearch') -> None:
        self.server = server
        settings.ELASTICSEARCH['host'] = server

        self.engine = create_engine("{engine}://{host}:{port}".format(**settings.ELASTICSEARCH))
    
        self.session_local = sessionmaker(
            bind=self.engine
        )

    def get_db(self):
        db = self.session_local()
        try:
            yield db
        finally:
            db.close()

    def get_strategy(self):
        db = next(self.get_db())
        return Raw(db)

    def filter_by(self, id):
        return self.get_strategy().filter_by(id)

    def get_all(self):
        return self.get_strategy().all()

    def delete_by(self, id):
        return self.get_strategy().delete_by(id)
    
    def insert_entry(self, fld1, fld2):
        return self.get_strategy().insert_entry(fld1, fld2)
    
    def update_entry(self, id, fld1, fld2):
        return self.get_strategy().update_entry(id, fld1, fld2)
