#!/usr/bin/env python
from functools import wraps
from json import dumps as json_dumps
from typing import Optional, Sequence, Set

from flask import Flask, request

from .apikey import ApiKey
from .http import get_api_key, get_project_id, get_resource_id, okay, unauthorized
from .model import Model


class Auth:
    app: Flask
    model: Model

    def __init__(self, app: Flask, model: Model):
        self.app = app
        self.model = model

    def create(self):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return (
                    func(*args, **kwargs)
                    if self.check(get_api_key(request), capability={"rw"})
                    else unauthorized
                )

            return wrapper

        return decorator

    def read(self, resource: str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                api_key = self.check(get_api_key(request), capability={"r", "rw"})
                if not api_key:
                    return unauthorized
                resource_id = get_resource_id(request) or ""
                obj = self.model.read_object(resource=resource, id=resource_id)
                if obj and (obj.project_id != api_key.project_id):
                    return okay(response=json_dumps({resource: []}))
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def update(self, resource: str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                api_key = self.check(get_api_key(request), capability={"rw"})
                if not api_key:
                    return unauthorized
                resource_id = get_resource_id(request) or ""
                obj = self.model.read_object(resource=resource, id=resource_id)
                if obj and (obj.project_id != api_key.project_id):
                    return unauthorized
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def delete(self, resource: str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                api_key = self.check(get_api_key(request), capability={"rw"})
                if not api_key:
                    return unauthorized
                obj = self.model.read_object(resource=resource, id=get_resource_id(request) or "")
                if obj and obj.project_id != api_key.project_id:
                    return unauthorized
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def list(self):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                access = lambda: func(*args, **kwargs)
                api_key = self.check(get_api_key(request), capability={"r", "rw"})
                if not api_key:
                    return unauthorized
                project_id = get_project_id(request)
                if not project_id or api_key.project_id != project_id:
                    return unauthorized
                return access()

            return wrapper

        return decorator

    def record(self, resource: str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                api_key = self.check(get_api_key(request), capability={"rw"})
                if not api_key:
                    return unauthorized
                resource_id = get_resource_id(request) or ""
                obj = self.model.read_object(resource=resource, id=resource_id)
                if obj and (obj.project_id != api_key.project_id):
                    return unauthorized
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def read_check_public(self, resource: str, key: str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                obj = self.model.read_object(resource=resource, id=get_resource_id(request) or "")
                public = hasattr(obj, "public") and getattr(obj, "public")
                if public:
                    return func(*args, **kwargs)
                api_key = self.check(get_api_key(request), capability={"r", "rw"})
                if not api_key:
                    return okay(response=json_dumps({key: []}))
                if obj and obj.project_id != api_key.project_id:
                    return okay(response=json_dumps({key: []}))
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def check(self, value: Optional[str], capability: Set[str]) -> Optional[ApiKey]:
        if not value:
            return
        parts = value.split(":")
        if len(parts) != 2:
            return
        project_id, api_key_id = parts
        predicate = (
            lambda obj: obj.api_key_id == api_key_id
            and obj.project_id == project_id
            and obj.capability in capability
        )
        keys = [v for v in self.model.storage["api_key"] if predicate(v)]
        return keys[0] if keys else None
