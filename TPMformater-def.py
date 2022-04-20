# Transform the contig abundance file so that all contigs are numbered as nameN_M, 
# where name is the name of the functional group, 
# N is the marker number, and M is the contig number

def formatting(markername):
    
    # raw file reading
    with open('rawTPM_' + markername + '.txt', 'r') as f1:
        tpm_list = f1.read().splitlines()
        
        for i in range(0, len(tpm_list)):
            tpm_list[i] = tpm_list[i].replace(':', '\t')
            tpm_list[i] = tpm_list[i].split('\t')    
    
    with open('ContigID_'+markername+'.txt', 'r') as f2:
        dict_list = f2.read().splitlines()
        
        for i in range(0, len(dict_list)):
            dict_list[i] = dict_list[i].split('\t')               
    
        # contig ID replacement
        for i in range(0, len(dict_list)):
            for j in range(0, len(tpm_list)):
                if tpm_list[j][1] == dict_list[i][2]:
                    tpm_list[j][1] = dict_list[i][0] + '_' + dict_list[i][1]
           
        tpm_list.sort(key = lambda x: x[1])
    
    with open('upTPM_' + markername + '.txt', 'w') as f3:
        f3.write('marker\tdiet\tlength\teff.len\tcount\tTPM\n')
        for i in range(0, len(tpm_list)):
            
            # reorder columns
            memory = tpm_list[i][0]
            tpm_list[i][0] = tpm_list[i][1]
            tpm_list[i][1] = memory.split('/')[-2].split('.')[0]
           
            for j in range(0, 5):
                f3.write(tpm_list[i][j] + '\t')
            f3.write(tpm_list[i][5] + '\n')
     
# Data:
with open('tdgfs_name.txt', 'r') as f1:
    tdgf_list = f1.read().splitlines()

# Work:
for i in tdgf_list: formatting(i)













