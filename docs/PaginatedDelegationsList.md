# PaginatedDelegationsList

A list of delegations for your organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Delegation]**](Delegation.md) | The delegations in the result set. | [optional] 
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**total_count** | **int** | The total number of items in the result set. | [optional] 

## Example

```python
from opal_security.models.paginated_delegations_list import PaginatedDelegationsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDelegationsList from a JSON string
paginated_delegations_list_instance = PaginatedDelegationsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDelegationsList.to_json())

# convert the object into a dict
paginated_delegations_list_dict = paginated_delegations_list_instance.to_dict()
# create an instance of PaginatedDelegationsList from a dict
paginated_delegations_list_from_dict = PaginatedDelegationsList.from_dict(paginated_delegations_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


