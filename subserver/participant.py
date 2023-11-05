#!/usr/bin/env python
from ulid import ULID

from .fake import fake
from .types import Participant as ParticipantRecord


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
