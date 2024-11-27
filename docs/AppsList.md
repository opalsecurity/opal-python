# AppsList

A list of apps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[App]**](App.md) |  | 

## Example

```python
from opal_security.models.apps_list import AppsList

# TODO update the JSON string below
json = "{}"
# create an instance of AppsList from a JSON string
apps_list_instance = AppsList.from_json(json)
# print the JSON string representation of the object
print(AppsList.to_json())

# convert the object into a dict
apps_list_dict = apps_list_instance.to_dict()
# create an instance of AppsList from a dict
apps_list_from_dict = AppsList.from_dict(apps_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


