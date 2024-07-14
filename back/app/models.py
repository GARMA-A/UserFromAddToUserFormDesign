from bson import ObjectId
from datetime import datetime, date


class Data:
    def __init__(self, name, age=None, level=None, msg=None, important=False, status=None, _id=None):
        try:
            self.id = _id if _id else ObjectId()
            self.name = name
            if isinstance(age, str):
                self.age = datetime.strptime(age, "%d/%m/%Y").date()
            elif isinstance(age, date):
                self.age = age
            else:
                self.age = datetime.now().date()

            self.level = level
            self.msg = msg
            self.important = important
            self.status = status if status is not None else "open"
        except Exception as e:
            raise ValueError(f"Error initializing Data object: {e}")

    def to_dict(self):
         try:
            return {
                "_id": str(self.id),
                "name": self.name,
                "age": self.age.isoformat() if self.age else None,
                "level": self.level,
                "msg": self.msg,
                "important": self.important,
                "status": self.status
            }
         except Exception as e:
            raise ValueError(f"Error converting Data object to dict: {e}")

    @classmethod
    def from_dict(cls, data):
        try:
            name = data.get("name")
            if not name:
                raise ValueError("Missing required field: name")

            age = data.get("age")
            if age:
                age = datetime.fromisoformat(age).date()

            level = data.get("level")
            if level and level not in ("easy", "normal", "hard"):
                raise ValueError("Invalid value for field: level")

            msg = data.get("msg")
            important = data.get("important", False)

            status = data.get("status")
            if status and status not in ("open", "close"):
                raise ValueError("Invalid value for field: status")

            _id = data.get("_id")
            if _id:
                _id = ObjectId(_id)

            return cls(name=name, age=age, level=level, msg=msg, important=important, status=status, _id=_id)
        except Exception as e:
            raise ValueError(f"Error creating Data object from dict: {e}")

