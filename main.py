# Minhas classes
from ChromeAuto import ChromeAuto
from Download import Download
from SearchAnimes import SearchAnimes
from Controll import Controll
from Favorites import Favorites
from Config import Config
# Meus enums
from Qualities import Qualities

for index, favorite in enumerate(Favorites().get_favorites()):
    print(str(index) + ' - ' + favorite['title'])
else:
    print(str(index + 1) + ' - Buscar um novo anime')

number = int(input('Digite a opção escolhida: '))

animes = SearchAnimes()
if number < len(Favorites().get_favorites()):
    animes.set_anime(Favorites().get_favorites()[number])
else:
    name = input("Digite o nome do anime: ")
    animes.search_anime(name)

    for index, anime in enumerate(animes.get_animes()):
        title = anime['title']
        print(f'{index} - {title}')
    number_anime = int(input("Digite o numero do anime: "))
    animes.set_anime(animes.get_animes()[number_anime])

if animes.get_anime('title')[-10:] == ' - Dublado':
    animes.set_name(animes.get_anime('title')[:-10])

current = int(input("Digite o episodio atual: "))
quantity = int(input("Digite a quantidade de episodios: "))

# Criação do diretorio
Controll().create_dir(animes.get_anime('title'))
chrome = ChromeAuto()

# Baixar os episódios
current = Controll().nextEpisode(animes.get_anime('title'), current)
config = Config()

for i in range(0, quantity):
    if len(str(current)) == 1:
        current = '0' + str(current)

    anime_url = animes.get_anime('url') + '/episodio-' + str(current) + '/download'
    chrome.access(anime_url)

    found = False
    for qualitiy in Qualities:
        if qualitiy.value == config.get_config('standard_quality') and found == False:
            found = True
            if chrome.check_exists_by_text(qualitiy.value):
                chrome.click_by_text(qualitiy.value)
                break
            else:
                continue
        else:
            if chrome.check_exists_by_text(qualitiy.value) and found == True:
                chrome.click_by_text(qualitiy.value)
                break
    
    # Verifica se não deu erro de segurança no Chrome
    if chrome.check_exists_by_text('Avançado'):
        chrome.click_by_text('Avançado')
        chrome.click_by_id('proceed-link')

    chrome.click_by_xpath('/html/body/div/header/div/div/button')
    chrome.back_page(0)
    url = chrome.get_atrib_by_xpath('/html/body/div/header/div/div/a', 'href')
    
    name_anime = animes.get_anime('title')

    if len(str(current)) == 1:
       current = '0' + str(current)

    title_file = f'{name_anime} {current}.mp4'
    
    Download(url, name_anime, title_file)
    print(f'Download do episódio {current} de {name_anime} concluido')

    current = Controll().nextEpisode(name_anime, current)