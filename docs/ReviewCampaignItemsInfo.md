# ReviewCampaignItemsInfo

Input for submitting review decisions on one or more campaign item reviews. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decisions** | [**List[ReviewCampaignItemDecisionInfo]**](ReviewCampaignItemDecisionInfo.md) | The decisions to record. Each targets a single campaign item review. | 

## Example

```python
from opal_security.models.review_campaign_items_info import ReviewCampaignItemsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewCampaignItemsInfo from a JSON string
review_campaign_items_info_instance = ReviewCampaignItemsInfo.from_json(json)
# print the JSON string representation of the object
print(ReviewCampaignItemsInfo.to_json())

# convert the object into a dict
review_campaign_items_info_dict = review_campaign_items_info_instance.to_dict()
# create an instance of ReviewCampaignItemsInfo from a dict
review_campaign_items_info_from_dict = ReviewCampaignItemsInfo.from_dict(review_campaign_items_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


