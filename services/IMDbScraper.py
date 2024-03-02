import requests
from bs4 import BeautifulSoup
from lxml import etree


class IMDbScraper:
    def __init__(self):
        self.url = 'https://m.imdb.com/chart/top/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/96.0.4664.110 Safari/537.36'
        }
        self.response = requests.get(self.url, headers=headers)
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        # Create an lxml etree from the BeautifulSoup object's HTML
        self.xml_tree = etree.HTML(str(self.soup))

    def get_title(self, index):
        return self.xml_tree.xpath('//*[@id="__next"]/main/div/div[3]/section/'
                                   f'div/div[2]/div/ul/li[{index}]/div[2]/div/div/div[1]/a/h3')[0].text[3:]

    def get_link(self, index):
        return self.xml_tree.xpath('//*[@id="__next"]/main/div/div[3]/section/'
                                   f'div/div[2]/div/ul/li[{index}]/div[2]/div/div/div[1]/a')[0].get('href')

    def get_year(self, index):
        return self.xml_tree.xpath('//*[@id="__next"]/main/div/div[3]/section/'
                                   f'div/div[2]/div/ul/li[{index}]/div[2]/div/div/div[2]/span[1]')[0].text

    def get_runtime(self, index):
        return self.xml_tree.xpath('//*[@id="__next"]/main/div/div[3]/section/'
                                   f'div/div[2]/div/ul/li[{index}]/div[2]/div/div/div[2]/span[2]')[0].text

    def get_rating(self, index):
        return (self.xml_tree.xpath('//*[@id="__next"]/main/div/div[3]/section/'
                                    f'div/div[2]/div/ul/li[{index}]/div[2]/div/div/span/div/span')[0]
                .get('aria-label'))[13:]

    def get_image(self, index):
        return self.xml_tree.xpath('//*[@id="__next"]/main/div/div[3]/section/'
                                   f'div/div[2]/div/ul/li[{index}]/div[1]/div/div[2]/img')[0].get('src')
