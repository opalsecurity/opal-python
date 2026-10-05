# ReviewCampaignItemsResponse

Result of submitting campaign item review decisions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviews** | [**List[CampaignItemReviewResult]**](CampaignItemReviewResult.md) | Updated reviews in the same order as the request decisions. | 

## Example

```python
from opal_security.models.review_campaign_items_response import ReviewCampaignItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewCampaignItemsResponse from a JSON string
review_campaign_items_response_instance = ReviewCampaignItemsResponse.from_json(json)
# print the JSON string representation of the object
print(ReviewCampaignItemsResponse.to_json())

# convert the object into a dict
review_campaign_items_response_dict = review_campaign_items_response_instance.to_dict()
# create an instance of ReviewCampaignItemsResponse from a dict
review_campaign_items_response_from_dict = ReviewCampaignItemsResponse.from_dict(review_campaign_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


