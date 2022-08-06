import json
import unittest

from globalcon_tools.calculator.calculator import Calculator


class TestEvaluation(unittest.TestCase):
    def test_all_inputs(self):
        with open("tests/input.json") as f:
            inputs = json.load(f)["Inputs"]
        for data in inputs:
            total = 0
            for key, val in data["input"].items():
                total += Calculator.evaluate(val, key)
            self.assertEqual(total, data["result"])
