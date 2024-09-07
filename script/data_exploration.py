from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment if you want to run in headless mode

# Path to your ChromeDriver executable
service = Service('/usr/local/bin/chromedriver')  # Update with your path
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get('https://www.imdb.com/chart/top/')
    time.sleep(5)  # Allow time for the page to load

    # Scroll until no more new content is loaded
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Wait for content to load

        # Check new height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("Reached the bottom of the page or no more content to load.")
            break
        last_height = new_height

    # Get the page source HTML after scrolling
    html = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all relevant <div> elements that contain movie details
    movie_divs = soup.find_all('div', class_='sc-b189961a-0 iqHBGn cli-children')

    # Extract movie details
    movie_details = []
    for div in movie_divs:
        title_tag = div.find('a', class_='ipc-title-link-wrapper')
        if title_tag:
            title = title_tag.find('h3', class_='ipc-title__text').get_text(strip=True).split('. ', 1)[-1]
        
        metadata_tags = div.find_all('span', class_='sc-b189961a-8 hCbzGp cli-title-metadata-item')
        if len(metadata_tags) >= 3:
            year = metadata_tags[0].get_text(strip=True)
            length = metadata_tags[1].get_text(strip=True)
            rating = metadata_tags[2].get_text(strip=True)
        
        review_tag = div.find('span', class_='ipc-rating-star--rating')
        review = review_tag.get_text(strip=True) if review_tag else 'N/A'
        
        movie_details.append({
            'Title': title,
            'Year': year,
            'Length': length,
            'Rating': rating,
            'Review': review
        })

    # Create a DataFrame and save to a CSV file
    df = pd.DataFrame(movie_details)
    print(df)
    df.to_csv('../data/imdb_top_250_movies.csv', index=False)

finally:
    driver.quit()


print("First few records:")
print(df.head())

# Calculate the size and dimensions of the dataset
print("\nSize and dimensions:")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print(f"Total number of entries: {df.size}")

# Identify missing data
print("\nMissing data information:")
print(df.isnull().sum())

