# RequestReviewerStages

The configured reviewer stages for every item in this request, or an error message if reviewers could not be loaded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from opal_security.models.request_reviewer_stages import RequestReviewerStages

# TODO update the JSON string below
json = "{}"
# create an instance of RequestReviewerStages from a JSON string
request_reviewer_stages_instance = RequestReviewerStages.from_json(json)
# print the JSON string representation of the object
print(RequestReviewerStages.to_json())

# convert the object into a dict
request_reviewer_stages_dict = request_reviewer_stages_instance.to_dict()
# create an instance of RequestReviewerStages from a dict
request_reviewer_stages_from_dict = RequestReviewerStages.from_dict(request_reviewer_stages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


