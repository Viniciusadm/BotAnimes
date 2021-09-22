from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep
from random import choice, randint
from os import listdir, system
from urllib.request import urlretrieve

class ChromeAuto:
    def __init__(self):
        self.driver_path = './chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-data-dir=perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options = self.options
        )

    def access(self, site):
        self.chrome.get(site)

    def out(self):
        self.chrome.quit()

    def click_select(self, element, item):
        try:
            select_element = self.chrome.find_element_by_id(element)
            select_object = Select(select_element)
            select_object.select_by_visible_text(item)
        except:
            print(f'Erro ao clicar no elemento {item}')

    def click_select_selector(self, element, item):
        select_element = self.chrome.find_element_by_css_selector(element)
        select_object = Select(select_element)
        select_object.select_by_visible_text(item)

    def click_input_id(self, button):
        try:
            btn = self.chrome.find_element_by_id(button)
            btn.click()
        except:
            print(f'Erro ao clicar no elemento {button}')

    def click_input_text(self, element):
        btn = self.chrome.find_element_by_link_text(element)
        btn.click()

    def click_input_selector(self, button):
        btn = self.chrome.find_element_by_css_selector(button)
        btn.click()

    def add_image(self, input, image):
        btn = self.chrome.find_element_by_css_selector(input)
        btn.send_keys(image)

    def write(self, element, text):
        btn = self.chrome.find_element_by_id(element)
        btn.send_keys(text)

    def clear(self, element):
        btn = self.chrome.find_element_by_id(element)
        btn.clear()

    def get_text(self, element):
        text = self.chrome.find_element_by_id(element).text
        return text

    def get_text_xpath(self, element):
        try:
            text = self.chrome.find_element_by_xpath(element).text
            return text
        except:
            return ''

    def get_atrib_xpath(self, element):
        try:
            atrib = self.chrome.find_element_by_xpath(element)
            return atrib.get_attribute('src')
        except:
            return ''

    def roll(self, top):
        self.chrome.execute_script(f"window.scrollTo(0, {top})")