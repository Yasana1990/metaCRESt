#Объединяем все в один файл таким образом, чтобы все контиги были пронумерованы как nameN_M,
# где name – название функциональной группы, N – номер маркера, а M – номер контига

def formatting(markername):

    f1 = open('rawTPM_' + markername + '.txt', 'r')
    tpm_list = f1.read().splitlines()
    
    for i in range(0, len(tpm_list)):
        tpm_list[i] = tpm_list[i].replace(':', '\t')
        tpm_list[i] = tpm_list[i].split('\t')

    #NB: кто вызовы делать будет?)
    f1.close()
    
    f2 = open('ContigID_'+markername+'_dict.txt', 'r')
    dict_list = f2.read().splitlines()
    
    for i in range(0, len(dict_list)):
        dict_list[i] = dict_list[i].split(' ')        
    
    f2.close()

    #NB: здесь нужны комментарии
    for i in range(0, len(dict_list)):
        for j in range(0, len(tpm_list)):
            if tpm_list[j][1] == dict_list[i][2]:
                tpm_list[j][1] = dict_list[i][0] + '_' + dict_list[i][1]
       
    tpm_list.sort(key = lambda x: x[1])
    
    f3 = open('upTPM_' + markername + '.txt', 'w')
    f3.write('marker\tdiet\tlength\teff.len\tcount\tTPM\n')
    for i in range(0, len(tpm_list)):
        member = tpm_list[i][0]
        tpm_list[i][0] = tpm_list[i][1]
        tpm_list[i][1] = member.split('/')[-2].split('_')[0]
       
        for j in range(0, 5):
            f3.write(tpm_list[i][j] + '\t')
        f3.write(tpm_list[i][5] + '\n')
     
    f3.close()

#Data:
Markers = ['muc2', 'but1','acet1','sulfat1']  

#Work:
for i in Markers: formatting(i)













