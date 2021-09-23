from time import sleep
from ChromeAuto import ChromeAuto

chrome = ChromeAuto()

audio = 'legendado'
anime = 'detective-conan'
start = 624
end = 628

for episode in range(start, end + 1):
    if len(str(episode)) == 1:
        episode = '0' + str(episode)
    chrome.access(f'https://betteranime.net/anime/{audio}/{anime}/episodio-{episode}/download')
    chrome.click_by_text('Qualidade HD')
    chrome.click_by_xpath('/html/body/div/header/div/div/button')
    chrome.back_page(0)
    chrome.click_by_xpath('/html/body/div/header/div/div/a')
    sleep(60)