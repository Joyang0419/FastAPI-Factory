from unittest import mock

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from src.application import app
from src.repos.orm.repo_user import IMPRepoUser

client = TestClient(app)


class TestUser:

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'users': []
                },
                id="no users"
            )
        ]
    )
    def test_get_all_users(self, test_case: dict):
        repository_mock = mock.Mock(spec=IMPRepoUser)
        repository_mock.get_all.return_value = test_case['users']

        with app.container.repo_user.override(repository_mock):
            response = client.get("/v1/users/get_all_users")

        assert response.status_code == status.HTTP_200_OK

        res_data = response.json()

        assert 'data' in res_data
