# RequestCommentList

A paginated list of request comments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**List[RequestComment]**](RequestComment.md) |  | 

## Example

```python
from opal_security.models.request_comment_list import RequestCommentList

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCommentList from a JSON string
request_comment_list_instance = RequestCommentList.from_json(json)
# print the JSON string representation of the object
print(RequestCommentList.to_json())

# convert the object into a dict
request_comment_list_dict = request_comment_list_instance.to_dict()
# create an instance of RequestCommentList from a dict
request_comment_list_from_dict = RequestCommentList.from_dict(request_comment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


