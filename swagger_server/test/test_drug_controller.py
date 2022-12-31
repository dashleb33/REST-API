# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.drug import Drug  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDrugController(BaseTestCase):
    """DrugController integration test stubs"""

    def test_createdrug(self):
        """Test case for createdrug

        Метод добавления нового льготного лекарства в каталог
        """
        body = Drug()
        response = self.client.open(
            '/api/drugs',
            method='POST',
            data=json.dumps(body),
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deletedrug_by_id(self):
        """Test case for deletedrug_by_id

        Метод удаления льготного лекарства по идентификатору
        """
        response = self.client.open(
            '/api/drugs/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getdrug_by_id(self):
        """Test case for getdrug_by_id

        Метод получения льготного лекарства по идентификатору
        """
        response = self.client.open(
            '/api/drugs/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getdrug_byexpiration(self):
        """Test case for getdrug_byexpiration

        Метод получения льготных лекарств по сроку годности
        """
        response = self.client.open(
            '/api/drugs/expiration/{expiration}'.format(expiration='expiration_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getdrugs(self):
        """Test case for getdrugs

        Метод получения списка льготных лекарств
        """
        response = self.client.open(
            '/api/drugs',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updatedrug(self):
        """Test case for updatedrug

        Метод обновления льготного лекарства в каталоге
        """
        body = Drug()
        response = self.client.open(
            '/api/drugs/{id}'.format(id='id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
