#!/usr/bin/env python


def make_counter(start: int, stop: int):
    def counter(start: int, stop: int):
        for i in range(start, stop):
            yield i

    c = counter(start, stop)

    def next():
        return c.__next__()

    return next


class NextIdCounter:
    @classmethod
    def next_id(cls) -> int:
        call = getattr(cls, "_next_id", None)
        if not call:
            call = make_counter(1, 10000000)
            setattr(cls, "_next_id", call)
        return call()
