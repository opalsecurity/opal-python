# RequestTemplateCustomFieldMetadata

Extra configuration for field types that need it. Exactly one member is set, and which one is determined by the field's `type`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callout_data** | [**RequestTemplateCustomFieldCalloutMetadata**](RequestTemplateCustomFieldCalloutMetadata.md) |  | [optional] 
**multi_choice_data** | [**RequestTemplateCustomFieldMultiChoiceMetadata**](RequestTemplateCustomFieldMultiChoiceMetadata.md) |  | [optional] 

## Example

```python
from opal_security.models.request_template_custom_field_metadata import RequestTemplateCustomFieldMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTemplateCustomFieldMetadata from a JSON string
request_template_custom_field_metadata_instance = RequestTemplateCustomFieldMetadata.from_json(json)
# print the JSON string representation of the object
print(RequestTemplateCustomFieldMetadata.to_json())

# convert the object into a dict
request_template_custom_field_metadata_dict = request_template_custom_field_metadata_instance.to_dict()
# create an instance of RequestTemplateCustomFieldMetadata from a dict
request_template_custom_field_metadata_from_dict = RequestTemplateCustomFieldMetadata.from_dict(request_template_custom_field_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


