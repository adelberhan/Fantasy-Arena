from datetime import datetime
import uuid
import secrets


def generate_id():
    """Generate a unique ID."""

    return uuid.uuid4().hex


def current_timestamp():
    """Return current timestamp."""

    return datetime.now().isoformat(timespec="seconds")


def generate_room_code():
    """Generate room code."""

    return secrets.token_hex(3).upper()


def parse_match_datetime(match_date, match_time):
    """Combine date and time into ISO format."""

    return datetime.fromisoformat(f"{match_date}T{match_time}").isoformat(
        timespec="minutes"
    )


def make_password_hash(password: str) -> str:
    # 1. إنشاء Salt عشوائي وآمن (16 بايت)
    salt = os.urandom(16)
    
    # 2. تشفير الكلمة باستخدام PBKDF2 و SHA256 مع 100,000 تكرار
    pwd_hash = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'), 
        salt, 
        100000
    )
    
    # 3. دمج الـ Salt مع الـ Hash لتخزينهما معاً في قاعدة البيانات
    return salt.hex() + "$" + pwd_hash.hex()

def verify_password(password: str, stored_hash: str) -> bool:
    salt_hex, pwd_hash_hex = stored_hash.split('$')
    salt = bytes.fromhex(salt_hex)
    
    new_hash = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'), 
        salt, 
        100000
    )
    return new_hash.hex() == pwd_hash_hex

