# CreatePaladinInfo

Information for creating a Paladin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Paladin. | 
**owner_id** | **UUID** | The ID of the owner of the Paladin. | 
**monitor_mode** | **bool** | When true, the Paladin reasons about requests but takes no action. Defaults to true. | [optional] [default to True]
**admin_view_only** | **bool** | When true, recommendations are visible only to admins. Only meaningful when monitor_mode is true. Defaults to false. | [optional] [default to False]
**enabled_connectors** | [**List[PaladinConnector]**](PaladinConnector.md) | The connectors the Paladin is allowed to use. | [optional] 
**instructions** | **str** | The free-form instructions that guide the Paladin&#39;s decisions. Optional; if omitted the Paladin is created without instructions. | [optional] 

## Example

```python
from opal_security.models.create_paladin_info import CreatePaladinInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaladinInfo from a JSON string
create_paladin_info_instance = CreatePaladinInfo.from_json(json)
# print the JSON string representation of the object
print(CreatePaladinInfo.to_json())

# convert the object into a dict
create_paladin_info_dict = create_paladin_info_instance.to_dict()
# create an instance of CreatePaladinInfo from a dict
create_paladin_info_from_dict = CreatePaladinInfo.from_dict(create_paladin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


