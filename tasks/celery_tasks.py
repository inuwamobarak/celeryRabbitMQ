# celery_tasks.py
import asyncio
from config.celery_config import celery_app


@celery_app.task
def my_task(x, y):
    ans = x + y
    print(ans)
    return ans


@celery_app.task
async def my_async_task(x, y):
    await asyncio.sleep(3)
    ans = x + y
    print(ans)
    return ans


@celery_app.task
def my_second_task(x, y):
    result = asyncio.run(my_async_task(x, y))
    return result
