from datetime import timedelta

from fastapi_jwt import JwtAccessBearer, JwtRefreshBearer

access_security = JwtAccessBearer(secret_key='secret', access_expires_delta=timedelta(seconds=15))
refresh_security = JwtRefreshBearer(secret_key='secret', refresh_expires_delta=timedelta(days=1))
