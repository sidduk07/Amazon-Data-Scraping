# Amazon Product Scraper

## Overview
The Amazon Product Scraper is an automated web scraping tool designed to extract real-time product data from Amazon.com. Utilizing technologies such as Flask, Selenium, and BeautifulSoup, this project enables users to perform dynamic searches on Amazon and collect essential product details for market research and analysis. The scraped data includes product descriptions, prices, ratings, review counts, and URLs.

## Features
- **Dynamic Scraping:** Utilizes Selenium for dynamic searches, ensuring accurate and up-to-date product information.
- **User-Friendly Interface:** Built with Flask, the scraper offers an intuitive interface for users to input search terms effortlessly.
- **Efficient Data Export:** Extracted product details are exported to a CSV file for further analysis and research.
- **Customizable:** Easily adaptable to different Amazon product categories or search parameters.

## Project Structure
- **Web Scraping Code:** The web scraping logic is implemented in `scrape_amazon.py`.
- **Web Interface:** The Flask web application is structured in `app.py` and uses `templates/index.html` for the front-end interface.
- **Requirements:** Required Python packages and versions are listed in `requirements.txt`.

## Technical Details
### Libraries Used
- Flask
- Selenium
- BeautifulSoup

### Web Scraping Process
- Utilizes Selenium for dynamic searches on Amazon.
- Extracts product data including descriptions, prices, ratings, review counts, and URLs.
- Handles missing or unavailable data gracefully to ensure robustness.

### Web Interface
- Provides a search bar for users to input search keywords.
- Displays scraped product data in a tabular format on the web page.
- Allows users to download the scraped data in CSV format.

## How to Use
1. **Clone the Repository:** `git clone https://github.com/username/Amazon-Product-Scraper.git`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Run the Application:** `python app.py`
4. **Access the Scraper:** Open your browser and go to `http://localhost:5000`
5. **Enter Search Term:** Input the desired product or keyword and click the "Search" button.
6. **View and Download Data:** The scraped product details will be displayed on the web page. Click the provided link to download the data in CSV format.

## Conclusion
The Amazon Product Scraper offers a convenient solution for businesses and researchers seeking real-time product data from Amazon.com. Its user-friendly interface and efficient data extraction make it a valuable tool for market analysis and decision-making processes. This project serves as a foundation for further enhancements and customization according to specific requirements.
