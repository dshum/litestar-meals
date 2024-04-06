from litestar import Controller, post, Request

from features.user.guards.auth import auth


class UserController(Controller):
    @post("/logout")
    async def logout(self, request: Request) -> None:
        request.cookies.pop(auth.key, None)
        request.clear_session()
