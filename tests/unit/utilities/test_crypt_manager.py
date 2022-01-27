from src.containers.container_utilities import ContainerUtilities
import pytest


class TestDBManager:

    def setup(self):
        """
        set attribute:
            crypt_manager()
        Returns:

        """
        self.crypt_manager = ContainerUtilities().crypt_manager()

    @staticmethod
    @pytest.fixture(scope='function', params=['test'])
    def test_plain_pwd(request):
        return request.param

    def test_get_pwd_hash(self, test_plain_pwd: str):
        """
        GIVEN an crypt_manager

        WHEN crypt_manager.get_pwd_hash()

        THEN assert hashed_pwd type is str
        """
        hashed_pwd = self.crypt_manager.get_pwd_hash(pwd=test_plain_pwd)
        assert isinstance(hashed_pwd, str)

    def test_verify_pwd(self, test_plain_pwd: str):
        """
        GIVEN an crypt_manager

        WHEN
          - crypt_manager.get_pwd_hash()
          - crypt_manager.test_verify_pwd()

        THEN assert test_verify_pwd() return value
        """
        hashed_pwd = self.crypt_manager.get_pwd_hash(pwd=test_plain_pwd)
        assert self.crypt_manager.verify_pwd(
            plain_pwd=test_plain_pwd,
            hashed_pwd=hashed_pwd
        )



