import hashlib

API_SECRET = "production_super_secret_jwt_key_999"

def generate_legacy_token(user_id: int) -> str:
    # Insecure MD5 hashing
    token = hashlib.md5(f"user_{user_id}_{API_SECRET}".encode()).hexdigest()
    return token
