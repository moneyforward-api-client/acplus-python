# moneyforward_acplus.SubAccountsApi

All URIs are relative to *https://api-enterprise-accounting.moneyforward.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sub_accounts**](SubAccountsApi.md#get_sub_accounts) | **GET** /sub-accounts | 補助科目一覧取得


# **get_sub_accounts**
> list[SubAccount] get_sub_accounts(offset=offset, limit=limit, account_ids=account_ids)

補助科目一覧取得

補助科目一覧を取得します。

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
    api_instance = moneyforward_acplus.SubAccountsApi(api_client)
    offset = 0 # int | The initial index of subAccounts to return. (optional) (default to 0)
limit = 100 # int | The number of subAccounts to return. (optional) (default to 100)
account_ids = [56] # list[int] | The id of account to get subAccount. (optional)

    try:
        # 補助科目一覧取得
        api_response = api_instance.get_sub_accounts(offset=offset, limit=limit, account_ids=account_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubAccountsApi->get_sub_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The initial index of subAccounts to return. | [optional] [default to 0]
 **limit** | **int**| The number of subAccounts to return. | [optional] [default to 100]
 **account_ids** | [**list[int]**](int.md)| The id of account to get subAccount. | [optional]

### Return type

[**list[SubAccount]**](SubAccount.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 補助科目一覧の取得が成功した場合 |  -  |
**400** | パラメータ不正などAPI呼び出し側理由のエラー |  -  |
**401** | APIキーが未設定または不正または失効済の場合のエラー |  -  |
**403** | アクセス権限がない場合のエラー |  -  |
**0** | 予期していないエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

