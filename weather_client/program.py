import bs4
import requests


def print_header():
    print('-----------------------')
    print('------WEATHER APP------')
    print('-----------------------')


def get_zipcode():
    pass


def get_html():
    url = 'https://www.wunderground.com/weather/de/munich'
    response = requests.get(url)
    return response.text


def parse_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    #print(soup)
    #cityCSS = '.region-content-header h1'
    #weatherscaleCSS = '.wu-unit-temperature.wu-label'
    #weatherTempCSS = '.wu-unit-temperature.wu-value'
    #weatherconditionCSS = '.condition-icon'

    loc = soup.find(class_='region-content-header').find('h1').get_text().strip()
    condition = soup.find(class_='condition-icon').get_text().strip()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text().strip()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text().strip()

    if scale == 'F':
        temp = (temp - 32) * 5.0 / 9.0
        scale = 'C'

    print(loc, condition, temp, scale)


def display_forecast():
    pass


def main():
    print_header()
    get_zipcode()
    html = get_html()
    parse_html(html)
    display_forecast()


if __name__ == '__main__':
    main()