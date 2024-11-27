# CreateTagInfo

# CreateTagInfo Object ### Description The `CreateTagInfo` object is used to represent configuration for a new tag.  ### Usage Example Use in the `POST Tag` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_key** | **str** | The key of the tag to create. | 
**tag_value** | **str** | The value of the tag to create. | [optional] 

## Example

```python
from opal_security.models.create_tag_info import CreateTagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagInfo from a JSON string
create_tag_info_instance = CreateTagInfo.from_json(json)
# print the JSON string representation of the object
print(CreateTagInfo.to_json())

# convert the object into a dict
create_tag_info_dict = create_tag_info_instance.to_dict()
# create an instance of CreateTagInfo from a dict
create_tag_info_from_dict = CreateTagInfo.from_dict(create_tag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


