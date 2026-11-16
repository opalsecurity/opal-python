# DenyRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acting_user_id** | **UUID** | Deny as this Opal user instead of the caller. Only for service users an admin has allowed to act for users, in organizations with the feature enabled. The user must be active in the identity provider and be a reviewer on the request&#39;s current stage and not the request&#39;s target; the decision counts as theirs. ADMIN level is rejected. | [optional] 
**comment** | **str** | Comment for the denial | 
**level** | [**RequestApprovalEnum**](RequestApprovalEnum.md) |  | [optional] 

## Example

```python
from opal_security.models.deny_request_request import DenyRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DenyRequestRequest from a JSON string
deny_request_request_instance = DenyRequestRequest.from_json(json)
# print the JSON string representation of the object
print(DenyRequestRequest.to_json())

# convert the object into a dict
deny_request_request_dict = deny_request_request_instance.to_dict()
# create an instance of DenyRequestRequest from a dict
deny_request_request_from_dict = DenyRequestRequest.from_dict(deny_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


