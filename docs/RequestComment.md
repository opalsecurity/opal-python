# RequestComment

# Request Comment Object ### Description The `RequestComment` object is used to represent a comment on a request.  ### Usage Example Returned from the `GET Requests` endpoint as part of a `Request` object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date and time the comment was created. | 
**request_id** | **str** | The unique identifier of the request the comment is associated with. | 
**user_id** | **str** | The unique identifier of the user who made the comment. | 
**user_full_name** | **str** | The user&#39;s full name. | [optional] 
**user_email** | **str** | The user&#39;s email address. | [optional] 
**comment** | **str** | The content of the comment. | 

## Example

```python
from opal_security.models.request_comment import RequestComment

# TODO update the JSON string below
json = "{}"
# create an instance of RequestComment from a JSON string
request_comment_instance = RequestComment.from_json(json)
# print the JSON string representation of the object
print(RequestComment.to_json())

# convert the object into a dict
request_comment_dict = request_comment_instance.to_dict()
# create an instance of RequestComment from a dict
request_comment_from_dict = RequestComment.from_dict(request_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


