# PaginatedCampaignsList

A list of campaigns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | The cursor with which to continue pagination if additional result pages exist. | [optional] 
**previous** | **str** | The cursor used to obtain the current result page. | [optional] 
**results** | [**List[Campaign]**](Campaign.md) |  | 

## Example

```python
from opal_security.models.paginated_campaigns_list import PaginatedCampaignsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCampaignsList from a JSON string
paginated_campaigns_list_instance = PaginatedCampaignsList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCampaignsList.to_json())

# convert the object into a dict
paginated_campaigns_list_dict = paginated_campaigns_list_instance.to_dict()
# create an instance of PaginatedCampaignsList from a dict
paginated_campaigns_list_from_dict = PaginatedCampaignsList.from_dict(paginated_campaigns_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


