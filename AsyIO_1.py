import asyncio , time

async def one():
	print("One start")
	await asyncio.sleep(1)
	print("One stop")

async def two():
	print("Two start")
	await asyncio.sleep(2)
	print("Two stop")

async def three():
	print('Three start')
	await asyncio.sleep(3)
	print("Three stop")

async def main():
	asyncio.create_task(one())
	asyncio.create_task(two())
	await asyncio.create_task(three())

timex = time.time()
asyncio.run(main())
print(time.time() - timex)