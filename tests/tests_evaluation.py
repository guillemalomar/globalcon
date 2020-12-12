import json
import unittest

from src.calculator import Calculator


class TestEvaluation(unittest.TestCase):
    def test_only_core(self):
        with open("input.json") as f:
            data = json.load(f)["Only Core"]
        total = 0
        for key, val in data["input"].items():
            total += Calculator.evaluate(val, key)
        self.assertEquals(total, data["result"])

    def test_only_rarities(self):
        with open("input.json") as f:
            data = json.load(f)["Only Rarities"]
        total = 0
        for key, val in data["input"].items():
            total += Calculator.evaluate(val, key)
        self.assertEquals(total, data["result"])
