# UpdateRequestTemplateInfo

Information for updating a request template. Omitted properties are left unchanged, but `custom_fields` replaces the template's fields wholesale when provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_template_id** | **UUID** | The ID of the request template to update. | 
**name** | **str** | The new name of the request template. | [optional] 
**custom_fields** | [**List[RequestTemplateCustomFieldInput]**](RequestTemplateCustomFieldInput.md) | The complete set of fields for the template. Any field not included is removed. | [optional] 

## Example

```python
from opal_security.models.update_request_template_info import UpdateRequestTemplateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRequestTemplateInfo from a JSON string
update_request_template_info_instance = UpdateRequestTemplateInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateRequestTemplateInfo.to_json())

# convert the object into a dict
update_request_template_info_dict = update_request_template_info_instance.to_dict()
# create an instance of UpdateRequestTemplateInfo from a dict
update_request_template_info_from_dict = UpdateRequestTemplateInfo.from_dict(update_request_template_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


