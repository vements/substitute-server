#!/usr/bin/env python

# Copyright 2023 Monster Street Systems LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from datetime import datetime
from typing import Any, Callable, Optional

from .fake import fake
from ulid import ULID

from .counter import NextIdCounter
from .errors import ConstraintViolation, NotFound
from .types import Achievement as AchievementRecord
from .types import ApiKey as ApiKeyRecord
from .types import Participant as ParticipantRecord
from .types import Progress as ProgressRecord
from .types import Project as ProjectRecord
from .types import Score as ScoreRecord
from .types import Scoreboard as ScoreboardRecord
from .types import User as UserRecord


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


class ApiKey(ApiKeyRecord):
    @classmethod
    def random(
        cls, project_id: ULID | str, api_key: Optional[str] = None, capability: Optional[str] = None
    ):
        return cls(
            api_key_id=api_key if api_key else fake.api_key_id(),
            project_id=project_id,
            display=fake.display("API Key"),
            capability=capability if capability else fake.api_key_capability(),
            deactivated=None,
            last_used=fake.date_time(),
            created=fake.date_time(),
            updated=fake.date_time(),
        )


class Participant(ParticipantRecord):
    @classmethod
    def random(cls, project_id: ULID | str):
        return cls(
            project_id=project_id,
            participant_id=fake.ulid(),
            display=fake.name(),
            image=fake.image_url(),
            external_id=fake.external_id(),
            extra=fake.pydict(),
            created=fake.date_time(),
            updated=fake.date_time(),
        )


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


class User(UserRecord):
    @classmethod
    def random(cls):
        return cls(
            user_id=fake.ulid(),
            display=fake.name(),
            email=fake.email(),
            created=fake.date_time(),
            updated=fake.date_time(),
        )


