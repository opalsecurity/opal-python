# OpalScript

# OpalScript Object ### Description The `OpalScript` object represents an OpalScript: a Starlark script that automates part of Opal's access lifecycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opal_script_id** | **UUID** | The ID of the OpalScript. | 
**name** | **str** | The name of the OpalScript. | 
**script_type** | [**OpalScriptTypeEnum**](OpalScriptTypeEnum.md) |  | 
**script** | **str** | The source of the OpalScript&#39;s latest version. | 
**version** | **int** | The version number of the OpalScript&#39;s latest version. | 
**updated_at** | **datetime** | The date the OpalScript was last updated. | [optional] 

## Example

```python
from opal_security.models.opal_script import OpalScript

# TODO update the JSON string below
json = "{}"
# create an instance of OpalScript from a JSON string
opal_script_instance = OpalScript.from_json(json)
# print the JSON string representation of the object
print(OpalScript.to_json())

# convert the object into a dict
opal_script_dict = opal_script_instance.to_dict()
# create an instance of OpalScript from a dict
opal_script_from_dict = OpalScript.from_dict(opal_script_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


