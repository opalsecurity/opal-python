# CreateRequestCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acting_user_id** | **UUID** | Comment as this Opal user instead of the caller. Only for service users an admin has allowed to act for users, in organizations with the feature enabled. The user must be active in the identity provider and be the request&#39;s requester, target or initiated_by user, an admin, or a reviewer who can act on or has acted on the request. | [optional] 
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


