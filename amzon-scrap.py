import csv
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver

def get_url(search_term):
    """ Generate URL from search term"""
    template = 'https://www.amazon.in/s?k={}&crid=2YNRYJAZ918QO&sprefix=ultrawide%2Caps%2C366&ref=nb_sb_ss_ts-doa-p_2_9'
    search_term = search_term.replace(' ', '+')
    url = template.format(search_term)
    # add page query placeholder
    url += '&page{}'
    return url

def extract_record(item):
    # description of the record
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')
    try:
        # price
        price = item.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).text
    except AttributeError:
        return None

    try:
        # rank and ratings
        ratings = item.find('span', {'class': 'a-icon-alt'}).text
        review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
    except AttributeError:
        ratings = ''
        review_count = ''

    return description, price, ratings, review_count, url

def main(search_term):
    """Run the main program"""
    records = []
    url = get_url(search_term)
    driver = webdriver.Firefox()  # Use Firefox driver, make sure geckodriver is in your PATH
    for page in range(1, 21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})
        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)
    driver.quit()

    # save the data to a CSV file
    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Description', 'Price', 'Ratings', 'ReviewCount', 'Url'])
        writer.writerows(records)

if __name__ == "__main__":
    main('ultrawide monitor')
