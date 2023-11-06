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
