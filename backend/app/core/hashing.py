from app.core.security import hash_password


class Hasher:
    @staticmethod
    def get_password_hash(password: str) -> str:
        return hash_password(password)
