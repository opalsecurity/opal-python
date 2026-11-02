# PaginatedCampaignItemsList

A paginated list of campaign items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[CampaignItem]**](CampaignItem.md) |  | 
**total_count** | **int** | Total number of items matching the filter (across all pages). | 

## Example

```python
from opal_security.models.paginated_campaign_items_list import PaginatedCampaignItemsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCampaignItemsList from a JSON string
paginated_campaign_items_list_instance = PaginatedCampaignItemsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCampaignItemsList.to_json())

# convert the object into a dict
paginated_campaign_items_list_dict = paginated_campaign_items_list_instance.to_dict()
# create an instance of PaginatedCampaignItemsList from a dict
paginated_campaign_items_list_from_dict = PaginatedCampaignItemsList.from_dict(paginated_campaign_items_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


