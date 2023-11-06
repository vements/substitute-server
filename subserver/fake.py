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

import random
import string

import faker
import faker.providers
import ulid


class ApiKeyAttributeProvider(faker.providers.BaseProvider):
    def api_key_id(self, prefix="vk_", count=36) -> str:
        r = count - len(prefix)
        s = string.ascii_letters + string.digits
        return prefix + "".join([random.choice(s) for _ in range(r)])

    def api_key_capability(self) -> str:
        return random.choice(["r", "rw"])


class BillingAttributeProvider(faker.providers.BaseProvider):
    def customer_id(self) -> str:
        return "customer_test_" + fake.bban()

    def event_id(self) -> str:
        return "event_test_" + fake.bban()

    def session_id(self) -> str:
        return "session_test_" + fake.bban()


class ParticipantAttributeProvider(faker.providers.BaseProvider):
    def external_id(self) -> str:
        return f"{fake.user_name()} {fake.bothify()}".replace(" ", "-")


class ResourceAttributeProvider(faker.providers.BaseProvider):
    def display(self, suffix: str = "") -> str:
        return fake.catch_phrase().title() + (" " + suffix if suffix else "")

    def ulid(self) -> str:
        return f"{ulid.ULID()}"


class ScoreboardAttributeProvider(faker.providers.BaseProvider):
    def rank_dir(self) -> str:
        return random.choice(["asc", "desc"])


fake = faker.Faker()

fake.add_provider(ApiKeyAttributeProvider)
fake.add_provider(BillingAttributeProvider)
fake.add_provider(ParticipantAttributeProvider)
fake.add_provider(ResourceAttributeProvider)
fake.add_provider(ScoreboardAttributeProvider)
