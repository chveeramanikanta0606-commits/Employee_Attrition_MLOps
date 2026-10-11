import unittest
from src.train import predict_attrition


class TestAttritionPrediction(unittest.TestCase):

    def test_young_employee_with_short_tenure(self):
        result = predict_attrition(
            age=23,
            monthly_income=2500,
            years_at_company=1,
        )
        self.assertEqual(result, "Likely to leave")

    def test_experienced_employee(self):
        result = predict_attrition(
            age=40,
            monthly_income=5000,
            years_at_company=10,
        )
        self.assertEqual(result, "Likely to stay")


if __name__ == "__main__":
    unittest.main()
