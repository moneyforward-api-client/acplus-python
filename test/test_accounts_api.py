# coding: utf-8

"""
    マネーフォワードクラウド会計Plus API

    マネーフォワードクラウド会計PlusのAPI  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: yasuhiroota26@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import moneyforward_acplus
from moneyforward_acplus.api.accounts_api import AccountsApi  # noqa: E501
from moneyforward_acplus.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = moneyforward_acplus.api.accounts_api.AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_accounts(self):
        """Test case for get_accounts

        勘定科目一覧取得  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
