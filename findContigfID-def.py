
def find_contigs(markername, threshold):
    f1 = open('tblastn_' + markername, 'r')
    tblast_list = f1.read().splitlines()
    
    for i in range(0, len(tblast_list)):
        
        if tblast_list[i].find("Score") != -1: 
            indexScore = tblast_list[i].find("Score") 
        
        if tblast_list[i].startswith("Sequences producing significant alignments"):
            start = i + 2
            break
    
    f1.close
    
    f2 = open('ContigID_' + markername + '.txt', 'w')
    f3 = open('ContigID_' + markername + '_dict.txt', 'w')
    
    numbermarker = 0
    while True:
        
        n = 0
        
        for i in range(0,10):
            if tblast_list[start][indexScore + n] != " ":
                n += 1
            else: break   
        
        lastscore = tblast_list[start][indexScore:indexScore + n]
        nScore = round(float(lastscore))
        
        start += 1
        numbermarker += 1
        
        if not threshold <= nScore:
            break
        
        f2.write(tblast_list[start-1].split()[0] + '\n')
        f3.write( markername +  " " + str(numbermarker) + " " + tblast_list[start-1].split()[0] + '\n')
           
    f2.close()
    f3.close()
    
#Data:
Markers = ['muc2', 'but1','acet1','sulfat1']
Threshold = 250

#Work:
for i in Markers: find_contigs(i, Threshold)








