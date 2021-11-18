"""
    Opal API

    Your Home For Developer Resources.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@opal.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from opal.api_client import ApiClient, Endpoint as _Endpoint
from opal.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from opal.model.user import User


class UsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.user_endpoint = _Endpoint(
            settings={
                'response_type': (User,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/user',
                'operation_id': 'user',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'email',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'email':
                        (str,),
                },
                'attribute_map': {
                    'user_id': 'user_id',
                    'email': 'email',
                },
                'location_map': {
                    'user_id': 'query',
                    'email': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def user(
        self,
        **kwargs
    ):
        """user  # noqa: E501

        Returns a `User` object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            user_id (str): The user ID of the user.. [optional]
            email (str): The email of the user. If both user ID and email are provided, user ID will take precedence. If neither are provided, an error will occur.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            User
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.user_endpoint.call_with_http_info(**kwargs)
