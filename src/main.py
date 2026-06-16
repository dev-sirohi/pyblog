from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from routers.v1.authentication_router import authentication_router
from routers.v1.post_router import post_router
from routers.v1.user_router import user_router
from routers.v1.feed_router import feed_router
from rate_limiter import rate_limiter

app = FastAPI()

app.state.limiter = rate_limiter  # required by slowapi, no use for us
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(authentication_router)
app.include_router(post_router)
app.include_router(user_router)
app.include_router(feed_router)


@app.get("/health")
def health():
    return {"status": "ok"}
