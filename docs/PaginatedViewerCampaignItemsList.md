# PaginatedViewerCampaignItemsList

A paginated list of viewer campaign items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist.  | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[ViewerCampaignItem]**](ViewerCampaignItem.md) |  | 
**total_count** | **int** | Total number of items matching the filter (across all pages). | 

## Example

```python
from opal_security.models.paginated_viewer_campaign_items_list import PaginatedViewerCampaignItemsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedViewerCampaignItemsList from a JSON string
paginated_viewer_campaign_items_list_instance = PaginatedViewerCampaignItemsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedViewerCampaignItemsList.to_json())

# convert the object into a dict
paginated_viewer_campaign_items_list_dict = paginated_viewer_campaign_items_list_instance.to_dict()
# create an instance of PaginatedViewerCampaignItemsList from a dict
paginated_viewer_campaign_items_list_from_dict = PaginatedViewerCampaignItemsList.from_dict(paginated_viewer_campaign_items_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


