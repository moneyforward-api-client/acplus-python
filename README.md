# acplus-python

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install moneyforward-acplus
```

Then import the package:
```python
import moneyforward_acplus
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import moneyforward_acplus
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api-enterprise-accounting.moneyforward.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**get_accounts**](docs/AccountsApi.md#get_accounts) | **GET** /accounts | 勘定科目一覧取得
*JournalsApi* | [**create_journal_file**](docs/JournalsApi.md#create_journal_file) | **POST** /journals/files | 仕訳帳作成要求
*JournalsApi* | [**delete_journal_file**](docs/JournalsApi.md#delete_journal_file) | **DELETE** /journals/files/{requestId} | 仕訳帳削除
*JournalsApi* | [**download_journal_file**](docs/JournalsApi.md#download_journal_file) | **GET** /journals/files/{requestId} | 仕訳帳ダウンロード
*JournalsApi* | [**get_journal_file_status**](docs/JournalsApi.md#get_journal_file_status) | **GET** /journals/files/{requestId}/status | 仕訳帳作成状況取得
*JournalsApi* | [**get_journal_file_status_list**](docs/JournalsApi.md#get_journal_file_status_list) | **GET** /journals/files/status | 仕訳帳作成状況一覧取得
*SubAccountsApi* | [**get_sub_accounts**](docs/SubAccountsApi.md#get_sub_accounts) | **GET** /sub-accounts | 補助科目一覧取得


## Documentation For Models

 - [Account](docs/Account.md)
 - [CreateJournalFileRequest](docs/CreateJournalFileRequest.md)
 - [CreateJournalFileResponse](docs/CreateJournalFileResponse.md)
 - [Error](docs/Error.md)
 - [ErrorDetail](docs/ErrorDetail.md)
 - [JournalFileStatus](docs/JournalFileStatus.md)
 - [SubAccount](docs/SubAccount.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author

api.acplus.support@moneyforward.co.jp


