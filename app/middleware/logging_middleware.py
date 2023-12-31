from datetime import datetime
from app.utility.logging import LoggingLevels, get_mongo_client, loggod
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

class RequestResponseLoggingMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, scope, receive, send, client: AsyncIOMotorClient = Depends(get_mongo_client)):
        if scope["type"] == "http":
            # HTTP request
            request = Request(scope, receive=receive)

            # Code executed before the request is processed
            start_time = datetime.utcnow()
            start_time_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request_log_entry = {
                "timestamp": start_time_log,
                "event_type": "request",
                "endpoint": request.url.path,
                "ip_address": request.client.host,
            }
            print(request_log_entry)

            async def send_wrapper(message):
                # Code executed after the request is processed
                end_time = datetime.utcnow()
                end_time_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                response_log_entry = {
                    "timestamp": end_time_log,
                    "event_type": "response",
                    "endpoint": request.url.path,
                    "ip_address": request.client.host,
                    "response_time": (end_time - start_time).total_seconds(),
                }
                print(response_log_entry)
                await send(message)
            response = await self.app(scope, receive, send_wrapper)

            return response
