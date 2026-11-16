# CancelRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acting_user_id** | **UUID** | Cancel as this Opal user instead of the caller. Only for service users an admin has allowed to act for users, in organizations with the feature enabled. The user must be active in the identity provider and be an Opal admin or the request&#39;s requester, target or initiated_by user. Unknown body fields are ignored, so a misspelled field cancels as the caller. | [optional] 

## Example

```python
from opal_security.models.cancel_request_request import CancelRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelRequestRequest from a JSON string
cancel_request_request_instance = CancelRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CancelRequestRequest.to_json())

# convert the object into a dict
cancel_request_request_dict = cancel_request_request_instance.to_dict()
# create an instance of CancelRequestRequest from a dict
cancel_request_request_from_dict = CancelRequestRequest.from_dict(cancel_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


