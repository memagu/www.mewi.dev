from datetime import datetime, UTC

from .extensions.db import db


def now() -> datetime:
    return datetime.now(UTC)


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), default=now)
    updated_at = db.Column(db.DateTime(timezone=True), default=now, onupdate=now)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({", ".join(f"{attr}={repr(value)}" for attr, value in map(lambda attr: (attr, getattr(self, attr)), dir(self)) if not (attr.startswith("__") or callable(value)))})"
