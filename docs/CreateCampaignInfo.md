# CreateCampaignInfo

# CreateCampaignInfo Object ### Description The `CreateCampaignInfo` object is used to create a campaign.  ### Usage Example Use in the `POST Campaigns` endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the campaign. | 
**configuration** | [**CreateCampaignConfigurationInfo**](CreateCampaignConfigurationInfo.md) | Configuration for the campaign. Required; must include a query. Other omitted fields use defaults. | 

## Example

```python
from opal_security.models.create_campaign_info import CreateCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCampaignInfo from a JSON string
create_campaign_info_instance = CreateCampaignInfo.from_json(json)
# print the JSON string representation of the object
print(CreateCampaignInfo.to_json())

# convert the object into a dict
create_campaign_info_dict = create_campaign_info_instance.to_dict()
# create an instance of CreateCampaignInfo from a dict
create_campaign_info_from_dict = CreateCampaignInfo.from_dict(create_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


