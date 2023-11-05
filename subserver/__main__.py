#!/usr/bin/env python
from datetime import datetime, date, time
from os import environ

from flask import Flask
from flask.json.provider import DefaultJSONProvider

from .model import Model
from .routes import Routes


class JSONProvider(DefaultJSONProvider):
    def default(self, o):
        if isinstance(o, datetime) or isinstance(o, date) or isinstance(o, time):
            return o.strftime("%Y-%m-%dT%H:%M:%SZ")
        return super().default(o)


def env(key: str, default: str) -> str:
    return (environ[key] or default) if key in environ else default


def main():
    debug = env("DEBUG", "false").lower() in ("true", "1", "y", "yes")
    host = env("HOST", "0.0.0.0")
    port = int(env("PORT", "5000"))
    url_version = env("REST_API_VERSION", "v1.0.3")

    app = Flask(__name__)
    app.json = JSONProvider(app)

    model = Model()
    routes = Routes(app, model, url_version)

    print("debug:", debug)
    print("name:", __name__)
    print("prefix:", routes.prefix)

    Flask.run(app, host=host, port=port, debug=debug)


if __name__ == "__main__":
    main()
