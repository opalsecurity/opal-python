# RequestTemplateCustomFieldMultiChoiceMetadata

The options a requester can pick from in a `MULTI_CHOICE` or `MULTI_SELECT` field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | **List[str]** |  | 

## Example

```python
from opal_security.models.request_template_custom_field_multi_choice_metadata import RequestTemplateCustomFieldMultiChoiceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTemplateCustomFieldMultiChoiceMetadata from a JSON string
request_template_custom_field_multi_choice_metadata_instance = RequestTemplateCustomFieldMultiChoiceMetadata.from_json(json)
# print the JSON string representation of the object
print(RequestTemplateCustomFieldMultiChoiceMetadata.to_json())

# convert the object into a dict
request_template_custom_field_multi_choice_metadata_dict = request_template_custom_field_multi_choice_metadata_instance.to_dict()
# create an instance of RequestTemplateCustomFieldMultiChoiceMetadata from a dict
request_template_custom_field_multi_choice_metadata_from_dict = RequestTemplateCustomFieldMultiChoiceMetadata.from_dict(request_template_custom_field_multi_choice_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


