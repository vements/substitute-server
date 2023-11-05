#!/usr/bin/env python
from ulid import ULID

from .counter import NextIdCounter
from .fake import fake
from .types import Score as ScoreRecord


class Score(ScoreRecord, NextIdCounter):
    @classmethod
    def random(cls, scoreboard_id: ULID | str, participant_id: ULID | str):
        score_id: int = cls.next_id()
        return cls(
            scoreboard_id=scoreboard_id,
            participant_id=participant_id,
            value=fake.pyint(),
            recorded=fake.date_time(),
            score_id=score_id,
        )
