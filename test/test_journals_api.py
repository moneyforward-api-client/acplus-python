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
from moneyforward_acplus.api.journals_api import JournalsApi  # noqa: E501
from moneyforward_acplus.rest import ApiException


class TestJournalsApi(unittest.TestCase):
    """JournalsApi unit test stubs"""

    def setUp(self):
        self.api = moneyforward_acplus.api.journals_api.JournalsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_journal_file(self):
        """Test case for create_journal_file

        仕訳帳作成要求  # noqa: E501
        """
        pass

    def test_delete_journal_file(self):
        """Test case for delete_journal_file

        仕訳帳削除  # noqa: E501
        """
        pass

    def test_download_journal_file(self):
        """Test case for download_journal_file

        仕訳帳ダウンロード  # noqa: E501
        """
        pass

    def test_get_journal_file_status(self):
        """Test case for get_journal_file_status

        仕訳帳作成状況取得  # noqa: E501
        """
        pass

    def test_get_journal_file_status_list(self):
        """Test case for get_journal_file_status_list

        仕訳帳作成状況一覧取得  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
