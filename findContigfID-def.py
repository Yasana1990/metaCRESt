
def find_contigs(markername, threshold):
    
    with open(DATA_DIR+'tblastn_' + markername, 'r') as f1:
        tblast_list = f1.read().splitlines()
    
    for i in range(0, len(tblast_list)):

        # find the index of the beginning of the Score column:
        # X-axis
        if tblast_list[i].find("Score") != -1: 
            indexScore = tblast_list[i].find("Score") 
        
        # Y-axis
        if tblast_list[i].startswith("Sequences producing significant alignments"):
            start = i + 2
            break

    
    with open('ContigID_' + markername + '.txt', 'w') as f2:
    
        numbermarker = 0
        counter = 0
        while True:
            
            # protection against freezing of the program
            counter += 1
            if counter >= 1000000000000:
                break
            
            # recording the Score value by individual digits
            n = 0
            for i in range(0,10):
                if tblast_list[start][indexScore + n] != " ":
                    n += 1
                else: break   
            
            lastscore = tblast_list[start][indexScore:indexScore + n]
            nScore = round(float(lastscore))
            
            # to the next Score value
            start += 1
            numbermarker += 1
    
            # recording contig IDs with a satisfactory Score
            if nScore < threshold:
                break
            f2.write( markername +  "\t" + str(numbermarker) + "\t" + tblast_list[start-1].split()[0] + '\n')
            
# Data:
DATA_DIR="" # relative path

with open('tdgfs_name.txt', 'r') as f1:
    tdgf_list = f1.read().splitlines()
Threshold = 250

# Work:
for i in tdgf_list: find_contigs(i, Threshold)








