# AccessRule

# Access Rule Object ### Description The `AccessRule` object is used to represent an access rule configuration.  ### Usage Example Get access rule configurations from the `GET Access Rule Configs` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_rule_id** | **str** | The ID (group ID) of the access rule. | 
**name** | **str** | The name of the access rule. | 
**description** | **str** | A description of the group. | 
**admin_owner_id** | **str** | The ID of the owner of the group. | 
**status** | **str** | The status of the access rule. | 
**rule_clauses** | [**RuleClauses**](RuleClauses.md) |  | 

## Example

```python
from opal_security.models.access_rule import AccessRule

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRule from a JSON string
access_rule_instance = AccessRule.from_json(json)
# print the JSON string representation of the object
print(AccessRule.to_json())

# convert the object into a dict
access_rule_dict = access_rule_instance.to_dict()
# create an instance of AccessRule from a dict
access_rule_from_dict = AccessRule.from_dict(access_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


