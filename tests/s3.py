from s3minimal import S3
from dotenv import load_dotenv

load_dotenv()


s3 = S3()


async def main():
    files = await s3.list_files("nts")
    print(files)
    print(len(files))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
