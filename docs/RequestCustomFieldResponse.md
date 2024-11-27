# RequestCustomFieldResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | 
**field_type** | [**RequestTemplateCustomFieldTypeEnum**](RequestTemplateCustomFieldTypeEnum.md) |  | 
**field_value** | [**RequestCustomFieldResponseFieldValue**](RequestCustomFieldResponseFieldValue.md) |  | 

## Example

```python
from opal_security.models.request_custom_field_response import RequestCustomFieldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCustomFieldResponse from a JSON string
request_custom_field_response_instance = RequestCustomFieldResponse.from_json(json)
# print the JSON string representation of the object
print(RequestCustomFieldResponse.to_json())

# convert the object into a dict
request_custom_field_response_dict = request_custom_field_response_instance.to_dict()
# create an instance of RequestCustomFieldResponse from a dict
request_custom_field_response_from_dict = RequestCustomFieldResponse.from_dict(request_custom_field_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


