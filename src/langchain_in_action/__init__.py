import os

from dotenv import load_dotenv

load_dotenv()
#print(os.getenv("OPENAI_API_KEY"))
#print(os.environ.get("OPENAI_API_KEY"))


def main() -> None:
    print("Hello from langchain-in-action!")


if __name__ == "__main__":
    main()
