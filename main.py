from dotenv import load_dotenv
import os

# Load enviroment variables
load_dotenv(".venv\.secrets")
token_todoist = os.getenv('TODOIST_TOKEN')
token_google_cal = os.getenv('GOOGLE_CALENDAR_TOKEN')

def main():
    ...

if __name__ == "__main__":
    main()