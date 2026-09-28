# UpdatePaladinInfo

Information for updating a Paladin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Paladin. | 
**monitor_mode** | **bool** | When true, the Paladin reasons about requests but takes no action. If omitted, the existing value is preserved. | [optional] 
**admin_view_only** | **bool** | When true, recommendations are visible only to admins. Only meaningful when monitor_mode is true. If omitted, the existing value is preserved. | [optional] 
**enabled_connectors** | [**List[PaladinConnector]**](PaladinConnector.md) | The connectors the Paladin is allowed to use. If omitted, the existing connectors are preserved. | [optional] 
**instructions** | **str** | The free-form instructions that guide the Paladin&#39;s decisions. If omitted, the existing instructions are preserved. | [optional] 

## Example

```python
from opal_security.models.update_paladin_info import UpdatePaladinInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaladinInfo from a JSON string
update_paladin_info_instance = UpdatePaladinInfo.from_json(json)
# print the JSON string representation of the object
print(UpdatePaladinInfo.to_json())

# convert the object into a dict
update_paladin_info_dict = update_paladin_info_instance.to_dict()
# create an instance of UpdatePaladinInfo from a dict
update_paladin_info_from_dict = UpdatePaladinInfo.from_dict(update_paladin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


