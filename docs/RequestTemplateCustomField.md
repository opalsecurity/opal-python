# RequestTemplateCustomField

A field on a request template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The label shown to the requester. &#x60;CALLOUT&#x60; fields are display-only, so their name is an internal identifier and is never displayed. | 
**description** | **str** | Helper text shown beneath the field. | [optional] 
**type** | [**RequestTemplateCustomFieldTypeEnum**](RequestTemplateCustomFieldTypeEnum.md) |  | 
**required** | **bool** | Whether the requester must answer. Always false for &#x60;CALLOUT&#x60; fields, which collect no answer. | [optional] 
**metadata** | [**RequestTemplateCustomFieldMetadata**](RequestTemplateCustomFieldMetadata.md) |  | [optional] 

## Example

```python
from opal_security.models.request_template_custom_field import RequestTemplateCustomField

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTemplateCustomField from a JSON string
request_template_custom_field_instance = RequestTemplateCustomField.from_json(json)
# print the JSON string representation of the object
print(RequestTemplateCustomField.to_json())

# convert the object into a dict
request_template_custom_field_dict = request_template_custom_field_instance.to_dict()
# create an instance of RequestTemplateCustomField from a dict
request_template_custom_field_from_dict = RequestTemplateCustomField.from_dict(request_template_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


