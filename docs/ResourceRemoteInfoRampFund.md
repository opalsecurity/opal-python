# ResourceRemoteInfoRampFund

Remote info for Ramp fund.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | **str** | The ID of the Ramp fund. | 

## Example

```python
from opal_security.models.resource_remote_info_ramp_fund import ResourceRemoteInfoRampFund

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoRampFund from a JSON string
resource_remote_info_ramp_fund_instance = ResourceRemoteInfoRampFund.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoRampFund.to_json())

# convert the object into a dict
resource_remote_info_ramp_fund_dict = resource_remote_info_ramp_fund_instance.to_dict()
# create an instance of ResourceRemoteInfoRampFund from a dict
resource_remote_info_ramp_fund_from_dict = ResourceRemoteInfoRampFund.from_dict(resource_remote_info_ramp_fund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


