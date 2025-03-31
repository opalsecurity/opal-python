# RuleDisjunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectors** | [**List[TagSelector]**](TagSelector.md) |  | 

## Example

```python
from opal_security.models.rule_disjunction import RuleDisjunction

# TODO update the JSON string below
json = "{}"
# create an instance of RuleDisjunction from a JSON string
rule_disjunction_instance = RuleDisjunction.from_json(json)
# print the JSON string representation of the object
print(RuleDisjunction.to_json())

# convert the object into a dict
rule_disjunction_dict = rule_disjunction_instance.to_dict()
# create an instance of RuleDisjunction from a dict
rule_disjunction_from_dict = RuleDisjunction.from_dict(rule_disjunction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


