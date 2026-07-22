from fastapi import APIRouter

from app.identity.interfaces.api.controllers.get_user_controller import get_user
from app.identity.interfaces.api.controllers.me_controller import me
from app.identity.interfaces.api.controllers.register_controller import register
from app.identity.interfaces.api.controllers.login_controller import login

privateRouter = APIRouter(prefix="/auth", tags=["auth"],)

privateRouter.add_api_route("/register", register, methods=["POST"])
privateRouter.add_api_route("/login", login, methods=["POST"])

publicRouter = APIRouter(tags=["public"],)

publicRouter.add_api_route("/me", me, methods=["GET"])
publicRouter.add_api_route("/user/{id}", get_user, methods=["GET"])