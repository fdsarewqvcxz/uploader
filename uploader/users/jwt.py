from typing import Optional

from flask_jwt_extended import JWTManager
from models import User

jwt = JWTManager()


def init_jwt(app) -> None:
    jwt.init_app(app)

    @jwt.additional_claims_loader
    def make_payload(user: User) -> dict:
        return {"created_at": user.created_at.strftime("%Y-%m-%dT%H:%M:%S")}

    @jwt.user_identity_loader
    def user_identity(user: Optional[User]) -> Optional[int]:
        if isinstance(user, User):
            return user.id
        return None

    @jwt.user_lookup_loader
    def user_lookup(header: dict, payload: dict) -> User:
        return User.query.get(payload["identity"])
