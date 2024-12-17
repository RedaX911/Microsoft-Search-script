from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import random
import string

# Path to your msedgedriver.exe Change this path to the path of your msegdedriver.exe
edge_driver_path = r'C:\Users\YourPath\Downloads\edgedriver_win64\msedgedriver.exe'

# New profile directory for a clean session
profile_dir = os.path.join(os.getcwd(), "edge_profile")
if not os.path.exists(profile_dir):
    os.mkdir(profile_dir)

# Create a Service object
service = Service(edge_driver_path)

# Create Edge options and assign the new profile directory
options = Options()
options.add_argument(f"--user-data-dir={profile_dir}")

# Start the Edge WebDriver with the Service and options
driver = webdriver.Edge(service=service, options=options)

# Go to bing.com
driver.get("https://www.bing.com")

# Wait a moment for the page to load
time.sleep(2)

# Function to generate a random search term with exactly 12 letters
def generate_random_search():
    # Generate a random string of exactly 12 lowercase letters
    random_search = ''.join(random.choices(string.ascii_lowercase, k=12))
    return random_search

# Function to type slowly
def slow_type(element, text, typing_delay=0.1):
    for char in text:
        element.send_keys(char)
        time.sleep(typing_delay)

# Perform the searches 30 times
for _ in range(30):
    # Re-locate the search box element (to avoid stale element error)
    search_box = driver.find_element(By.NAME, "q")

    # Generate a random search term of exactly 12 letters
    random_search = generate_random_search()

    # Clear the search box and type slowly
    search_box.clear()  # Clear the search box
    slow_type(search_box, random_search, typing_delay=0.1)  # Type the search term slowly
    search_box.send_keys(Keys.RETURN)  # Press Enter to search

    # Wait 4 seconds before searching again
    time.sleep(4)

# Wait 5 seconds before closing the browser
time.sleep(5)

# Close the browser
driver.quit()
