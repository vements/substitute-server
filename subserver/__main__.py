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
