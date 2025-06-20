# PageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** | Whether there are more items after the end cursor | 
**end_cursor** | **str** | The cursor to continue pagination forwards | 
**has_previous_page** | **bool** | Whether there are more items before the start cursor | 
**start_cursor** | **str** | The cursor to continue pagination backwards | 

## Example

```python
from opal_security.models.page_info import PageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PageInfo from a JSON string
page_info_instance = PageInfo.from_json(json)
# print the JSON string representation of the object
print(PageInfo.to_json())

# convert the object into a dict
page_info_dict = page_info_instance.to_dict()
# create an instance of PageInfo from a dict
page_info_from_dict = PageInfo.from_dict(page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


