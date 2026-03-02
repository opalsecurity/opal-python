# Tag

# Tag Object ### Description The `Tag` object is used to represent a tag.  ### Usage Example Get tags from the `GET Tag` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **str** | The ID of the tag. | 
**created_at** | **datetime** | The date the tag was created. | [optional] 
**updated_at** | **datetime** | The date the tag was last updated. | [optional] 
**user_creator_id** | **str** | The ID of the user that created the tag. | [optional] 
**key** | **str** | The key of the tag. | [optional] 
**value** | **str** | The value of the tag. | [optional] 

## Example

```python
from opal_security.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print(Tag.to_json())

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_from_dict = Tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


