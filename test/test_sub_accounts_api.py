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
from moneyforward_acplus.api.sub_accounts_api import SubAccountsApi  # noqa: E501
from moneyforward_acplus.rest import ApiException


class TestSubAccountsApi(unittest.TestCase):
    """SubAccountsApi unit test stubs"""

    def setUp(self):
        self.api = moneyforward_acplus.api.sub_accounts_api.SubAccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_sub_accounts(self):
        """Test case for get_sub_accounts

        補助科目一覧取得  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
