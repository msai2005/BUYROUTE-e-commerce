import os
from itsdangerous import URLSafeTimedSerializer 
secret_key = os.getenv("TOKEN_SECRET")
salt='otpverify'
def endata(data):
    serilalizer=URLSafeTimedSerializer(secret_key)
    return serilalizer.dumps(data,salt=salt)
def dndata(data):
    serilalizer=URLSafeTimedSerializer(secret_key)
    return serilalizer.loads(data,salt=salt)