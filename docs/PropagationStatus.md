# PropagationStatus

The state of whether the push action was propagated to the remote system. If this is null, the access was synced from the remote system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PropagationStatusEnum**](PropagationStatusEnum.md) |  | 

## Example

```python
from opal_security.models.propagation_status import PropagationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PropagationStatus from a JSON string
propagation_status_instance = PropagationStatus.from_json(json)
# print the JSON string representation of the object
print(PropagationStatus.to_json())

# convert the object into a dict
propagation_status_dict = propagation_status_instance.to_dict()
# create an instance of PropagationStatus from a dict
propagation_status_from_dict = PropagationStatus.from_dict(propagation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


