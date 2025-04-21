from functools import wraps
from flask import session, redirect, jsonify, url_for

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = session.get('user_role')
            if user_role == role:
                return func(*args, **kwargs)
            else:
                return jsonify({'error': 'Unauthorized - Insufficient role'}), 403
            
        return wrapper
    return decorator