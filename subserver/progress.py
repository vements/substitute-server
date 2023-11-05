#!/usr/bin/env python
from ulid import ULID

from .counter import NextIdCounter
from .fake import fake
from .types import Progress as ProgressRecord


class Progress(ProgressRecord, NextIdCounter):
    @classmethod
    def random(cls, achievement_id: ULID | str, participant_id: ULID | str):
        progress_id: int = cls.next_id()
        return cls(
            progress_id=progress_id,
            achievement_id=achievement_id,
            participant_id=participant_id,
            value=fake.pyint(),
            recorded=fake.date_time(),
        )
