from endpoints.models import Endpoint
from endpoints.models import MLAlgo
from endpoints.models import MLAlgoStatus


class MLRegistry:
    def __init__(self):
        self.endpoints = {}

    def add_algo(
        self,
        endpoint_name,
        algo_object,
        algo_name,
        algo_status,
        algo_version,
        owner,
        algo_desc,
        algo_code,
    ):
        # endpoint
        endpoint, _ = Endpoint.objects.get_or_create(name=endpoint_name, owner=owner)
        # get algo
        database_object, algo_created = MLAlgo.objects.get_or_create(
            name=algo_name,
            description=algo_desc,
            code=algo_code,
            version=algo_version,
            owner=owner,
            parent_endpoint=endpoint,
        )
        if algo_created:
            status = MLAlgoStatus(
                status=algo_status,
                created_by=owner,
                parent_mlalgo=database_object,
                active=True,
            )
        status.save()
        self.endpoints[database_object.id] = algo_object
