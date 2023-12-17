import asyncio

async def add_tasks_to_event_loop():
    asyncio.create_task(func1())
    asyncio.create_task(func2())
    # The add_tasks_to_event_loop function is awaited. So the event loop will think "Oh, this is an async function.
    # It means I am allowed to do something else instead of sitting idle. What can I do in these 6 seconds instead of sitting idle ? 
    # I have two more tasks created and added in the loop. They are also async. Which means I am allowed to run them as well. Let's run them."
    await asyncio.sleep(6)

async def func1():    
    await asyncio.sleep(4)
    print("Hello from func1!")

async def func2():
    await asyncio.sleep(2)
    print("Hello from func2!")


if __name__ == '__main__':
    # The event loop gets created and starts with run function. The first task of the event loop is to run the add_tasks_to_event_loop function.
    asyncio.run(add_tasks_to_event_loop())

    """
    Here's the sequence of events:

    The event loop starts, and the first task is to run add_tasks_to_event_loop().
    Inside add_tasks_to_event_loop():
    - Two tasks, func1() and func2(), are created and added to the event loop. They start running concurrently.
    - The event loop is allowed to do other work while it waits for the await asyncio.sleep(6) to complete.
    - After 2 seconds, "Hello from func2!" is printed.
    - After 4 seconds (6 seconds in total from the start), "Hello from func1!" is printed.
    
    So, the expected output will be:
    ________________________________
    Hello from func2!
    Hello from func1!
    
    This output reflects the concurrency and non-blocking nature of asynchronous programming. 
    Both func1() and func2() are running concurrently, and the event loop efficiently utilizes 
    the waiting time during the sleep operation to execute other tasks
        
    """





