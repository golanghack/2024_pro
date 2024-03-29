from django.db import models


class Endpoint(models.Model):
    """
    The Endpoint object ML API endpoint

    Attrs:
            name: The name of the endpoint, used in API URL,
            owner: The string with owner name,
            created_at: The date when endpoint was created.
    """

    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True, blank=True)


class MLAlgo(models.Model):
    """
    The MlAlgo represent the ML algorithm object.

    Attrs:
            name: The name of the algo,
            description: The short description of how the algo works,
            code: The code of the algo,
            version: The version of the algo similar to software versions.
            owner: The name of the owner,
            created_at: The date when MLAlgo was added,
            parent_endpoint: The reference to the Endpoint
    """

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgoStatus(models.Model):
    """
    The MLAlgoStatus represent status of the MLAlhgo with canchange during the time.

    Attrs:
            status: The status of algo in the endpoint.Can be -> testing, staging, prodaction,
            active: The boolean flag which point to currently active status,
            created: by: The name of crreator,
            created_at: Th date of status creation,
            parent_mlalgo: The refernce to corresponding MLAlgo
    """

    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgo = models.ForeignKey(
        MLAlgo, on_delete=models.CASCADE, related_name="status"
    )


class MLRequest(models.Model):
    """
    The MLRequest will keep info about all requests to ML algos.

    Attrs:
            input_data: The input data to ML algo in JSON,
            full_response: The response of the ML algo,
            response: The response of the ML algo in JSON,
            feedback: The feedback about the response in JSON,
            created_at: The date when request, was created,
            parent_mlalgo: The reference to MLAlgo used to compute response.
    """

    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgo = models.ForeignKey(MLAlgo, on_delete=models.CASCADE)


class ABTest(models.Model):
    """
    The ABTest will keep about A/B tests.

    Attrs:
            title: The title of test,
            created_by: The name of creator,
            created_at: The date of test creation,
            ended_at: The date of test stop.
            summary: The description with test summary, created at test stop,
            parent_mlalgo_1: The reference to the first corresponding MlAlgo,
            parent_mlalgo_2: The reference to the second corresponding MLAlgo.
    """

    title = models.CharField(max_length=10000)
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    summary = models.CharField(max_length=10000, blank=True, null=True)
    parent_mlalgo_1 = models.ForeignKey(
        MLAlgo, on_delete=models.CASCADE, related_name="parent_mlalgo_1"
    )
    parent_mlalgo_2 = models.ForeignKey(
        MLAlgo, on_delete=models.CASCADE, related_name="parent_mlalgo_2"
    )
