# OpalAccessResultNode

A matched access grant from an ACCESS OpalQuery — one per (principal, entitlement, access level), with every access path as metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_id** | **UUID** | The principal entity ID. | 
**entitlement_id** | **UUID** | The entitlement entity ID. | 
**access_level_remote_id** | **str** | Remote ID of the access level. | [optional] 
**access_level_name** | **str** | Display name of the access level. | [optional] 
**effective_expiration** | **datetime** | The expiration in effect across all paths (the latest-expiring; a permanent path wins). Null means access never expires. | [optional] 
**is_direct** | **bool** | True when any path is a direct grant. | 
**paths** | [**List[OpalAccessPathDetail]**](OpalAccessPathDetail.md) | Every access path reaching this grant. | 

## Example

```python
from opal_security.models.opal_access_result_node import OpalAccessResultNode

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessResultNode from a JSON string
opal_access_result_node_instance = OpalAccessResultNode.from_json(json)
# print the JSON string representation of the object
print(OpalAccessResultNode.to_json())

# convert the object into a dict
opal_access_result_node_dict = opal_access_result_node_instance.to_dict()
# create an instance of OpalAccessResultNode from a dict
opal_access_result_node_from_dict = OpalAccessResultNode.from_dict(opal_access_result_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


