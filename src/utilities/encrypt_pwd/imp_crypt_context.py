from src.utilities.encrypt_pwd.interface import IFCryptManager
from passlib.context import CryptContext


class IMPCryptManager(IFCryptManager):

    def __init__(self, crypt_context: CryptContext):
        self.crypt_context = crypt_context

    def get_pwd_hash(self, pwd: str) -> str:
        return self.crypt_context.hash(pwd)

    def verify_pwd(
            self,
            plain_pwd: str,
            hashed_pwd: str
    ) -> bool:
        return self.crypt_context.verify(plain_pwd, hashed_pwd)
