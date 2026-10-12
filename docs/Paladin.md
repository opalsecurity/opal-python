# Paladin

# Paladin Object ### Description The `Paladin` object represents a Paladin, Opal's AI access-request reviewer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paladin_id** | **UUID** | The ID of the Paladin. Use this value as a reviewer in a request configuration&#39;s service_user_ids. | 
**name** | **str** | The name of the Paladin. | 
**owner_id** | **UUID** | The ID of the owner of the Paladin. | 
**monitor_mode** | **bool** | When true, the Paladin reasons about requests but takes no action. Shown as \&quot;Monitor mode\&quot; in the UI. | 
**admin_view_only** | **bool** | When true, the Paladin&#39;s recommendations are visible only to admins. Only meaningful when monitor_mode is true. | 
**enabled_connectors** | [**List[PaladinConnector]**](PaladinConnector.md) | The connectors the Paladin is allowed to use. | 
**instructions** | **str** | The free-form instructions that guide the Paladin&#39;s decisions. | 

## Example

```python
from opal_security.models.paladin import Paladin

# TODO update the JSON string below
json = "{}"
# create an instance of Paladin from a JSON string
paladin_instance = Paladin.from_json(json)
# print the JSON string representation of the object
print(Paladin.to_json())

# convert the object into a dict
paladin_dict = paladin_instance.to_dict()
# create an instance of Paladin from a dict
paladin_from_dict = Paladin.from_dict(paladin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


