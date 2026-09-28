# RequestTemplate

A template describing what a requester is asked when requesting access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_template_id** | **UUID** | The ID of the request template. | 
**name** | **str** | The name of the request template. | 
**custom_fields** | [**List[RequestTemplateCustomField]**](RequestTemplateCustomField.md) | The fields on this template, in the order they are shown. | [optional] 

## Example

```python
from opal_security.models.request_template import RequestTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTemplate from a JSON string
request_template_instance = RequestTemplate.from_json(json)
# print the JSON string representation of the object
print(RequestTemplate.to_json())

# convert the object into a dict
request_template_dict = request_template_instance.to_dict()
# create an instance of RequestTemplate from a dict
request_template_from_dict = RequestTemplate.from_dict(request_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


