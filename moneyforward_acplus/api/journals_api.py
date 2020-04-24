# coding: utf-8

"""
    マネーフォワードクラウド会計Plus API

    マネーフォワードクラウド会計PlusのAPI  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: api.acplus.support@moneyforward.co.jp
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from moneyforward_acplus.api_client import ApiClient
from moneyforward_acplus.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class JournalsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_journal_file(self, create_journal_file_request, **kwargs):  # noqa: E501
        """仕訳帳作成要求  # noqa: E501

        仕訳帳作成をリクエストします。仕訳帳はリクエスト受付後に非同期で作成されます。仕訳帳の作成状況の確認や作成結果の取得は受付成功時に返却される作成要求IDを指定して仕訳帳作成状況取得APIや仕訳帳ダウンロードAPIを呼び出します。開始日と終了日に含まれる会計期は1つである必要があります。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_journal_file(create_journal_file_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateJournalFileRequest create_journal_file_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CreateJournalFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_journal_file_with_http_info(create_journal_file_request, **kwargs)  # noqa: E501

    def create_journal_file_with_http_info(self, create_journal_file_request, **kwargs):  # noqa: E501
        """仕訳帳作成要求  # noqa: E501

        仕訳帳作成をリクエストします。仕訳帳はリクエスト受付後に非同期で作成されます。仕訳帳の作成状況の確認や作成結果の取得は受付成功時に返却される作成要求IDを指定して仕訳帳作成状況取得APIや仕訳帳ダウンロードAPIを呼び出します。開始日と終了日に含まれる会計期は1つである必要があります。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_journal_file_with_http_info(create_journal_file_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreateJournalFileRequest create_journal_file_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CreateJournalFileResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'create_journal_file_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_journal_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_journal_file_request' is set
        if self.api_client.client_side_validation and ('create_journal_file_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_journal_file_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_journal_file_request` when calling `create_journal_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_journal_file_request' in local_var_params:
            body_params = local_var_params['create_journal_file_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/journals/files', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateJournalFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_journal_file(self, request_id, **kwargs):  # noqa: E501
        """仕訳帳削除  # noqa: E501

        作成済の仕訳帳を削除します。パラメータで指定する作成要求IDは仕訳帳作成要求APIで取得したものです。作成要求IDで指定する仕訳帳が作成中の場合は失敗します。すでに削除済の仕訳帳に対して削除を実行した場合は成功します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_journal_file(request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int request_id: 作成要求ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_journal_file_with_http_info(request_id, **kwargs)  # noqa: E501

    def delete_journal_file_with_http_info(self, request_id, **kwargs):  # noqa: E501
        """仕訳帳削除  # noqa: E501

        作成済の仕訳帳を削除します。パラメータで指定する作成要求IDは仕訳帳作成要求APIで取得したものです。作成要求IDで指定する仕訳帳が作成中の場合は失敗します。すでに削除済の仕訳帳に対して削除を実行した場合は成功します。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_journal_file_with_http_info(request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int request_id: 作成要求ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'request_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_journal_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'request_id' is set
        if self.api_client.client_side_validation and ('request_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['request_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request_id` when calling `delete_journal_file`")  # noqa: E501

        if self.api_client.client_side_validation and 'request_id' in local_var_params and local_var_params['request_id'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `request_id` when calling `delete_journal_file`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'request_id' in local_var_params:
            path_params['requestId'] = local_var_params['request_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/journals/files/{requestId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_journal_file(self, request_id, **kwargs):  # noqa: E501
        """仕訳帳ダウンロード  # noqa: E501

        仕訳帳をCSV形式でダウンロードできます。 パラメータで指定する作成要求IDは仕訳帳作成要求APIで取得したものです。文字コードは仕訳帳作成要求APIでUTF8またはShiftJISから選択できます。デフォルトはUTF8となります。作成後90日以内の仕訳帳のみダウンロード可能です。 作成中または削除済の仕訳帳はダウンロードできません。   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_journal_file(request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int request_id: 作成要求ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.download_journal_file_with_http_info(request_id, **kwargs)  # noqa: E501

    def download_journal_file_with_http_info(self, request_id, **kwargs):  # noqa: E501
        """仕訳帳ダウンロード  # noqa: E501

        仕訳帳をCSV形式でダウンロードできます。 パラメータで指定する作成要求IDは仕訳帳作成要求APIで取得したものです。文字コードは仕訳帳作成要求APIでUTF8またはShiftJISから選択できます。デフォルトはUTF8となります。作成後90日以内の仕訳帳のみダウンロード可能です。 作成中または削除済の仕訳帳はダウンロードできません。   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_journal_file_with_http_info(request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int request_id: 作成要求ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(file, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'request_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_journal_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'request_id' is set
        if self.api_client.client_side_validation and ('request_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['request_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request_id` when calling `download_journal_file`")  # noqa: E501

        if self.api_client.client_side_validation and 'request_id' in local_var_params and local_var_params['request_id'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `request_id` when calling `download_journal_file`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'request_id' in local_var_params:
            path_params['requestId'] = local_var_params['request_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/journals/files/{requestId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_journal_file_status(self, request_id, **kwargs):  # noqa: E501
        """仕訳帳作成状況取得  # noqa: E501

        仕訳帳作成状況を取得します。パラメータで指定する作成要求IDは仕訳帳作成要求APIで取得したものです。作成後90日以内の仕訳帳のみ状況を取得可能です。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_journal_file_status(request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int request_id: 作成要求ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: JournalFileStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_journal_file_status_with_http_info(request_id, **kwargs)  # noqa: E501

    def get_journal_file_status_with_http_info(self, request_id, **kwargs):  # noqa: E501
        """仕訳帳作成状況取得  # noqa: E501

        仕訳帳作成状況を取得します。パラメータで指定する作成要求IDは仕訳帳作成要求APIで取得したものです。作成後90日以内の仕訳帳のみ状況を取得可能です。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_journal_file_status_with_http_info(request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int request_id: 作成要求ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(JournalFileStatus, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'request_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_journal_file_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'request_id' is set
        if self.api_client.client_side_validation and ('request_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['request_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `request_id` when calling `get_journal_file_status`")  # noqa: E501

        if self.api_client.client_side_validation and 'request_id' in local_var_params and local_var_params['request_id'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `request_id` when calling `get_journal_file_status`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'request_id' in local_var_params:
            path_params['requestId'] = local_var_params['request_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/journals/files/{requestId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JournalFileStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_journal_file_status_list(self, **kwargs):  # noqa: E501
        """仕訳帳作成状況一覧取得  # noqa: E501

        仕訳帳作成状況の一覧を取得します。作成後90日以内の仕訳帳のみ状況を取得可能です。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_journal_file_status_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: 仕訳帳作成状況一覧の取得開始位置
        :param int limit: 仕訳帳作成状況一覧の取得件数
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[JournalFileStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_journal_file_status_list_with_http_info(**kwargs)  # noqa: E501

    def get_journal_file_status_list_with_http_info(self, **kwargs):  # noqa: E501
        """仕訳帳作成状況一覧取得  # noqa: E501

        仕訳帳作成状況の一覧を取得します。作成後90日以内の仕訳帳のみ状況を取得可能です。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_journal_file_status_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: 仕訳帳作成状況一覧の取得開始位置
        :param int limit: 仕訳帳作成状況一覧の取得件数
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[JournalFileStatus], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'offset',
            'limit'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_journal_file_status_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_journal_file_status_list`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_journal_file_status_list`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_journal_file_status_list`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/journals/files/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JournalFileStatus]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
