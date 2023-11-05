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

# NB: This is a generated file; any changes will be lost.

from datetime import datetime
from typing import List, Optional

from ulid import ULID


class User:
    user_id: str
    email: str
    display: str
    db: str
    created: datetime
    updated: datetime
    deleted: Optional[datetime]

    def __init__(
        self,
        user_id: str,
        email: str,
        display: str,
        db: str,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        deleted: Optional[datetime] = None,
    ):
        self.user_id = user_id
        self.email = email
        self.display = display
        self.db = db
        self.created = created or datetime.now()
        self.updated = updated or datetime.now()
        self.deleted = deleted


class Project:
    project_id: ULID | str
    user_id: str
    display: str
    created: datetime
    updated: datetime
    deleted: Optional[datetime]
    extra: Optional[object]

    def __init__(
        self,
        project_id: ULID | str,
        user_id: str,
        display: str,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        deleted: Optional[datetime] = None,
        extra: Optional[object] = None,
    ):
        self.project_id = project_id
        self.user_id = user_id
        self.display = display
        self.created = created or datetime.now()
        self.updated = updated or datetime.now()
        self.deleted = deleted
        self.extra = extra


class ApiKey:
    api_key_id: str
    project_id: ULID | str
    display: str
    capability: str
    deactivated: Optional[datetime]
    last_used: Optional[datetime]
    created: datetime
    updated: datetime
    deleted: Optional[datetime]

    def __init__(
        self,
        api_key_id: str,
        project_id: ULID | str,
        display: str,
        capability: str,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        deactivated: Optional[datetime] = None,
        last_used: Optional[datetime] = None,
        deleted: Optional[datetime] = None,
    ):
        self.api_key_id = api_key_id
        self.project_id = project_id
        self.display = display
        self.capability = capability
        self.deactivated = deactivated
        self.last_used = last_used
        self.created = created or datetime.now()
        self.updated = updated or datetime.now()
        self.deleted = deleted


class Achievement:
    achievement_id: ULID | str
    project_id: ULID | str
    display: str
    goal: int
    repeats: int
    locked_image: Optional[str]
    unlocked_image: Optional[str]
    position: int
    public: bool
    created: datetime
    updated: datetime
    deleted: Optional[datetime]
    extra: Optional[object]

    def __init__(
        self,
        achievement_id: ULID | str,
        project_id: ULID | str,
        display: str,
        goal: int,
        repeats: int,
        position: int,
        public: bool = False,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        locked_image: Optional[str] = "",
        unlocked_image: Optional[str] = "",
        deleted: Optional[datetime] = None,
        extra: Optional[object] = None,
    ):
        self.achievement_id = achievement_id
        self.project_id = project_id
        self.display = display
        self.goal = goal
        self.repeats = repeats
        self.locked_image = locked_image
        self.unlocked_image = unlocked_image
        self.position = position
        self.public = public
        self.created = created or datetime.now()
        self.updated = updated or datetime.now()
        self.deleted = deleted
        self.extra = extra


class Participant:
    participant_id: ULID | str
    project_id: ULID | str
    display: str
    external_id: str
    image: Optional[str]
    created: datetime
    updated: datetime
    deleted: Optional[datetime]
    extra: Optional[object]

    def __init__(
        self,
        participant_id: ULID | str,
        project_id: ULID | str,
        display: str,
        external_id: str,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        image: Optional[str] = "",
        deleted: Optional[datetime] = None,
        extra: Optional[object] = None,
    ):
        self.participant_id = participant_id
        self.project_id = project_id
        self.display = display
        self.external_id = external_id
        self.image = image
        self.created = created or datetime.now()
        self.updated = updated or datetime.now()
        self.deleted = deleted
        self.extra = extra


class Scoreboard:
    scoreboard_id: ULID | str
    project_id: ULID | str
    display: str
    rank_dir: str
    public: bool
    created: datetime
    updated: datetime
    deleted: Optional[datetime]
    extra: Optional[object]

    def __init__(
        self,
        scoreboard_id: ULID | str,
        project_id: ULID | str,
        display: str,
        rank_dir: str,
        public: bool = False,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        deleted: Optional[datetime] = None,
        extra: Optional[object] = None,
    ):
        self.scoreboard_id = scoreboard_id
        self.project_id = project_id
        self.display = display
        self.rank_dir = rank_dir
        self.public = public
        self.created = created or datetime.now()
        self.updated = updated or datetime.now()
        self.deleted = deleted
        self.extra = extra


class Progress:
    progress_id: int
    achievement_id: ULID | str
    participant_id: ULID | str
    value: int
    recorded: Optional[datetime]

    def __init__(
        self,
        progress_id: int,
        achievement_id: ULID | str,
        participant_id: ULID | str,
        value: int,
        recorded: Optional[datetime] = None,
    ):
        self.progress_id = progress_id
        self.achievement_id = achievement_id
        self.participant_id = participant_id
        self.value = value
        self.recorded = recorded


