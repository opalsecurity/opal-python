# RequestTemplateCustomFieldInput

A field to put on a request template. Separate from `RequestTemplateCustomField` because a callout's name may be omitted on write, while a field read back always has one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The label shown to the requester. Required for every type except &#x60;CALLOUT&#x60;, which is display-only -- its name is an internal identifier, never displayed, and is generated if omitted. | [optional] 
**description** | **str** | Helper text shown beneath the field. | [optional] 
**type** | [**RequestTemplateCustomFieldTypeEnum**](RequestTemplateCustomFieldTypeEnum.md) |  | 
**required** | **bool** | Whether the requester must answer. Ignored for &#x60;CALLOUT&#x60; fields, which collect no answer. | [optional] 
**metadata** | [**RequestTemplateCustomFieldMetadata**](RequestTemplateCustomFieldMetadata.md) |  | [optional] 

## Example

```python
from opal_security.models.request_template_custom_field_input import RequestTemplateCustomFieldInput

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTemplateCustomFieldInput from a JSON string
request_template_custom_field_input_instance = RequestTemplateCustomFieldInput.from_json(json)
# print the JSON string representation of the object
print(RequestTemplateCustomFieldInput.to_json())

# convert the object into a dict
request_template_custom_field_input_dict = request_template_custom_field_input_instance.to_dict()
# create an instance of RequestTemplateCustomFieldInput from a dict
request_template_custom_field_input_from_dict = RequestTemplateCustomFieldInput.from_dict(request_template_custom_field_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


