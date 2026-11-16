# RuleConjunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clauses** | [**List[RuleDisjunction]**](RuleDisjunction.md) | Empty only when the access rule has &#x60;uses_opal_query&#x60; set. | 

## Example

```python
from opal_security.models.rule_conjunction import RuleConjunction

# TODO update the JSON string below
json = "{}"
# create an instance of RuleConjunction from a JSON string
rule_conjunction_instance = RuleConjunction.from_json(json)
# print the JSON string representation of the object
print(RuleConjunction.to_json())

# convert the object into a dict
rule_conjunction_dict = rule_conjunction_instance.to_dict()
# create an instance of RuleConjunction from a dict
rule_conjunction_from_dict = RuleConjunction.from_dict(rule_conjunction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


