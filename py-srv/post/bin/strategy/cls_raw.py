import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.sql import text

class Raw():
    UNSUPPORTED = {"results": "This action is unsupported"}

    def __init__(self, db: sessionmaker) -> None:
        self.table = os.environ["INDEX_NAME"]
        self.db = db

    def jsonify_results(self, collection: CursorResult) -> dict:
        results = [
            {
                "id": item.id,
                "breed": item.breed,
                "color": item.color
            } for item in collection]

        return {"results": results}
    
    def all(self):
        collection = self.db.execute(text(f"SELECT * FROM {self.table}"))
        return self.jsonify_results(collection)

    def commit_refresh(self, args: dict, stm) -> dict:
        self.db.execute(statement=stm,params=args)
        self.db.commit()
        return self.all()

    def filter_by(self, dog_id: int):
        stm = text(f"SELECT * FROM {self.table} WHERE id = :dog_id")
        collection = self.db.execute(statement=stm,params={"dog_id": int(dog_id)})
        return self.jsonify_results(collection)

    def delete_by(self, dog_id: int):
        return self.UNSUPPORTED
    
    def insert_entry(self, dog_breed: str, dog_color: str):
        return self.UNSUPPORTED

    def update_entry(self, dog_id: int, dog_breed: str, dog_color: str):
        return self.UNSUPPORTED
