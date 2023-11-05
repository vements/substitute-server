#!/usr/bin/env python
from ulid import ULID

from .fake import fake
from .types import Scoreboard as ScoreboardRecord


class Scoreboard(ScoreboardRecord):
    @classmethod
    def random(cls, project_id: ULID | str, public: bool = False):
        return cls(
            project_id=project_id,
            scoreboard_id=fake.ulid(),
            display=fake.display("Scoreboard"),
            rank_dir=fake.rank_dir(),
            public=public,
            extra=fake.pydict(),
            created=fake.date_time(),
            updated=fake.date_time(),
        )
