#!/usr/bin/env python
from .fake import fake
from .types import Project as ProjectRecord


class Project(ProjectRecord):
    @classmethod
    def random(cls, user_id: str):
        return cls(
            user_id=user_id,
            project_id=fake.ulid(),
            display=fake.display("Project"),
            created=fake.date_time(),
            updated=fake.date_time(),
        )
