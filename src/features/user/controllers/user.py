from litestar import Controller, post, Request, get

from features.user.guards.auth import auth


class UserController(Controller):
    @get("/csrf-cookie")
    async def csrf_token(self, request: Request) -> None:
        return None

    @post("/logout")
    async def logout(self, request: Request) -> None:
        request.cookies.pop(auth.key, None)
        request.clear_session()
