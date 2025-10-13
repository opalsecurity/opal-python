# DenyRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment for the denial | 

## Example

```python
from opal_security.models.deny_request_request import DenyRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DenyRequestRequest from a JSON string
deny_request_request_instance = DenyRequestRequest.from_json(json)
# print the JSON string representation of the object
print(DenyRequestRequest.to_json())

# convert the object into a dict
deny_request_request_dict = deny_request_request_instance.to_dict()
# create an instance of DenyRequestRequest from a dict
deny_request_request_from_dict = DenyRequestRequest.from_dict(deny_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


