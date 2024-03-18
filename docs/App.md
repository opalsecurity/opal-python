# App

# App Object ### Description The `App` object is used to represent an app to an application.  ### Usage Example List from the `GET Apps` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | The ID of the app. | 
**name** | **str** | The name of the app. | 
**description** | **str** | A description of the app. | 
**admin_owner_id** | **str** | The ID of the owner of the app. | 
**app_type** | [**AppTypeEnum**](AppTypeEnum.md) |  | 

## Example

```python
from opal.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print(App.to_json())

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_form_dict = app.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


