# UARScope

If set, the access review will only contain resources and groups that match at least one of the filters in scope.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[TagFilter]**](TagFilter.md) | This access review will include resources and groups who are tagged with one of the given tags. | [optional] 
**names** | **List[str]** | This access review will include resources and groups whose name contains one of the given strings. | [optional] 
**admins** | **List[str]** | This access review will include resources and groups who are owned by one of the owners corresponding to the given IDs. | [optional] 

## Example

```python
from opal.models.uar_scope import UARScope

# TODO update the JSON string below
json = "{}"
# create an instance of UARScope from a JSON string
uar_scope_instance = UARScope.from_json(json)
# print the JSON string representation of the object
print UARScope.to_json()

# convert the object into a dict
uar_scope_dict = uar_scope_instance.to_dict()
# create an instance of UARScope from a dict
uar_scope_form_dict = uar_scope.from_dict(uar_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


