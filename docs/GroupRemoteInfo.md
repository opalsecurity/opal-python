# GroupRemoteInfo

Information that defines the remote group. This replaces the deprecated remote_id and metadata fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_directory_group** | [**GroupRemoteInfoActiveDirectoryGroup**](GroupRemoteInfoActiveDirectoryGroup.md) |  | [optional] 
**github_team** | [**GroupRemoteInfoGithubTeam**](GroupRemoteInfoGithubTeam.md) |  | [optional] 
**gitlab_group** | [**GroupRemoteInfoGitlabGroup**](GroupRemoteInfoGitlabGroup.md) |  | [optional] 
**google_group** | [**GroupRemoteInfoGoogleGroup**](GroupRemoteInfoGoogleGroup.md) |  | [optional] 
**ldap_group** | [**GroupRemoteInfoLdapGroup**](GroupRemoteInfoLdapGroup.md) |  | [optional] 
**okta_group** | [**GroupRemoteInfoOktaGroup**](GroupRemoteInfoOktaGroup.md) |  | [optional] 
**duo_group** | [**GroupRemoteInfoDuoGroup**](GroupRemoteInfoDuoGroup.md) |  | [optional] 
**azure_ad_security_group** | [**GroupRemoteInfoAzureAdSecurityGroup**](GroupRemoteInfoAzureAdSecurityGroup.md) |  | [optional] 
**azure_ad_microsoft_365_group** | [**GroupRemoteInfoAzureAdMicrosoft365Group**](GroupRemoteInfoAzureAdMicrosoft365Group.md) |  | [optional] 

## Example

```python
from opal_security.models.group_remote_info import GroupRemoteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRemoteInfo from a JSON string
group_remote_info_instance = GroupRemoteInfo.from_json(json)
# print the JSON string representation of the object
print(GroupRemoteInfo.to_json())

# convert the object into a dict
group_remote_info_dict = group_remote_info_instance.to_dict()
# create an instance of GroupRemoteInfo from a dict
group_remote_info_from_dict = GroupRemoteInfo.from_dict(group_remote_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