class Model:
    storage: dict
    storage_keys: list = [
        "achievement",
        "api_key",
        "participant",
        "progress",
        "project",
        "scoreboard",
        "score",
        "user",
    ]

    def __init__(self, db: Optional[dict] = None):
        self.reset(db=db)

    def reset(self, db: Optional[dict] = None) -> None:
        self.storage = self.default() if db is None else db

    @classmethod
    def default(cls) -> dict:
        return dict((k, []) for k in cls.storage_keys)

    @classmethod
    def random(cls, user_count=3, user_project_count=3, api_key_count=10) -> dict:
        db = cls.default()
        db["user"] = users = [User.random() for _ in range(user_count)]
        projects = db["project"]
        api_keys = db["api_key"]
        achievements = db["achievement"]
        participants = db["participant"]
        scoreboards = db["scoreboard"]
        progress = db["progress"]
        score = db["score"]

        for user in users:
            user_projects = [
                Project.random(user_id=user.user_id) for _ in range(user_project_count)
            ]
            projects.extend(user_projects)

            for project in user_projects:
                api_keys.extend(
                    [ApiKey.random(project_id=project.project_id) for _ in range(api_key_count)]
                )

                project_achievements = [
                    Achievement.random(project_id=project.project_id) for _ in range(3)
                ]

                project_participants = [
                    Participant.random(project_id=project.project_id) for _ in range(3)
                ]

                project_scoreboards = [
                    Scoreboard.random(project_id=project.project_id) for _ in range(3)
                ]

                achievement_progress = [
                    Progress.random(
                        achievement_id=a.achievement_id,
                        participant_id=p.participant_id,
                    )
                    for a in project_achievements
                    for p in project_participants
                ]

                scoreboard_scores = [
                    Score.random(
                        scoreboard_id=s.scoreboard_id,
                        participant_id=p.participant_id,
                    )
                    for s in project_scoreboards
                    for p in project_participants
                ]

                achievements.extend(project_achievements)
                participants.extend(project_participants)
                progress.extend(achievement_progress)
                scoreboards.extend(project_scoreboards)
                score.extend(scoreboard_scores)

        return db

    def create(self, resource: str, params: dict) -> dict:
        type = globals()[resource.capitalize()]
        added = params.copy()
        added[resource + "_id"] = fake.ulid()
        added["created"] = datetime.now()
        added["updated"] = datetime.now()
        obj = type(**added)
        self.storage[resource].append(obj)
        return {f"insert_{resource}_one": obj.__dict__}

    def read_object(self, resource: str, id: str) -> Optional[Any]:
        values = [v for v in self.storage[resource] if getattr(v, resource + "_id") == id]
        return values[0] if values else None

    def read(self, resource: str, id: str) -> dict:
        v = self.read_object(resource, id)
        return {resource: [v.__dict__] if v else []}

    def update(self, resource: str, id: str, params: dict) -> dict:
        values = [v for v in self.storage[resource] if getattr(v, resource + "_id") == id]
        if not values:
            return {}
        obj = values[0]
        if "project_id" in params and params["project_id"] != obj.project_id:
            raise ConstraintViolation("project_id cannot be changed")
        ids = (f"{resource}_id", "project_id")
        params = dict((k, v) for k, v in params.items() if k not in ids)
        for k, v in params.items():
            setattr(obj, k, v)
        obj.updated = datetime.now()
        return {f"update_{resource}_by_pk": obj.__dict__}

    def delete(self, resource: str, id: str) -> dict:
        for value in self.storage[resource]:
            if getattr(value, resource + "_id") == id:
                value.deleted = datetime.now()
                break
        return {}

    def list(self, resource: str, project_id: str, limit: int = 10, offset: int = 0) -> dict:
        values = [
            v for v in self.storage[resource] if v.project_id == project_id and v.deleted is None
        ]
        return {f"{resource}": [v.__dict__ for v in values[offset : offset + limit]]}

    def progress_create(self, achievement_id: str, participant_id: str, value: int):
        if value == 0:
            raise ConstraintViolation("score cannot be zero")
        progress = Progress(
            progress_id=Progress.next_id(),
            participant_id=participant_id,
            achievement_id=achievement_id,
            value=value,
            recorded=datetime.now(),
        )
        self.storage["progress"].append(progress)
        return {"insert_progress_one": progress.__dict__}

    def achievement_leaderboard(self, achievement_id: str, params: dict) -> dict:
        return {
            "achievement_leaderboard": [
                {
                    "participant": [
                        p for p in self.storage["participant"] if p.participant_id == participant_id
                    ][0].__dict__,
                    "progress": sum(
                        a.value
                        for a in self.storage["progress"]
                        if a.participant_id == participant_id and a.achievement_id == achievement_id
                    ),
                    "iterations": 0,
                }
                for participant_id in self.unique_participant_ids(
                    "progress", lambda p: p.achievement_id == achievement_id
                )
            ]
        }

    def participant_progress(self, participant_id: str, params: dict) -> dict:
        achievements = self.unique_achievement_ids(participant_id)
        progress = [
            {
                "achievement": [
                    a for a in self.storage["achievement"] if a.achievement_id == achievement_id
                ][0].__dict__,
                "progress": sum(
                    p.value
                    for p in self.storage["progress"]
                    if p.participant_id == participant_id and p.achievement_id == achievement_id
                ),
                "iterations": 0,
            }
            for achievement_id in achievements
        ]
        return {"participant_progress": progress}

    def participant_scores(self, participant_id: str, params: dict) -> dict:
        scoreboards = self.unique_scoreboard_ids(participant_id)
        scores = [
            {
                "scoreboard": [
                    v.__dict__ for v in self.storage["scoreboard"] if v.scoreboard_id == s
                ][0],
                "rank": 1,
                "total": sum(
                    s.value
                    for s in self.storage["score"]
                    if s.scoreboard_id == s.scoreboard_id and s.participant_id == participant_id
                ),
            }
            for s in scoreboards
        ]
        return {"participant_scores": scores}

    def scoreboard_scores(self, scoreboard_id: str, params: dict) -> dict:
        scoreboard = self.read_object("scoreboard", scoreboard_id)
        if not scoreboard:
            raise NotFound("scoreboard not found")
        scores = [
            {
                "participant_id": participant_id,
                "participant": self.participant(participant_id),
                "total": sum(
                    a.value
                    for a in self.storage["score"]
                    if a.participant_id == participant_id and a.scoreboard_id == scoreboard_id
                ),
                "rank": 0,
            }
            for participant_id in self.unique_participant_ids(
                "score", lambda s: s.scoreboard_id == scoreboard_id
            )
        ]
        scores.sort(
            key=lambda s: s["total"],
            reverse=scoreboard.rank_dir == "desc",
        )
        for i, score in enumerate(scores):
            score["rank"] = i + 1
        return {"scoreboard_scores": scores}

    def score_create(self, scoreboard_id: str, participant_id: str, value: int) -> dict:
        if value == 0:
            raise ConstraintViolation("score cannot be zero")
        score = Score(
            score_id=Score.next_id(),
            scoreboard_id=scoreboard_id,
            participant_id=participant_id,
            value=value,
        )
        self.storage["score"].append(score)
        return {"insert_score_one": score.__dict__}

    def unique_achievement_ids(self, participant_id: str) -> set:
        return set(
            progress.achievement_id
            for progress in self.storage["progress"]
            if progress.participant_id == participant_id
        )

    def unique_scoreboard_ids(self, participant_id: str) -> set:
        return set(
            score.scoreboard_id
            for score in self.storage["score"]
            if score.participant_id == participant_id
        )

    def unique_participant_ids(self, resource: str, key: Callable) -> set:
        return set(getattr(v, "participant_id") for v in self.storage[resource] if key(v))

    def participant(self, participant_id) -> Optional[dict]:
        parts = [p for p in self.storage["participant"] if p.participant_id == participant_id]
        return parts[0].__dict__ if parts else None
