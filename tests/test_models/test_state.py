#!/usr/bin/python3
""" State model test module """
import unittest
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """ State model test module """

    def test_init(self):
        """ test init """
        self.assertIs(State, type(State()))

    def test_init_by_kwargs(self):
        """ test init by kwargs """
        self.assertIs(State, type(State(name="Test")))


class TestSave(unittest.TestCase):
    """ test save"""

    def test_save(self):
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_save_updates(self):
        state = State()
        state.save()
        sleep(0.1)
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_to_dict(self):
        state = State()
        state.save()

        self.assertIs(type(state.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
