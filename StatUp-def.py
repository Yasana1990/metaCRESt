import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import spearmanr
from scipy.stats import pearsonr

def desai_processing(Funx, FunxBact, rel = 'yes'):
    df = pd.read_csv('desai.txt', sep = '\t')    
    lstBact = []
    for fb in range(0, len(FunxBact)):
        lstBact += FunxBact[fb]
    dct = {}
    df = df[df.Sampletype == 'cecal']
    for f in Funx:
        dct[f] = {}    
        for g in df.Group.unique():
            dfG = df[df.Group == g]
            dct[f][g] = []  
            for i in dfG.index:
                var = 0
                for fb in range(0, len(FunxBact[Funx.index(f)])):
                    var += df.loc[i, FunxBact[Funx.index(f)][fb]] 
                # to relative values
                if rel == 'yes':
                    allF = 0   
                    for b in range(0, len(lstBact)):
                        allF += df.loc[i, lstBact[b]] 
                elif rel == 'no': allF = 100
                else: print('incorrect input!')
                dct[f][g].append(var/allF)
    return(dct)
            
def functional_processing(Funx, rel = 'yes', zoomFactor = 5000):
    dct = {}
    # summarizing TPM for all contigs
    for f in Funx:
        df = pd.read_csv('upTPM_' + f + '.txt', sep = '\t')
        dct[f] = {}
        for d in df.diet.unique():
            sm = df.loc[df['diet'] == d, 'TPM'].sum()       
            dct[f][d] = [sm/zoomFactor]
    # to relative values
    if rel == 'yes':       
        for d in df.diet.unique():
            smR = 0
            for f1 in Funx: smR += dct[f1][d][0]
            for f2 in Funx: dct[f2][d][0] = dct[f2][d][0]/smR

    elif rel != 'no':
        print('incorrect input!')
    
    # combining biological replica by diet type
    for f in Funx: 
        for d in df.diet.unique():
            tD = d
            while (tD[-1]) in str(list(range(0,10))): tD = tD [0:-1]  
            if tD not in dct[f]:
                dct[f][tD] = dct[f].pop(d)           
            else: 
                dct[f][tD] += dct[f].pop(d)
    return(dct)

def plotting(funcGroup, deletionList = []):

    for dietDel in deletionList: 
        if dietDel in dataFunc[funcGroup]: del dataFunc[funcGroup][dietDel]
    for dietDel in deletionList: 
        if dietDel in dataTax[funcGroup]: del dataTax[funcGroup][dietDel]
        
    abundance = []
    dietLst = []
    method = []
    marker = []
    for diet in dataFunc[funcGroup]:
        for i in range(0,len(dataFunc[funcGroup][diet])):
            abundance.append(dataFunc[funcGroup][diet][i])
            dietLst.append(diet)
            method.append('Functional_marker:'+funcGroup)
            marker.append(funcGroup)
            
    for diet in dataTax[funcGroup]:
        for i in range(0,len(dataTax[funcGroup][diet])):
            abundance.append(dataTax[funcGroup][diet][i])
            dietLst.append(diet)
            method.append('Amplicon_16S_rRNA')
            marker.append(funcGroup)
    titleY = 'Relative_abundance'
    dataInput = pd.DataFrame(data={titleY: abundance,
                                    'Diet': dietLst,
                                    'Method': method,
                                    'Marker': marker})
    
    sns.catplot(x="Diet", y=titleY, hue="Method", kind="point", data=dataInput)

def calculate_statistics(funcGroup, deletionList = []):

    for dietDel in deletionList: 
        if dietDel in dataFunc[funcGroup]: del dataFunc[funcGroup][dietDel]
    for dietDel in deletionList: 
        if dietDel in dataTax[funcGroup]: del dataTax[funcGroup][dietDel]
        
    #pairwise match all values from dataFunc to all values from dataTax for each functional group:
    a = []
    b = []
    for k in dataFunc['muc2'].keys():
        for i in dataFunc['muc2'][k]:
            for j in dataTax['muc2'][k]: a.append(i)
        
        b += dataTax['muc2'][k]*len(dataFunc['muc2'][k]) 
    
    print(spearmanr(a,b))
    print(pearsonr(a,b))


#Data:
Markers = ['muc2', 'but1','acet1','sulfat1']
# list of bacteria corresponding to functional groups:
LstBacteria = [['Amuc','Bc','Bt','Bar'], ['Eur','Ros','Csum','Fpra'],['Mfor'],['Des']]  
usedМarker = 'sulfat1'
deletedDiets = ['FP','P']

#Work:
# dataTax = desai_processing('no')           
# dataFunc = functional_processing('no')
dataTax = desai_processing(Markers,LstBacteria)           
dataFunc = functional_processing(Markers)

plotting(usedМarker,deletedDiets)
calculate_statistics(usedМarker,deletedDiets)
    