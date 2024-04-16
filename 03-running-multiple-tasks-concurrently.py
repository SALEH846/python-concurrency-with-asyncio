import asyncio
from util import delay

async def main() -> None:
    # All the tasks will get scheduled, but not start running
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    # Once we hit first `await`, all the tasks which are registered start executing
    # Because the event loop is started
    await sleep_for_three
    await sleep_again
    await sleep_once_more


asyncio.run(main())