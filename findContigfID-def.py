
def find_contigs(markername, threshold):
    #NB: для каждого маркера этот путь всё равно будет свой, поэтому нужно либо договориться об именовании папок, либо
    #формировать его динамически
    f1 = open(DATA_DIR+'tblastn_' + markername, 'r')
    tblast_list = f1.read().splitlines()
    
    for i in range(0, len(tblast_list)):

        #NB: Излишняя проверка, поскольку в случае, если скор не найдётся, то переменная indexScore не будет корректно
        #проинициализирована и ниже произойдёт некорректный вызов по индексу indexScore + n
        if tblast_list[i].find("Score") != -1: 
            indexScore = tblast_list[i].find("Score") 
        
        if tblast_list[i].startswith("Sequences producing significant alignments"):
            start = i + 2
            break

    #NB: кто вызовы делать будет?)
    f1.close()
    
    f2 = open('ContigID_' + markername + '.txt', 'w')
    f3 = open('ContigID_' + markername + '_dict.txt', 'w')
    
    numbermarker = 0
    #NB: потенциально может случиться зависание программы при некорректном вводе. Устранить установлением потолка
    #итераций и сообщением об ошибке в случае его превышения
    while True:
        
        n = 0
        #NB: Добавь комментарии к коду
        for i in range(0,10):
            #NB: Потенциальная проблема в случае, если indexScore не проинициализирована
            if tblast_list[start][indexScore + n] != " ":
                n += 1
            else: break   
        
        lastscore = tblast_list[start][indexScore:indexScore + n]
        nScore = round(float(lastscore))
        
        start += 1
        numbermarker += 1

        #NB: почему не if nScore < threshold?
        if not threshold <= nScore:
            break
        
        f2.write(tblast_list[start-1].split()[0] + '\n')
        f3.write( markername +  " " + str(numbermarker) + " " + tblast_list[start-1].split()[0] + '\n')
           
    f2.close()
    f3.close()
    
#Data:
DATA_DIR=""#по умолчанию, относительный путь. Но можно указать абсолютный до папки с результатами tblastn
#NB: сделать считыванием в цикле из файла маркеров
Markers = ['muc2', 'but1','acet1','sulfat1']
Threshold = 250

#Work:
for i in Markers: find_contigs(i, Threshold)








