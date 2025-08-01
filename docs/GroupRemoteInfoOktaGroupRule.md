# GroupRemoteInfoOktaGroupRule

Remote info for Okta Directory group rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The id of the Okta group rule. | 

## Example

```python
from opal_security.models.group_remote_info_okta_group_rule import GroupRemoteInfoOktaGroupRule

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfoOktaGroupRule from a JSON string
group_remote_info_okta_group_rule_instance = GroupRemoteInfoOktaGroupRule.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfoOktaGroupRule.to_json())

# convert the object into a dict
group_remote_info_okta_group_rule_dict = group_remote_info_okta_group_rule_instance.to_dict()
# create an instance of GroupRemoteInfoOktaGroupRule from a dict
group_remote_info_okta_group_rule_from_dict = GroupRemoteInfoOktaGroupRule.from_dict(group_remote_info_okta_group_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


