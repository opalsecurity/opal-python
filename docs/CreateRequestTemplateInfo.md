# CreateRequestTemplateInfo

Information for creating a request template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the request template. | 
**custom_fields** | [**List[RequestTemplateCustomFieldInput]**](RequestTemplateCustomFieldInput.md) | The fields to put on the template, in the order they are shown. | [optional] 

## Example

```python
from opal_security.models.create_request_template_info import CreateRequestTemplateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestTemplateInfo from a JSON string
create_request_template_info_instance = CreateRequestTemplateInfo.from_json(json)
# print the JSON string representation of the object
print(CreateRequestTemplateInfo.to_json())

# convert the object into a dict
create_request_template_info_dict = create_request_template_info_instance.to_dict()
# create an instance of CreateRequestTemplateInfo from a dict
create_request_template_info_from_dict = CreateRequestTemplateInfo.from_dict(create_request_template_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


