#!/usr/bin/env python
from typing import Optional

from ulid import ULID

from .fake import fake
from .types import ApiKey as ApiKeyRecord


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
