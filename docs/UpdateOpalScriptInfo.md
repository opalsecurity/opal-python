# UpdateOpalScriptInfo

Information for updating an OpalScript. Omitted fields are left unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the OpalScript. | [optional] 
**script** | **str** | The source of the OpalScript. A new version is recorded only when the source differs from the current one. | [optional] 

## Example

```python
from opal_security.models.update_opal_script_info import UpdateOpalScriptInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOpalScriptInfo from a JSON string
update_opal_script_info_instance = UpdateOpalScriptInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateOpalScriptInfo.to_json())

# convert the object into a dict
update_opal_script_info_dict = update_opal_script_info_instance.to_dict()
# create an instance of UpdateOpalScriptInfo from a dict
update_opal_script_info_from_dict = UpdateOpalScriptInfo.from_dict(update_opal_script_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


