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

from flask import Flask, request

from .auth import Auth
from .errors import ConstraintViolation
from .http import bad_request, unauthorized
from .model import Model


class Routes:
    prefix: str
    version: str

    def __init__(self, app: Flask, model: Model, version: str):
        self.prefix = "/api/rest/" + version + "/"
        self.version = version
        self.install(app, model)

    def install(self, app: Flask, model: Model):
        auth = Auth(app, model)
        prefix = self.prefix

        @app.route(prefix + "achievement", methods=["GET"])
        @auth.list()
        def achievement_list(limit: int = 10, offset: int = 0):
            project_id = request.args.get("project_id") or ""
            return model.list(
                resource="achievement", project_id=project_id, limit=limit, offset=offset
            )

        @app.route(prefix + "achievement/<id>", methods=["GET"])
        @auth.read("achievement")
        def achievement_read(id):
            return model.read(resource="achievement", id=id)

        @app.route(prefix + "achievement/<id>", methods=["DELETE"])
        @auth.delete("achievement")
        def achievement_delete(id):
            return model.delete(resource="achievement", id=id)

        @app.route(prefix + "achievement", methods=["PUT"])
        @auth.create()
        def achievement_create():
            return model.create(resource="achievement", params=request.json or {})

        @app.route(prefix + "achievement/<id>", methods=["POST"])
        @auth.update("achievement")
        def achievement_update(id):
            try:
                return model.update(resource="achievement", id=id, params=request.json or {})
            except ConstraintViolation:
                return unauthorized

        @app.route(prefix + "participant", methods=["GET"])
        @auth.list()
        def participant_list(limit: int = 10, offset: int = 0):
            project_id = request.args.get("project_id") or ""
            return model.list(
                resource="participant", project_id=project_id, limit=limit, offset=offset
            )

        @app.route(prefix + "participant/<id>", methods=["GET"])
        @auth.read("participant")
        def participant_read(id):
            return model.read(resource="participant", id=id)

        @app.route(prefix + "participant/<id>", methods=["DELETE"])
        @auth.delete("participant")
        def participant_delete(id):
            return model.delete(resource="participant", id=id)

        @app.route(prefix + "participant", methods=["PUT"])
        @auth.create()
        def participant_create():
            return model.create(resource="participant", params=request.json or {})

        @app.route(prefix + "participant/<id>", methods=["POST"])
        @auth.update("participant")
        def participant_update(id):
            try:
                return model.update(resource="participant", id=id, params=request.json or {})
            except ConstraintViolation:
                return unauthorized

        @app.route(prefix + "scoreboard", methods=["GET"])
        @auth.list()
        def scoreboard_list(limit: int = 10, offset: int = 0):
            project_id = request.args.get("project_id") or ""
            return model.list(
                resource="scoreboard", project_id=project_id, limit=limit, offset=offset
            )

        @app.route(prefix + "scoreboard/<id>", methods=["GET"])
        @auth.read("scoreboard")
        def scoreboard_read(id):
            return model.read(resource="scoreboard", id=id)

        @app.route(prefix + "scoreboard/<id>", methods=["DELETE"])
        @auth.delete("scoreboard")
        def scoreboard_delete(id):
            return model.delete(resource="scoreboard", id=id)

        @app.route(prefix + "scoreboard", methods=["PUT"])
        @auth.create()
        def scoreboard_create():
            return model.create(resource="scoreboard", params=request.json or {})

        @app.route(prefix + "scoreboard/<id>", methods=["POST"])
        @auth.update("scoreboard")
        def scoreboard_update(id):
            try:
                return model.update(resource="scoreboard", id=id, params=request.json or {})
            except ConstraintViolation:
                return unauthorized

        # install "the extra 6" routes

        @app.route(prefix + f"/achievement/<achievement_id>/progress", methods=["PUT"])
        @auth.record(resource="achievement")
        def progress_create(achievement_id):
            try:
                params = request.json or {}
                return model.progress_create(
                    achievement_id=achievement_id,
                    participant_id=params["participant_id"],
                    value=params["value"],
                )
            except ConstraintViolation:
                return bad_request

        @app.route(prefix + f"/achievement/<id>/leaderboard", methods=["GET"])
        @auth.read_check_public(resource="achievement", key="achievement_leaderboard")
        def achievement_leaderboard(id):
            return model.achievement_leaderboard(achievement_id=id, params={})

        @app.route(prefix + f"/participant/<id>/progress", methods=["GET"])
        @auth.read_check_public(resource="participant", key="participant_progress")
        def participant_progress(id):
            return model.participant_progress(participant_id=id, params={})

        @app.route(prefix + f"/participant/<id>/scores", methods=["GET"])
        @auth.read_check_public(resource="participant", key="participant_scores")
        def participant_scores(id):
            return model.participant_scores(participant_id=id, params={})

        @app.route(prefix + f"/scoreboard/<scoreboard_id>/score", methods=["PUT"])
        @auth.record(resource="scoreboard")
        def score_create(scoreboard_id):
            try:
                params = request.json or {}
                return model.score_create(
                    scoreboard_id=scoreboard_id,
                    participant_id=params["participant_id"],
                    value=params["value"],
                )
            except ConstraintViolation:
                return bad_request

        @app.route(prefix + f"/scoreboard/<id>/scores", methods=["GET"])
        @auth.read_check_public(resource="scoreboard", key="scoreboard_scores")
        def scoreboard_scores(id):
            return model.scoreboard_scores(scoreboard_id=id, params={})

        # install "database" methods, no auth required

        @app.route(prefix + "/-/database", methods=["GET"])
        def database():
            db = {}
            for key in model.storage:
                db[key] = [value.__dict__ for value in model.storage[key]]
            return db

        @app.route(prefix + "/-/database", methods=["DELETE"])
        def database_reset():
            model.reset()
            return database()

        @app.route(prefix + "/-/database", methods=["POST"])
        def database_reset_random():
            model.reset(model.random())
            return database()

