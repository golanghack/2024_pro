from django.test import TestCase
from ml.classifier.random_forest import RandomForestClassifier
from ml.classifier.extra_tree import ExtraTreesClassifier
import inspect
from ml.registry import MLRegistry


class MLTests(TestCase):
    def test_rf_algo(self):
        input_data = {
            "age": 37,
            "workclass": "Private",
            "fnlwgt": 34146,
            "education": "HS-grad",
            "education-num": 9,
            "marital-status": "Married-civ-spouse",
            "occupation": "Craft-repair",
            "relationship": "Husband",
            "race": "White",
            "sex": "Male",
            "capital-gain": 0,
            "capital-loss": 0,
            "hours-per-week": 68,
            "native-country": "United-States",
        }
        my_algo = RandomForestClassifier()
        response = my_algo.compute_prediction(input_data)
        self.assertEqual("OK", response["status"])
        self.assertTrue("label" in response)
        self.assertEqual("<=50K", response["label"])

    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "income_classifier"
        algo_object = RandomForestClassifier()
        algo_name = "random forest"
        algo_status = "production"
        algo_version = "0.0.1"
        owner = "Serg"
        algo_desc = "Random Forest with simple pre- and post-processing"
        algo_code = inspect.getsource(RandomForestClassifier)

        registry.add_algo(
            endpoint_name=endpoint_name,
            algo_status=algo_status,
            algo_object=algo_object,
            algo_name=algo_name,
            algo_version=algo_version,
            owner=owner,
            algo_desc=algo_desc,
            algo_code=algo_code,
        )
        self.assertEqual(len(registry.endpoints), 1)

    def test_extra_algo(self):
        input_data = {
            "age": 37,
            "workclass": "Private",
            "fnlwgt": 34146,
            "education": "HS-grad",
            "education-num": 9,
            "marital-status": "Married-civ-spouse",
            "occupation": "Craft-repair",
            "relationship": "Husband",
            "race": "White",
            "sex": "Male",
            "capital-gain": 0,
            "capital-loss": 0,
            "hours-per-week": 68,
            "native-country": "United-States",
        }
        my_alg = ExtraTreesClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual("OK", response["status"])
        self.assertTrue("label" in response)
        self.assertEqual("<=50K", response["label"])
