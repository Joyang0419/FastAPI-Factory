from fastapi.security import OAuth2PasswordBearer


def get_security():
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    return oauth2_scheme
