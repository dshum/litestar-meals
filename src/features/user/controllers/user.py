from lib.jwt import auth
from litestar import Controller, post, Request


class UserController(Controller):
    @post("/logout")
    async def logout(self, request: Request) -> None:
        request.cookies.pop(auth.key, None)
        request.clear_session()
