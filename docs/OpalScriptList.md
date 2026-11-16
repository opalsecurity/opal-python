# OpalScriptList

# OpalScriptList Object ### Description A list of `OpalScript` objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OpalScript]**](OpalScript.md) |  | 

## Example

```python
from opal_security.models.opal_script_list import OpalScriptList

# TODO update the JSON string below
json = "{}"
# create an instance of OpalScriptList from a JSON string
opal_script_list_instance = OpalScriptList.from_json(json)
# print the JSON string representation of the object
print(OpalScriptList.to_json())

# convert the object into a dict
opal_script_list_dict = opal_script_list_instance.to_dict()
# create an instance of OpalScriptList from a dict
opal_script_list_from_dict = OpalScriptList.from_dict(opal_script_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


