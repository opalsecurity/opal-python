# opal-security
The Opal API is a RESTful API that allows you to interact with the Opal Security platform programmatically.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- [Releases](https://github.com/opalsecurity/opal-python/releases/)
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://www.opal.dev/](https://www.opal.dev/)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install
We recommend installing from [PyPI](https://pypi.org) using `pip`:
```sh
pip install opal-security
```

You can also install via git:
```sh
pip install git+https://github.com/opalsecurity/opal-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/opalsecurity/opal-python.git`)

Then import the package:
```python
import opal_security as opal
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import opal_security as opal
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

from opal_security.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with opal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal.AccessRulesApi(api_client)
    access_rule_id = '1b978423-db0a-4037-a4cf-f79c60cb67b3' # str | The access rule ID (group ID) of the access rule.

    try:
        api_response = api_instance.get_access_rule(access_rule_id)
        print("The response of AccessRulesApi->get_access_rule:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccessRulesApi->get_access_rule: %s\n" % e)

```

Example with Events API:

```python
import time
import opal_security as opal
from pprint import pprint
# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with opal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opal.EventsApi(api_client)
    start_date_filter = "2021/11/01" # str | A start date filter for the events. (optional)
    end_date_filter = "2021-11-12" # str | An end date filter for the events. (optional)
    actor_filter = "29827fb8-f2dd-4e80-9576-28e31e9934ac" # str | An actor filter for the events. Supply the ID of the actor. (optional)
    object_filter = "29827fb8-f2dd-4e80-9576-28e31e9934ac" # str | An object filter for the events. Supply the ID of the object. (optional)
    event_type_filter = "29827fb8-f2dd-4e80-9576-28e31e9934ac" # str | An event type filter for the events. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    page_size = 200 # int | Number of results to return per page. Default is 200. (optional)

    try:
        api_response = api_instance.events(start_date_filter=start_date_filter, end_date_filter=end_date_filter, actor_filter=actor_filter, object_filter=object_filter, event_type_filter=event_type_filter, cursor=cursor, page_size=page_size)
        pprint(api_response.dict())
    except opal.ApiException as e:
        print("Exception when calling EventsApi->events: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.opal.dev/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccessRulesApi* | [**get_access_rule**](docs/AccessRulesApi.md#get_access_rule) | **GET** /access-rules/{access_rule_id} | 
*AccessRulesApi* | [**update_access_rule**](docs/AccessRulesApi.md#update_access_rule) | **PUT** /access-rules/{access_rule_id} | 
*AppsApi* | [**get_app**](docs/AppsApi.md#get_app) | **GET** /apps/{app_id} | 
*AppsApi* | [**get_apps**](docs/AppsApi.md#get_apps) | **GET** /apps | 
*AppsApi* | [**get_sync_errors**](docs/AppsApi.md#get_sync_errors) | **GET** /sync_errors | 
*BundlesApi* | [**add_bundle_group**](docs/BundlesApi.md#add_bundle_group) | **POST** /bundles/{bundle_id}/groups | 
*BundlesApi* | [**add_bundle_resource**](docs/BundlesApi.md#add_bundle_resource) | **POST** /bundles/{bundle_id}/resources | 
*BundlesApi* | [**create_bundle**](docs/BundlesApi.md#create_bundle) | **POST** /bundles | 
*BundlesApi* | [**delete_bundle**](docs/BundlesApi.md#delete_bundle) | **DELETE** /bundles/{bundle_id} | 
*BundlesApi* | [**get_bundle**](docs/BundlesApi.md#get_bundle) | **GET** /bundles/{bundle_id} | 
*BundlesApi* | [**get_bundle_groups**](docs/BundlesApi.md#get_bundle_groups) | **GET** /bundles/{bundle_id}/groups | 
*BundlesApi* | [**get_bundle_resources**](docs/BundlesApi.md#get_bundle_resources) | **GET** /bundles/{bundle_id}/resources | 
*BundlesApi* | [**get_bundle_visibility**](docs/BundlesApi.md#get_bundle_visibility) | **GET** /bundles/{bundle_id}/visibility | 
*BundlesApi* | [**get_bundles**](docs/BundlesApi.md#get_bundles) | **GET** /bundles | 
*BundlesApi* | [**remove_bundle_group**](docs/BundlesApi.md#remove_bundle_group) | **DELETE** /bundles/{bundle_id}/groups/{group_id} | 
*BundlesApi* | [**remove_bundle_resource**](docs/BundlesApi.md#remove_bundle_resource) | **DELETE** /bundles/{bundle_id}/resources/{resource_id} | 
*BundlesApi* | [**set_bundle_visibility**](docs/BundlesApi.md#set_bundle_visibility) | **PUT** /bundles/{bundle_id}/visibility | 
*BundlesApi* | [**update_bundle**](docs/BundlesApi.md#update_bundle) | **PUT** /bundles/{bundle_id} | 
*ConfigurationTemplatesApi* | [**create_configuration_template**](docs/ConfigurationTemplatesApi.md#create_configuration_template) | **POST** /configuration-templates | 
*ConfigurationTemplatesApi* | [**delete_configuration_template**](docs/ConfigurationTemplatesApi.md#delete_configuration_template) | **DELETE** /configuration-templates/{configuration_template_id} | 
*ConfigurationTemplatesApi* | [**get_configuration_templates**](docs/ConfigurationTemplatesApi.md#get_configuration_templates) | **GET** /configuration-templates | 
*ConfigurationTemplatesApi* | [**update_configuration_template**](docs/ConfigurationTemplatesApi.md#update_configuration_template) | **PUT** /configuration-templates | 
*EventsApi* | [**events**](docs/EventsApi.md#events) | **GET** /events | 
*GroupBindingsApi* | [**create_group_binding**](docs/GroupBindingsApi.md#create_group_binding) | **POST** /group-bindings | 
*GroupBindingsApi* | [**delete_group_binding**](docs/GroupBindingsApi.md#delete_group_binding) | **DELETE** /group-bindings/{group_binding_id} | 
*GroupBindingsApi* | [**get_group_binding**](docs/GroupBindingsApi.md#get_group_binding) | **GET** /group-bindings/{group_binding_id} | 
*GroupBindingsApi* | [**get_group_bindings**](docs/GroupBindingsApi.md#get_group_bindings) | **GET** /group-bindings | 
*GroupBindingsApi* | [**update_group_bindings**](docs/GroupBindingsApi.md#update_group_bindings) | **PUT** /group-bindings | 
*GroupsApi* | [**add_group_containing_group**](docs/GroupsApi.md#add_group_containing_group) | **POST** /groups/{group_id}/containing-groups | 
*GroupsApi* | [**add_group_resource**](docs/GroupsApi.md#add_group_resource) | **POST** /groups/{group_id}/resources/{resource_id} | 
*GroupsApi* | [**add_group_user**](docs/GroupsApi.md#add_group_user) | **POST** /groups/{group_id}/users/{user_id} | 
*GroupsApi* | [**create_group**](docs/GroupsApi.md#create_group) | **POST** /groups | 
*GroupsApi* | [**delete_group**](docs/GroupsApi.md#delete_group) | **DELETE** /groups/{group_id} | 
*GroupsApi* | [**delete_group_user**](docs/GroupsApi.md#delete_group_user) | **DELETE** /groups/{group_id}/users/{user_id} | 
*GroupsApi* | [**get_group**](docs/GroupsApi.md#get_group) | **GET** /groups/{group_id} | 
*GroupsApi* | [**get_group_containing_group**](docs/GroupsApi.md#get_group_containing_group) | **GET** /groups/{group_id}/containing-groups/{containing_group_id} | 
*GroupsApi* | [**get_group_containing_groups**](docs/GroupsApi.md#get_group_containing_groups) | **GET** /groups/{group_id}/containing-groups | 
*GroupsApi* | [**get_group_message_channels**](docs/GroupsApi.md#get_group_message_channels) | **GET** /groups/{group_id}/message-channels | 
*GroupsApi* | [**get_group_on_call_schedules**](docs/GroupsApi.md#get_group_on_call_schedules) | **GET** /groups/{group_id}/on-call-schedules | 
*GroupsApi* | [**get_group_resources**](docs/GroupsApi.md#get_group_resources) | **GET** /groups/{group_id}/resources | 
*GroupsApi* | [**get_group_reviewer_stages**](docs/GroupsApi.md#get_group_reviewer_stages) | **GET** /groups/{group_id}/reviewer-stages | 
*GroupsApi* | [**get_group_reviewers**](docs/GroupsApi.md#get_group_reviewers) | **GET** /groups/{group_id}/reviewers | 
*GroupsApi* | [**get_group_tags**](docs/GroupsApi.md#get_group_tags) | **GET** /groups/{group_id}/tags | 
*GroupsApi* | [**get_group_users**](docs/GroupsApi.md#get_group_users) | **GET** /groups/{group_id}/users | 
*GroupsApi* | [**get_group_visibility**](docs/GroupsApi.md#get_group_visibility) | **GET** /groups/{group_id}/visibility | 
*GroupsApi* | [**get_groups**](docs/GroupsApi.md#get_groups) | **GET** /groups | 
*GroupsApi* | [**remove_group_containing_group**](docs/GroupsApi.md#remove_group_containing_group) | **DELETE** /groups/{group_id}/containing-groups/{containing_group_id} | 
*GroupsApi* | [**set_group_message_channels**](docs/GroupsApi.md#set_group_message_channels) | **PUT** /groups/{group_id}/message-channels | 
*GroupsApi* | [**set_group_on_call_schedules**](docs/GroupsApi.md#set_group_on_call_schedules) | **PUT** /groups/{group_id}/on-call-schedules | 
*GroupsApi* | [**set_group_resources**](docs/GroupsApi.md#set_group_resources) | **PUT** /groups/{group_id}/resources | 
*GroupsApi* | [**set_group_reviewer_stages**](docs/GroupsApi.md#set_group_reviewer_stages) | **PUT** /groups/{group_id}/reviewer-stages | 
*GroupsApi* | [**set_group_reviewers**](docs/GroupsApi.md#set_group_reviewers) | **PUT** /groups/{group_id}/reviewers | 
*GroupsApi* | [**set_group_visibility**](docs/GroupsApi.md#set_group_visibility) | **PUT** /groups/{group_id}/visibility | 
*GroupsApi* | [**update_groups**](docs/GroupsApi.md#update_groups) | **PUT** /groups | 
*IdpGroupMappingsApi* | [**delete_idp_group_mappings**](docs/IdpGroupMappingsApi.md#delete_idp_group_mappings) | **DELETE** /idp-group-mappings/{app_resource_id}/{group_id}/ | 
*IdpGroupMappingsApi* | [**get_idp_group_mappings**](docs/IdpGroupMappingsApi.md#get_idp_group_mappings) | **GET** /idp-group-mappings/{app_resource_id} | 
*IdpGroupMappingsApi* | [**update_idp_group_mappings**](docs/IdpGroupMappingsApi.md#update_idp_group_mappings) | **PUT** /idp-group-mappings/{app_resource_id} | 
*MessageChannelsApi* | [**create_message_channel**](docs/MessageChannelsApi.md#create_message_channel) | **POST** /message-channels | 
*MessageChannelsApi* | [**get_message_channel**](docs/MessageChannelsApi.md#get_message_channel) | **GET** /message-channels/{message_channel_id} | 
*MessageChannelsApi* | [**get_message_channels**](docs/MessageChannelsApi.md#get_message_channels) | **GET** /message-channels | 
*NonHumanIdentitiesApi* | [**get_nhis**](docs/NonHumanIdentitiesApi.md#get_nhis) | **GET** /non-human-identities | 
*OnCallSchedulesApi* | [**create_on_call_schedule**](docs/OnCallSchedulesApi.md#create_on_call_schedule) | **POST** /on-call-schedules | 
*OnCallSchedulesApi* | [**get_on_call_schedule**](docs/OnCallSchedulesApi.md#get_on_call_schedule) | **GET** /on-call-schedules/{on_call_schedule_id} | 
*OnCallSchedulesApi* | [**get_on_call_schedules**](docs/OnCallSchedulesApi.md#get_on_call_schedules) | **GET** /on-call-schedules | 
*OwnersApi* | [**create_owner**](docs/OwnersApi.md#create_owner) | **POST** /owners | 
*OwnersApi* | [**delete_owner**](docs/OwnersApi.md#delete_owner) | **DELETE** /owners/{owner_id} | 
*OwnersApi* | [**get_owner**](docs/OwnersApi.md#get_owner) | **GET** /owners/{owner_id} | 
*OwnersApi* | [**get_owner_from_name**](docs/OwnersApi.md#get_owner_from_name) | **GET** /owners/name/{owner_name} | 
*OwnersApi* | [**get_owner_users**](docs/OwnersApi.md#get_owner_users) | **GET** /owners/{owner_id}/users | 
*OwnersApi* | [**get_owners**](docs/OwnersApi.md#get_owners) | **GET** /owners | 
*OwnersApi* | [**set_owner_users**](docs/OwnersApi.md#set_owner_users) | **PUT** /owners/{owner_id}/users | 
*OwnersApi* | [**update_owners**](docs/OwnersApi.md#update_owners) | **PUT** /owners | 
*RequestsApi* | [**create_request**](docs/RequestsApi.md#create_request) | **POST** /requests | 
*RequestsApi* | [**get_requests**](docs/RequestsApi.md#get_requests) | **GET** /requests | 
*ResourcesApi* | [**add_resource_nhi**](docs/ResourcesApi.md#add_resource_nhi) | **POST** /resources/{resource_id}/non-human-identities/{non_human_identity_id} | 
*ResourcesApi* | [**add_resource_user**](docs/ResourcesApi.md#add_resource_user) | **POST** /resources/{resource_id}/users/{user_id} | 
*ResourcesApi* | [**create_resource**](docs/ResourcesApi.md#create_resource) | **POST** /resources | 
*ResourcesApi* | [**delete_resource**](docs/ResourcesApi.md#delete_resource) | **DELETE** /resources/{resource_id} | 
*ResourcesApi* | [**delete_resource_nhi**](docs/ResourcesApi.md#delete_resource_nhi) | **DELETE** /resources/{resource_id}/non-human-identities/{non_human_identity_id} | 
*ResourcesApi* | [**delete_resource_user**](docs/ResourcesApi.md#delete_resource_user) | **DELETE** /resources/{resource_id}/users/{user_id} | 
*ResourcesApi* | [**get_resource**](docs/ResourcesApi.md#get_resource) | **GET** /resources/{resource_id} | 
*ResourcesApi* | [**get_resource_message_channels**](docs/ResourcesApi.md#get_resource_message_channels) | **GET** /resources/{resource_id}/message-channels | 
*ResourcesApi* | [**get_resource_nhis**](docs/ResourcesApi.md#get_resource_nhis) | **GET** /resources/{resource_id}/non-human-identities | 
*ResourcesApi* | [**get_resource_reviewer_stages**](docs/ResourcesApi.md#get_resource_reviewer_stages) | **GET** /resources/{resource_id}/reviewer-stages | 
*ResourcesApi* | [**get_resource_reviewers**](docs/ResourcesApi.md#get_resource_reviewers) | **GET** /resources/{resource_id}/reviewers | 
*ResourcesApi* | [**get_resource_tags**](docs/ResourcesApi.md#get_resource_tags) | **GET** /resources/{resource_id}/tags | 
*ResourcesApi* | [**get_resource_users**](docs/ResourcesApi.md#get_resource_users) | **GET** /resources/{resource_id}/users | 
*ResourcesApi* | [**get_resource_visibility**](docs/ResourcesApi.md#get_resource_visibility) | **GET** /resources/{resource_id}/visibility | 
*ResourcesApi* | [**get_resources**](docs/ResourcesApi.md#get_resources) | **GET** /resources | 
*ResourcesApi* | [**resource_user_access_status_retrieve**](docs/ResourcesApi.md#resource_user_access_status_retrieve) | **GET** /resource-user-access-status/{resource_id}/{user_id} | 
*ResourcesApi* | [**set_resource_message_channels**](docs/ResourcesApi.md#set_resource_message_channels) | **PUT** /resources/{resource_id}/message-channels | 
*ResourcesApi* | [**set_resource_reviewer_stages**](docs/ResourcesApi.md#set_resource_reviewer_stages) | **PUT** /resources/{resource_id}/reviewer-stages | 
*ResourcesApi* | [**set_resource_reviewers**](docs/ResourcesApi.md#set_resource_reviewers) | **PUT** /resources/{resource_id}/reviewers | 
*ResourcesApi* | [**set_resource_visibility**](docs/ResourcesApi.md#set_resource_visibility) | **PUT** /resources/{resource_id}/visibility | 
*ResourcesApi* | [**update_resource_user**](docs/ResourcesApi.md#update_resource_user) | **PUT** /resources/{resource_id}/users/{user_id} | 
*ResourcesApi* | [**update_resources**](docs/ResourcesApi.md#update_resources) | **PUT** /resources | 
*SessionsApi* | [**sessions**](docs/SessionsApi.md#sessions) | **GET** /sessions | 
*TagsApi* | [**add_group_tag**](docs/TagsApi.md#add_group_tag) | **POST** /tags/{tag_id}/groups/{group_id} | 
*TagsApi* | [**add_resource_tag**](docs/TagsApi.md#add_resource_tag) | **POST** /tags/{tag_id}/resources/{resource_id} | 
*TagsApi* | [**add_user_tag**](docs/TagsApi.md#add_user_tag) | **POST** /tags/{tag_id}/users/{user_id} | 
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /tag | 
*TagsApi* | [**delete_tag_by_id**](docs/TagsApi.md#delete_tag_by_id) | **DELETE** /tag/{tag_id} | 
*TagsApi* | [**get_tag**](docs/TagsApi.md#get_tag) | **GET** /tag | 
*TagsApi* | [**get_tag_by_id**](docs/TagsApi.md#get_tag_by_id) | **GET** /tag/{tag_id} | 
*TagsApi* | [**get_tags**](docs/TagsApi.md#get_tags) | **GET** /tags | 
*TagsApi* | [**remove_group_tag**](docs/TagsApi.md#remove_group_tag) | **DELETE** /tags/{tag_id}/groups/{group_id} | 
*TagsApi* | [**remove_resource_tag**](docs/TagsApi.md#remove_resource_tag) | **DELETE** /tags/{tag_id}/resources/{resource_id} | 
*TagsApi* | [**remove_user_tag**](docs/TagsApi.md#remove_user_tag) | **DELETE** /tags/{tag_id}/users/{user_id} | 
*UarsApi* | [**create_uar**](docs/UarsApi.md#create_uar) | **POST** /uar | 
*UarsApi* | [**get_uar**](docs/UarsApi.md#get_uar) | **GET** /uar/{uar_id} | 
*UarsApi* | [**get_uars**](docs/UarsApi.md#get_uars) | **GET** /uars | 
*UsersApi* | [**get_user_tags**](docs/UsersApi.md#get_user_tags) | **GET** /users/{user_id}/tags | 
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users | 
*UsersApi* | [**user**](docs/UsersApi.md#user) | **GET** /user | 


## Documentation For Models

 - [Access](docs/Access.md)
 - [AccessList](docs/AccessList.md)
 - [AccessRuleCondition](docs/AccessRuleCondition.md)
 - [AddBundleGroupRequest](docs/AddBundleGroupRequest.md)
 - [AddBundleResourceRequest](docs/AddBundleResourceRequest.md)
 - [AddGroupResourceRequest](docs/AddGroupResourceRequest.md)
 - [AddGroupUserRequest](docs/AddGroupUserRequest.md)
 - [AddResourceNhiRequest](docs/AddResourceNhiRequest.md)
 - [AddResourceUserRequest](docs/AddResourceUserRequest.md)
 - [App](docs/App.md)
 - [AppTypeEnum](docs/AppTypeEnum.md)
 - [AppValidation](docs/AppValidation.md)
 - [AppValidationSeverityEnum](docs/AppValidationSeverityEnum.md)
 - [AppValidationStatusEnum](docs/AppValidationStatusEnum.md)
 - [AppsList](docs/AppsList.md)
 - [AwsPermissionSetMetadata](docs/AwsPermissionSetMetadata.md)
 - [AwsPermissionSetMetadataAwsPermissionSet](docs/AwsPermissionSetMetadataAwsPermissionSet.md)
 - [Bundle](docs/Bundle.md)
 - [BundleGroup](docs/BundleGroup.md)
 - [BundleResource](docs/BundleResource.md)
 - [Condition](docs/Condition.md)
 - [ConfigurationTemplate](docs/ConfigurationTemplate.md)
 - [CreateBundleInfo](docs/CreateBundleInfo.md)
 - [CreateConfigurationTemplateInfo](docs/CreateConfigurationTemplateInfo.md)
 - [CreateGroupBindingInfo](docs/CreateGroupBindingInfo.md)
 - [CreateGroupBindingInfoGroupsInner](docs/CreateGroupBindingInfoGroupsInner.md)
 - [CreateGroupInfo](docs/CreateGroupInfo.md)
 - [CreateMessageChannelInfo](docs/CreateMessageChannelInfo.md)
 - [CreateOnCallScheduleInfo](docs/CreateOnCallScheduleInfo.md)
 - [CreateOwnerInfo](docs/CreateOwnerInfo.md)
 - [CreateRequest200Response](docs/CreateRequest200Response.md)
 - [CreateRequestConfigurationInfoList](docs/CreateRequestConfigurationInfoList.md)
 - [CreateRequestInfo](docs/CreateRequestInfo.md)
 - [CreateRequestInfoCustomMetadataInner](docs/CreateRequestInfoCustomMetadataInner.md)
 - [CreateRequestInfoGroupsInner](docs/CreateRequestInfoGroupsInner.md)
 - [CreateRequestInfoResourcesInner](docs/CreateRequestInfoResourcesInner.md)
 - [CreateRequestInfoSupportTicket](docs/CreateRequestInfoSupportTicket.md)
 - [CreateResourceInfo](docs/CreateResourceInfo.md)
 - [CreateTagInfo](docs/CreateTagInfo.md)
 - [CreateUARInfo](docs/CreateUARInfo.md)
 - [EntityTypeEnum](docs/EntityTypeEnum.md)
 - [Event](docs/Event.md)
 - [Group](docs/Group.md)
 - [GroupAccessLevel](docs/GroupAccessLevel.md)
 - [GroupBinding](docs/GroupBinding.md)
 - [GroupBindingGroup](docs/GroupBindingGroup.md)
 - [GroupContainingGroup](docs/GroupContainingGroup.md)
 - [GroupContainingGroupList](docs/GroupContainingGroupList.md)
 - [GroupRemoteInfo](docs/GroupRemoteInfo.md)
 - [GroupRemoteInfoActiveDirectoryGroup](docs/GroupRemoteInfoActiveDirectoryGroup.md)
 - [GroupRemoteInfoAzureAdMicrosoft365Group](docs/GroupRemoteInfoAzureAdMicrosoft365Group.md)
 - [GroupRemoteInfoAzureAdSecurityGroup](docs/GroupRemoteInfoAzureAdSecurityGroup.md)
 - [GroupRemoteInfoDuoGroup](docs/GroupRemoteInfoDuoGroup.md)
 - [GroupRemoteInfoGithubTeam](docs/GroupRemoteInfoGithubTeam.md)
 - [GroupRemoteInfoGitlabGroup](docs/GroupRemoteInfoGitlabGroup.md)
 - [GroupRemoteInfoGoogleGroup](docs/GroupRemoteInfoGoogleGroup.md)
 - [GroupRemoteInfoLdapGroup](docs/GroupRemoteInfoLdapGroup.md)
 - [GroupRemoteInfoOktaGroup](docs/GroupRemoteInfoOktaGroup.md)
 - [GroupRemoteInfoSnowflakeRole](docs/GroupRemoteInfoSnowflakeRole.md)
 - [GroupResource](docs/GroupResource.md)
 - [GroupResourceList](docs/GroupResourceList.md)
 - [GroupTypeEnum](docs/GroupTypeEnum.md)
 - [GroupUser](docs/GroupUser.md)
 - [GroupUserList](docs/GroupUserList.md)
 - [GroupWithAccessLevel](docs/GroupWithAccessLevel.md)
 - [IdpGroupMapping](docs/IdpGroupMapping.md)
 - [IdpGroupMappingList](docs/IdpGroupMappingList.md)
 - [MessageChannel](docs/MessageChannel.md)
 - [MessageChannelIDList](docs/MessageChannelIDList.md)
 - [MessageChannelList](docs/MessageChannelList.md)
 - [MessageChannelProviderEnum](docs/MessageChannelProviderEnum.md)
 - [OnCallSchedule](docs/OnCallSchedule.md)
 - [OnCallScheduleIDList](docs/OnCallScheduleIDList.md)
 - [OnCallScheduleList](docs/OnCallScheduleList.md)
 - [OnCallScheduleProviderEnum](docs/OnCallScheduleProviderEnum.md)
 - [Owner](docs/Owner.md)
 - [PaginatedBundleGroupList](docs/PaginatedBundleGroupList.md)
 - [PaginatedBundleList](docs/PaginatedBundleList.md)
 - [PaginatedBundleResourceList](docs/PaginatedBundleResourceList.md)
 - [PaginatedConfigurationTemplateList](docs/PaginatedConfigurationTemplateList.md)
 - [PaginatedEventList](docs/PaginatedEventList.md)
 - [PaginatedGroupBindingsList](docs/PaginatedGroupBindingsList.md)
 - [PaginatedGroupsList](docs/PaginatedGroupsList.md)
 - [PaginatedOwnersList](docs/PaginatedOwnersList.md)
 - [PaginatedResourcesList](docs/PaginatedResourcesList.md)
 - [PaginatedTagsList](docs/PaginatedTagsList.md)
 - [PaginatedUARsList](docs/PaginatedUARsList.md)
 - [PaginatedUsersList](docs/PaginatedUsersList.md)
 - [PropagationStatus](docs/PropagationStatus.md)
 - [PropagationStatusEnum](docs/PropagationStatusEnum.md)
 - [Request](docs/Request.md)
 - [RequestConfiguration](docs/RequestConfiguration.md)
 - [RequestCustomFieldResponse](docs/RequestCustomFieldResponse.md)
 - [RequestCustomFieldResponseFieldValue](docs/RequestCustomFieldResponseFieldValue.md)
 - [RequestList](docs/RequestList.md)
 - [RequestStatusEnum](docs/RequestStatusEnum.md)
 - [RequestTemplateCustomFieldTypeEnum](docs/RequestTemplateCustomFieldTypeEnum.md)
 - [RequestedItem](docs/RequestedItem.md)
 - [Resource](docs/Resource.md)
 - [ResourceAccessLevel](docs/ResourceAccessLevel.md)
 - [ResourceAccessUser](docs/ResourceAccessUser.md)
 - [ResourceAccessUserList](docs/ResourceAccessUserList.md)
 - [ResourceNHI](docs/ResourceNHI.md)
 - [ResourceRemoteInfo](docs/ResourceRemoteInfo.md)
 - [ResourceRemoteInfoAwsAccount](docs/ResourceRemoteInfoAwsAccount.md)
 - [ResourceRemoteInfoAwsEc2Instance](docs/ResourceRemoteInfoAwsEc2Instance.md)
 - [ResourceRemoteInfoAwsEksCluster](docs/ResourceRemoteInfoAwsEksCluster.md)
 - [ResourceRemoteInfoAwsIamRole](docs/ResourceRemoteInfoAwsIamRole.md)
 - [ResourceRemoteInfoAwsPermissionSet](docs/ResourceRemoteInfoAwsPermissionSet.md)
 - [ResourceRemoteInfoAwsRdsInstance](docs/ResourceRemoteInfoAwsRdsInstance.md)
 - [ResourceRemoteInfoGcpBigQueryDataset](docs/ResourceRemoteInfoGcpBigQueryDataset.md)
 - [ResourceRemoteInfoGcpBigQueryTable](docs/ResourceRemoteInfoGcpBigQueryTable.md)
 - [ResourceRemoteInfoGcpBucket](docs/ResourceRemoteInfoGcpBucket.md)
 - [ResourceRemoteInfoGcpComputeInstance](docs/ResourceRemoteInfoGcpComputeInstance.md)
 - [ResourceRemoteInfoGcpFolder](docs/ResourceRemoteInfoGcpFolder.md)
 - [ResourceRemoteInfoGcpGkeCluster](docs/ResourceRemoteInfoGcpGkeCluster.md)
 - [ResourceRemoteInfoGcpOrganization](docs/ResourceRemoteInfoGcpOrganization.md)
 - [ResourceRemoteInfoGcpProject](docs/ResourceRemoteInfoGcpProject.md)
 - [ResourceRemoteInfoGcpServiceAccount](docs/ResourceRemoteInfoGcpServiceAccount.md)
 - [ResourceRemoteInfoGcpSqlInstance](docs/ResourceRemoteInfoGcpSqlInstance.md)
 - [ResourceRemoteInfoGithubRepo](docs/ResourceRemoteInfoGithubRepo.md)
 - [ResourceRemoteInfoGitlabProject](docs/ResourceRemoteInfoGitlabProject.md)
 - [ResourceRemoteInfoOktaApp](docs/ResourceRemoteInfoOktaApp.md)
 - [ResourceRemoteInfoOktaCustomRole](docs/ResourceRemoteInfoOktaCustomRole.md)
 - [ResourceRemoteInfoOktaStandardRole](docs/ResourceRemoteInfoOktaStandardRole.md)
 - [ResourceRemoteInfoPagerdutyRole](docs/ResourceRemoteInfoPagerdutyRole.md)
 - [ResourceRemoteInfoSalesforcePermissionSet](docs/ResourceRemoteInfoSalesforcePermissionSet.md)
 - [ResourceRemoteInfoSalesforceProfile](docs/ResourceRemoteInfoSalesforceProfile.md)
 - [ResourceRemoteInfoSalesforceRole](docs/ResourceRemoteInfoSalesforceRole.md)
 - [ResourceRemoteInfoTeleportRole](docs/ResourceRemoteInfoTeleportRole.md)
 - [ResourceTypeEnum](docs/ResourceTypeEnum.md)
 - [ResourceUser](docs/ResourceUser.md)
 - [ResourceUserAccessStatus](docs/ResourceUserAccessStatus.md)
 - [ResourceUserAccessStatusEnum](docs/ResourceUserAccessStatusEnum.md)
 - [ResourceWithAccessLevel](docs/ResourceWithAccessLevel.md)
 - [ReviewerIDList](docs/ReviewerIDList.md)
 - [ReviewerStage](docs/ReviewerStage.md)
 - [ReviewerStageList](docs/ReviewerStageList.md)
 - [RiskSensitivityEnum](docs/RiskSensitivityEnum.md)
 - [RuleClauses](docs/RuleClauses.md)
 - [RuleConjunction](docs/RuleConjunction.md)
 - [RuleDisjunction](docs/RuleDisjunction.md)
 - [Session](docs/Session.md)
 - [SessionsList](docs/SessionsList.md)
 - [SubEvent](docs/SubEvent.md)
 - [SyncError](docs/SyncError.md)
 - [SyncErrorList](docs/SyncErrorList.md)
 - [Tag](docs/Tag.md)
 - [TagFilter](docs/TagFilter.md)
 - [TagSelector](docs/TagSelector.md)
 - [TagsList](docs/TagsList.md)
 - [TicketPropagationConfiguration](docs/TicketPropagationConfiguration.md)
 - [TicketingProviderEnum](docs/TicketingProviderEnum.md)
 - [UAR](docs/UAR.md)
 - [UARReviewerAssignmentPolicyEnum](docs/UARReviewerAssignmentPolicyEnum.md)
 - [UARScope](docs/UARScope.md)
 - [UpdateConfigurationTemplateInfo](docs/UpdateConfigurationTemplateInfo.md)
 - [UpdateGroupBindingInfo](docs/UpdateGroupBindingInfo.md)
 - [UpdateGroupBindingInfoList](docs/UpdateGroupBindingInfoList.md)
 - [UpdateGroupInfo](docs/UpdateGroupInfo.md)
 - [UpdateGroupInfoList](docs/UpdateGroupInfoList.md)
 - [UpdateGroupResourcesInfo](docs/UpdateGroupResourcesInfo.md)
 - [UpdateIdpGroupMappingsRequest](docs/UpdateIdpGroupMappingsRequest.md)
 - [UpdateIdpGroupMappingsRequestMappingsInner](docs/UpdateIdpGroupMappingsRequestMappingsInner.md)
 - [UpdateOwnerInfo](docs/UpdateOwnerInfo.md)
 - [UpdateOwnerInfoList](docs/UpdateOwnerInfoList.md)
 - [UpdateResourceInfo](docs/UpdateResourceInfo.md)
 - [UpdateResourceInfoList](docs/UpdateResourceInfoList.md)
 - [UpdateResourceUserRequest](docs/UpdateResourceUserRequest.md)
 - [User](docs/User.md)
 - [UserHrIdpStatusEnum](docs/UserHrIdpStatusEnum.md)
 - [UserIDList](docs/UserIDList.md)
 - [UserList](docs/UserList.md)
 - [VisibilityInfo](docs/VisibilityInfo.md)
 - [VisibilityTypeEnum](docs/VisibilityTypeEnum.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication


## Author

hello@opal.dev


