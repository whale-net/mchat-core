"""Password authentication. No interaction with database, only processes information."""
import uuid
import hashlib

def create_password_str(password):
    """Create db string for a new account."""
    algorithm = 'sha512'
    salt = uuid.uuid4().hex
    return generate_password_str(algorithm, salt, password)

def verify_password_str(password, password_db_str):
    """Verify password matches database string."""
    split_password_db = password_db_str.split('$')
    algorithm = split_password_db[0]
    salt = split_password_db[1]
    return password_db_str == generate_password_str(algorithm, salt, password)

def generate_password_str(algorithm, salt, password):
    """Generate db entry for password from algorithm, salt, and password."""
    hash_obj = hashlib.new(algorithm)
    salted_password = salt + password
    hash_obj.update(salted_password.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    return '$'.join([algorithm, salt, password_hash])
