# Imdb_top_250_movies_web_scraping

1. Overview of the Data Extraction Process
This part of the project involves extracting data from the IMDb Top 250 Movies page using a combination of Python, Selenium, and BeautifulSoup. The goal is to retrieve movie details such as the title, release year, length, rating, and review score for each of the 250 movies listed on the webpage.

2. Data Sources
Source URL: https://www.imdb.com/chart/top/
Description: The IMDb Top 250 Movies page lists the top-rated 250 movies based on IMDb user ratings. Each movie entry includes details like title, release year, runtime, content rating, and IMDb rating.

3. Data Extraction Script
Description of the Script: The script uses Selenium to automate the web browser and load the entire IMDb Top 250 Movies page by scrolling to the bottom until no more new content is loaded. After the page is fully loaded, BeautifulSoup is utilized to parse the HTML content and extract relevant movie information.
- Key Steps in the Script:
Setting Up Selenium:
Selenium is used to open the IMDb Top 250 Movies webpage and simulate user behavior to scroll down until all content is loaded. This is necessary because the page dynamically loads content via JavaScript.
Parsing HTML with BeautifulSoup:
Once the page is fully loaded, BeautifulSoup is employed to parse the HTML and identify the relevant <div> elements containing movie details.
Extracting Movie Details:
The script searches for all <a> elements with the class 'ipc-title-link-wrapper' to find movie titles.
The metadata, including the release year, movie length, and content rating, is extracted from corresponding <span> elements.
Review ratings are captured from the <span> elements with the class 'ipc-rating-star--rating'.
Storing Data in a DataFrame:
The extracted data is stored in a pandas DataFrame and then saved as a CSV file (imdb_top_250_movies.csv).
Data Exploration:
After extracting the data, basic exploratory operations are performed to understand the dataset's size, dimensions, and any missing values.


