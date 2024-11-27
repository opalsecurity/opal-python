# CreateRequestConfigurationInfoList

# CreateRequestConfigurationInfoList Object ### Description The `CreateRequestConfigurationInfoList` object is used as an input to the CreateRequestConfigurations API.  ### Formatting Requirements The `CreateRequestConfigurationInfoList` object must contain a list of `RequestConfiguration` objects. Exactly one default `RequestConfiguration` must be provided.  A default `RequestConfiguration` is one with a `condition` of `null` and a `priority` of `0`.  The default `RequestConfiguration` will be used when no other `RequestConfiguration` matches the request.  Only one `RequestConfiguration` may be provided for each priority, and the priorities must be contiguous.  For example, if there are two `RequestConfigurations` with priorities 0 and 2, there must be a `RequestConfiguration` with priority 1.  To use the `condition` field, the `condition` must be a valid JSON object.  The `condition` must be a JSON object with the key `group_ids` (more options may be added in the future), whose value is a list of group IDs. The `condition` will match if the user requesting access is a member of any of the groups in the list. Currently, we only support using a single group as a condition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_configurations** | [**List[RequestConfiguration]**](RequestConfiguration.md) | A list of request configurations to create. | 

## Example

```python
from opal_security.models.create_request_configuration_info_list import CreateRequestConfigurationInfoList

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestConfigurationInfoList from a JSON string
create_request_configuration_info_list_instance = CreateRequestConfigurationInfoList.from_json(json)
# print the JSON string representation of the object
print(CreateRequestConfigurationInfoList.to_json())

# convert the object into a dict
create_request_configuration_info_list_dict = create_request_configuration_info_list_instance.to_dict()
# create an instance of CreateRequestConfigurationInfoList from a dict
create_request_configuration_info_list_from_dict = CreateRequestConfigurationInfoList.from_dict(create_request_configuration_info_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


