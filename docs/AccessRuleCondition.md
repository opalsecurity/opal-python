# AccessRuleCondition

# Access Rule Config Object ### Description The `AccessRuleConfig` object is used to represent an access rule configuration.  ### Usage Example Get access rule configurations from the `GET Access Rule Configs` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the access rule. | 
**rule_clauses** | [**RuleClauses**](RuleClauses.md) |  | 

## Example

```python
from opal_security.models.access_rule_condition import AccessRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRuleCondition from a JSON string
access_rule_condition_instance = AccessRuleCondition.from_json(json)
# print the JSON string representation of the object
print(AccessRuleCondition.to_json())

# convert the object into a dict
access_rule_condition_dict = access_rule_condition_instance.to_dict()
# create an instance of AccessRuleCondition from a dict
access_rule_condition_from_dict = AccessRuleCondition.from_dict(access_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


