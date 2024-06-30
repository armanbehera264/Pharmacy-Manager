import datetime
from jwt import encode
from django.conf import settings

def create_token(user_id: int) -> str:
    payload = dict(
        id = user_id,
        exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=24),
        iat = datetime.datetime.now(datetime.UTC) - datetime.timedelta(seconds=60) # 60 seconds is subtracted to counter ImmatureSignatureError
    )
    
    token = encode(payload, settings.JWT_SECRET, algorithm="HS256")
    
    return token