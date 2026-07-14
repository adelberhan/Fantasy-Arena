from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash


class User:
    """User model."""

    def __init__(
        self,
        id,
        username,
        password,
        created_at,
        updated_at,
    ):
        self.id = id
        self.username = username
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at

    def verify_password(self, password):
        """Check if password is correct."""

        return check_password_hash(
            self.password,
            password,
        )

    @staticmethod
    def hash_password(password):
        """Hash password."""

        return generate_password_hash(password)

    def to_dict(self):
        """Convert object to dictionary."""

        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data):
        """Create User from dictionary."""

        return cls(**data)