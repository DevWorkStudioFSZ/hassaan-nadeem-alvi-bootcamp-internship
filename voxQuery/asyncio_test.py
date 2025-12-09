
import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    print("Start")

    # Create two tasks that run concurrently
    task1 = asyncio.create_task(say_after(3, "Hello"))
    task2 = asyncio.create_task(say_after(1, "World"))

    # Wait for both tasks to finish
    await task1
    await task2

    print("End")

asyncio.run(main())
