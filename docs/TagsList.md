# TagsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[Tag]**](Tag.md) |  | 

## Example

```python
from opal_security.models.tags_list import TagsList

# TODO update the JSON string below
json = "{}"
# create an instance of TagsList from a JSON string
tags_list_instance = TagsList.from_json(json)
# print the JSON string representation of the object
print(TagsList.to_json())

# convert the object into a dict
tags_list_dict = tags_list_instance.to_dict()
# create an instance of TagsList from a dict
tags_list_from_dict = TagsList.from_dict(tags_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


