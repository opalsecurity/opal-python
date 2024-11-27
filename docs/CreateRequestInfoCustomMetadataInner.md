# CreateRequestInfoCustomMetadataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**RequestTemplateCustomFieldTypeEnum**](RequestTemplateCustomFieldTypeEnum.md) |  | 
**value** | **str** |  | 

## Example

```python
from opal_security.models.create_request_info_custom_metadata_inner import CreateRequestInfoCustomMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestInfoCustomMetadataInner from a JSON string
create_request_info_custom_metadata_inner_instance = CreateRequestInfoCustomMetadataInner.from_json(json)
# print the JSON string representation of the object
print(CreateRequestInfoCustomMetadataInner.to_json())

# convert the object into a dict
create_request_info_custom_metadata_inner_dict = create_request_info_custom_metadata_inner_instance.to_dict()
# create an instance of CreateRequestInfoCustomMetadataInner from a dict
create_request_info_custom_metadata_inner_from_dict = CreateRequestInfoCustomMetadataInner.from_dict(create_request_info_custom_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


