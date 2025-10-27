# ApproveRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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


