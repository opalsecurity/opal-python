# ResourceRemoteInfoGcpBigQueryTable

Remote info for GCP BigQuery Table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The id of the project the table is in. | 
**dataset_id** | **str** | The id of the dataset the table is in. | 
**table_id** | **str** | The id of the table. | 

## Example

```python
from opal_security.models.resource_remote_info_gcp_big_query_table import ResourceRemoteInfoGcpBigQueryTable

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGcpBigQueryTable from a JSON string
resource_remote_info_gcp_big_query_table_instance = ResourceRemoteInfoGcpBigQueryTable.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGcpBigQueryTable.to_json())

# convert the object into a dict
resource_remote_info_gcp_big_query_table_dict = resource_remote_info_gcp_big_query_table_instance.to_dict()
# create an instance of ResourceRemoteInfoGcpBigQueryTable from a dict
resource_remote_info_gcp_big_query_table_from_dict = ResourceRemoteInfoGcpBigQueryTable.from_dict(resource_remote_info_gcp_big_query_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


