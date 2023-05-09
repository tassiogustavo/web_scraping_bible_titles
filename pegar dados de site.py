import urllib.request
from bs4 import BeautifulSoup, NavigableString, Tag

#cria um arquivo txt para escrita
file = open("commands.txt","w")

#lista de livros da biblia
books = ['genesis','exodo','levitico','numeros','deuteronomio','josue','juizes','rute','1_samuel','2_samuel','1_reis','2_reis','1_cronicas','2_cronicas','esdras','neemias','ester','jo','salmos','proverbios','eclesiastes','cantico_dos_canticos','isaias','jeremias','lamentacoes','ezequiel','daniel','oseias','joel','amos','obadias','jonas','miqueias','naum','habacuque','sofonias','ageu','zacarias','malaquias','mateus','marcos','lucas','joao','atos_dos_apostolos','romanos','1_corintios','2_corintios','galatas','efesios','filipenses','colossenses','1_tessalonicenses','2_tessalonicenses','1_timoteo','2_timoteo','tito','filemom','hebreus','tiago','1_pedro','2_pedro','1_joao','2_joao','3_joao','judas','apocalipse']
#lista de quantidade de capitulos de cada livro da biblia
qtd_chapter_by_book = [50,40,27,36,34,24,21,4,31,24,22,25,29,36,10,13,10,42,150,31,12,8,66,52,5,48,12,14,3,9,1,4,7,3,3,3,2,14,4,28,16,24,21,28,16,16,13,6,6,4,4,5,3,6,4,3,1,13,5,5,3,5,1,1,1,22]

#loop varrendo todos capitulos de cada livro
for j in range(len(books)):
    for k in range(qtd_chapter_by_book[j]):

        #concatena nome do livro e numero do capitulo a url
        wiki = 'https://www.bibliaon.com/'+books[j]+'_'+str(k+1)+'/'
        #pega o html da url
        page = urllib.request.urlopen(wiki)
        #faz o parse do html para beutifulSoup
        soup = BeautifulSoup(page, 'html.parser')

        checker = False
        vet_next_verse_reference = []
        vet_sub_titles = []

        #pega o texto de toda tag h2
        for title in soup.find_all('h2'):
            vet_sub_titles.append(title.text.replace("  ", ""))

        for item in soup.find(attrs={'class': 'versiculos-detail'}):
            if isinstance(item, NavigableString):
                continue
            if isinstance(item, Tag):
                if str(item.span) == 'None':
                    checker = True
                else:
                    if checker:
                        vet_next_verse_reference.append(item.span.text)
                        checker = False
                

        i = 0
        for title in vet_next_verse_reference:
            #cria um texto para cada titulo
            #concatenando livro, capitulo e numero do versiculo
            #que vem depois do titulo encontrado
            command = 'Livro: '+books[j]+', Capítulo: '+str(k+1)+', Próximo versiculo: '+vet_next_verse_reference[i]+', Texto: "'+vet_sub_titles[i]+'");
            #escreve texto concatenado no arquivo txt
            file.write(command)
            print(command.replace("\n", ""))
            i += 1

        k += 1

    j += 1

#fecha o arquivo
file.close()
