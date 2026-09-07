# UpdateCampaignInfo

# UpdateCampaignInfo Object ### Description The `UpdateCampaignInfo` object is used to partially update a campaign. Omitted fields are left unchanged.  ### Usage Example Use in the `PUT Campaign` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the campaign. | [optional] 
**configuration** | [**UpdateCampaignConfigurationInfo**](UpdateCampaignConfigurationInfo.md) | Configuration fields to create or update. | [optional] 

## Example

```python
from opal_security.models.update_campaign_info import UpdateCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCampaignInfo from a JSON string
update_campaign_info_instance = UpdateCampaignInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateCampaignInfo.to_json())

# convert the object into a dict
update_campaign_info_dict = update_campaign_info_instance.to_dict()
# create an instance of UpdateCampaignInfo from a dict
update_campaign_info_from_dict = UpdateCampaignInfo.from_dict(update_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