class Score:
    score_id: int
    scoreboard_id: ULID | str
    participant_id: ULID | str
    value: int
    recorded: Optional[datetime]

    def __init__(
        self,
        score_id: int,
        scoreboard_id: ULID | str,
        participant_id: ULID | str,
        value: int,
        recorded: Optional[datetime] = None,
    ):
        self.score_id = score_id
        self.scoreboard_id = scoreboard_id
        self.participant_id = participant_id
        self.value = value
        self.recorded = recorded


class AchievementLeaderboardItem:
    participant: Participant
    progress: int
    iterations: int

    def __init__(
        self,
        participant: Participant,
        progress: int,
        iterations: int,
    ):
        self.participant = participant
        self.progress = progress
        self.iterations = iterations


class ParticipantProgressItem:
    achievement: Achievement
    progress: int
    iterations: int

    def __init__(
        self,
        achievement: Achievement,
        progress: int,
        iterations: int,
    ):
        self.achievement = achievement
        self.progress = progress
        self.iterations = iterations


class ParticipantScoreItem:
    scoreboard: Scoreboard
    rank: int
    total: int

    def __init__(
        self,
        scoreboard: Scoreboard,
        rank: int,
        total: int,
    ):
        self.scoreboard = scoreboard
        self.rank = rank
        self.total = total


class ScoreboardScoreItem:
    participant_id: ULID | str
    participant: Participant
    rank: int
    total: int

    def __init__(
        self,
        participant_id: ULID | str,
        participant: Participant,
        rank: int,
        total: int,
    ):
        self.participant_id = participant_id
        self.participant = participant
        self.rank = rank
        self.total = total


class AchievementLeaderboardResponse:
    achievement_leaderboard: List[AchievementLeaderboardItem]

    def __init__(
        self,
        achievement_leaderboard: List[AchievementLeaderboardItem],
    ):
        self.achievement_leaderboard = achievement_leaderboard


class AchievementProgressResponse:
    insert_progress_one: Progress

    def __init__(
        self,
        insert_progress_one: Progress,
    ):
        self.insert_progress_one = insert_progress_one


class ParticipantProgressResponse:
    participant_progress: List[ParticipantProgressItem]

    def __init__(
        self,
        participant_progress: List[ParticipantProgressItem],
    ):
        self.participant_progress = participant_progress


class ParticipantScoresResponse:
    participant_scores: List[ParticipantScoreItem]

    def __init__(
        self,
        participant_scores: List[ParticipantScoreItem],
    ):
        self.participant_scores = participant_scores


class ScoreboardScoreResponse:
    insert_score_one: Score

    def __init__(
        self,
        insert_score_one: Score,
    ):
        self.insert_score_one = insert_score_one


class ScoreboardScoresResponse:
    scoreboard_scores: List[ScoreboardScoreItem]

    def __init__(
        self,
        scoreboard_scores: List[ScoreboardScoreItem],
    ):
        self.scoreboard_scores = scoreboard_scores


class AchievementProgressRequest:
    participant_id: ULID | str
    value: int
    recorded: Optional[datetime]

    def __init__(
        self,
        participant_id: ULID | str,
        value: int,
        recorded: Optional[datetime] = None,
    ):
        self.participant_id = participant_id
        self.value = value
        self.recorded = recorded


class ScoreboardScoreRequest:
    participant_id: ULID | str
    value: int
    recorded: Optional[datetime]

    def __init__(
        self,
        participant_id: ULID | str,
        value: int,
        recorded: Optional[datetime] = None,
    ):
        self.participant_id = participant_id
        self.value = value
        self.recorded = recorded


class AchievementCreateRequest:
    project_id: ULID | str
    display: str
    goal: int
    repeats: int
    locked_image: Optional[str]
    unlocked_image: Optional[str]
    position: int
    public: bool
    extra: Optional[object]

    def __init__(
        self,
        project_id: ULID | str,
        display: str,
        goal: int,
        repeats: int,
        position: int,
        public: bool = False,
        locked_image: Optional[str] = "",
        unlocked_image: Optional[str] = "",
        extra: Optional[object] = None,
    ):
        self.project_id = project_id
        self.display = display
        self.goal = goal
        self.repeats = repeats
        self.locked_image = locked_image
        self.unlocked_image = unlocked_image
        self.position = position
        self.public = public
        self.extra = extra


class AchievementCreateResponse:
    insert_achievement_one: Achievement

    def __init__(
        self,
        insert_achievement_one: Achievement,
    ):
        self.insert_achievement_one = insert_achievement_one


class AchievementReadResponse:
    achievement: List[Achievement]

    def __init__(
        self,
        achievement: List[Achievement],
    ):
        self.achievement = achievement


