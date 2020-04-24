# moneyforward_acplus.AccountsApi

All URIs are relative to *https://api-enterprise-accounting.moneyforward.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /accounts | 勘定科目一覧取得


# **get_accounts**
> list[Account] get_accounts(accept_charset=accept_charset)

勘定科目一覧取得

勘定科目一覧を取得します。デフォルトではJSON形式となりますが、勘定科目の一覧をCSVで取得する場合はHTTPヘッダ Acceptでtext/csvを指定してください。CSVで取得する場合はHTTPヘッダ Accept-CharsetでUTF-8またはShift_JISを指定可能です。未指定の場合はUTF-8となります。

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
    api_instance = moneyforward_acplus.AccountsApi(api_client)
    accept_charset = 'utf-8' # str | The charset type of text/csv. (optional) (default to 'utf-8')

    try:
        # 勘定科目一覧取得
        api_response = api_instance.get_accounts(accept_charset=accept_charset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_charset** | **str**| The charset type of text/csv. | [optional] [default to &#39;utf-8&#39;]

### Return type

[**list[Account]**](Account.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 勘定科目一覧の取得が成功した場合 |  -  |
**400** | パラメータ不正などAPI呼び出し側理由のエラー |  -  |
**401** | APIキーが未設定または不正または失効済の場合のエラー |  -  |
**403** | アクセス権限がない場合のエラー |  -  |
**0** | 予期していないエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

