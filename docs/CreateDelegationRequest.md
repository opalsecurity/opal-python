# CreateDelegationRequest

Request body for creating a new delegation of access review requests from one user to another.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegator_user_id** | **str** | The ID of the user delegating their access review requests. | 
**delegate_user_id** | **str** | The ID of the user being delegated to. | 
**start_time** | **datetime** | The start time of the delegation. | 
**end_time** | **datetime** | The end time of the delegation. | 
**reason** | **str** | The reason for the delegation. | 

## Example

```python
from opal_security.models.create_delegation_request import CreateDelegationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDelegationRequest from a JSON string
create_delegation_request_instance = CreateDelegationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDelegationRequest.to_json())

# convert the object into a dict
create_delegation_request_dict = create_delegation_request_instance.to_dict()
# create an instance of CreateDelegationRequest from a dict
create_delegation_request_from_dict = CreateDelegationRequest.from_dict(create_delegation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


