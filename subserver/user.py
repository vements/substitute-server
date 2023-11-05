#!/usr/bin/env python
from .fake import fake
from .types import User as UserRecord


class User(UserRecord):
    @classmethod
    def random(cls):
        return cls(
            user_id=fake.ulid(),
            display=fake.name(),
            email=fake.email(),
            db="db1",
            created=fake.date_time(),
            updated=fake.date_time(),
        )
