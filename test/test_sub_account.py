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
import datetime

import moneyforward_acplus
from moneyforward_acplus.models.sub_account import SubAccount  # noqa: E501
from moneyforward_acplus.rest import ApiException

class TestSubAccount(unittest.TestCase):
    """SubAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = moneyforward_acplus.models.sub_account.SubAccount()  # noqa: E501
        if include_optional :
            return SubAccount(
                account_id = 56,
                sub_account_name = '0',
                tax = '0'
            )
        else :
            return SubAccount(
                account_id = 56,
                sub_account_name = '0',
                tax = '0',
        )

    def testSubAccount(self):
        """Test SubAccount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
