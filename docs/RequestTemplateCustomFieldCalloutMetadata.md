# RequestTemplateCustomFieldCalloutMetadata

The message shown to a requester by a `CALLOUT` field, and how prominently to show it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** | How prominently the message is shown. | 
**text** | **str** | The message shown to the requester. | 

## Example

```python
from opal_security.models.request_template_custom_field_callout_metadata import RequestTemplateCustomFieldCalloutMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTemplateCustomFieldCalloutMetadata from a JSON string
request_template_custom_field_callout_metadata_instance = RequestTemplateCustomFieldCalloutMetadata.from_json(json)
# print the JSON string representation of the object
print(RequestTemplateCustomFieldCalloutMetadata.to_json())

# convert the object into a dict
request_template_custom_field_callout_metadata_dict = request_template_custom_field_callout_metadata_instance.to_dict()
# create an instance of RequestTemplateCustomFieldCalloutMetadata from a dict
request_template_custom_field_callout_metadata_from_dict = RequestTemplateCustomFieldCalloutMetadata.from_dict(request_template_custom_field_callout_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


