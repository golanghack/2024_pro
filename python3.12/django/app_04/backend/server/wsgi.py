"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

application = get_wsgi_application()

# registry ml model
import inspect
from ml.registry import MLRegistry
from ml.classifier.random_forest import RandomForestClassifier
from ml.classifier.extra_tree import ExtraTreesClassifier

try:
    registry = MLRegistry()

    rf = RandomForestClassifier()
    registry.add_algo(
        endpoint_name="income_classifier",
        algo_object=rf,
        algo_name="random forest",
        algo_status="production",
        algo_version="0.0.1",
        owner="Serg",
        algo_desc="Random Forest with pre- and post-processing",
        algo_code=inspect.getsource(RandomForestClassifier),
    )

    extra = ExtraTreesClassifier()
    registry.add_algo(
        endpoint_name="income_classifier",
        algo_object=extra,
        algo_name="extra tree algo",
        algo_status="testing",
        algo_version="0.0.1",
        owner="Serg",
        algo_desc="Extra trees with pre- post-processing",
        algo_code=inspect.getsource(ExtraTreesClassifier),
    )
except Exception as err:
    print("Expecption while loading", str(err))
