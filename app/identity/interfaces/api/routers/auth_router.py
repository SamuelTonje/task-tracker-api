from fastapi import APIRouter

from app.identity.interfaces.api.controllers.register_controller import register
from app.identity.interfaces.api.controllers.login_controller import login

router = APIRouter(prefix="/auth", tags=["auth"],)

router.add_api_route("/register", register, methods=["POST"])
router.add_api_route("/login", login, methods=["POST"])