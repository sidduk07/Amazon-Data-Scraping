import csv
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from selenium import webdriver

app = Flask(__name__)

def get_url(search_term):
    template = 'https://www.amazon.in/s?k={}&crid=2YNRYJAZ918QO&sprefix=ultrawide%2Caps%2C366&ref=nb_sb_ss_ts-doa-p_2_9'
    search_term = search_term.replace(' ', '+')
    url = template.format(search_term)
    url += '&page{}'
    return url

def extract_record(item):
    description_element = item.find('span', {'class': 'a-size-medium'})
    price_element = item.find('span', {'class': 'a-price-whole'})
    ratings_element = item.find('span', {'class': 'a-icon-alt'})
    review_count_element = item.find('span', {'class': 'a-size-base'})
    url_element = item.find('a', {'class': 'a-link-normal'})

    # Handle cases where elements are not found
    description = description_element.text.strip() if description_element else 'N/A'
    price = price_element.text.strip() if price_element else 'N/A'
    ratings = ratings_element.text.strip() if ratings_element else 'N/A'
    review_count = review_count_element.text.strip() if review_count_element else 'N/A'
    url = 'https://www.amazon.in' + url_element['href'] if url_element and 'href' in url_element.attrs else '#'

    return description, price, ratings, review_count, url



# def extract_record(item):
#     atag = item.h2.a
#     description = atag.text.strip()
#     url = 'https://www.amazon.in' + atag.get('href')  # Use amazon.in instead of amazon.com
#     try:
#         price = item.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).text
#     except AttributeError:
#         return None
#
#     try:
#         ratings = item.find('span', {'class': 'a-icon-alt'}).text
#         review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
#     except AttributeError:
#         ratings = ''
#         review_count = ''
#
#     return description, price, ratings, review_count, url

def scrape_amazon(search_term,file_name):
    records = []
    url = get_url(search_term)
    driver = webdriver.Firefox()  # Make sure geckodriver is in your PATH
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
    with open(f'{file_name}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Description', 'Price', 'Ratings', 'ReviewCount', 'Url'])
        writer.writerows(records)

    return records

@app.route('/', methods=['GET', 'POST'])
def index():
    records = []
    global file_name
    if request.method == 'POST':
        search_term = request.form['search_term']
        file_name = search_term
        records = scrape_amazon(search_term,file_name)
    return render_template('index.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
