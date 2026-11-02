# GroupRemoteInfoCalendlyGroup

Remote info for Calendly Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | The group id of the Calendly Group. | 

## Example

```python
from opal_security.models.group_remote_info_calendly_group import GroupRemoteInfoCalendlyGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoCalendlyGroup from a JSON string
group_remote_info_calendly_group_instance = GroupRemoteInfoCalendlyGroup.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoCalendlyGroup.to_json())

# convert the object into a dict
group_remote_info_calendly_group_dict = group_remote_info_calendly_group_instance.to_dict()
# create an instance of GroupRemoteInfoCalendlyGroup from a dict
group_remote_info_calendly_group_from_dict = GroupRemoteInfoCalendlyGroup.from_dict(group_remote_info_calendly_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


