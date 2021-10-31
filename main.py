# Bibliotecas
from time import sleep
# Minhas classes
from ChromeAuto import ChromeAuto
from Files import Files
from Fillers import Fillers
from SearchAnimes import SearchAnimes
from Controll import Controll
from Favorites import Favorites

favorites = Favorites()

for index, favorite in enumerate(favorites.get_favorites()):
    print(str(index) + ' - ' + favorite['title'])
else:
    print(str(index + 1) + ' - Buscar um novo anime')

number = int(input('Digite a opção escolhida: '))

animes = SearchAnimes()
if number < len(favorites.get_favorites()):
    animes.set_anime(favorites.get_favorites()[number])
else:
    name = input("Digite o nome do anime: ")
    animes.search_anime(name)

    for index, anime in enumerate(animes.get_animes()):
        title = anime['title']
        print(f'{index} - {title}')
        number_anime = int(input("Digite o numero do anime: "))
        animes.set_anime(animes.get_animes()[number_anime])

current = int(input("Digite o episodio atual: "))
quantity = int(input("Digite a quantidade de episodios: "))

fillers = Fillers(animes.get_anime()['title']).get_fillers()

# Criação do diretorio
files = Files('/home/vinicius/Downloads/', '/home/vinicius/Vídeos/Animes/' + animes.get_anime()['title'], quantity)
files.create_dir()
chrome = ChromeAuto()

# Baixar os episódios
currentContext = Controll().nextEpisode(fillers, current)
for i in range(0, quantity):
    if len(str(currentContext)) == 1:
        currentContext = '0' + str(currentContext)

    anime_url = animes.get_anime()['url'] + '/episodio-' + str(currentContext) + '/download'
    chrome.access(anime_url)
    if chrome.check_exists_by_text('Qualidade HD'):
        chrome.click_by_text('Qualidade HD')
    else:
        chrome.click_by_text('Qualidade SD')
    
    # Verifica se não deu erro de segurança no Chrome
    if chrome.check_exists_by_text('Avançado'):
        chrome.click_by_text('Avançado')
        chrome.click_by_id('proceed-link')

    chrome.click_by_xpath('/html/body/div/header/div/div/button')
    chrome.back_page(0)
    chrome.click_by_xpath('/html/body/div/header/div/div/a')
    sleep(180)

    currentContext = Controll.nextEpisode(fillers, currentContext)

# Renomar e mover episódios
list_episodes = files.check_downloaded()
currentContext = Controll().nextEpisode(fillers, current)

for episode in list_episodes:
    sleep(1)
    if len(str(currentContext)) == 1:
       currentContext = '0' + str(currentContext)
    
    print(files.move_file(episode, animes.get_anime()['title'], currentContext))
    currentContext = Controll().nextEpisode(fillers, currentContext)
