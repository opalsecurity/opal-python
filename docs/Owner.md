# Owner

# Owner Object ### Description The `Owner` object is used to represent an owner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** | The ID of the owner. | 
**name** | **str** | The name of the owner. | [optional] 
**description** | **str** | A description of the owner. | [optional] 
**access_request_escalation_period** | **int** | The amount of time (in minutes) before the next reviewer is notified. Use 0 to remove escalation policy. | [optional] 
**reviewer_message_channel_id** | **str** |  | [optional] 
**source_group_id** | **str** |  | [optional] 

## Example

```python
from opal_security.models.owner import Owner

# TODO update the JSON string below
json = "{}"
# create an instance of Owner from a JSON string
owner_instance = Owner.from_json(json)
# print the JSON string representation of the object
print(Owner.to_json())

# convert the object into a dict
owner_dict = owner_instance.to_dict()
# create an instance of Owner from a dict
owner_from_dict = Owner.from_dict(owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


