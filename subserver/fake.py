#!/usr/bin/env python
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
