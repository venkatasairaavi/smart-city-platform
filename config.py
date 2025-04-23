import os

# App secret
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

# Flask-Mail config
MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "True") == "True"
MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", "False") == "True"
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = os.getenv("MAIL_USERNAME")
MAIL_TIMEOUT = int(os.getenv("MAIL_TIMEOUT", 5))

# Database config
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///smart_city.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False