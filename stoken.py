from itsdangerous import URLSafeTimedSerializer
secret_key='snm2456'
salt='otpverify'
def endata(data):
    serilalizer=URLSafeTimedSerializer(secret_key)
    return serilalizer.dumps(data,salt=salt)
def dndata(data):
    serilalizer=URLSafeTimedSerializer(secret_key)
    return serilalizer.loads(data,salt=salt)