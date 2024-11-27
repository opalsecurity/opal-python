# ResourceRemoteInfoGcpBigQueryDataset

Remote info for GCP BigQuery Dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The id of the project the dataset is in. | 
**dataset_id** | **str** | The id of the dataset. | 

## Example

```python
from opal_security.models.resource_remote_info_gcp_big_query_dataset import ResourceRemoteInfoGcpBigQueryDataset

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGcpBigQueryDataset from a JSON string
resource_remote_info_gcp_big_query_dataset_instance = ResourceRemoteInfoGcpBigQueryDataset.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGcpBigQueryDataset.to_json())

# convert the object into a dict
resource_remote_info_gcp_big_query_dataset_dict = resource_remote_info_gcp_big_query_dataset_instance.to_dict()
# create an instance of ResourceRemoteInfoGcpBigQueryDataset from a dict
resource_remote_info_gcp_big_query_dataset_from_dict = ResourceRemoteInfoGcpBigQueryDataset.from_dict(resource_remote_info_gcp_big_query_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


