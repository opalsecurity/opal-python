# Condition

# Condition Object ### Description The `Condition` object is used to represent a condition.  ### Usage Example Used to match request configurations to users in `RequestConfiguration`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_ids** | **List[str]** | The list of group IDs to match. | [optional] 
**role_remote_ids** | **List[str]** | The list of role remote IDs to match. | [optional] 

## Example

```python
from opal_security.models.condition import Condition

# TODO update the JSON string below
json = "{}"
# create an instance of Condition from a JSON string
condition_instance = Condition.from_json(json)
# print the JSON string representation of the object
print(Condition.to_json())

# convert the object into a dict
condition_dict = condition_instance.to_dict()
# create an instance of Condition from a dict
condition_from_dict = Condition.from_dict(condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


