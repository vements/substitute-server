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
