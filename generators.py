# -*- coding: utf-8 -*-

"""
入力されるコーパスは, 1行に1文ずつ記述されていること.
"""

class StartGenerator(object):

    def __init__(self, path):
        self.path = path

    def __iter__(self):
        for x in open(self.path):
            yield x


class FakeGenerator(object):

    def __init__(self, origin, f):
        self.origin = origin
        self.f = f

    def __iter__(self):
        for x in self.f(self.origin):
            yield x


class ChainGenerator(object):

    def __init__(self, *iterables):
        self.iterables = iterables

    def __iter__(self):
        for it in self.iterables:
            for x in it:
                yield x
