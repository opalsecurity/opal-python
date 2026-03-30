# Delegation

# Delegation Object ### Description The `Delegation` object represents a delegation of access review requests from one user to another.  ### Usage Example List from the `GET Delegations` endpoint. Get from the `GET Delegation` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the delegation. | 
**delegator_user_id** | **str** | The ID of the user delegating their access review requests. | 
**delegate_user_id** | **str** | The ID of the user being delegated to. | 
**start_time** | **datetime** | The start time of the delegation. | 
**end_time** | **datetime** | The end time of the delegation. | 
**reason** | **str** | The reason for the delegation. | 
**created_at** | **datetime** | The creation time of the delegation. | 
**updated_at** | **datetime** | The last updated time of the delegation. | 

## Example

```python
from opal_security.models.delegation import Delegation

# TODO update the JSON string below
json = "{}"
# create an instance of Delegation from a JSON string
delegation_instance = Delegation.from_json(json)
# print the JSON string representation of the object
print(Delegation.to_json())

# convert the object into a dict
delegation_dict = delegation_instance.to_dict()
# create an instance of Delegation from a dict
delegation_from_dict = Delegation.from_dict(delegation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


