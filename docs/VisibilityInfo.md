# VisibilityInfo

Visibility infomation of an entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visibility** | [**VisibilityTypeEnum**](VisibilityTypeEnum.md) |  | 
**visibility_group_ids** | **List[str]** |  | [optional] 

## Example

```python
from opal_security.models.visibility_info import VisibilityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VisibilityInfo from a JSON string
visibility_info_instance = VisibilityInfo.from_json(json)
# print the JSON string representation of the object
print(VisibilityInfo.to_json())

# convert the object into a dict
visibility_info_dict = visibility_info_instance.to_dict()
# create an instance of VisibilityInfo from a dict
visibility_info_from_dict = VisibilityInfo.from_dict(visibility_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


