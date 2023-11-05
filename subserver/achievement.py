#!/usr/bin/env python
from ulid import ULID

from .fake import fake
from .types import Achievement as AchievementRecord


class Achievement(AchievementRecord):
    @classmethod
    def random(cls, project_id: ULID | str, public: bool = False):
        return cls(
            project_id=project_id,
            achievement_id=fake.ulid(),
            display=fake.display("Achievement"),
            goal=fake.pyint(),
            repeats=fake.pyint(),
            locked_image=fake.image_url(),
            unlocked_image=fake.image_url(),
            position=fake.pyint(),
            public=public,
            extra=fake.pydict(),
            created=fake.date_time(),
            updated=fake.date_time(),
        )
