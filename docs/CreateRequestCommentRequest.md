# CreateRequestCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | comment | 

## Example

```python
from opal_security.models.create_request_comment_request import CreateRequestCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestCommentRequest from a JSON string
create_request_comment_request_instance = CreateRequestCommentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRequestCommentRequest.to_json())

# convert the object into a dict
create_request_comment_request_dict = create_request_comment_request_instance.to_dict()
# create an instance of CreateRequestCommentRequest from a dict
create_request_comment_request_from_dict = CreateRequestCommentRequest.from_dict(create_request_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


