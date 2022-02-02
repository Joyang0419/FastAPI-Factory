from fastapi.security import OAuth2PasswordBearer
from src.containers.container_services import ContainerServices

service_auth = ContainerServices().service_auth()


def get_permissions_required_decorator(permissions):
    return service_auth.permissions_required_decorator(permissions)


def get_security():
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/token")
    return oauth2_scheme
