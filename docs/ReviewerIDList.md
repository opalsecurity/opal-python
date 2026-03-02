# ReviewerIDList

A list of reviewer IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewer_ids** | **List[str]** |  | 

## Example

```python
from opal_security.models.reviewer_id_list import ReviewerIDList

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewerIDList from a JSON string
reviewer_id_list_instance = ReviewerIDList.from_json(json)
# print the JSON string representation of the object
print(ReviewerIDList.to_json())

# convert the object into a dict
reviewer_id_list_dict = reviewer_id_list_instance.to_dict()
# create an instance of ReviewerIDList from a dict
reviewer_id_list_from_dict = ReviewerIDList.from_dict(reviewer_id_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


