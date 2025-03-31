# RuleClauses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when** | [**RuleConjunction**](RuleConjunction.md) |  | 
**unless** | [**RuleConjunction**](RuleConjunction.md) |  | [optional] 

## Example

```python
from opal_security.models.rule_clauses import RuleClauses

# TODO update the JSON string below
json = "{}"
# create an instance of RuleClauses from a JSON string
rule_clauses_instance = RuleClauses.from_json(json)
# print the JSON string representation of the object
print(RuleClauses.to_json())

# convert the object into a dict
rule_clauses_dict = rule_clauses_instance.to_dict()
# create an instance of RuleClauses from a dict
rule_clauses_from_dict = RuleClauses.from_dict(rule_clauses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


