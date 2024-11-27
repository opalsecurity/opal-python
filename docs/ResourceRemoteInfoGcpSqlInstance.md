# ResourceRemoteInfoGcpSqlInstance

Remote info for GCP SQL instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | The id of the SQL instance. | 
**project_id** | **str** | The id of the project the instance is in. | 

## Example

```python
from opal_security.models.resource_remote_info_gcp_sql_instance import ResourceRemoteInfoGcpSqlInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRemoteInfoGcpSqlInstance from a JSON string
resource_remote_info_gcp_sql_instance_instance = ResourceRemoteInfoGcpSqlInstance.from_json(json)
# print the JSON string representation of the object
print(ResourceRemoteInfoGcpSqlInstance.to_json())

# convert the object into a dict
resource_remote_info_gcp_sql_instance_dict = resource_remote_info_gcp_sql_instance_instance.to_dict()
# create an instance of ResourceRemoteInfoGcpSqlInstance from a dict
resource_remote_info_gcp_sql_instance_from_dict = ResourceRemoteInfoGcpSqlInstance.from_dict(resource_remote_info_gcp_sql_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


