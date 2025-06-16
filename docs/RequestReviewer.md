# RequestReviewer

A reviewer in a request stage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the reviewer | 
**status** | **str** | The status of this reviewer&#39;s review | 

## Example

```python
from opal_security.models.request_reviewer import RequestReviewer

# TODO update the JSON string below
json = "{}"
# create an instance of RequestReviewer from a JSON string
request_reviewer_instance = RequestReviewer.from_json(json)
# print the JSON string representation of the object
print(RequestReviewer.to_json())

# convert the object into a dict
request_reviewer_dict = request_reviewer_instance.to_dict()
# create an instance of RequestReviewer from a dict
request_reviewer_from_dict = RequestReviewer.from_dict(request_reviewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


