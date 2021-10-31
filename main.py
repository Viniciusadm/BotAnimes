# Bibliotecas
from time import sleep
# Minhas classes
from ChromeAuto import ChromeAuto
from Files import Files
from Fillers import Fillers
from SearchAnimes import SearchAnimes
from Controll import Controll

name = 'Detective Conan'
# name = input("Digite o nome do anime: ")
animes = SearchAnimes(name)

# for index, anime in enumerate(animes.get_animes()):
#     title = anime['title']
#     print(f'{index} - {title}')

number_anime = 0
# number_anime = int(input("Digite o numero do anime: "))
animes.set_anime(animes.get_animes()[number_anime])

current = 713
quantity = 2
# current = int(input("Digite o primeiro episodio: "))
# quantity = int(input("Digite a quantidade de episodios: "))

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
    sleep(120)

    currentContext = Controll.nextEpisode(fillers, currentContext)

# Renomar e mover episódios
list_episodes = files.check_downloaded()
currentContext = Controll().nextEpisode(fillers, current)

for episode in list_episodes:
    sleep(0.5)
    if len(str(currentContext)) == 1:
       currentContext = '0' + str(currentContext)
    
    print(files.move_file(episode, animes.get_anime()['title'], currentContext))
    currentContext = Controll().nextEpisode(fillers, currentContext)