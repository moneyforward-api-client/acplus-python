# moneyforward_acplus.JournalsApi

All URIs are relative to *https://api-enterprise-accounting.moneyforward.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_journal_file**](JournalsApi.md#create_journal_file) | **POST** /journals/files | 仕訳帳作成要求
[**delete_journal_file**](JournalsApi.md#delete_journal_file) | **DELETE** /journals/files/{requestId} | 仕訳帳削除
[**download_journal_file**](JournalsApi.md#download_journal_file) | **GET** /journals/files/{requestId} | 仕訳帳ダウンロード
[**get_journal_file_status**](JournalsApi.md#get_journal_file_status) | **GET** /journals/files/{requestId}/status | 仕訳帳作成状況取得
[**get_journal_file_status_list**](JournalsApi.md#get_journal_file_status_list) | **GET** /journals/files/status | 仕訳帳作成状況一覧取得


# **create_journal_file**
> CreateJournalFileResponse create_journal_file(create_journal_file_request)

仕訳帳作成要求

仕訳帳作成をリクエストします。仕訳帳はリクエスト受付後に非同期で作成されます。仕訳帳の作成状況の確認や作成結果の取得は受付成功時に返却される作成要求IDを指定して仕訳帳作成状況取得APIや仕訳帳ダウンロードAPIを呼び出します。開始日と終了日に含まれる会計期は1つである必要があります。

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import moneyforward_acplus
from moneyforward_acplus.rest import ApiException
from pprint import pprint
configuration = moneyforward_acplus.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Defining host is optional and default to https://api-enterprise-accounting.moneyforward.com/api/v1
configuration.host = "https://api-enterprise-accounting.moneyforward.com/api/v1"

# Enter a context with an instance of the API client
with moneyforward_acplus.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moneyforward_acplus.JournalsApi(api_client)
    create_journal_file_request = moneyforward_acplus.CreateJournalFileRequest() # CreateJournalFileRequest |

    try:
        # 仕訳帳作成要求
        api_response = api_instance.create_journal_file(create_journal_file_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JournalsApi->create_journal_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_journal_file_request** | [**CreateJournalFileRequest**](CreateJournalFileRequest.md)|  |

### Return type

[**CreateJournalFileResponse**](CreateJournalFileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | 仕訳作成要求の受付が成功した場合 |  -  |
**400** | パラメータ不正などAPI呼び出し側理由のエラー |  -  |
**401** | APIキーが未設定または不正または失効済の場合のエラー |  -  |
**403** | アクセス権限がない場合のエラー |  -  |
**415** | 指定されたデータフォーマットに対応していない場合 |  -  |
**0** | 予期していないエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_journal_file**
> delete_journal_file(request_id)

仕訳帳削除

作成済の仕訳帳を削除します。パラメータで指定する作成要求IDは仕訳帳作成要求APIで取得したものです。作成要求IDで指定する仕訳帳が作成中の場合は失敗します。すでに削除済の仕訳帳に対して削除を実行した場合は成功します。

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import moneyforward_acplus
from moneyforward_acplus.rest import ApiException
from pprint import pprint
configuration = moneyforward_acplus.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Defining host is optional and default to https://api-enterprise-accounting.moneyforward.com/api/v1
configuration.host = "https://api-enterprise-accounting.moneyforward.com/api/v1"

# Enter a context with an instance of the API client
with moneyforward_acplus.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moneyforward_acplus.JournalsApi(api_client)
    request_id = 56 # int | 作成要求ID

    try:
        # 仕訳帳削除
        api_instance.delete_journal_file(request_id)
    except ApiException as e:
        print("Exception when calling JournalsApi->delete_journal_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**| 作成要求ID |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 仕訳帳の削除が成功した場合 |  -  |
**400** | パラメータ不正などAPI呼び出し側理由のエラー |  -  |
**401** | APIキーが未設定または不正または失効済の場合のエラー |  -  |
**403** | アクセス権限がない場合のエラー |  -  |
**404** | 指定されたリソースが存在しない場合のエラー |  -  |
**0** | 予期していないエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_journal_file**
> file download_journal_file(request_id)

仕訳帳ダウンロード

仕訳帳をCSV形式でダウンロードできます。 パラメータで指定する作成要求IDは仕訳帳作成要求APIで取得したものです。文字コードは仕訳帳作成要求APIでUTF8またはShiftJISから選択できます。デフォルトはUTF8となります。作成後90日以内の仕訳帳のみダウンロード可能です。 作成中または削除済の仕訳帳はダウンロードできません。

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import moneyforward_acplus
from moneyforward_acplus.rest import ApiException
from pprint import pprint
configuration = moneyforward_acplus.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Defining host is optional and default to https://api-enterprise-accounting.moneyforward.com/api/v1
configuration.host = "https://api-enterprise-accounting.moneyforward.com/api/v1"

# Enter a context with an instance of the API client
with moneyforward_acplus.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moneyforward_acplus.JournalsApi(api_client)
    request_id = 56 # int | 作成要求ID

    try:
        # 仕訳帳ダウンロード
        api_response = api_instance.download_journal_file(request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JournalsApi->download_journal_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**| 作成要求ID |

### Return type

**file**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 仕訳帳のダウンロードが成功した場合 |  -  |
**400** | パラメータ不正などAPI呼び出し側理由のエラー |  -  |
**401** | APIキーが未設定または不正または失効済の場合のエラー |  -  |
**403** | アクセス権限がない場合のエラー |  -  |
**404** | 指定されたリソースが存在しない場合のエラー |  -  |
**410** | 指定されたリソースにアクセスできなくなった場合のエラー |  -  |
**0** | 予期していないエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_file_status**
> JournalFileStatus get_journal_file_status(request_id)

仕訳帳作成状況取得

仕訳帳作成状況を取得します。パラメータで指定する作成要求IDは仕訳帳作成要求APIで取得したものです。作成後90日以内の仕訳帳のみ状況を取得可能です。

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import moneyforward_acplus
from moneyforward_acplus.rest import ApiException
from pprint import pprint
configuration = moneyforward_acplus.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Defining host is optional and default to https://api-enterprise-accounting.moneyforward.com/api/v1
configuration.host = "https://api-enterprise-accounting.moneyforward.com/api/v1"

# Enter a context with an instance of the API client
with moneyforward_acplus.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moneyforward_acplus.JournalsApi(api_client)
    request_id = 56 # int | 作成要求ID

    try:
        # 仕訳帳作成状況取得
        api_response = api_instance.get_journal_file_status(request_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JournalsApi->get_journal_file_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**| 作成要求ID |

### Return type

[**JournalFileStatus**](JournalFileStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 仕訳帳作成状況の取得が成功した場合 |  -  |
**400** | パラメータ不正などAPI呼び出し側理由のエラー |  -  |
**401** | APIキーが未設定または不正または失効済の場合のエラー |  -  |
**403** | アクセス権限がない場合のエラー |  -  |
**404** | 指定されたリソースが存在しない場合のエラー |  -  |
**0** | 予期していないエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_file_status_list**
> list[JournalFileStatus] get_journal_file_status_list(offset=offset, limit=limit)

仕訳帳作成状況一覧取得

仕訳帳作成状況の一覧を取得します。作成後90日以内の仕訳帳のみ状況を取得可能です。

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import moneyforward_acplus
from moneyforward_acplus.rest import ApiException
from pprint import pprint
configuration = moneyforward_acplus.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# Defining host is optional and default to https://api-enterprise-accounting.moneyforward.com/api/v1
configuration.host = "https://api-enterprise-accounting.moneyforward.com/api/v1"

# Enter a context with an instance of the API client
with moneyforward_acplus.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moneyforward_acplus.JournalsApi(api_client)
    offset = 0 # int | 仕訳帳作成状況一覧の取得開始位置 (optional) (default to 0)
limit = 100 # int | 仕訳帳作成状況一覧の取得件数 (optional) (default to 100)

    try:
        # 仕訳帳作成状況一覧取得
        api_response = api_instance.get_journal_file_status_list(offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JournalsApi->get_journal_file_status_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| 仕訳帳作成状況一覧の取得開始位置 | [optional] [default to 0]
 **limit** | **int**| 仕訳帳作成状況一覧の取得件数 | [optional] [default to 100]

### Return type

[**list[JournalFileStatus]**](JournalFileStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 仕訳帳作成状況の一覧の取得が成功した場合 |  -  |
**400** | パラメータ不正などAPI呼び出し側理由のエラー |  -  |
**401** | APIキーが未設定または不正または失効済の場合のエラー |  -  |
**403** | アクセス権限がない場合のエラー |  -  |
**0** | 予期していないエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

