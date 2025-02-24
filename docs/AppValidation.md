# AppValidation

# App validation object ### Description The `AppValidation` object is used to represent a validation check of an apps' configuration and permissions.  ### Usage Example List from the `GET Apps` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the app validation. These are not unique IDs between runs. | 
**name** | **object** |  | 
**usage_reason** | **str** | The reason for needing the validation. | [optional] 
**details** | **str** | Extra details regarding the validation. Could be an error message or restrictions on permissions. | [optional] 
**severity** | [**AppValidationSeverityEnum**](AppValidationSeverityEnum.md) |  | 
**status** | [**AppValidationStatusEnum**](AppValidationStatusEnum.md) |  | 
**updated_at** | **datetime** | The date and time the app validation was last run. | 

## Example

```python
from opal_security.models.app_validation import AppValidation

# TODO update the JSON string below
json = "{}"
# create an instance of AppValidation from a JSON string
app_validation_instance = AppValidation.from_json(json)
# print the JSON string representation of the object
print(AppValidation.to_json())

# convert the object into a dict
app_validation_dict = app_validation_instance.to_dict()
# create an instance of AppValidation from a dict
app_validation_from_dict = AppValidation.from_dict(app_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