class AchievementUpdateRequest:
    display: str
    goal: int
    repeats: int
    locked_image: Optional[str]
    unlocked_image: Optional[str]
    position: int
    public: bool
    extra: Optional[object]

    def __init__(
        self,
        display: str,
        goal: int,
        repeats: int,
        position: int,
        public: bool = False,
        locked_image: Optional[str] = "",
        unlocked_image: Optional[str] = "",
        extra: Optional[object] = None,
    ):
        self.display = display
        self.goal = goal
        self.repeats = repeats
        self.locked_image = locked_image
        self.unlocked_image = unlocked_image
        self.position = position
        self.public = public
        self.extra = extra


class AchievementUpdateResponse:
    update_achievement_by_pk: Achievement

    def __init__(
        self,
        update_achievement_by_pk: Achievement,
    ):
        self.update_achievement_by_pk = update_achievement_by_pk


class AchievementDeleteResponse:
    delete_achievement_by_pk: Optional[Achievement]

    def __init__(
        self,
        delete_achievement_by_pk: Optional[Achievement] = None,
    ):
        self.delete_achievement_by_pk = delete_achievement_by_pk


class AchievementListResponse:
    achievement: List[Achievement]

    def __init__(
        self,
        achievement: List[Achievement],
    ):
        self.achievement = achievement


class ParticipantCreateRequest:
    project_id: ULID | str
    display: str
    external_id: str
    image: Optional[str]
    extra: Optional[object]

    def __init__(
        self,
        project_id: ULID | str,
        display: str,
        external_id: str,
        image: Optional[str] = "",
        extra: Optional[object] = None,
    ):
        self.project_id = project_id
        self.display = display
        self.external_id = external_id
        self.image = image
        self.extra = extra


class ParticipantCreateResponse:
    insert_participant_one: Participant

    def __init__(
        self,
        insert_participant_one: Participant,
    ):
        self.insert_participant_one = insert_participant_one


class ParticipantReadResponse:
    participant: List[Participant]

    def __init__(
        self,
        participant: List[Participant],
    ):
        self.participant = participant


class ParticipantUpdateRequest:
    display: str
    external_id: str
    image: Optional[str]
    extra: Optional[object]

    def __init__(
        self,
        display: str,
        external_id: str,
        image: Optional[str] = "",
        extra: Optional[object] = None,
    ):
        self.display = display
        self.external_id = external_id
        self.image = image
        self.extra = extra


class ParticipantUpdateResponse:
    update_participant_by_pk: Participant

    def __init__(
        self,
        update_participant_by_pk: Participant,
    ):
        self.update_participant_by_pk = update_participant_by_pk


class ParticipantDeleteResponse:
    delete_participant_by_pk: Optional[Participant]

    def __init__(
        self,
        delete_participant_by_pk: Optional[Participant] = None,
    ):
        self.delete_participant_by_pk = delete_participant_by_pk


class ParticipantListResponse:
    participant: List[Participant]

    def __init__(
        self,
        participant: List[Participant],
    ):
        self.participant = participant


class ScoreboardCreateRequest:
    project_id: ULID | str
    display: str
    rank_dir: str
    public: bool
    extra: Optional[object]

    def __init__(
        self,
        project_id: ULID | str,
        display: str,
        rank_dir: str,
        public: bool = False,
        extra: Optional[object] = None,
    ):
        self.project_id = project_id
        self.display = display
        self.rank_dir = rank_dir
        self.public = public
        self.extra = extra


class ScoreboardCreateResponse:
    insert_scoreboard_one: Scoreboard

    def __init__(
        self,
        insert_scoreboard_one: Scoreboard,
    ):
        self.insert_scoreboard_one = insert_scoreboard_one


class ScoreboardReadResponse:
    scoreboard: List[Scoreboard]

    def __init__(
        self,
        scoreboard: List[Scoreboard],
    ):
        self.scoreboard = scoreboard


class ScoreboardUpdateRequest:
    display: str
    rank_dir: str
    public: bool
    extra: Optional[object]

    def __init__(
        self,
        display: str,
        rank_dir: str,
        public: bool = False,
        extra: Optional[object] = None,
    ):
        self.display = display
        self.rank_dir = rank_dir
        self.public = public
        self.extra = extra


class ScoreboardUpdateResponse:
    update_scoreboard_by_pk: Scoreboard

    def __init__(
        self,
        update_scoreboard_by_pk: Scoreboard,
    ):
        self.update_scoreboard_by_pk = update_scoreboard_by_pk


class ScoreboardDeleteResponse:
    delete_scoreboard_by_pk: Optional[Scoreboard]

    def __init__(
        self,
        delete_scoreboard_by_pk: Optional[Scoreboard] = None,
    ):
        self.delete_scoreboard_by_pk = delete_scoreboard_by_pk


class ScoreboardListResponse:
    scoreboard: List[Scoreboard]

    def __init__(
        self,
        scoreboard: List[Scoreboard],
    ):
        self.scoreboard = scoreboard

