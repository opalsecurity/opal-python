# UpdateAccessRuleInfo

# UpdateAccessRuleInfo Object ### Description The `UpdateAccessRuleInfo` object is used as an input to the UpdateAccessRule and CreateAccessRule API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the access rule. | 
**description** | **str** | A description of the group. | 
**admin_owner_id** | **UUID** | The ID of the owner of the group. | 
**status** | **str** | The status of the access rule. | 
**rule_clauses** | [**RuleClauses**](RuleClauses.md) |  | 

## Example

```python
from opal_security.models.update_access_rule_info import UpdateAccessRuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccessRuleInfo from a JSON string
update_access_rule_info_instance = UpdateAccessRuleInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateAccessRuleInfo.to_json())

# convert the object into a dict
update_access_rule_info_dict = update_access_rule_info_instance.to_dict()
# create an instance of UpdateAccessRuleInfo from a dict
update_access_rule_info_from_dict = UpdateAccessRuleInfo.from_dict(update_access_rule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


