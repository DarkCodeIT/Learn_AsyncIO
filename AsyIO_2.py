import asyncio, aiohttp, requests, time

#Other
headers = {
	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

# Test with aiohttp AVG is 0.97

async def aparsing(url: str):

	async with aiohttp.ClientSession() as session:
		print("Aget start")
		async with session.get(url=url, headers=headers) as response:
			print("Aget stop")

#Test with requests AVG 3.69

async def parsing(url: str):
	
	with requests.Session() as session:
		print("GET start")
		with session.get(url=url) as response:
			print("GET stop")

#Main

async def main():
	t = time.time()
	await asyncio.gather(
		aparsing("https://www.google.com/"),
		aparsing("https://www.google.com/"),
		aparsing("https://www.google.com/"),
		aparsing("https://www.google.com/"),
		aparsing("https://www.google.com/")
	)
	print(time.time() - t)

	# await asyncio.gather(
	# 	parsing("https://www.google.com/"),
	# 	parsing("https://www.google.com/"),
	# 	parsing("https://www.google.com/"),
	# 	parsing("https://www.google.com/"),
	# 	parsing("https://www.google.com/")
	# )
	# print(time.time() - t)


if __name__ == "__main__":
	asyncio.run(main())