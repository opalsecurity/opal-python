# CreateOpalScriptInfo

Information for creating an OpalScript.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the OpalScript. | 
**script_type** | [**OpalScriptTypeEnum**](OpalScriptTypeEnum.md) |  | 
**script** | **str** | The source of the OpalScript. | 
**owner_id** | **UUID** | The owner of the service user Opal provisions for a &#x60;REQUEST_REVIEW&#x60; script. Required for that script type and ignored for the others, which have no reviewer identity. | [optional] 

## Example

```python
from opal_security.models.create_opal_script_info import CreateOpalScriptInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOpalScriptInfo from a JSON string
create_opal_script_info_instance = CreateOpalScriptInfo.from_json(json)
# print the JSON string representation of the object
print(CreateOpalScriptInfo.to_json())

# convert the object into a dict
create_opal_script_info_dict = create_opal_script_info_instance.to_dict()
# create an instance of CreateOpalScriptInfo from a dict
create_opal_script_info_from_dict = CreateOpalScriptInfo.from_dict(create_opal_script_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


