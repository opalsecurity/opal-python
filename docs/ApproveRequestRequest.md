# ApproveRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acting_user_id** | **UUID** | Approve as this Opal user instead of the caller. Only for service users an admin has allowed to act for users, in organizations with the feature enabled. The user must be active in the identity provider and be a reviewer on the request&#39;s current stage and not the request&#39;s target; the decision counts as theirs. Requests that require MFA to approve, and ADMIN level, are rejected. | [optional] 
**level** | [**RequestApprovalEnum**](RequestApprovalEnum.md) |  | 
**comment** | **str** | Optional comment for the approval | [optional] 

## Example

```python
from opal_security.models.approve_request_request import ApproveRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveRequestRequest from a JSON string
approve_request_request_instance = ApproveRequestRequest.from_json(json)
# print the JSON string representation of the object
print(ApproveRequestRequest.to_json())

# convert the object into a dict
approve_request_request_dict = approve_request_request_instance.to_dict()
# create an instance of ApproveRequestRequest from a dict
approve_request_request_from_dict = ApproveRequestRequest.from_dict(approve_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


