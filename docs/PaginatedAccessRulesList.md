# PaginatedAccessRulesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to retrieve the previous page of results. | [optional] 
**results** | [**List[AccessRule]**](AccessRule.md) |  | 

## Example

```python
from opal_security.models.paginated_access_rules_list import PaginatedAccessRulesList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAccessRulesList from a JSON string
paginated_access_rules_list_instance = PaginatedAccessRulesList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAccessRulesList.to_json())

# convert the object into a dict
paginated_access_rules_list_dict = paginated_access_rules_list_instance.to_dict()
# create an instance of PaginatedAccessRulesList from a dict
paginated_access_rules_list_from_dict = PaginatedAccessRulesList.from_dict(paginated_access_rules_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


