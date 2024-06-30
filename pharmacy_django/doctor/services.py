import datetime
from jwt import encode
import os

def create_token(user_id: int) -> str:
    payload = dict(
        id = user_id,
        exp = datetime.datetime.now() + datetime.timedelta(hours=24),
        iat = datetime.datetime.now()
    )
    
    token = encode(payload, os.environ.get('JWT_SECRET'), algorithm="HS256")
    
    return token