#!/usr/bin/env python
from typing import Optional

from flask import Request, Response


bad_request = Response(status=400)
unauthorized = Response(status=401)


def get_api_key(r: Request) -> Optional[str]:
    return r.headers.get("x-api-key")


def get_project_id(r: Request) -> Optional[str]:
    return r.args.get("project_id")


def get_resource_id(r: Request) -> Optional[str]:
    return (r.view_args or {}).get("id")


def okay(status: int = 200, response: Optional[str] = None) -> Response:
    return Response(status=status, response=response)
