import asyncio

async def task():
    await asyncio.sleep(4)
    print("Task done")

async def main():
    await task()
    print("Next task")

asyncio.run(main())