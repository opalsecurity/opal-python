# OpalAccessPathResultNode

A matched access path from an ACCESS_PATH OpalQuery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_id** | **UUID** | The principal entity ID. | 
**entitlement_id** | **UUID** | The entitlement entity ID. | 
**access_level_remote_id** | **str** | Remote ID of the terminal access level. | [optional] 
**access_level_name** | **str** | Display name of the terminal access level. | [optional] 
**expiration** | **datetime** | Expiration of the terminal access, if any. | [optional] 
**depth** | **int** | Number of hops from principal to entitlement (path length - 1). | 
**path** | **List[UUID]** | Entity IDs along the path from principal to entitlement. | 

## Example

```python
from opal_security.models.opal_access_path_result_node import OpalAccessPathResultNode

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessPathResultNode from a JSON string
opal_access_path_result_node_instance = OpalAccessPathResultNode.from_json(json)
# print the JSON string representation of the object
print(OpalAccessPathResultNode.to_json())

# convert the object into a dict
opal_access_path_result_node_dict = opal_access_path_result_node_instance.to_dict()
# create an instance of OpalAccessPathResultNode from a dict
opal_access_path_result_node_from_dict = OpalAccessPathResultNode.from_dict(opal_access_path_result_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


