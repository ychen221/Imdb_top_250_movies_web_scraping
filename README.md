# IMDb Top 250 Movies Web Scraping

## Overview of the Data Extraction Process
This project involves extracting data from the IMDb Top 250 Movies page using a combination of Python, Selenium, and BeautifulSoup. The objective is to retrieve movie details such as the title, release year, length, rating, and review score for each of the 250 movies listed on the webpage.

## Data Sources
- **Source URL**: [IMDb Top 250 Movies](https://www.imdb.com/chart/top/)
- **Description**: The IMDb Top 250 Movies page lists the top-rated 250 movies based on IMDb user ratings. Each movie entry includes details like the title, release year, runtime, content rating, and IMDb rating.

## Data Extraction Script

### Description of the Script
The script uses Selenium to automate the web browser and load the entire IMDb Top 250 Movies page by scrolling to the bottom until no more new content is loaded. After the page is fully loaded, BeautifulSoup is utilized to parse the HTML content and extract relevant movie information.

### Key Steps in the Script

1. **Setting Up Selenium**
   - **Purpose**: To open the IMDb Top 250 Movies webpage and simulate user behavior to scroll down until all content is loaded.
   - **Reason**: The page dynamically loads content via JavaScript, which requires a browser simulation to capture all the data.

2. **Parsing HTML with BeautifulSoup**
   - **Purpose**: To parse the fully loaded page and identify the relevant `<div>` elements containing movie details.
   - **Tools Used**: BeautifulSoup library for HTML parsing.

3. **Extracting Movie Details**
   - **Title Extraction**: The script searches for all `<a>` elements with the class `'ipc-title-link-wrapper'` to find movie titles.
   - **Metadata Extraction**: Extracts the release year, movie length, and content rating from corresponding `<span>` elements.
   - **Review Rating Extraction**: Captures review ratings from the `<span>` elements with the class `'ipc-rating-star--rating'`.

4. **Storing Data in a DataFrame**
   - **Purpose**: The extracted data is stored in a pandas DataFrame to facilitate easy manipulation and analysis.
   - **Output**: The DataFrame is saved as a CSV file (`imdb_top_250_movies.csv`).

5. **Data Exploration**
   - **Purpose**: After data extraction, basic exploratory operations are performed to understand the dataset's size, dimensions, and any missing values.
   - **Operations**: Displaying the first few records, calculating the size and dimensions of the dataset, and identifying any missing data.

## Usage

1. Run the script in a Python environment with the necessary libraries (`selenium`, `BeautifulSoup`, and `pandas`) installed.
2. Ensure that ChromeDriver is installed and its path is correctly set in the script.
3. The script will output a CSV file (`imdb_top_250_movies.csv`) containing the details of the top 250 movies on IMDb.

## Requirements
- Python 3.x
- Selenium
- BeautifulSoup
- pandas
- ChromeDriver 

## Author
- Yu-Chieh(Willow) Chen

