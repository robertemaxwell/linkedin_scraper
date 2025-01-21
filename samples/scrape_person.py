import os
from linkedin_scraper import Person, actions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setup Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Optional: Run in headless mode

# Set path to specific chromedriver file in Downloads folder
# Update this filename to match your actual chromedriver file
chromedriver_path = os.path.expanduser("~/Downloads/chromedriver-mac-arm64/chromedriver") 
service = Service(executable_path=chromedriver_path)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

email = os.getenv("LINKEDIN_USER")
password = os.getenv("LINKEDIN_PASSWORD")
actions.login(driver, email, password) # if email and password isn't given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver)
