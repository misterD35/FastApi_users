import time
from fastapi import FastAPI, Request
from routers import router_commands, router_users, router_login, router_info

# uvicorn main_dir.main:app --reload --port 2020


app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(router_info.router)
app.include_router(router_users.router)
app.include_router(router_login.router)
app.include_router(router_commands.router)
