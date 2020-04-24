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
from moneyforward_acplus.models.journal_file_status import JournalFileStatus  # noqa: E501
from moneyforward_acplus.rest import ApiException

class TestJournalFileStatus(unittest.TestCase):
    """JournalFileStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JournalFileStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = moneyforward_acplus.models.journal_file_status.JournalFileStatus()  # noqa: E501
        if include_optional :
            return JournalFileStatus(
                request_id = 0,
                requested_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                request_params = moneyforward_acplus.models.create_journal_file_request.CreateJournalFileRequest(
                    from_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                    to_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                    approval_status = 'approved',
                    character_set = 'utf8', ),
                status = 'pending',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return JournalFileStatus(
                request_id = 0,
                requested_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                request_params = moneyforward_acplus.models.create_journal_file_request.CreateJournalFileRequest(
                    from_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                    to_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                    approval_status = 'approved',
                    character_set = 'utf8', ),
                status = 'pending',
        )

    def testJournalFileStatus(self):
        """Test JournalFileStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
