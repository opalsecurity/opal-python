# OpalAccessPathDetail

A single access path within an ACCESS result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[UUID]** | Entity IDs along the path from principal to entitlement. | 
**expiration** | **datetime** | This path&#39;s expiration, if any. | [optional] 

## Example

```python
from opal_security.models.opal_access_path_detail import OpalAccessPathDetail

# TODO update the JSON string below
json = "{}"
# create an instance of OpalAccessPathDetail from a JSON string
opal_access_path_detail_instance = OpalAccessPathDetail.from_json(json)
# print the JSON string representation of the object
print(OpalAccessPathDetail.to_json())

# convert the object into a dict
opal_access_path_detail_dict = opal_access_path_detail_instance.to_dict()
# create an instance of OpalAccessPathDetail from a dict
opal_access_path_detail_from_dict = OpalAccessPathDetail.from_dict(opal_access_path_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


