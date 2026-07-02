# OpalQueryResultNode

A matched entity from an OpalQuery result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The entity&#39;s unique identifier. | 
**name** | **str** | The display name of the entity. | 
**entity_type** | **str** | The top-level entity type. | 
**entity_item_type** | [**EntityItemTypeEnum**](EntityItemTypeEnum.md) |  | 

## Example

```python
from opal_security.models.opal_query_result_node import OpalQueryResultNode

# TODO update the JSON string below
json = "{}"
# create an instance of OpalQueryResultNode from a JSON string
opal_query_result_node_instance = OpalQueryResultNode.from_json(json)
# print the JSON string representation of the object
print(OpalQueryResultNode.to_json())

# convert the object into a dict
opal_query_result_node_dict = opal_query_result_node_instance.to_dict()
# create an instance of OpalQueryResultNode from a dict
opal_query_result_node_from_dict = OpalQueryResultNode.from_dict(opal_query_result_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


