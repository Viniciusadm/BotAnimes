from selenium.webdriver.support.select import Select
from selenium import webdriver

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

    def back_page(self, page):
        self.chrome.switch_to_window(self.chrome.window_handles[page])
    
    def roll(self, top):
        self.chrome.execute_script(f"window.scrollTo(0, {top})")

    def click_select_by_id(self, element, item):
        try:
            select_element = self.chrome.find_element_by_id(element)
            select_object = Select(select_element)
            select_object.select_by_visible_text(item)
        except:
            print(f'Erro ao clicar no elemento {item}')

    def click_select_by_selector(self, element, item):
        try:
            select_element = self.chrome.find_element_by_css_selector(element)
            select_object = Select(select_element)
            select_object.select_by_visible_text(item)
        except:
            print(f'Erro ao clicar no elemento {item}')

    def click_by_id(self, element):
        try:
            btn = self.chrome.find_element_by_id(element)
            btn.click()
        except:
            print(f'Erro ao clicar no elemento {element}')

    def click_by_text(self, element):
        try:
            btn = self.chrome.find_element_by_link_text(element)
            btn.click()
        except:
            print(f'Erro ao clicar no elemento {element}')

    def click_by_selector(self, element):
        try:
            btn = self.chrome.find_element_by_css_selector(element)
            btn.click()
        except:
            print(f'Erro ao clicar no elemento {element}')

    def click_by_xpath(self, element):
        try:
            btn = self.chrome.find_element_by_xpath(element)
            btn.click()
        except:
            print(f'Erro ao clicar no elemento {element}')

    def add_image_by_selector(self, element, image):
        try:
            btn = self.chrome.find_element_by_css_selector(element)
            btn.send_keys(image)
        except:
            print(f'Erro ao adicionar a imagem')

    def write_by_id(self, element, text):
        try:
            btn = self.chrome.find_element_by_id(element)
            btn.send_keys(text)
        except:
            print(f'Erro ao escrever o texto')

    def clear_by_id(self, element):
        try:
            btn = self.chrome.find_element_by_id(element)
            btn.clear()
        except:
            print(f'Erro ao apagar o elemento {element}')

    def get_text_by_id(self, element):
        try:
            text = self.chrome.find_element_by_id(element).text
            return text
        except:
            return ''

    def get_text_xpath(self, element):
        try:
            text = self.chrome.find_element_by_xpath(element).text
            return text
        except:
            return ''

    def get_atrib_by_xpath(self, element, atrib):
        try:
            tag = self.chrome.find_element_by_xpath(element)
            return tag.get_attribute(atrib)
        except:
            return ''

    def get_atrib_by_tag(self, element, atrib) -> str:
        try:
            tag = self.chrome.find_element_by_tag_name(element)
            return tag.get_attribute(atrib)
        except:
            return ''

    def get_element_by_text(self, text):
        try:
            element = self.chrome.find_element_by_link_text(text)
            return element
        except:
            return ''

    def check_exists_by_text(self, text):
        try:
            self.chrome.find_element_by_link_text(text)
        except:
            return False
        return True

    def check_exists_by_tag(self, tag):
        try:
            self.chrome.find_element_by_tag_name(tag)
        except:
            return False
        return True
            