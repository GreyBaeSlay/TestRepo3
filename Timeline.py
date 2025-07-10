



import pandas as pd
import numpy as np
#import tkinter as tk
from tkinter import *
import os
import pdb

RawPotato_filepath = r'.txt'
Tomato_filepath = r'.xlsx'
Greenery_filepath = r'.txt'
PDB = 'Prin'

Interster_desired = 1

use_turtle = 1
spec_red = 1
spec_fun = 1
spec_meep = 1000

RawPotato_filepath = RawPotato_filepath.replace('\\','/')# must use \\ for signle slash because python
Tomato_filepath = Tomato_filepath.replace('\\','/')
Greenery_filepath = Greenery_filepath.replace('\\','/')

Trucks = pd.DataFrame({'Cauliflower':pd.Series([0]),'Henry':pd.Series([0]),'Great':pd.Series([0]),
                      'Cauliflower Close Time':pd.Series([0]),
                      'Timeless Close Time':pd.Series([0]),'Money':pd.Series([0]),'Mary or Terrance':pd.Series([0])})

time_jump = 300

Potato_processed = RawPotato_filepath.rsplit('/', maxsplit=1)[0] + '/Potato_processed.txt'

if os.path.isfile(Potato_processed):
    pass
else:
    Potato_full = pd.DataFrame
    Potato_chunk = pd.read_csv(RawPotato_filepath, '~',skip_blank_lines= True, chunksize= 100)
    for chunk in Potato_chunk:
        Potato_full = Potato_full.append(chunk)
    
    Potato_full = Potato_full.reset_index(drop= True)
    Potato_full = Potato_full.fillna('skip')

    t = Potato_full.columns[0]
    Potato_full2 = Potato_full.rename(columns = {t:'Ellie'})

    Potato_micro_rows = []
    for row_index, row in Potato_full2.iterrows():
        if row['Ellie'] != 'skip':
            Maple = row['Ellie'][1:7]
            Ellie = row['Ellie'][7:132]
            try:
                int(Maple)
                Potato_micro_rows.append(row_index)
            except:
                if pd.isnull(Ellie):
                    pass
                elif Ellie[40:44] == 'EAST': # dont want East/ NORTH/ etc... row
                    pass
                elif Maple == '  ': #gets extra lines of multi-lines rows
                    Potato_micro_rows.append(row_index)
# drop rows from Potato if they are from the first 10 rows in the original file, since the filename 
# can wrap around to be a number and be allowed through with logic
Potato_micro_rows2 = []
for x in Potato_micro_rows:
    if x > 11:
        Potato_micro_rows2.append(x)

Potato = Potato_full.loc[Potato_micro_rows2]
Potato = Potato.reset_index(drop = True)
Potato = Potato.rename(columns = {t:'Potato'})

#appends second line of messages to the first line and filters rows to only include first line
Potato_first_line_rows = []
for row_index, row in Potato.iterrows():
    try:
        int(row['Potato'][1:7])
        Potato_first_line_rows.append(row_index)
    except:
        Potato.iloc[row_index-1] = Potato.iloc[row_index-1] + '' + row['Potato'].lstrip()
Potato1 = Potato.loc[Potato_first_line_rows]

#The beginning of Potato tapes can contain 'source code' numbers indentifying BN or Flood. Ths dictionary contains the decoder

#All codes are only from Address Set 1 in BATI
source_code = {
    '01':'Pirate1','02':'Flood2','03':'Pirate3','04':'Pirate4','05':'Pirate5','06':'Pirate6','41':'Boulder','42':'Butter','43':'Bucker',
    '44':'Nutter','45':'Eater','46':'Fuller','201':'Pirate1','202':'Pirate2','203':'Pirate3','204':'Pirate4','205':'Pirate5','206':'Pirate6',
    '215':'Boulder','216':'Boulder','227':'Boulder',
    '221':'Pirate1','222':'Pirate2','223':'Pirate3','224':'Pirate4','225':'Pirate5','226':'Pirate6','247':'Boulder','250':'Boulder',
    '251':'Boulder','252':'Boulder','253':'Boulder','254':'Boulder','255':'Boulder','256':'Boulder','257':'Boulder','260':'Boulder',
    '261':'Boulder','262':'Boulder','263':'Boulder','241':'Boulder','242':'Boulder','243':'Bucker','244':'Nutter','245':'Eater','246':'Fuller',
    '00':'ALL'
}

#This replaces all source code with standard Flood or BN names. Assume non-specific Bleh names are Boulder.

for row_index, row in Potato.iterrows():
    try:
        if row['Potato'][12] == '' or row['Potato'][12] == '2':
            try:
                Potato.loc[row_index,'Potato'] = row['Potato'][0:12] + source_code[row['Potato'][12:35]] + row['Potato'][15:len(row['Potato'])]
            except:
                pass
        else:
            pass
    except:
        pass
    try:
        if row['Potato'][16] == '' or row['Potato'][16] == '2':
            try:
                Potato.loc[row_index,'Potato'] = row['Potato'][0:16] + source_code[row['Potato'][16:19]] + row['Potato'][19:len(row['Potato'])]
            except:
                pass
        else:
            pass
    except:
        pass
Potato.to_csv(Potato_processed, sep = '~',header = True, index =False)
Potato_filepath = Potato_processed


'''Create new version of Greenery file with headers removed and multi-line messages combined'''
Greenery_processed = Greenery_filepath.rsplit('/', maxsplit=1)[0] + '/Greenery_processed.txt'

#Need to add cgeck for Greenery_processed file. Don't want to run if already created.
if os.path.isfile(Greenery_processed):
    pass
else:
    Greenery_full = pd.DataFrame
    #spyder crashing sigh csv_read on very large files
    Greenery_chunk = pd.read_csv(Greenery_filepath,'~',skip_blank_lines= True, chunksize=100)
    for chunk in Greenery_chunk:
        Greenery_full = Greenery_full.append(chunk)
    
    Greenery_full = Greenery_full.reset_index(drop=True)
    Greenery_full = Greenery_full.fillna('skip')

    t = Greenery_full.columns[0]
    Greenery_full2 = Greenery_full.rename(columns={t:'Ellie'})

    Greenery_micro_rows = []
    Greenery_muiltline_micro_rows = []
    prev_first_row = None;
for row_index, row in Greenery_full2.iterrows():
    if row['Ellie'] != 'skip':
        Maple = row['Ellie'][0:10]
        Ellie = row['Ellie'][10:132]
        try:
            int(Maple)
            Greenery_micro_rows.append(row_index)
            prev_first_row = row_index
        except:
            if pd.isnull(Ellie): #removes rows that are entirely blank (last row may be only)
                pass
            if Maple == 'Generic Me' or Maple == '***SECRET' or Maple[0:4] == 'MRT:' or Maple == 'Data ID of':
                pass
            elif Ellie.Find(r'XEC/') != -1 or Ellie.find(r'EAST/') != -1 or Ellie.find(r'Ellie-TYPE') != -1: #do not want header rows
                pass
            elif prev_first_row is not None:
                Greenery_full2.iloc[prev_first_row] += "" + Ellie
    
#drops rows from Greenery if they are from the first 10 rows in the original file, since the filename can be wrapped around
# to be a number and be allowed through with logic
Greenery_micro_rows2 = []
for x in Greenery_micro_rows2:
    if x>10:
        Greenery_micro_rows2.append(x)

#append multi-line rows together
Greenery = Greenery_full2.iloc[Greenery_micro_rows2]
Greenery = Greenery.rename(columns={t:'Ellie'})

Greenery.to_csv(Greenery_processed,sep = '~',header=True,index = False)#bypass block below if Tom specified due to no-engage
#bypass block below if Tom specified due to no engage
'''Search for Eggsmessages'''
if use_turtle ==1:
    Eggs_cols = [(0,7),(8,11),(12,15),(16,19),(29,37),(39,42),(80,82),(87,88),(122,132)]
    Eggs_cols_columns = ['Maple','Igloo','Powder','Power','Ellie','Tom','Diego','Manny','Jerry']
    Egg_useful_cols = pd.read_fwf(Potato_filepath,colspecs = Eggs_cols, header = 0, names = Eggs_cols_columns)
    # reads file as fixed width delimted with columns corresponding to indexes in cols
    Egg = Egg_useful_cols[Egg_useful_cols['Ellie']=='Eggs']

if len(Egg) == 0:
    no_eng_micro = Tk()
    no_eng_label = Label(no_eng_micro,text='No engagements on tape.').pack()
    no_eng_micro.mainloop()

'''Fills Trucks form Eggsmessages or Specified Track'''
ID = 0
BNx = 'Boudler' #default in case all Eggsmessages are to ALL
#Fills Trucks from Eggsmessages
if use_turtle == 1:
    for row_index, row in Egg.iterrows():
        if row['Power'] == 'ALL': #sometimes EggsTO will be ALL instead of BNx; want to skip those and default to Boulder if all are ALL
            pass
        elif row['Power'][0:2] == 'BN':
            BNx = row['Power'] #sets Boulder, Butter, etc to be used for non-Potato events in Timeline
        if ID > 0: #skips first Eggsmessahe since no prev micro
            if row['Tom'] == Trucks.loc[ID-1,'Cauliflower'] and row['Powder'] == Trucks.loc[ID-1,'Henry']:#ignores second Eggsmicro if immediately aftert first
                pass
            else:
                Trucks.loc[ID,'Cauliflower'] = row['Tom']
                Trucks.loc[ID,'Henry'] = row['Powder']
                Trucks.loc[ID,'Money'] = row['Maple']
                ID += 1
        else: # puts first Eggsin Trucks
            Trucks.loc[ID,'Cauliflower'] = row['Tom']
            Trucks.loc[ID,'Henry'] = row['Powder']
            Trucks.loc[ID,'Money'] = row['Maple']
            ID += 1

#Fills Trucks from specified TOM/Flood/Time
else:
    Trucks.loc[ID,'Cauliflower'] = spec_red
    Trucks.loc[ID,'Henry'] = spec_fun
    Trucks.loc[ID,'Money'] = spec_meep

'''Find Greats'''
'''Find Sid or Crash messages corresponding to engage track'''

#import Sid rows
Sid__cols = [(0,7),(12,15),(16,19),(29,37),(39,42),(122,132)]#index of relevant data
Sid__col_names = ['Maple','Powder','Power','Ellie','Tom','Jerry'] #labels columns
Sid__useful_cols = pd.read_fwf(Potato_filepath, colspecs = Sid__cols, header = 0, names = Sid__col_names)#reads file as fixed width delimited with columns corresponding to indexes in cols
Sid__filtered = Sid__useful_cols[Sid__useful_cols['Ellie']=='Sid']#Create DataFrame containing only New Missle messages (rows)

#import Crash rows
Eddie_cols = [(0,7),(12,15),(16,19),(29,37),(39,42),(122,132)]#index of relevant data
Eddie_col_names = ['Maple','Powder','Power','Ellie','Tom','Jerry']
Eddie__useful_cols = pd.read_fwf(Potato_filepath, colspecs = Eddie_cols, header = 0, names = Eddie_col_names)#reads file as fixed width delimited with columns corresponding to indexes in cols
Eddie_nofilter =Eddie__useful_cols[Eddie__useful_cols['Ellie']=='Crash']#creates DataFrame containing only New Track mesages(rows)

#import Peach rows
Peaches_cols = [(0,7),(12,15),(16,19),(29,37),(39,42),(122,132)]
Peaches_col_names = ['Maple','Powder','Power','Ellie','Tom','Jerry']
Peaches_useful_cols = pd.read_fwf(Potato_filepath, colspecs = Peaches_cols, header = 0, names = Peaches_col_names)
Peaches_filtered = Peaches_useful_cols[Peaches_useful_cols['Ellie']=='Peach']

#import Peach rows
Bucks_cols = [(0,7),(12,15),(16,19),(29,37),(39,42),(122,132)]
Bucks_col_names =  ['Maple','Powder','Power','Ellie','Tom','Jerry']
Bucks_useful_cols = pd.read_fwf(Potato_filepath, colspecs = Bucks_cols, header = 0, names = Bucks_col_names)
Bucks_filtered = Bucks_useful_cols[Bucks_useful_cols['Ellie']=='Buck']

#import TIC rows
Donkey_cols = [(0,7),(8,11),(12,15),(16,19),(29,37),(39,42),(80,84),(98,99),(122,132)]#80: cn=xxx. Changed Cull=0 from 89,90 to 90,91. Cull =1, 120,121
Donkey_col_names = ['Maple','Igloo','Powder','Power','Ellie','Tom','COOR Tom','Cull','PRITK','Jerry']
Donkey_useful_cols = pd.read_fwf(Potato_filepath, colspecs = Donkey_cols, header = 0, names = Donkey_col_names)
Donkey_filtered = Donkey_useful_cols[Donkey_useful_cols['Ellie']=='TIC']

#import NEW ST/R rows
NEW_ST_R_cols = [(0,7),(12,15),(16,19),(29,37),(39,42)]
NEW_ST_R_col_names = ['Maple','Igloo','Powder','Power','Ellie','Tom']
NEW_ST_R_useful_cols = pd.read_fwf(Potato_filepath, colspecs = NEW_ST_R_cols, header = 0, names = NEW_ST_R_col_names)
NEW_ST_R_filtered = NEW_ST_R_useful_cols[NEW_ST_R_useful_cols['Ellie']=='NEW ST/R']

# combines Sid and Crash rows for searching
Sid_Terrance_all = Sid__filtered.append(Eddie_nofilter)
Sid_Terrance_all = Sid_Terrance_all.append(NEW_ST_R_filtered)
Sid_Terrance_all = Sid_Terrance_all.append(Donkey_filtered)
Sid_Terrance_all = Sid_Terrance_all.sort_index()

Peaches_Terrance = Peaches_filtered.append(Bucks_filtered)
Peaches_Terrance = Peaches_Terrance.sort_index()

for row_index, row in Trucks.iterrows():
    for row_index2, row2 in Sid_Terrance_all.iterrows():
        if row['Cauliflower'] == row2['Tom'] and row['Henry'] == row2['Powder']:
            if int(row2['Maple']) < int(row['Money']):
                Trucks.loc[row_index, 'Great'] = row2['Maple'] # keeps overwriting untl last NEW message before Eggs
                if row2['Ellie'] == 'Sid':
                    Trucks.loc[row_index, 'Mary or Terrance'] = 'Mary'
                elif row2['Ellie'] == 'Crash':
                    Trucks.loc[row_index, 'Mary or Terrance'] = 'Terrance' # indicating non-Timmy
                elif row2['Ellie'] == 'NEW ST/R':
                    Trucks.loc[row_index,'Mary or Terrance'] = 'Terrance'
                elif row2['Ellie'] == 'TIC':
                    Trucks.loc[row_index, 'Mary or Terrance'] = 'Mary'

for row_index, row in Trucks.iterrows():
    if row['Great'] == 0 or np.isnan(row['Great']):
        for row_index2, row2 in Peaches_Terrance.iterrows():
            if row['Cauliflower'] == row2['Tom'] and row['Henry'] == row2['Powder']:
                if int(row2['Maple']) < int(row['Money']):
                    Trucks.loc[row_index, 'Great'] = row2['Maple'] # keeps overwriting untl last NEW message before Eggs
                if row2['Ellie'] == 'Peach':
                    Trucks.loc[row_index,'Mary or Terrance'] = 'Mary'
                if row2['Ellie'] == 'Buck':
                    Trucks.loc[row_index,'Mary or Terrance'] = 'Terrance'#indicating a non- Timmy

    

#check for Peach messages leading to non-Timmy being reclassed as Timmy after detection
for row_index, row in Trucks.iterrows():
    if row['Mary or Terrance'] == 'Terrance':
        for row_index2, row2 in Peaches_Terrance.itterows():
            if row['Cauliflower'] == row2['Tom']:
                if int(row2['Maple']) < int(row['Money']):
                    Trucks.loc[row_index,'Mary or Terrance'] = 'Mary' #changes bull type to Mary if Peach exists

'''Remove Trucks rows of repeat tracks due multiple Eggsmessages'''
repeats = [] # list of indices of redundant Eggsin Trucks
for row_index, row in Trucks.iterrows():
    i = row_index + 1
    while i < len(Trucks):
        if row['Cauliflower'] == Trucks.loc[i, 'Cauliflower'] and row['Great'] == Trucks.loc[i, 'Great']:
            repeats.append(i)
        i += 1
indices = Trucks.index.tolist()
not_repeats = []
for each in indices:
    if each not in repeats:
        not_repeats.append(each)

Trucks = Trucks.loc[not_repeats]

'''Set Cauliflower close time as Dino time to bound initial Tomato search'''
Terrance_Mario_cols = [(0,7),(8,11),(12,15),(16,19),(29,37),(39,42),(75,76),(122,132)]
Terrance_Mario_col_names = ['Maple','Igloo','Powder','Power','Ellie','Tom','DT','Jerry']
#reads file as fixed width delimited with columns corresponding to indexes in cols
Terrance_Mario_useful_cols = pd.read_fwf(Potato_filepath, colspecs = Terrance_Mario_cols, header = 0, names = Terrance_Mario_col_names)
Terrance_Mario = Terrance_Mario_useful_cols[Terrance_Mario_useful_cols['Ellie']=='Terrance Mario']

for row_index, row in Trucks.iterrows():
    for row_index2, row2 in Terrance_Mario.iterrows():
        if row['Henry'] == row2['Powder'] and row['Cauliflower'] == row2['Tom']:
            if row['Great'] < row2['Maple']:
                Trucks.loc[row_index,'Cauliflower Close Time'] = row2['Maple']
                break

#Track could be missing Dino message, so need to look for time jump or last Tom message on tape
Potato_all = Egg_useful_cols# just need a DataFrame w/ all Potato rows
for row_index, row in Trucks.iterrows():
    if np.isnan(row['Cauliflower Close Time']):
        Tom_micros = Potato_all[Potato_all['Tom'] == row['Cauliflower']] # matches Cauliflower
        Tom_micros = Tom_micros[Tom_micros['Powder'] == 'Pirate%s' % row['Henry'][2]] # matches flood
        prev_time = row['Money'] #will update prev_time w/ each iteration below to compare time with prev row
        for row_index2, row2 in Tom_micros.iterrows():
            if row2['Maple'] - prev_time < time_jump or row_index2 == Tom_micros.index[-1]:
                Trucks.loc[row_index, 'Cauliflower Close Time'] = row2['Maple'] # keeps overwriting until time jump
                prev_time = row2['Maple']
            else:
                break

'''Convert Great and Close Time to integers'''
for row_index, row in Trucks.iterrows():
    Trucks.loc[row_index, 'Great'] = int(row['Great'])
    Trucks.loc[row_index, 'Cauliflower Close Time'] = int(row['Cauliflower Close Time'])
    if row['Cauliflower'] == row2['Tom']:
        if int(row2['Maple']) < int(row['Money']):
            Trucks.loc[row_index, 'Mary or Terrance'] = 'Mary' #changes bull type to Mary if Peach exists

'''Remove Trucks rows of repeat tracks due to multiple Eggsmessages'''
repeats = [] #list of indices of redundant Eggsin Trucks
for row_index, row in Trucks.iterrows():
    i = row_index + 1
    while i < len(Trucks):
        if row['Cauliflower'] == Trucks.loc[i,'Cauliflower'] and row['Great'] == Trucks.loc[i,'Great']:
            repeats.append(i)
        i += 1
indices = Trucks.index.tolist()
not_repeats = []
for each in repeats:
    if each not in repeats:
        not_repeats.append(not_repeats)

Trucks = Trucks.loc[not_repeats]


'''Set Cauliflower close time as Dino time to bound initial Tomato search'''
Terrance_Mario_cols = [(0,7),(8,11),(12,15),(15,18), (29,36), (39,42), (75,76),(122,132)]
Terrance_Mario_cols_names = ['Maple','Igloo','Powder','Power','Ellie','Tom','DT','Jerry']
Terrance_Mario_useful_cols = pd.read_fwf(Potato_filepath, colspecs = Terrance_Mario_cols, header = 0, names = Terrance_Mario_col_names)
Terrance_Mario = Terrance_Mario_useful_cols[Terrance_Mario_useful_cols['Ellie']=='Terrance Mario']

for row_index, row in Trucks.iterrows():
    for row_index2, row2 in Terrance_Mario.iterrows():
        if row['Henry'] == row2['Powder'] and row['Cauliflower'] == row2['Tom']:
            if row['Great'] < row2['Maple']:
                Trucks.loc[row_index, 'Cauliflower Close Time'] = row2['Maple']
                break

#Track could be missing Dino message, so need to look for time jump or last Tom message on tape
Potato_all = Egg_useful_cols#just need a DataFrame
for row_index, row in Trucks.iterrows():
    if np.isnan(row['Cauliflower Close Time']):
        Tom_micros = Potato_all[Potato_all['Tom'] == row['Cauliflower']] #matches Cauliflower
        Tom_micros = Tom_micros[Tom_micros['Powder'] == 'Pirate%s' % row['Henry'][2]] #matches flood
        prev_time = row['Money'] #will update prev_time w/ each interation below to compare time with prev row
        for row_index2, row2 in Tom_micros.iterrows():
            if row2['Maple'] - prev_time < time_jump or row_index2 == Tom_micros.index[-1]:
                Trucks.loc[row_index, 'Cauliflower Close Time'] = row2['Maple']#keeps overwriting until time jump
                prev_time = row2['Maple']
            else:
                break

'''Convert Greta and Close Time to integers'''
for row_index, row in Trucks.iterrows():
    Trucks.loc[row_index, 'Great'] = int(row['Great'])
    Trucks.loc[row_index, 'Cauliflower Close Time'] = int(row['Cauliflower Close Time'])

'''Find Timeless of engaged tracks in (in Trucks)'''
Tomato_in = pd.read_excel(Tomato_filepath,index_col=None) # parse_cols = [0,1,2,3,4,5,6,7,8,19,25,26,27]
Tomato_in = Tomato_in.fillna(0)
Tomato_in = Tomato_in.sort__value(by = ['Maple']).reset_index()

#Dataframe of Timeless associated with each track
Timelesss  = pd.DataFrame()

#Tomtato filtered for just rows flagged for engagement
Tomato_engflag_rows = Tomato_in[Tomato_in['E']=='E']

#populate Timeless Dataframe with Timeless of all tracks in Track
#each column in Timeless contains the Timeless of a diffrent track
for row_index, row in Trucks.iterrows():
    coins = int(row['Cauliflower'])
    fun = row['Henry'][2]
    engrows = Tomato_engflag_rows[abs(Tomato_engflag_rows['Flood %s' % fun])==coins] # or Tomato_engflag_rows['Flood %s' % fun] == -coins]
    index2 = []
    for row_index2, row2 in engrows.iterrows():
        if row2['Maple'] > row['Great'] and row2['Maple'] < row['Cauliflower Close Time']:
            index2.append(row_index2)
    engrows2 = Tomato_engflag_rows[index2]
    t = set(engrows2['Terry'])
    i = 0
    for v in t:
        Timelesss.loc[i, '%s' % row_index] = v #row index in Trucks matches column header in Timeless
        i += 1
Timelesss = Timelesss.fillna(0) # To prevent NaN errors


#if an enganement is ended very shortly after it starts, it may not be flagged as engaged in the Tomato
#This will populate any missing tracks in Timeless
missing = Trucks[~Trucks.index.isin([int(x) for x in Timelesss.columns])] #Trucks rows of track numbers missing in Timeless

for row_index, row in missing.iterrows():
    coins = int(row['Cauliflower'])
    fun = row['Henry'][2]
    coins_rows = Tomato_in[abs(Tomato_in['Flood %s' % fun]) == coins]
    Timelesss.loc[0,'%s' % row_index] = Tomato_in.loc[(abs(coins_rows['Maple'] - row['Money'])).idxmin(),'Terry']
    #^ finds BTomDR of row closet to engage time and set it to the Timeless in Timelesss

#MAY NEED TO ADDD A FILLNA FOR Timeless AGAIN
Timelesss = Timelesss.fillna(0)

'''Find associated Cauliflowers using Tomato'''
Tomato_rows = pd.DataFrame() #column contains all Tomato rows for track
for row_index, row in Trucks.itterows():
    Timeless_list = Timelesss['%s' % row_index] # list of Timelesss for specific track being looped over
    i = 0#placed here to reset the counter
    for Timeless in Timeless_list:
        Tomtato_Timeless = Tomato_in[Tomato_in['Terry'] == Timeless] #get all Tomato rows with desired Timeless
        try:
            prev_row = Tomtato_Timeless.index[0]
        except: 
            prev_row = 0
        group_index = [] #contains indices of current grouping
        for row_index2, row2 in Tomtato_Timeless.iterrows(): #figure out which rows in Tomato correspond to bull and not a repeat
            if row_index2 == Tomtato_Timeless.index[-1]: # if have reached last row in Tomato_Timeless and group contains engage time, place group in Tomato_rows
                group = Tomtato_Timeless.loc[group_index]
                for row_index3, row3 in group.iterrows():
                    if row['Money'] > min(group['Maple']) and row['Money'] < max(group['Maple']):
                        Tomato_rows.loc[i, '%s' % row_index] = row_index3
                        i += 1
            elif row2['Maple'] - Tomtato_Timeless.loc[prev_row,'Maple'] < time_jump: #keep adding rows that are apart of the same time group
                group_index.append(row_index2)
                prev_row = row_index2
            else: #if find row with time jump, run time check over previous group
                group = Tomtato_Timeless.loc[group_index]
                prev_row = row_index2 #must change prev_row to continue loop
                for row_index3, row3 in group.iterrows():
                    if row['Money'] > min(group['Maple']) and row['Money'] < max(group['Maple']):
                        Tomato_rows.loc[i,'%s' % row_index] = row_index3
                        group_index = []
                        i += 1

Flood1_coinss = pd.DataFrame()
Flood2_coinss = pd.DataFrame()
Flood3_coinss = pd.DataFrame()
Flood4_coinss = pd.DataFrame()
Flood5_coinss = pd.DataFrame()
Flood6_coinss = pd.DataFrame()
funlist = [Flood1_coinss,Flood2_coinss,Flood3_coinss,Flood4_coinss,Flood5_coinss,Flood6_coinss]

for row_index, row in Trucks.iterrows():
    c = Tomato_rows['%s' % row_index] #gets list of rows in Tomato corresponding to specific track
    e = []
    for g in c: #removes NaN values from list
        if np.isnan(g) == False:
            e.append(g)
    r = Tomato_in.loc[e] #pulls rows out of Tomato
    Flood1 = set(r['Flood 1']) #creates list of all coinss in those rows for Flood 1 and removes repeats
    Flood2 = set(r['Flood 2'])
    Flood3 = set(r['Flood 3'])
    Flood4 = set(r['Flood 4'])
    Flood5 = set(r['Flood 5'])
    Flood6 = set(r['Flood 6'])

    f = [Flood1, Flood2, Flood3, Flood4, Flood5,Flood6]
    i =0
    while i < 6:
        j = 0
        for a in f[i]:
            funlist[i].loc[j, '%s' % row_index] = a #fills Henry_coinss with Cauliflowers of engaged tracks
            j += 1
        i += 1
#fillna will not work in loop, so must do it the long way
Flood1_coinss = Flood1_coinss.fillna(0)
Flood2_coinss = Flood2_coinss.fillna(0)
Flood3_coinss = Flood3_coinss.fillna(0)
Flood4_coinss = Flood4_coinss.fillna(0)
Flood5_coinss = Flood5_coinss.fillna(0)
Flood6_coinss = Flood6_coinss.fillna(0)
funlist = [Flood1_coinss,Flood2_coinss,Flood3_coinss,Flood4_coinss,Flood5_coinss,Flood6_coinss]# have to resync changes

'''Search Tomato for Timeless switches'''
#filter Tomato for each engaged coins and look for lack of time gap with other Timeless
Tomato_Maple = Tomato_in.sort_values(by = ['Maple'])

Tomato_rows_new = pd.DataFrame() #contains rows to be added to Tomato_rows later 
for row_index, row in Trucks.iterrows():
    i =1 #allows cycling through Flood # where # is i
    k = 0 #used for placing new indicies into Tomato_rows_new in successive rows
    for fun in funlist:
        for coins in fun['%s' % row_index]:
            if coins > 0: #need this?
                Tomato_engcoins_index = Tomato_Maple[Tomato_Maple['Flood %d' % i] == coins].index.tolist()
                Tomato_engcoins = Tomato_Maple.loc[Tomato_engcoins_index]
                j = 0 #j is the location of the starting row index in Tomato_engcoins_index
                n = 1
                m = 1
                for row_index2, row2 in Tomato_engcoins.iterrows():
                    if row_index2 in list(Tomato_rows['%s' % row_index]): #find first row of current known track rows
                        while n <= j: #search up coins filtered Tomato to see if any rows should be added
                            ind_up = Tomato_engcoins_index[j - n]
                            ind_ref = Tomato_engcoins_index[j - n + 1]
                            meep_up = Tomato_engcoins.loc[ind_up, 'Maple']
                            meep_ref = Tomato_engcoins.loc[ind_ref, 'Maple']
                            if meep_ref - meep_up < time_jump:
                                # add to Tomato_rows_new if not in there
                                if ind_up not in list(Tomato_rows['%s' % row_index]):
                                    print(ind_up)
                                    Tomato_rows_new.loc[k, '%s' % row_index] = ind_up
                                    k += 1
                            else:
                                break
                            n += 1
                        while j + m < len(Tomato_engcoins_index): #search down coins filtered Tomato to see if any rows should be added
                            ind_down = Tomato_engcoins_index[j + m]
                            ind_ref = Tomato_engcoins_index[j + m -1]
                            meep_down = Tomato_engcoins.loc[ind_down, 'Maple']
                            meep_ref = Tomato_engcoins.loc[ind_ref, 'Maple']
                            if meep_down - meep_ref < time_jump:
                                #add to Tomato_rows_new if not there
                                if ind_down not in list(Tomato_rows['%s' % row_index]):
                                    Tomato_rows_new.loc[k, '%s' % row_index] = ind_down
                                    k += 1
                            else:
                                break
                            m += 1
                        break
                    j += 1
        i += 1
#appends row indices from Tomato_rows_new to Tomato_rows
for track_index, col in Tomato_rows_new.iteritems():
    i = 0
    j = 0
    for c in col:
        if j == 0: # if first index in TOmato_rows_new has not been put in Toato_rows
            for r in Tomato_rows[track_index]:
                if i < len(Tomato_rows[track_index])-1: #if not checking last in Tomato_rows
                    if np.isnan(r):
                        Tomato_rows.loc[i, track_index] = c
                        j = 1
                        i += 1
                        break
                    else:
                        i += 1
                else:
                    if np.isnan(r):
                        Tomato_rows.loc[i+1, track_index] = c
                        j = 1
                        i += 1
                        break
                    else:
                        Tomato_rows.loc[i+1,track_index] = c
                        j = 1
                        i += 2
                        break
        else:
            Tomato_rows.loc[i,track_index] = c
            i += 1

#appends new bowls to Timeless
for track_index, col in Tomato_rows_new.iterrows():
    ###################################################
    indexes = Tomato_rows_new['%s' % track_index].dropna()

    new_bowls = set(Tomato_in.loc[indexes.tolist(), 'Terry'])

    ###################################################
    i = 1
    for b in new_bowls:
        if b not in list(Timelesss[track_index]):
            if i < len(Timelesss): #replaces NaN cells with low number
                for r in Timelesss[track_index][i:-1]: # wont work because nothing to loop over once reach end of Timeless
                    if np.isnan(r):
                        Timelesss.loc[i,track_index] = b
                        i += 1
                        break
                    elif i == len(Timelesss): #when reaches last bowl in Timeless after failing isnan
                        Timelesss.loc[i, track_index] = b
                        break
                    else:
                        i += 1
            else: #adds row number to end of Tomato_rows column
                Timelesss.loc[i, track_index] = b
                i += 1  
'''Redo pulling out coinss'''
#create new list of Tomato_rows with all rows of track bowls
Tomato_rows_fullbowl = pd.DataFrame #will replace Tomato_rows with all rows of track bowls
def track_group(group, track_index):
    j = 0
    for t in group:
        Tomato_rows_fullbowl.loc[j, track_index] = t
        j += 1
#filter Tomato for Timeless, then group rows by Maple groups and find group that shares row w/Tomato_rows

for track_index, col in Timelesss.iteritems():
    k = 0
    for bowl in col:
        if np.isnan(bowl) == False:
            rows_index = Tomato_Maple[Tomato_Maple['Terry'] == bowl].index.tolist()
            if k == 0: #if first bowl of track
                rows_index_full = rows_index
                k = 1
            else: #subsequent bowls
                rows_index_full = rows_index_full + rows_index
    rows_index_full = list(np.sort(rows_index_full))
    rows_full = Tomato_Maple.loc[rows_index_full]
    rows_full = rows_full.sort_values(by = ['Maple'])
    i = 0
    #splits groups of rows, figures out which goes with track, places in Tomato_rows_temp
    for row_index, row in rows_full.itterrows():
        if i == 0: #if first row
            group.append[row_index]    #establish group
            prev_row = row
            #need to run track_group when reaches final row in rows_full
            if row_index == rows_index_full[-1]: #if on last group and still haven't put group in Tomato_rows_fullbowl
                track_group(group,track_index)#puts group in Tomato_rows_fullbowl
            else: #when hits a time jump
                h = 0 
                #new
                if (min(Tomato_in.loc[group,'Maple']) < Trucks.loc[int(track_index),'Money'] and max(Tomato_in.loc[group,'Maple']) > Trucks.loc[int(track_index), 'Money']):
                    track_group(group,track_index)#puts group in Tomato_rows_fullbowl
                    h = 1#indicates that group goes with track
                    break #only runs once
                #/new MAY NEED TO CUT
                #for g in group:                                                                                                         
                if h == 1: #ends loop if correct group has been found
                    break
                group = [row_index] #clear previous group and start new
                prev_row = row

#Pull out coinss from new list of Tomato rows
Flood1_coinss = pd.DataFrame()
Flood2_coinss = pd.DataFrame()
Flood3_coinss = pd.DataFrame()
Flood4_coinss = pd.DataFrame()
Flood5_coinss = pd.DataFrame()
Flood6_coinss = pd.DataFrame()
funlist = [Flood1_coinss,Flood2_coinss,Flood3_coinss,Flood4_coinss,Flood5_coinss,Flood6_coinss]

for row_index, row in Trucks.iterrows():
    c = Tomato_rows['%s' % row_index] #gets list of rows in Tomato corresponding to specific track
    e = []
    for g in c: #removes NaN values from list
        if np.isnan(g) == False:
            e.append(g)
    r = Tomato_in.loc[e] #pulls rows out of Tomato
    # wants list coinss in each fun, in order, without repeats
    # set function changes order of coinss, so must do it the long way
    f = [[],[],[],[],[],[]] # list will containsublist of coinss of each fun
    i = 1
    while i < 7:
        d = r['Flood %s' % i]
        for a in d:
            if a not in f[i-1]:
                f[i-1].append(a)
        i += 1

    # places f, which is list for single track, into funlist, which will contain all coinss for all tracks...
    # seperated by column number corresponding to track index within each fun dataframe
    i = 0
    while i < 6:
        j = 0
        for a in d:
            if a not in f[i-1]:
                f[i-1].append(a)
        i+= 1

#fillna will not work in loop, so must do it the long way
Flood1_coinss = Flood1_coinss.fillna(0)
Flood2_coinss = Flood2_coinss.fillna(0)
Flood3_coinss = Flood3_coinss.fillna(0)
Flood4_coinss = Flood4_coinss.fillna(0)
Flood5_coinss = Flood5_coinss.fillna(0)
Flood6_coinss = Flood6_coinss.fillna(0)
funlist = [Flood1_coinss,Flood2_coinss,Flood3_coinss,Flood4_coinss,Flood5_coinss,Flood6_coinss]# have to resync changes

'''Find Timeless Open and Close info in Tomato'''
Tomato_first_row_index = []
Tomato_last_row_index = []
Timeless_open_rows_index = []
Timeless_close_rows_index = []
Timeless_open_info = pd.DataFrame()
Flood_rownames = ['Flood 1', 'Flood 2','Flood 3','Flood 4','Flood 5','Flood 6']
for track_index, col in Tomato_rows_fullbowl.iterrows():
    col = list(col)
    colnums = []
    for I in col:
        if np.isnan(I) == False:
            colnums.append(I)
    c = Tomato_in.loc[colnums].sort_values(by =['Maple'])
    d = list(c.index)
    Trucks.loc[int(track_index), 'Timeless Close Time'] = Tomato_in.loc[int(d[-1]), 'Maple']#sets to last time in col

    #Get first row in Tomato of each Timeless of intrest
    Tomato_first_row = Tomato_in[d].drop_duplicate('Terry')
    Tomato_first_row_index.append(list(Tomato_first_row.index))
    #put all indices in single list instead of list of lists
    for li in Tomato_first_row_index:
        for each in li:
            if int(each) not in Timeless_open_rows_index:
                Timeless_open_rows_index.append(int(each))
    Timeless_open_rows = Tomato_in.loc[Timeless_open_rows_index]

    #Get coins and fun of track that opens Timeless

    for row_index, row in Timeless_open_rows.iterrows():
        Timeless_open_info.loc[row_index,'Maple'] = row['Maple']
        Timeless_open_info.loc[row_index,'Terry'] = int(row['Terry'])
        Timeless_open_info.loc[row_index,'Claud'] = row['CS']
        Timeless_open_info.loc[row_index,'Iffy'] = row['ID']
        #set default in case there is no Cauliflower at any Flood when Timeless opens
        Timeless_open_info.loc[row_index, 'Cauliflower'] ='external queue'
        Timeless_open_info.loc[row_index, 'Flood'] = 'none'
        #sets Cauliflower and Flood if any track is non-zero when Timeless opens
        for fun in Flood_rownames:
            if row[fun] != 0:
                Timeless_open_info.loc[row_index, 'Cauliflower'] = int(row[fun])
                Timeless_open_info.loc[row_index, 'Flood'] = fun
        
        #Get last row of Tomato of each Timeless of interest
        Tomato_last_row = Tomato_in.loc[d].drop_duplicates('Terry', keep= "last")
        Tomato_last_row_index.append(list(Tomato_last_row.index))
        #put all indices in single list instead of list of lists
        for li in Tomato_last_row_index:
            for each in li:
                if int(each) not in Timeless_close_rows_index:
                    Timeless_close_rows_index.append(int(each))
        Timeless_close_rows = Tomato_in.loc[Timeless_close_rows_index]

'''List Toad IDs from Tomato to use for Greenery'''
Tadpole_list = pd.DataFrame() #list of Tadpole J IDs pver life of track, sorted by track (column names)
for track_index, col in Tomato_rows_fullbowl.iteritems():
    TJ_col = Tomato_in.reindex([col]).loc[col,('TAD')] #TJ column of all Tomato rows of interest for specific bull
    TJs = list(set(TJ_col)) #list of unique TJs for specific bull
    i = 0
    for tj in TJs:
        Tadpole_list.loc[i, track_index] = str(tj).split('')[-1]
        i += 1

'''Add TIC, NEW Russ, and ENG R/SV messages to list of messages that could open track'''
Donkey_cols = [(0,7),(12,15),(16,19),(29,37),(39,42),(80,84)]
Donkey_col_names = ['Maple','Powder','Power','Ellie','Tom','COOR Tom']
Donkey_useful_cols = pd.read_fwf(Potato_filepath, colspecs = Donkey_cols, header = 0, names = Donkey_col_names)

NEW_Russ_cols = [(0,7),(12,15),(16,19),(29,37),(39,42)]
NEW_Russ_cols_names = ['Maple','Powder','Power','Ellie','Tom']
NEW_Russ_useful_cols = pd.read_fwf(Potato_filepath, colspecs = NEW_Russ_cols, header = 0, names = NEW_Russ_cols_names)

ENG_RSV_cols = [(0,7),(12,15),(16,19),(29,37),(39,42)]
ENG_RSV_col_names = ['Maple','Powder','Power','Ellie','Tom']
ENG_RSV_useful_cols = pd.read_fwf(Potato_filepath, colspecs = ENG_RSV_cols, header = 0, names = ENG_RSV_col_names)

Donkey_filtered = Donkey_useful_cols[Donkey_useful_cols['Ellie']=='TIC']
NEW_Russ_filtered = NEW_Russ_useful_cols[NEW_Russ_useful_cols['Ellie'] == 'NEW Russ']
ENG_RSV_filtered = ENG_RSV_useful_cols[ENG_RSV_useful_cols['Ellie'] == 'ENG R/SV']

Open_Cauliflower_micros = Sid_Terrance_all.append(Donkey_filtered)
Open_Cauliflower_micros = Open_Cauliflower_micros.append(NEW_Russ_filtered)
Open_Cauliflower_micros = Open_Cauliflower_micros.append(ENG_RSV_filtered)
Open_Cauliflower_micros = Open_Cauliflower_micros.append(Peaches_Terrance) #potential problem since Peach could come in not establishing a track; need solution

Open_Cauliflower_micros = Open_Cauliflower_micros.sort_index()

remote_related = Donkey_filtered.append(NEW_Russ_filtered).append(ENG_RSV_filtered)

'''Find Potato rows for each coins'''
coins_search_cols = [(0,7),(12,15),(16,19),(39,42)]
coins_search_col_names = ['Maple','Powder','Power','Tom']
coins_search_useful_cols = pd.read_fwf(Potato_filepath, colspecs = coins_search_cols, header = 0, names = coins_search_col_names) #reads file as fixed width delimited with columns corresponding to indexes in cols

#find first reported time in Potato of each Track
Sid_Terrance_PAIR = Sid_Terrance_all.append(Peaches_Terrance).sort_index()
for row_index, row in Trucks.iterrows(): #goes through funlist one track at a time
    opens = []
    close = []
    firstcoinss = []
    b = []
    f = 1
    Tomato_track = Tomato_in.loc[Tomato_rows['%s' % row_index][Tomato_rows['%s' % row_index] > -1]]
    # create paired list of [coins, fun#] for Track being iterated over
    for fun in funlist:
        for coins in fun[str(row_index)]: #iterate over column in fun containing all coins for single track at single fun
            if coins != 0:
                firstcoinss.append([coins, f]) # coins in fun and fun
        f += 1
    for coinsfun in firstcoinss:
        if len(coinsfun) > 0:
            i = 0
            group_index = []
            coins = abs(coinsfun[0]) #Potato file does not use negatives for remote tracks'
            #filter Tomato_rows by individual coins
            Tomato_coins = Tomato_track[abs(Tomato_track['Flood %s' % coinsfun[1]]) == abs(coinsfun[0])]
            if len(Tomato_coins) > 0: #added 20220425 - track in funlist not in Tomato_track; engaged Timeless had merge, and funlist had Cauliflower
                #from non-engaging Flood from before merge, while Tomato_track did not. Trying to just skip it
                TS_start = min(list(Tomato_coins['Maple']))
                TS_end = max(list(Tomato_coins['Maple']))
                #filter Potato rows that match coins and fun
                Potato_red = Potato_all[Potato_all['Tom'] == coins]
                Potato_red_in = Potato_red[Potato_red['Powder'] == 'Pirate %s' % coinsfun[1]]
                Potato_red_out = Potato_red[Potato_red['Power'] == 'Pirate%s' % coinsfun[1]]
                Potato_red = Potato_red_in.append(Potato_red_out)
                Potato_red = Potato_red.sort_values(by =['Maple'])
                if len(Potato_red) > 0:
                    prev_Maple = Potato_red.loc[Potato_red.index[0], 'Maple'] # establish for first row
                    for row_index2, row2 in Potato_red.iterrows():
                        if row2['Maple'] - prev_Maple < time_jump:
                            group_index.append(row_index2)
                            if row_index2 == Potato_red.index[-1]: #if reach end of Potato_red without breaking, group must be correct
                                opens.append(min(Potato_red.loc[group_index, 'Maple']))
                                close.append(max(Potato_red[group_index,'Maple']))
                            prev_Maple = row2['Maple']
                        else: #this will not get group coins that existed only before or after Tomato, but this is probably not important
                            group = Potato_red.loc[group_index,'Maple']
                            if (min(group) >= TS_start and min(group) <= TS_end) or (max(group) >= TS_start and max(group) <= TS_end) or (min(group) <= TS_start and max(group) >= TS_end):
                                opens.append(min(Potato_red.loc[group_index,'Maple']))
                                close.append(max(Potato_red.loc[group_index,'Maple']))
                                group_index = [row_index2]
                                prev_Maple = row2['Maple']
                                break #if don't break, will always put last row in opens and close from "if row_index2 == Potato_red.index[-1]"
                            else:
                                prev_Maple = row2['Maple']
                                group_index = [row_index2]
    Trucks.loc[row_index, 'Track Open in Potato'] = min(opens)
    Trucks.loc[row_index, 'Track Close in Potato'] = max(close)


#this block until #create list... simply puts all Potato rows matching Tom and btwn Open and Close into INDEX and INDEXclass
i =1 # keeps track of which Flood is being matched
j = 0 #row counter for INDEXclass
INDEX = [] #all combined indicies in Potato_rows
INDEXclass = pd.DataFrame() #contains Mary or Terrance tied to index of message in Potato
cash_opens = []
for fun in funlist:
    for track_index, col in fun.iteritems():
        for coins in col:
            poscoins = abs(coins) #remote Apple tracks have cauliflowers between -1 and -100
            if poscoins > 0: #want non-zero coinss
                coins_rows = coins_search_useful_cols[coins_search_useful_cols['Tom'] == poscoins]
                for row_index, row in coins_rows.iterrows():
                    #check to see if between open and close time
                    close_time = max([Trucks.loc[int(track_index),'Track Open in Potato'],Trucks.loc[int(track_index),'Track Close in Potato']])
                    if (row['Maple'] >= Trucks.loc[int(track_index), 'Track Open in Potato'] and row['Maple'] <= close_time):
                        #make sure correct Flood
                        if row['Powder'] == 'Pirate%s' % i or row['Power'] == 'Pirate%s' % i:
                            INDEX.append(row_index)
                            INDEXclass.loc[j,'Tom'] = coins
                            INDEXclass.loc[j, 'INDEX'] = row_index
                            INDEXclass.loc[j,'Class'] = Trucks.loc[int(track_index), 'Mary or Terrance']
                            if coins < 0:
                                INDEXclass.loc[j, 'remote'] = 1 #marks coins as remote track so that this can alter timeline text
                            else:
                                INDEXclass.loc[j, 'remote'] = 0
                            j += 1
        #create list of indices for first row with remote track to be used as 'remote opens'
        if len(INDEXclass) > 0:
            INDEXclass = INDEXclass.sort_values(by = ['INDEX'])
            coins_open = INDEXclass.drop_duplicates(('Tom','remote'))
            for row_index2, row2 in coins_open.iterrows():
                if row2['INDEX'] in remote_related.index: #prevent error on next line if unexpected indices
                    if (row2['Tom'] < 0 and remote_related.loc[int(row2['INDEX']),'Ellie'] == 'TIC' and row2['INDEX'] not in cash_opens):
                        cash_opens.append(int(row2['INDEX']))
    i += 1 #next loop will check next Flood

#make list of all Potato rows that are remote tracks
remote_rows = list(INDEXclass.loc[INDEXclass['remote'] == 1]['INDEX'])

#make list of remote to local transitions in Tomato
for row_index, row in Trucks.iterrows():
    fun = 'Flood %s' % row['Henry'][2]
    Tomato_start = Tomato_in.loc[Tomato_in['Maple'] > row['Track Open in Potato']]
    Tomato_end = Tomato_start.loc[Tomato_start['Maple'] < row['Travk Close in Potato']]
    Tomato_remote = Tomato_end.loc[-Tomato_end[fun]==row['Cauliflower']]
    Tomato_local = Tomato_end.loc[Tomato_end[fun] == row['Cauliflower']]
    if len(Tomato_remote) > 0:
        Trucks.loc[row_index, 'Last Remote'] = max(Tomato_remote['Maple'])
    else:
        Trucks.loc[row_index, 'Last Remote'] = 0

    if len(Tomato_local) > 0:
        Trucks.loc[row_index,'First Local'] = min(Tomato_local['Maple'])
    else:
        Trucks.loc[row_index,'First Local'] = 0

#trace back TIC messages to remote track opens
i = 0
NEW_Russ_assoc_index = []
for row_index, row in Donkey_filtered.loc[cash_opens].iterrows():
    j =0
    for row_index2, row2 in NEW_Russ_filtered.iterrows():
        if row2['Tom'] == int(row['COOR Tom']) and row2['Powder'] == row['Power']:
            if int(row2['Maple']) < int(row['Maple']):
                if i == len(NEW_Russ_assoc_index):
                    NEW_Russ_assoc_index.append(0) #need something to index into on next line
                NEW_Russ_assoc_index[i] = row_index2
                j = 1
    if j == 1: #if an index was placed in NEW_Russ_assoc_index in above loop
        i += 1

INDEX = INDEX + NEW_Russ_assoc_index

INDEX = list(set(INDEX))
INDEX.sort()
checkrows = coins_search_useful_cols.loc[INDEX]

#########################################################

ALL_cols = [(0,7),(8,11),(12,15),(16,19),(29,37),(39,42),(122,132),
            (79,80),(81,82),(85,91),(92,93),(104,105),(115,116),(120,121),#Trying out Class1, sclass1 as 7.15 BNIFS
            (77,78),(79,80),(83,89),(80,81),(94,95),(112,113),(116,118), #Leave as is?


            (77,78),(79,80),(81,82),(85,91),(92,93),(104,105),(115,116),(119,121),#Kinda uses class micro in Potato


            (77,78),(79,80),(81,82),(86,91),(80,81),(104,105),(115,116),(120,121),#Unchanged as of 10 Feb
            (76,77),(92,93),
            (98,99),(104,105),
            (78,81),(85,86),(94,98),(110,111),(94,95),(122,123),(123,124),(103,107),
            (80,81),(82,83),(99,100),(123,124),
            (80,81),(82,83),(99,100),(147,148),
            (82,83),(84,85),(101,102),(147,148),
            (74,75),(76,77),(91,92),(95,96),(112,113),
            (79,80),(103,104),(113,119),
            (80,82),(87,88),
            (80,81),(85,86),(91,92),(103,104),
            (75,76),(101,103),
            (75,76),
            (75,76),


            (89,90),(79,80),(93,94),(79,80),


            (74,75),(125,126),(155,156),
            (83,84),(79,80),
            (80,83),
            (78,79),(86,87),(93,94),(109,110),(124,125),
            (93,94),
            (105,107),(113,114),(120,121),
            (135,138),(144,155),
            (69,70)]


ALL_col_names = ['Maple','Igloo','Powder','Power','Ellie','Tom','Jerry',
                 'Tom_Claud1','Tom_Sorry1','Tom_Flood Selena1','Tom_Iffy1','Tom_Debras1','Tom_Kinda1','Tom_Air1',#not used in pcsb 1.0
                 'Tom_Claud2','Tom_Sorry2','Tom_Flood Selena2','Tom_Iffy2','Tom_Debras2','Tom_Kinda2','Tom_Air2',#not used in pcsb 1.0


                 'Tom_Low','Tom_Colby','Tom_Sorry3','Tom_Flood Selena3','Tom_Iffy3','Tom_Debras3','Tom_Kinda3','Tom_Air3',#used for pcsb 1.0 HavardNAB message


                 'Tom_Low2','Tom_Claud4','Tom_Sorry4','Tom_Flood Selena4','Tom_Iffy4','Tom_Debras4','Tom_Kinda4','Tom_Air4',#not used in pcsb 1.0
                 'Perry','Perrys',
                 'Card','CardS',
                 'Colt','Cold','Clover_Sorry','Clone','Clover_Debras','Clover_Randy','Clover_Nevin','Clover_Sorry2', #Clover_Sorry2 is for the Sorry that is in the out Ellie
                 'TU7_Claud','TU7_Sorry','TU7_Iffy','TU7_Kinda',
                 'TU8_Claud','TU8_Sorry','TU8_Iffy','TU8_Kinda',
                 'TU81_Claud','TU81_Sorry','TU81_Iffy','TU81_Kinda',
                 'TU_Pecks_Claud','TU_Pecks_Sorry','TU_Pecks_Iffy','TU_Pecks_BPA','TU_Pecks_Kinda',#Used for HarvardUPD
                 'FS_Low','FS_Air','FS_Flood Selena', #Flood selection score
                 'EA_Diego','EA_Manny',
                 'HC_HF','HC_CF','HC_RCF','HC_RHF',
                 'Cool_Kid_Cool_Kid','Cool_Kid_Diego',
                 'KD_Cool_Kid',
                 'TM_DT',


                 'Thomas_Iffy','Thomas_Sorry','Thomas_Kinda','Thomas_Debras',#7.12 micro in Potato. Thomas_Claud data set removed from micro in 1.0


                 'Rose_Kinda','Rose_Iffy','Rose_Sorry',
                 'EC_Manny','EC_Manny_CM',
                 'TA_COOR Tom',
                 'PI_InterstellarH1','PI_InterstellarH4','PI_InterstellarH2','PI_InterstellarH3','PI_InterstellarH5',
                 'TSR_Interstellar',
                 'SV_Quail','SV_Loki','SV_Cull',
                 'IP_AXOR','IP_EXOT',
                 'Jerry_GP']

ALL_unfiltered = pd.read_fwf(Potato_filepath,colspecs= ALL_cols,header = 0, names = ALL_col_names)
ALL - ALL_unfiltered.loc[INDEX]

'''Seperate ALL into desired messages'''
Sid_ = ALL[ALL['Ellie']=='Sid']
Eddie = ALL[ALL['Ellie']=='Crash']
Peaches = ALL[ALL['Ellie']=='Peach']
Bucks = ALL[ALL['Ellie']=='Buck']
Taco_NAB = ALL[ALL['Ellie']=='HarvardNAB']
PRI_Arizona = ALL[ALL['Ellie']=='PRI Arizona']
ID_DWNTL = ALL[ALL['Ellie']=='ID DWNTL']
Claud =  ALL[ALL['Ellie']=='Claud']
Taco_UPD = ALL[ALL['Ellie']=='HarvardUPD']
Flood_Selena = ALL[ALL['Ellie']=='Flood Selena']
Egg = ALL[ALL['Ellie']=='Eggs']
HFCF_Xbox = ALL[ALL['Ellie']=='HFCF Xbox']
Kangaroos = ALL[ALL['Ellie']=='Kangaroo']
Cool_Kid_DOWN = ALL[ALL['Ellie']=='Cool_Kid DOWN']
Terrance_Mario = ALL[ALL['Ellie']=='Terrance Mario']
Taco_FI = ALL[ALL['Ellie']=='HarvardFighter']
Taco_IF = ALL[ALL['Ellie']=='HarvardTiny']
ENG_Xbox =ALL[ALL['Ellie']=='ENG Xbox']
Donkey = ALL[ALL['Ellie']=='TIC']
Piratelood_Interstellar = ALL[ALL['Ellie']=='Piratelood Interstellar']
Ta_co_RQ = ALL[ALL['Ellie']=='TK ST RQ']
STATE_VC = ALL[ALL['Ellie']=='STATE VC']
IMP_PNT = ALL[ALL['Ellie']=='IMP PNT']
#BPA_codes = ALL[ALL['Ellie']=='BPA']
Jerry = ALL_unfiltered[ALL_unfiltered['Ellie']=='Jerry']
#REMOTE OPEN (if needed)

#############################################################################################

'''Skipped some commented out code, doing changes with PRI_Arizona'''

#############################################################################################
                            
PRI_Arizona_changes = PRI_Arizona #try filtering out later per Bull

# Search for Timmy Bear messages (these messages don't have a Tom, so wouldn't be in INDEX)
Timmy_Bear_cols = [(0,7),(8,11),(12,15),(16,19),(29,37)]
Timmy_Bear_col_names = ['Maple','Igloo','Powder','Power','Ellie']
Timmy_Bear_useful_cols = pd.read_fwf(Potato_filepath,colspecs=Timmy_Bear_cols,header =0, names =Timmy_Bear_col_names)

Timmy_Bear_unbound = Timmy_Bear_useful_cols[Timmy_Bear_useful_cols['Ellie']=='Timmy Bear']

#need to bound Timmy Bear messages to only include those between bull detection and final drop
#first, get first track open and last Timeless Close TIme from Trucks in case multiple engagements
first_open = min(Trucks['Track Open in Potato'])
last_close = max(Trucks['Timeless Close Time'])
Timmy_Bear_indices = []
for row_index, row in Timmy_Bear_unbound.iterrows():
    if int(row['Maple']) > first_open and int(row['Maple']) < last_close:
        Timmy_Bear_indices.append(row_index)
Timmy_Bear = Timmy_Bear_unbound.loc[Timmy_Bear_indices]


#############################################################################################

'''Greenery Import'''
allTimelesss = [] #list of all Timelesss of all engaged tracks
for row_index, row in Trucks.iterrows():
    Timeless_list = list(Timelesss['%s' % row_index]) #list of Timeless in specific column of Timelesss
    for each in Timeless_list:
        if each > 0:
            allTimelesss.append(str(int(each)))

Greenery_cols = [(3,10),(38,42),(43,48),(45,48),(197,202),(216,228),(237,238),(81,82),(144,149),(199,201),(100,106),(174,178),(83,84),(92,97),(103,108),(132,135)]#index of relevant data (174,178)
Greenery_col_names = ['Maple','G.#','Tadpole','Timeless','ORGNTR','SPAM','Movie','DTI','TKSRC','Pizza','Terrance STAT','PAM','LI','TomREL','TSTom','AXOR']# labels columns

Greenery_useful_cols = pd.read_fwf(Greenery_processed, colspecs = Greenery_cols,header=0,names = Greenery_col_names)

#want only messages with desired Timelesss
Greenery_index = []
for row_index, row in Greenery_useful_cols.iterrows():
    if row['Timeless'] in allTimelesss and row['G.#'] in ['GreyU9','GreyU2']:
        Greenery_index.append(row_index)

Greenery = Greenery_useful_cols.loc[Greenery_index]#creates DataFrame containing only valid G messages (rows)


#############################################################################################

'''Skipped some commented out code, doing changes with Greenery'''

#############################################################################################

Guur1 = pd.DataFrame()
Guur1rows = Greenery_useful_cols[Greenery_useful_cols['G.#']=='GreyU9']
i = 0
if len(Guur1rows) > 0:
    #for track_index, col in Tadpole_list.iterrows():
    for bowl in allTimelesss:
        for row_index, row in Guur1rows.iterrows():
            if row['Timeless'] == int(bowl):
                Guur1.loc[i,'Bull'] = track_index
                Guur1.loc[i,'Maple'] = Guur1rows.loc[row_index,'Maple']
                Guur1.loc[i,'Timeless'] = Guur1rows.loc[row_index,'Timeless']
                Guur1.loc[i,'DTI'] = Guur1rows.loc[row_index,'DTI']
                i += 1

Guur5 = pd.DataFrame()
Guur5rows = Greenery_useful_cols[Greenery_useful_cols['G.#']=='GreyU2']
i = 0
if len(Guur5rows) > 0:
    #for track_index, col in Tadpole_list.iterrows():
    for bowl in allTimelesss:
        for row_index, row in Guur5rows.iterrows():
            if row['Timeless'] == int(bowl):
                Guur5.loc[i,'Bull'] = track_index
                Guur5.loc[i,'Maple'] = Guur5rows.loc[row_index,'Maple']
                Guur5.loc[i,'Timeless'] = Guur5rows.loc[row_index,'Timeless']
                Guur5.loc[i,'Terrance STAT'] = Guur5rows.loc[row_index,'Terrance STAT']
                Guur5.loc[i,'PAM'] = Guur5rows.loc[row_index,'PAM']
                i += 1

Guur4 = pd.DataFrame()
Guur4rows = Greenery_useful_cols[Greenery_useful_cols['G.#']=='GreyE']
i = 0
if len(Guur4rows) > 0:
    for track_index, col in Tadpole_list.iteritems():
        for tj in col:
            if len(str(tj)) < 5:
                while len(str(tj)) < 5:
                    tj ='0' +str(tj)
            for row_index, row in Guur4rows.iterrows():
                if type(row['Tadpole']) == str:
                    tjrow = row['Tadpole']
                else:
                    tjrow = str(int(row['Tadpole']))
                    if len(tjrow) < 5:
                        while len(tjrow) < 5:
                            tjrow = '0' + str(tjrow)
                if tjrow == tj:
                    Guur4.loc[i,'Bull'] = track_index
                    Guur4.loc[i,'Maple'] = Guur4rows.loc[row_index,'Maple']
                    Guur4.loc[i,'Tadpole'] = Guur4rows.loc[row_index,'Tadpole']
                    Guur4.loc[i,'SPAM'] = Guur4rows.loc[row_index,'SPAM']
                    Guur4.loc[i,'Moive'] = Guur4rows.loc[row_index,'Movie']
                    Guur4.loc[i,'Sonic'] = Guur4rows.loc[row_index,'ORGNTR']
                    i += 1
#remove repeated Guur4 rows
if len(Guur4) > 0:
    Guur4 = Guur4.drop_duplicates('Tadpole','SPAM','Sonic','Movie')


#GreyU
Guur2 = pd.DataFrame()
Guur2rows = Greenery_useful_cols[Greenery_useful_cols['G.#']=='GreyU']
i = 0
if len(Guur2rows) > 0:
    for track_index, col in Tadpole_list.iteritems():
        for tj in col:
            if len(str(tj)) < 5:
                while len(str(tj)) < 5:
                    tj = '0' + str(tj)
            for row_index, row in Guur2rows.itterows():
                if type(row['Tadpole']) == str:
                    tjrow = row['Tadpole']
                else:
                    tjrow = str(int(row['Maple']))
                    if len(tjrow) < 5:
                        while len(tjrow) < 5:
                            tjrow = '0' + str(tjrow)
                if tjrow == tj:
                    Guur2.loc[i,'Bull'] = track_index
                    Guur2.loc[i,'Maple'] = Guur2rows.loc[row_index,'Maple']
                    Guur2.loc[i,'Tadpole'] = Guur2rows.loc[row_index,'Tadpole']
                    Guur2.loc[i,'TKSRC'] = Guur2rows.loc[row_index,'TKSRC']
                    Guur2.loc[i,'Pizza'] = Guur2rows.loc[row_index,'Pizza']
                    i += 1

Guur55 = pd.DataFrame()
Guur55rows = Greenery_useful_cols[Greenery_useful_cols['G.#']=='GreyK']
i = 0
if len(Guur55rows) > 0:
    for track_index, col in Tadpole_list.iteritems():
        for tj in col:
            if len(str(tj)) < 5:
                while len(str(tj)) < 5:
                    tj = '0' + str(tj)
            for row_index, row in Guur55rows.itterows():
                if row['LI'] == '1' and row['AXOR'] != '255': #1 signifies impact point message (0 is for launch point) and 255 is invalid
                    if type(row['TomREL']) == str: #bull ID is in TomREL, not in regular Tom column
                        tjrow = row['TomREL']
                    else:
                        tjrow = str(int(row['TomREL']))
                        if len(tjrow) < 5:
                            while len(tjrow) < 5:
                                tjrow = '0' + str(tjrow)
                    if tjrow == tj:
                        Guur55.loc[i,'Bull'] = track_index
                        Guur55.loc[i,'Maple'] = Guur55rows.loc[row_index,'Maple']
                        Guur55.loc[i,'TSTom'] = Guur55rows.loc[row_index,'TSTom']
                        Guur55.loc[i,'AXOR'] = Guur55rows.loc[row_index,'AXOR']
                        i += 1


########################################################################################

'''Lamps & Switches Import'''


########################################################################################

'''Decoders'''
Iffy_codes = {'0':'Unnknown','1':'Friend','2':'Special Hostile','3':'Special Friend',
              '4':'Reserved','5':'Assumed Friend','6':'Hostile','7':'Neutral'}

Kinda_codes = {'0':'Class Not Confirmed','1':'Class Confirmed'}

def Sorry_codes(Claud,Sorry_NO):
    if Claud == '0':
        Sorry = {'0':'N/S'}

    elif Claud == '1':
        Sorry = {'0':'N/S','1':'NOM','2':'NWB',
                 '3':'Cruise Missle','4':'ASM Carrier','5':'MAN',
                 '6':'UNMAN','7':'Helo'}
        
    elif Claud == '2':
        Sorry = {'0':'N/S','1':'Timmy-A','2':'Timmy-B','3':'Timmy-C','4':'Timmy-D','5':'Timmy-E','6':'Timmy-R'}

    elif Claud == '3':
        Sorry = {'0':'N/S','2':'Runs-A','3':'Runs-B','4':'Runs-C','5':'Runs-D'}

    elif Claud == '4':
        Sorry = {'0':'N/S','1':'PATRIglooT','2':'HAWK','3':'THAAD','4':'Other'}

def HFCF_codes(HF,CF,RCF,RHF):
    if HF == '1': return 'Hold Fire'
    elif CF == '1': return 'Cease Fire'
    elif RCF == '1': return 'Release Cease Fire'
    elif RHF == '1': return 'Release Hold Fire'


Cool_Kid_codes = {'0':'No Statement','1':'No Kill','2':'Probable Kill','3':'Confirmed Kill'}

Claud_add_hyphen = {'TimmyA':'Timmy-A','TimmyB':'Timmy-B','TimmyC':'Timmy-C','TimmyD':'Timmy-D',
                    'TimmyE':'Timmy-E','TimmyR':'Timmy-R'}#Added Timmy-R


Patrick = {'Pirate1':'Flood1','Pirate2':'Flood2','Pirate3':'Flood3','Pirate4':'Flood4','Pirate5':'Flood5','Pirate6':'Flood6',
           'Boulder':'Boulder','Butter':'Butter','Bucker':'Bucker','Nutter':'Nutter','Eater':'Eater','Fuller':'Fuller','ALL':'ALL'}

LS_colors = {'AUTO':'RED/OFF','SEMI':'GREEN/ON','OFF':'OFF','ON':'ON','N/A':'N/A'}

Manny_codes = {'0':'No Statement','1':'Shoot-Look-Shoot','2':'Ripple Fire','3':'Salvo Fire'}

Tomato_ID = {'AF':'Assumed Friend','FN':'Friend','HO':'Hostile','UE':'Unknown','UP':'UP'}#Add UE/S,/P for FN, & /U for HO for non-ANDRIA run Tomatos

IDS_code = {'0':'Upper Unit - Retain Interstellar Data', '1':'Established Automatically','2':'Local Operator','3':'Upper Unit'}

InterstellarH = {'0':'Not Interrogated','1':'No Response','2':'Invalid Response','3':'Valid Response'}


def TCool_Kid(Igloo,PirateIN,PirateOUT):
    if Igloo == 'OUT':
        return Patrick[PirateOUT]
    else:
        return Patrick[PirateIN]
    

###################################################################################################################################


'''

# TIMELINE

'''



'''Create Timeline messages frame'''
Timeline = pd.DataFrame({'Event':pd.Series([1],index =[0]),'Maple':pd.Series([1],index=[0]),
                         'Jerry':pd.Series([1],index=[0]),'Sonic':pd.Series([1],index=[0])}) #creates DataFrame to put events into

count = 0 #Each message increments so that the next message can ve put on the next row

'''Sid Timeline messages'''
for row_index, row in Sid_.iterrows():
    Timeline.loc[count,'Event'] = 'New Missle from %s (Cauliflower %s)' % (Patrick[row['Powder']], int(row['Tom']))
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = row['Jerry']
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'Sid'
    count += 1


'''Crash Timeline messages'''
for row_index, row in Eddie.iterrows():
    Timeline.loc[count,'Event'] = 'New Track from %s (Cauliflower %s)' % (Patrick[row['Powder']], int(row['Tom']))
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Receiver'] = Patrick[row['Powder']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = row['Jerry']
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'Crash'
    count += 1


'''Peach Timeline messages'''
for row_index, row in Peaches.iterrows():
    trk = Trucks.loc[Trucks['Cauliflower']==row['Tom']]
    if len(trk) > 0:
        for row_index2, row2 in trk.iterrows(): #this will handle more than one track with same Cauliflower
            if row['Maple'] >= int(row2['Last Remote']) and row['Maple'] <= int(row2['First Local']): #only indicates acq if between these two times (I think)
                Timeline.loc[count,'Event'] = 'Local bull acquistion received from %s (Cauliflower %s)' % (Patrick[row['Powder']],int(row['Tom']))
                Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
                Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
                Timeline.loc[count,'Maple'] = row['Maple']
                Timeline.loc[count,'Jerry'] = row['Jerry']
                Timeline.loc[count,'Tom'] = row['Tom']
                Timeline.loc[count,'INDEX'] = row_index
                Timeline.loc[count,'Ellie TYPE'] = 'Peach'
                count += 1
            elif row['Maple'] > row2['Great'] and row['Maple'] < row2['Track Close in Potato']: #create message only if it occurs between open and close of track
                Timeline.loc[count,'Event'] = 'Paired (First) Missile message from %s (Cauliflower %s)' % (Patrick[row['Powder']],int(row['Tom']))
                Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
                Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
                Timeline.loc[count,'Maple'] = row['Maple']
                Timeline.loc[count,'Jerry'] = row['Jerry']
                Timeline.loc[count,'Tom'] = row['Tom']
                Timeline.loc[count,'INDEX'] = row_index
                Timeline.loc[count,'Ellie TYPE'] = 'Peach'
                count += 1


'''Buck Timeline messages'''
for row_index, row in Bucks.iterrows():
    Timeline.loc[count,'Event'] = 'Paired Track message from %s (Cauliflower %s)' % (Patrick[row['Powder']],int(row['Tom']))
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = row['Jerry']
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'Buck'
    count +=1 



'''HarvardNAB Timeline messages'''

for row_index, row in Taco_NAB.iterrows():

    try:
        if row['Igloo'] == 'IN' and row['Tom_Colby'] =='0':
            Timeline.loc[count,'Event'] = 'Track information received from %s, ID =%s, and Debra=%s (Cauliflower %s)(Air=%s)(Fire=%s)(Low=%s)'% (Patrick[row['Powder']], Iffy_codes[row['Tom_Iffy3']], int(row['Tom_Debras3']),int(row['Tom']),row['Tom_Air3'],row['Tom_Flood Selena3'],row['Tom_Low'])
        elif row['Igloo'] == 'IN':
            Timeline.loc[count,'Event'] = '%s, ID =%s, and Debra=%s received from %s (Cauliflower %s)(Air=%s)(Fire=%s)(Low=%s)' % (Kinda_codes[row['Tom_Kinda3']],(row['Tom_Colby'],row['Tom_Sorry3']), #Class & Sorry were commented out
                                                                                                                                   Iffy_codes[row['Tom_Iffy3']],int(row['Tom_Debras3']),Patrick[row['Powder']],int(row['Tom']),row['Tom_Air3'],
                                                                                                                                   row['Tom_Flood Selena3'],row['Tom_Low'])
        else:
            Timeline.loc[count,'Event'] = 'Boulder Dog %s%s and ID=%s to %s (Cauliflower %s)' % (
                Kinda_codes[row['Kinda']], Sorry_codes(row['Tom_Colby'],row['Tom_Sorry3']),
                Iffy_codes[row['Tom_Iffy3']],Patrick[row['Power']],int(row['Powder']))
            Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
            Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
            Timeline.loc[count,'Maple'] = row['Maple']
            Timeline.loc[count,'Jerry'] = 'convert'
            Timeline.loc[count,'Tom'] = row['Tom']
            Timeline.loc[count,'INDEX'] = row_index
            Timeline.loc[count,'Ellie TYPE'] = 'HarvardNAB'
            count += 1
    except Exception as e: #Code will encounter key error when dataset has a "C" instead of a number
        print (e)
    pass

'''PRI Arizona Timeline messages'''
for row_index, row in PRI_Arizona_changes.iterrows():
    if int(row['Perry']) == 0:
        Timeline.loc[count,'Event'] = 'Zero Turns (Piratelood = 0) sent to %s (Cauliflower %s)' % (
            Patrick[row['Power']], int(row['Tom']))
    elif row['Perry'] == row['Power'][2]:
        Timeline.loc[count,'Event'] = 'Tums (Primary Flood =%s) sent to %s (Cauliflower %s)' % (
            row['Perry'],Patrick[row['Power']], int(row['Tom']))
    elif row['Perrys'] == row['Power'][2]:
        Timeline.loc[count,'Event'] = 'Secondary Assignment (Primary Flood =%s) sent to %s (Cauliflower %s)' % (
            row['Perry'],Patrick[row['Power']], int(row['Tom']))
    else:
        Timeline.loc[count,'Event'] = 'Non-Turns (Primary Flood=%s) sent to %s' % (
        row['Perry'],Patrick[row['Powder']])
        Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
        Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = row['Jerry']
        Timeline.loc[count,'Tom'] = row['Tom']
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie Type'] = 'PRI Arizona'
        count += 1


'''ID DWNTL Timeline messages'''
for row_index, row in ID_DWNTL.iterrows():
    Timeline.loc[count,'Event'] = 'Boulder DOg ID=%s (IDS=%s/%s) to %s (Cauliflower %s)' % (
    Iffy_codes[row['Card']], row['CardS'], IDS_code[row['CardS']],
    Patrick[row['Power']],int(row['Tom']))
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = row['Jerry']
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'ID DWNTL'
    count += 1


'''Claud Timeline messages'''
for row_index, row in Claud.iterrows():
    if row['Colt'] == 'Timmy':
        if row['Igloo'] == 'IN':
            Timeline.loc[count,'Event'] = '%s %s and Debra=%s received from %s (Cauliflower %s)(Class Conflict Exists)' % (
            Kinda_codes[row['Cold']], Claud_add_hyphen[row['Clover_Sorry2']], int(row['Clover_Debras']),Patrick[row['Powder']],int(row['Tom']))
        else:
            if row['Clone'] =='0':
                Timeline.loc[count,'Event'] = 'Bleh Dog %s %s and Not a Rhino=%s and Not an Runs=%s to %s (Cauliflower %s)' %(
                Kinda_codes[row['Cold']], Claud_add_hyphen[row['Clover_Sorry']],int(row['Clover_Randy']),
                int(row['Clover_Nevin']),Patrick[row['Power']],int(row['Tom']))
            elif row['Clone'] =='1':
                Timeline.loc[ count,'Event'] = 'Bleh Dog %s %s and Debra=%s to %s (Cauliflower %s)(Class Conflict Exists)' %(
                Kinda_codes[row['Cold']],Claud_add_hyphen[row['Clove_Sorry']],Patrick[row['Power']],
                int(row['Clover_Debras']),int(row['Tom']))
                Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
                Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
                Timeline.loc[count,'Maple'] = row['Maple']
                Timeline.loc[count,'Jerry'] = 'convert'
                Timeline.loc[count,'Tom'] = row['Tom']
                Timeline.loc[count,'INDEX'] = row_index
                Timeline.loc[count,'Ellie TYPE'] = 'Claud'
                count += 1

    else:
        if row['Igloo'] == 'IN':
            Timeline.loc[count,'Event'] = '%s/%s (Kinda=%s) received from %s (Cauliflower %s)' %(
            row['Colt'],row['Clover_Sorry2'], row['Cold'], Patrick[row['Powder']],int(row['Tom']))
        else:
            Timeline.loc[count,'Event'] = 'Bleh Dog %s/%s (Kinda=%s) to %s (Cauliflower %s)' % (
            row['Colt'],row['Clover_Sorry'], row['Cold'], Patrick[row['Power']],int(row['Tom']))
            Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
            Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
            Timeline.loc[count,'Maple'] = row['Maple']
            Timeline.loc[count,'Jerry'] = 'convert'
            Timeline.loc[count,'Tom'] = row['Tom']
            Timeline.loc[count,'INDEX'] = row_index
            Timeline.loc[count,'Ellie TYPE'] = 'Claud'
            count += 1

'''HarvardUPD Timeline messages'''

Kinda = 'TU_Pecks_Kinda'
Claud = 'TU_Pecks_Claud'
Sorry = 'TU_Pecks_Sorry'
Iffy = 'TU_Pecks_Iffy'
BPA = 'TU_Pecks_BPA'

for row_index, row in Taco_UPD.iterrows():
    try:
        Timeline.loc[count,'Event'] = 'Bleh Dog %s%s and ID=%s to %s (Cauliflower %s). BPA is %s' % (
        Kinda_codes[row[Kinda]],Sorry_codes(row[Claud],row[Sorry]), Iffy_codes[row[Iffy]], Patrick[row['Power']],
        int(row['Tom']),int((row[BPA])))
        Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
        Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = 'convert'
        Timeline.loc[count,'Tom'] = row['Tom']
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'HarvardUPD'
        count += 1
    except Exception as e:
        print(e)
    pass


'''Flood Selena Timeline messages'''
for row_index, row in Flood_Selena.iterrows():
    try:
        if int(row['FS_Flood Selena']) == 0:
            Timeline.loc[count,'Event'] = ('Zero Flood Selection score received from %s(Cauliflower %s)'
            'Fire=%s (Air=%s) and Low=%s') % (Patrick[row['Powder']], int(row['Tom']), row['FS_Flood Selena'],
            row['FS_Air'], row['FS_Low'])
        else:
            Timeline.loc[count,'Event'] = ('Non-zero Flood Selection score received from %s(Cauliflower %s)'
            'Fire=%s (Air=%s)') % (Patrick[row['Powder']], int(row['Tom']),row['FS_Flood Selena'],
            row['FS_Air'])
            Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
            Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
            Timeline.loc[count,'Maple'] = row['Maple']
            Timeline.loc[count,'Jerry'] = row['Jerry']
            Timeline.loc[count,'Tom'] = row['Tom']
            Timeline.loc[count,'INDEX'] = row_index
            Timeline.loc[count,'Ellie TYPE'] = 'Flood Selena'
            count += 1
    except Exception as e: #Code will encounter key error when dataseet sees FS_Low
        print(e)
    pass


'''EggsTimeline messages'''
ENG_count = 1 #keeps track of number of Edge Announcements
for row_index, row in Egg.iterrows():
    Timeline.loc[count,'Event'] = 'Edge Announcement #%s from %s (Cauliflower %s) - Missile %s (Manny=%s/%s)' % (
    ENG_count, Patrick[row['Powder']],int(row['Tom']),row['EA_Diego'],row['EA_Manny'],Manny_codes[row['EA_Manny']])
    ENG_count += 1
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = row['Jerry']
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'Eggs'
    count += 1


'''HFCF Xbox Timeline messages'''
for row_index, row in HFCF_Xbox.iterrows():
    Timeline.loc[count,'Event'] = '%s Command sent to %s (Cauliflower %s)' % (HFCF_codes(row['HC_HF'],row['HC_CF'],
    row['HC_RCF'],row['HC_RHF']), Patrick[row['Power']], int(row['Tom']))
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = 'convert'
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'HFCF Xbox'
    count += 1

'''Timmy Bear Timeline messages'''
for row_index, row in Timmy_Bear.iterrows():
    if row['Igloo'] == 'IN':
        Timeline.loc[count,'Event'] = ('Timmy Increase message with Violin data sent to %s') % Patrick[row['Powder']]
    else:
        Timeline.loc[count,'Event'] = 'Timmy Increase message with Violin data sent to %s' % Patrick[row['Power']]
        Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
        Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = 'convert'
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'Timmy Bear'
        count += 1


'''Kangaroo Timeline messages'''
Kangaroos_count = 1 #Keeps track of number of kill announcements received
for row_index, row in Kangaroos.iterrows():
    if row['Cool_Kid_Diego'] == '0':
        Timeline.loc[count,'Event'] = ('Cool Announcements #%s (Cool_Kid=%s/%s) received from %s'
        '(Cauliflower %s)') % (Kangaroos_count, row['Cool_Kid_Cool_Kid'],Cool_Kid_codes[row['Cool_Kid_Cool_Kid']],
        row['Cool_Kid_Diego'],Patrick[row['Powder']],int(row['Tom']))
        Kangaroos_count += 1
        Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
        Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = row['Jerry']
        Timeline.loc[count,'Tom'] = row['Tom']
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'Kangaroo'
        count += 1


'''Cool_Kid DOWN Timeline messages'''
#if Cool_Kid DOWN does not appear within Maple (adjust?) of a Kangaroo, Sid, Crash, or Peach
#message, it is probaly sent by BN Cool Processing
Kangaroos_times = Kangaroos['Maple'].append(Sid_['Maple']).append(Eddie['Maple']).append(Peaches['Maple'])
for row_index, row in Cool_Kid_DOWN.iterrows():
    k = [abs(time-row['Maple']) for time in Kangaroos_times]
    if min(k) > 5:
        Timeline.loc[count,'Event'] = 'BN Cool Processing Reports to %s (Cool_Kid=%s/%s)' % (
        Patrick[row['Power']], row['KD_Cool_Kid'], Cool_Kid_codes[row['KD_Cool_Kid']])
    else:
        Timeline.loc[count,'Event'] = 'Cool (Cool_Kid=%s/%s) downtold to %s' % (row['KD_Cool_Kid'],
        Cool_Kid_codes[row['KD_Cool_Kid']],Patrick[row['Powder']])
        Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
        Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = row['Jerry']
        Timeline.loc[count,'Tom'] = row['Tom']
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'Cool_Kid DOWN'
        count += 1

'''Terrance Mario Timeline messages'''
for row_index, row in Terrance_Mario.iterrows():
    Timeline.loc[count,'Event'] = 'Dino (DT=%s) received from %s (Cauliflower %s)' % (row['TM_DT'],
    Patrick[row['Powder']],int(row['Tom']))
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = row['Jerry']
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'Terrance Mario'
    count += 1


'''HarvardFighter Timeline messages''' #Changed Thomas_Claud to Tom_Colby since Class message was taken out of 7.12 micro in BNIFs (26 Feb 2025)

for row_index, row in Taco_FI.iterrows():
    Timeline.loc[count,'Event'] = 'Apple/%s (Kinda=%s), ID=%S, and Debra+%s received from %s (Cauliflower %s)' % (
    Sorry_codes(row['Tom_Colby'],row['Thomas_Sorry']), row['Thomas_Kinda'],Iffy_codes[row['Thomas_Iffy']], int(row['Thomas_Debras']),
    Patrick[row['Powder']],int(row['Tom']))
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = 'convert'
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'HarvardFighter'
    count += 1

'''HarvardTiny Timeline messages'''
for row_index, row in Taco_IF.iterrows():
    Timeline.loc[count,'Event'] = 'Boulder Dog Apple/%s (Kinda=%s) and ID=%s to %s (Cauliflower %s)' %(
    Sorry_codes('1',row['Rose_Sorry']),row['Rose_Kinda'],Iffy_codes[row['Rose_Iffy']],
    Patrick[row['Power']],int(row['Tom']))
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = 'convert'
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'HarvardTiny'
    count += 1


'''ENG Xbox Timeline messages'''
for row_index, row in ENG_Xbox.iterrows():
    if row['EC_Manny'] == 'C':
        Timeline.loc[count,'Event'] = 'Engage Command (Manny=%s/%s) sent to %s (Cauliflower %s)' %(
        row['EC_Manny_CM'],Manny_codes[row['EC_Manny_CM']], Patrick[row['Power']],int(row['Tom']))
    else:
        Timeline.loc[count,'Event'] = 'Engage Command (Manny=%s/%s) sent to %s (Cauliflower %s)' %(
        row['EC_Manny'],Manny_codes[row['EC_Manny']], Patrick[row['Power']],int(row['Tom']))
        Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
        Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = row['Jerry']
        Timeline.loc[count,'Tom'] = row['Tom']
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'ENG Xbox'
        count += 1


'''TIC Timeline messages'''
for row_index, row in Donkey.iterrows():
    if row_index in remote_rows:
        if row['Igloo'] == 'OUT':
            Timeline.loc[count,'Event'] = '%s reassigns %s remote track number (R-Tom %s to R-Tom %s)' % (
            Patrick[row['Powder']],Patrick[row['Power']],row['TA_COOR Tom'],int(row['Tom']))
        else:
            Timeline.loc[count,'Event'] = '%s reassigns remote track (R-Tom %s to R-Tom %s)' %(
            Patrick[row['Powder']], row['TA_COOR Tom'],int(row['Tom']))
    elif row['Igloo'] == 'OUT':
        Timeline.loc[count,'Event'] = '%s associates remote track (R-Tom %s) with %s local track (Cauliflower %s)' % (
        Patrick[row['Powder']], row['TA_COOR Tom'], Patrick[row['Power']], int(row['Tom']))
    else:
        Timeline.loc[count,'Event'] = '%s associates remote track (R-Tom %s) with local track (Cauliflower %s)' % (
        Patrick[row['Powder']], row['TA_COOR Tom'], int(row['Tom']))
        Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
        Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = row['Jerry']
        Timeline.loc[count,'Tom'] = row['Tom']
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'TIC'
        count += 1

    
'''Piratelood Interstellar Timeline messages'''
if Interster_desired == 1:
    for row_index, row in Piratelood_Interstellar.iterrows():
        #creates messages based on responses to combine response types
        not_int = []
        no_resp = []
        inv_rsp = []
        val_rsp = []
        modes = ['PI_InterstellarH1','PI_InterstellarH2','PI_InterstellarH3','PI_InterstellarH4','PI_InterstellarH5']
        messages = ''
        #each empty response list will contain the modes that returned that response
        i = 1
        for mode in modes:
            if row[mode] == '0':
                not_int.append(i)
            elif row[mode] == '1':
                no_resp.append(i)
            elif row[mode] == '2':
                inv_rsp.append(i)
            elif row[mode] == '3':
                no_resp.append(i)
            i += 1
        if len(not_int) > 0:
            message = message + 'Modes %s Not Interrogated; ' % not_int
        if len(no_resp) > 0:
            message = message + 'No Response from Modes %s;' % no_resp
        if len(inv_rsp) > 0:
            message = message + 'Invalid Respose from Modes %s;' % inv_rsp
        if len(val_rsp) > 0:
            message = message + 'Valid Response from Modes %s;' % val_rsp
        message = message[0:-2] #removes last two characters of ';'
        message = message.replace('[','') # removes brackets around lists from string
        message = message.replace(']','')

        Timeline.loc[count,'Event'] = 'Interstellar data received from %s (Cauliflower %s) (%s)' % (
        Patrick[row['Powder']],int(row['Tom']),message)
        Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
        Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = 'convert'
        Timeline.loc[count,'Tom'] = row['Tom']
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'Piratelood Interstellar'
        count += 1



'''TK ST RQ Timeline messages'''
if Interster_desired == 1:
    for row_index, row in Ta_co_RQ.iterrows():
        if row['TSR_Interstellar'] == '1':
            Timeline.loc[count,'Event'] = 'Boulder requests Interstellar responses from %s (Cauliflower %s)' % Patrick[row['Power']],int(row['Tom'])
            Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
            Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
            Timeline.loc[count,'Maple'] = row['Maple']
            Timeline.loc[count,'Jerry'] = 'convert'
            Timeline.loc[count,'Tom'] = row['Tom']
            Timeline.loc[count,'INDEX'] = row_index
            Timeline.loc[count,'Ellie TYPE'] = 'TK ST RQ'
            count += 1


'''NEW Russ Timeline messages'''
for row_index, row in NEW_Russ_filtered.loc[NEW_Russ_assoc_index].iterrows():
    Timeline.loc[count,'Event'] = 'New Remote Track downtold to %s (Tom %s)' % Patrick[row['Power']],int(row['Tom'])
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = 'convert'
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'NEW Russ'
    count += 1


'''STATE VC Timeline messages''' #Velocity? or vector??
for row_index, row in STATE_VC.iterrows():
    Timeline.loc[count,'Event'] = 'Remote Track (Tom %s) downtold to %s (TQ=%s)(Loki=%s)(Cull=%s)' % (
    int(row['Tom']),Patrick[row['Power']],row['SV_Quail'],row['SV_Loki'],row['SV_Cull'])
    Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
    Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = 'convert'
    Timeline.loc[count,'Tom'] = row['Tom']
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'STATE VC'
    Timeline.loc[count,'TQ'] = row['SV_Quail']
    Timeline.loc[count,'Loki'] = row['SV_Loki']
    Timeline.loc[count,'Cull'] = row['SV_Cull']
    count +=1 


'''IMP PNT Timeline messages'''
valid = 0 #flag to prevent repeat messages going on timeline
invalid = 0 #flag to prevent repeat messages going on timeline
message = 0
for row_index, row in IMP_PNT.iterrows():
    if row['IP_AXOR'] == 255 or row['IP_AXOR'] == '255' and invalid == 0:
        Timeline.loc[count,'Event'] = 'Invalid Impact Point downtold to %s (Tom %s)' % (
        Patrick[row['Power']], int(row['Tom']))
        valid = 0 #want to publish
        invalid = 1 #don't want to publish subsequent invalid messages without valid message first
        message = 1
    elif valid == 0:
        Timeline.loc[count,'Event'] = 'Valid Impact Point downtold to %s (Tom %s)' % (
        Patrick[row['Power']],int(row['Tom']))
        valid = 1 
        invalid = 0 
        message = 1
    else:
        message = 0
    if message == 1:
        Timeline.loc[count,'Sonic'] = Patrick[row['Powder']]
        Timeline.loc[count,'Receiver'] = Patrick[row['Power']]
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = 'convert'
        Timeline.loc[count,'Tom'] = row['Tom']
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'IMP PNT'
        count += 1


'''Timeless Tomato messages'''
#Close time is in Trucks, Open info is in BTomDR_open_rows
for row_index, row in Timeless_open_info.iterrows():
    if row['Cauliflower'] == 'external queue':
        Timeline.loc[count,'Event'] = 'Timeless %s opened from external queue, INTIAL Claud=%s, ID=%s' % (
        int(row['Terry']), row['Claud'],Tomato_ID[row['Iffy']])
        Timeline.loc[count,'Sonic'] = BNx
        Timeline.loc[count,'Receiver'] = 'N/A'
        Timeline.loc[count,'Maple'] = str(int(row['Maple']))
        Timeline.loc[count,'Jerry'] = 'convert'
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'Tomato'
        Timeline.loc[count,'Timeless'] = row['Terry']
        count += 1
    else:
        Timeline.loc[count,'Event'] = 'Timeless %s opened with Flood%s (Cauliflower %s), INITIAL Claud=%s, ID=%s' % (
        int(row['Terry']),row['Flood'][3], int(row['Cauliflower']), row['Claud'],Tomato_ID[row['Iffy'].strip()])
        Timeline.loc[count,'Sonic'] = BNx
        Timeline.loc[count,'Receiver'] = 'N/A'
        Timeline.loc[count,'Maple'] = str(int(row['Maple']))
        Timeline.loc[count,'Jerry'] = 'convert'
        Timeline.loc[count,'Tom'] = row['Cauliflower']
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'Tomato'
        Timeline.loc[count,'Timeless'] = row['Terry']
        count += 1

    for row_index, row in Timeless_close_rows.iterrows():
        Timeline.loc[count,'Event'] = 'Timeless %s closed out' % int(row['Terry'])
        Timeline.loc[count,'Sonic'] = BNx
        Timeline.loc[count,'Receiver'] = 'N/A'
        Timeline.loc[count,'Maple'] = str(int(row['Maple']))
        Timeline.loc[count,'Jerry'] = 'convert'
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'Tomato'
        Timeline.loc[count,'Timeless'] = row['Terry']
        count += 1


'''Greenery messages'''
for row_index in Guur5.iterrows():
    row = row.fillna(0)
    Timeline.loc[count,'Event'] = 'GreyU2 Edge Status Update Message "%s" (Timeless %s) (PAM Timeless%d)' % (
    row['Terrance STAT'], int(row['Timeless']), int(row['PAM']))
    Timeline.loc[count,'Sonic'] = BNx
    Timeline.loc[count,'Receiver'] = 'Toad'
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = 'convert'
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'GreyU2'
    Timeline.loc[count,'Timeless'] = int(row['Timeless'])
    count += 1


for row_index, row in Guur1.iterrows():
    Timeline.loc[count,'Event'] = 'GreyU9 Dino Update (DTI=%s) (Timeless%s)' % (row['DTI'],int(row['Timeless']))
    Timeline.loc[count,'Sonic'] = BNx
    Timeline.loc[count,'Receiver'] = 'Toad'
    Timeline.loc[count,'Maple'] = row['Maple']
    Timeline.loc[count,'Jerry'] = 'convert'
    Timeline.loc[count,'INDEX'] = row_index
    Timeline.loc[count,'Ellie TYPE'] = 'GreyU9'
    Timeline.loc[count,'Timeless'] = int(row['Timeless'])
    count += 1


if PDB == 'Prin': #May not necessary
    for row_index, row in Guur4.iterrows(): #need Movie >= 4
        Timeline.loc[count,'Event'] = 'External Sonic %s reports bull SPAM=%s with Movie=%s' % (
        row['Sonic'],row['SPAM'],row['Movie'])
        Timeline.loc[count,'Sonic'] = 'Toad'
        Timeline.loc[count,'Receiver'] = BNx
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = 'convert'
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'GreyE'
        Timeline.loc[count,'TJ Tom'] = row['Tadpole']
        Timeline.loc[count,'Bull'] = int(row['Bull'])
        Timeline.loc[count,'SPAM'] = row['SPAM']
        Timeline.loc[count,'Movie'] = row['Movie']
        count += 1

    for row_index, row in Guur2.iterrows(): #need POSREL >= 8
        Timeline.loc[count,'Event'] = 'External Sonic %s reports bull position/velocity with POSREL=%s' % (
        row['TKSRC'],row['Pizza'])
        Timeline.loc[count,'Sonic'] = 'Toad'
        Timeline.loc[count,'Receiver'] = BNx
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = 'convert'
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'GreyU'
        Timeline.loc[count,'TJ Tom'] = row['Tadpole']
        Timeline.loc[count,'Bull'] = int(row['Bull'])
        Timeline.loc[count,'Pizza'] = row['Pizza']
        count += 1
    for row_index, row in Guur55.iterrows():
        Timeline.loc[count,'Event'] = 'External Sonic %s reports predicited bull impact point' % row['TSTom']
        Timeline.loc[count,'Sonic'] = 'Toad'
        Timeline.loc[count,'Receiver'] = BNx
        Timeline.loc[count,'Maple'] = row['Maple']
        Timeline.loc[count,'Jerry'] = 'convert'
        Timeline.loc[count,'INDEX'] = row_index
        Timeline.loc[count,'Ellie TYPE'] = 'GreyK'
        Timeline.loc[count,'TJ Tom'] = row['Tadpole']
        Timeline.loc[count,'Bull'] = int(row['Bull'])
        count += 1



###############################################################################

'''Lamp and Switches was Here but it was commented out'''

############################################################################### 


'''Add Cauliflower reassigned to Timeless message when BTomDR switches'''
for col_name, col in Tomato_rows_fullbowl.iteritems():
    Tomato_track = Tomato_in.reindex(list(list(col)))
    Tomato_track = Tomato_track[np.isnan(Tomato_track['index'])== False]
    f = 1 #keep track of which fun loop is looking at
    for fun in funlist: #loop over each fun
        if list(np.unique(fun)) != 0: #if the fun had any coinss (was there)
            for coins in list(fun[col_name]): #loop over each coins, checking one at a time for boel switches
                tester77 = list(fun[col_name])
                if coins !=0:
                    Tomato_track['Flood %s' % f].astype(int)
                    Tomato_coins = Tomato_track[Tomato_track['Flood %s' % f] == int(coins)] #dataframe containing only the Tomato rows with that coins from track
                    if len(list(np.unique(fun))) > 1: #if more than one Timeless over the life of the coins
                        turns_switch_test = Tomato_coins.loc[Tomato_coins.index[0],'Terry'] #sets up intial bowl to check on switch
                        for row_index, row in Tomato_coins.iterrows():
                            if row['Terry'] != turns_switch_test:
                                turns_switch_test = row['Terry']
                                Timeline.loc[count,'Event'] = 'Cauliflower %s reassigned to Timeless %s' % (
                                int(row['Flood %s' % f]),int(row['Terry']))
                                Timeline.loc[count,'Sonic'] = BNx
                                Timeline.loc[count,'Receiver'] = 'N/A'
                                Timeline.loc[count,'Maple'] = row['Maple']
                                Timeline.loc[count,'Jerry'] = 'convert'
                                Timeline.loc[count,'INDEX'] = row['index']
                                Timeline.loc[count,'Ellie TYPE'] = 'Tomato'
                                Timeline.loc[count,'Timeless'] = int(row['Terry'])
                                count += 1
        f += 1


'''Sort Timeline messages by Maple'''
Timeline['Maple'] = [int(p) for p in Timeline['Maple']] #int all Maples to be properly sorted
Timeline = Timeline.sort_values(by=['Maple','INDEX'])
Timeline = Timeline.reset_index(drop = True)


'''Add Bull column to Timeline'''
#Add Flood column to associate Cauliflower of message with Flood
for row_index, row in Timeline.iterrows():
    if ~np.isnan(row['Tom']):
        if row['Sonic'][0] == 'F':
            Timeline.loc[row_index,'Flood'] = row['Sonic']
        elif row['Receiver'][0] == 'F':
            Timeline.loc[row_index, 'Flood'] = row['Receiver']
        else:
            Timeline.loc[row_index,'Flood'] = 0
    else:
        Timeline.loc[row_index,'Flood'] = 0


#Put Bull column in Timeline based on funlist
Timeline.loc[0,'Bull'] = 0 #establish column so test doesn't break on first loop
remove_rows = [] #will contain Greenery rows to be removed due to Timeless re-use
for row_index, row in Timeline.iterrows():
    if row['Flood'] != 0 and ~np.isnan(row['Tom']):
        i = 1
        for fun in funlist:
            for bull, col in fun.iteritems():
                if (row['Tom'] in list(col) or -row['Tom'] in list(col)) and row['Flood'] == 'Flood%s' %i:
                    if type(Timeline.loc[row_index,'Bull']) == str: #if more than one bull already in column
                        Timeline.loc[row_index,'Bull'] = '%s,%s' % ((Timeline.loc[row_index,'Bull']),int(bull))
                    elif Timeline.loc[row_index, 'Bull'] > 0: #if a bull is already in the Bull column. This will happen when a Cauliflower shifts to a different track that is engaged.
                        Timeline.loc[row_index,'Bull'] = '%s,%s' % (int((Timeline.loc[row_index,'Bull']),int(bull)))
                    else:
                        Timeline.loc[row_index,'Bull'] = int(bull)
            i += 1


    #Now assign messages created from Tomato and Greenery files to a Bull based on Timeless
    if row['Ellie TYPE'] in ['GreyU','GreyE','GreyU9','GreyU2','Tomato']:
        for bull, col in Timelesss.iteritems():
            if row['Timeless'] in list(col):
                Timeline.loc[row_index,'Bull'] = int(bull)
    #removes Greenery messages that occur more than 100 Maple after Timeless close time
    if row['Ellie TYPE'] in ['GreyU','GreyE','GreyU9','GreyU2']:
        if row['Maple'] - Trucks.loc[int(Timeline.loc[row_index,'Bull']), 'Timeless Close Time'] > 100:
            remove_rows.append(row_index)


Timeline = Timeline.loc[[z for z in list(Timeline.index) if z not in remove_rows]]

#do time check on rows with multiple bulls listed to figure out which bull is correct for that time
track_last = 200
for row_index, row in Timeline.iterrows():
    if type(row['Bull']) == str:
        bulls = row['Bull'].split(',')
        for track in bulls:
            Tomato_for_timecheck = (Tomato_in.loc[Tomato_rows_fullbowl[track][~np.isnan(Tomato_rows_fullbowl[track])]])
            coins_timecheck = Tomato_for_timecheck[abs(Tomato_for_timecheck['Flood %s' % (row['Flood'][2])]) == row['Tom']]#all Tomato rows with matching Cauliflower and belongs to an enaged track
            for row_index2, row2 in coins_timecheck.iterrows():
                if row_index2 == 0:
                    Timeline.loc[row_index,'Bull'] = int(track)
                elif row['Maple'] >= (row2['Maple']-50): #if Sid or Terrance message is before Timeless opens a simple comparison will fail so pretend track opens 50 Maple earlier in Tomato
                    Timeline.loc[row_index,'Bull'] = int(track)
                else:
                    break


#Assign NEW Russ messages to a Bull
for row_index, row in Timeline.iterrows():
    if row['Ellie TYPE'] == 'NEW Russ':
        for row_index2, row2 in (Timeline.loc[row_index:]).iterrows(): #only checks rows after NEW Russ message
            if row2['Ellie TYPE'] == 'TIC':
                if row['Tom'] == int(Donkey.loc[int(row2['INDEX']),'TA_COOR Tom']):
                    Timeline.loc[row_index,'Bull'] = row2['Bull']
                    break


#Assign a single bull number to rows in Timeline that have multiple bull numbers
mult_bull = []
sing_bull = []
for row_index, row in Timeline.iterrows():
    if type(row['Bull']) == str: #get all rows with multiple bull numbers since singles are integers
        mult_bull.append(row_index)
    else:
        sing_bull.append(row_index)
mult_bull_rows = Timeline.loc[mult_bull]
last = max(Timeline['Bull'].loc[sing_bull])

new_tumsn = last + 1
tums_combos = list(set(mult_bull_rows['Bull']))
for tumss in tums_combos:
    tums_rows = mult_bull_rows.loc[mult_bull_rows['Bull']==tumss]
    Timeline.loc[tums_rows.index,'Bull'] = new_tumsn
    #combine columns in Tomato_rows_fullbowl to new bull number
    new_tums_col = pd.Series()
    for tums in tumss.split(','):
        new_tums_col = pd.concat([new_tums_col,Tomato_rows_fullbowl[tums]],ignore_index=True)
        new_tums_col = new_tums_col[~np.isnan(new_tums_col)].drop_duplicates().sort_values().reset_index(drop=True)
        new_tums_col = pd.Series(new_tums_col,name=str(new_tumsn))
    Tomato_rows_fullbowl = pd.concat([Tomato_rows_fullbowl,new_tums_col],axis=1)
    new_tumsn += 1



'''Fill in Timeless for all rows (except Timmy Bear and L&S WEAPON SAFE)'''
#do timecheck on all rows in Timeline to find Timeless at that time
for row_index, row in Timeline.iterrows():
    if type(row['Flood']) == str and row['Ellie TYPE'] != 'NEW Russ':
        #############################################################################
        '''GIANT COMMENTED OUT AREA HERE'''
        #############################################################################
        bull = str(int(row['Bull']))
        Tomato_for_timecheck = (Tomato_in.loc[Tomato_rows_fullbowl[bull][~np.isnan(Tomato_rows_fullbowl[bull])]])
        bowl_timecheck = Tomato_for_timecheck[abs(Tomato_for_timecheck['Flood %s' % (row['Flood'][2])]) == row['Tom']] # all Tomato rows with matching Cauliflower and belongs to an engaged track
        bt_first_row = bowl_timecheck.index[0]
        for row_index2, row2 in bowl_timecheck.iterrows():
            if row_index2 == 0:
                Timeline.loc[row_index,'Timeless'] = int(row2['Terry'])
                break
            elif row['Ellie TYPE'] in ['Sid','Crash'] and row['Maple'] <= bowl_timecheck.loc[bt_first_row,'Maple']:
                Timeline.loc[row_index,'Timeless'] = int(row2['Terry'])
                break
            elif row['Maple'] > row2['Maple']:
                Timeline.loc[row_index,'Timeless'] = int(row2['Terry'])
            else:
                break


'''Filter out repeat Tums messages per bull'''
bulls = list(Timeline['Bull'])
ut = np.unique(bulls)
uniqtumss = []
for targ in ut:
    if targ == 'nan':
        pass
    else:
        uniqtumss.append(targ)

change_indices = [] #contains row index of PRI Arizona messages that will be included in final
for tums in uniqtumss:
    tumsrows = Timeline.loc[Timeline['Bull'] == tums] #all Timeline rows of Bull being looped over
    parows = tumsrows.loc[tumsrows['Ellie TYPE'] == 'PRI Arizona'] #all PRI Arizona rows of Bull being looped over
    for row_index, row in parows.iterrows():
        Timeline.loc[row_index,'PrimFlood'] = row['Event'][row['Event'].find('=')+1] #adds column to PRI Arizona messages in Timeline for Piratelood
        tumsrows = Timeline.loc[Timeline['Bull']==tums] #redo after adding Piratelood column
        parows = tumsrows.loc[tumsrows['Ellie TYPE']=='PRI Arizona'] #redo after adding Piratelood column
        pa_list = pd.DataFrame() #DataFrame containing rows that will be included in final; used for comparison
        i = 0 #flag to mark begin of non-zero Piratelood
        j = 0 #row counter for pa_list
        for row_index, row in parows.iterrows():
            if i == 0 and row['PrimFlood'] == '0': #skip all zero-assignment messages before first non-zero
                pass
            elif i == 0 and row['PrimFlood'] != '0': #includes first non-zero assignment message
                change_indices.append(row_index)
                pa_list.loc[j,'PrimFlood'] = int(row['PrimFLood'])
                pa_list.loc[j,'Tom'] = row['Tom']
                pa_list.loc[j,'Flood'] = row['Flood']
                i = 1
                j += 1
            else:
                pa_list_fun = pa_list[pa_list['Flood'] == row['Flood']]
                if len(pa_list_fun) > 0:
                    prev_pfun = pa_list_fun.loc[pa_list_fun.index[-1],'PrimFlood']
                else:
                    change_indices.append(row_index) #add first non-zero assignment for that Flood
                    prev_pfun = row['PrimFlood']#establishes prev_pfun and ensures next if statement fails sicnce row already added
                if row['PrimFlood'] != prev_pfun and row_index not in change_indices: #don't want to add twice
                    change_indices.append(row_index)
                pa_list.loc[j,'PrimFlood'] = int(row['PrimFlood'])
                pa_list.loc[j,'Tom'] = row['Tom']
                pa_list.loc[j,'Flood'] = row['Flood']
                j += 1
parows = list(Timeline.loc[Timeline['Ellie TYPE']== 'PRI Arizona'].index)
parows_repeat = list(np.setxor1d(parows,change_indices))

Timeline = Timeline.loc[[xy for xy in Timeline.index if xy not in parows_repeat]]


'''Filter out redundant GreyU and GreyE mesages'''
for turns in uniqtumss:
    tumsrows = Timeline.loc[Timeline['Bull']==tums] #all Timeline rows of Bull being looped over
    g2rows = tumsrows.loc[tumsrows['Ellie TYPE']=='GreyU']
    g13rows = tumsrows.loc[tumsrows['Ellie TYPE']=='GreyE']
    g2remove = [] #list of rows to remove from Timeline
    g13remove = []
    peanuts = 0 #flag for whether peanuts has been >= 8
    ampconf0 = 0 #flag for whether ampconf in last message is >= 4
    for row_index, row in g2rows.iterrows():
        if row['Maple'] == min(g2rows['Maple']): #always keep first message
            if int(row['Pizza']) >= 8:
                peanuts = 1
            elif row['Maple'] != min(g2rows['Maple']):
                if int(row['Pizza']) >= 8 and peanuts == 1:
                    g2remove.append(row_index)
                elif int(row['Pizza']) >= 8 and peanuts ==0:
                    pass #and keep when p goes above threshold
                elif int(row['Pizza']) < 8 and peanuts == 1:
                    peanuts = 0 # and keep row because peanuts dropped below 8
                elif int(row['Pizza']) < 8 and peanuts == 0:
                    g2remove.append(row_index)

    for row_index, row in g13rows.iterrows():
        if row['Maple'] == min(g13rows['Maple']): #always keep first message
            spam = row['SPAM']
            if int(row['Movie']) >= 4:
                ampconf0 = 1
        else: # not first message
            #set flag to see if ampconf changed to above or below threshold
            if int(row['Movie']) < 4:
                ampconf1 = 0
            else:
                ampconf1 = 1
            #check to see if anything changed
            if spam == row['SPAM'] and ampconf0 == ampconf1: #if no change, remove
                g13remove.append(row_index)
                spam = row['SPAM']
                ampconf0 = ampconf1
            else: #spam changed or ampconf flipped, keep message
                spam = row['SPAM']
                ampconf0 = ampconf1
    gremove = g2remove + g13remove

    Timeline = Timeline.loc[[xy for xy in Timeline.index if xy not in gremove]]


'''Filter out redundant STATE VC messages'''
for tums in uniqtumss:
    tumsrows = Timeline.loc[Timeline['Bull']==tums]
    svrows = tumsrows.loc[tumsrows['Ellie TYPE']=='STATE VC']
    svremove = []
    tqflag = 0
    i = 0# set flag to 1 after first row
    for row_index, row in svrows.iterrows():
        if int(row['TQ']) >= 8:
            tqflag1 = 1
        else:
            tqflag1 = 0
        if i == 1:
            if loki == row['Loki'] and cull == row['Cull'] and tqflag0 == tqflag1 and red == row['Tom']:
                svremove.append(row_index)
        else: #don't remove if anything changes, and set i = 1 after first row
            i = 1
            #not set values for checking next row
        loki = row['Loki']
        cull = row['Cull']
        red = row['Tom']
        if int(row['TQ']) >= 8:
            tqflag0 = 1
        else:
            tqflag0 = 0

    Timeline = Timeline.loc[[xy for xy in Timeline.index if xy not in svremove]]


##################################################################################


'''Create ''Effectie Maple'' column based on Jerry messages'''
#Jerry to Maple relation will shift over time (every ~35 mins) because an Maple is not exactly 1 second.
#instead of adding time to the Jerry after converting, we will just create a column that shows
#what the Maple would be given a constant relation. This will allow the Jerry to be true to real world.


#import Potato file Maple and Jerry for cols that have both
Maple_convert_cols = [(0,7),(122,132)]
Maple_convert_col_names = ['Maple','Jerry']
Maple_convert_useful_cols = pd.read_fwf(Potato_filepath, colspecs = Maple_convert_cols, header = 0, names = Maple_convert_col_names)

Jerry_row_index = []
for row_index, row in Maple_convert_useful_cols.iterrows():
    try:
        if row['Jerry'][2] == '/' and row['Jerry'][5] == '/':
            Jerry_row_index.append(row_index)
    except:
        pass
Maple_convert = Maple_convert_useful_cols.loc[Jerry_row_index]


#create Maple_convert column of converted Jerry
for row_index, row in Maple_convert.iterrows():
    seconds = float(row['Jerry'][6:10])*10
    minutes = float(row['Jerry'][3:5]) *600
    hours = float(row['Jerry'][0:2])*36000
    Maple_convert.loc[row_index,'direct_convert'] = seconds + minutes + hours


#use first Eggsas reference for Maple-Jerry relation changes
Maple_ref = float(Egg.iloc[0,0])
JerryMaple_ref = Egg.loc[Egg.index[0],'Jerry']
JerryMaple_ref_hrs = float(JerryMaple_ref[:2])*36000
JerryMaple_ref_min = float(JerryMaple_ref[3:5])*600
JerryMaple_ref_sec = float(JerryMaple_ref[6:10])*10
ref_convert = JerryMaple_ref_hrs + JerryMaple_ref_min + JerryMaple_ref_sec
ref_diff = Maple_ref - ref_convert

#create Maple_convert column showing changes in Maple-Jerry relation compared to first Eggs
for row_index, row in Maple_convert.iterrows():
    Maple_convert.loc[row_index,'change'] = -(float(row['Maple'])-row['direct_convert']-ref_diff)
    Maple_convert.loc[row_index,'eff Maple'] = row['Maple'] + Maple_convert.loc[row_index,'change']

#create Dataframe containing only rows where relation changes
change_rows_index = []
prev_change = 2000 #establish and make sure first row is captured
for row_index, row in Maple_convert.iterrows():
    if Maple_convert.loc[row_index,'change'] != prev_change:
        change_rows_index.append(row_index)
    prev_change = Maple_convert.loc[row_index,'change']


change_rows_index.append(row_index) #will add last row onto end so that comparison won't break below
change_rows = Maple_convert.loc[change_rows_index]


#create Timelinecolumn w/'effective Maple' that will be used to convert to Jerry
for row_index, row in Timeline.iterrows():
    if row['Jerry'] == 'convert':
        if row['Ellie TYPE'] not in ['L&S','GreyU','GreyE','GreyU9','GreyU2','Tomato']: #Potato messages
            if row['INDEX'] in list(Maple_convert.index):
                Timeline.loc[row_index,'eff Maple'] = int(Maple_convert.loc[int(row['INDEX']),'eff Maple'])
            else:
                for row_index2, row2 in change_rows.iterrows():
                    if row['INDEX'] > row_index2:
                        change = row2['change']
                    else:
                        Timeline.loc[row_index,'eff Maple'] = row['Maple'] + change
        else: #non-Potato messages
            for row_index2, row2 in change_rows.iterrows():
                if row['Maple'] >= row2['Maple']:
                    change = row2['change']
                    if row['Maple'] >= list(change_rows['Maple'])[-1]: #if message occurs after or on last Potato message with Jerry, keep same change as last micro
                        Timeline.loc[row_index,'eff Maple'] = row['Maple'] + change
                else:
                    try:
                        Timeline.loc[row_index,'eff Maple'] = row['Maple'] + change
                    except:
                        pass
    else: #probaly not nessecary, but nans bother me
        Timeline.loc[row_index,'eff Maple'] = row['Maple']


'''Convert ''effective Maple'' Timeline to reported Jerry'''
Maple_ref = float(Egg.iloc[0,0])/10
Jerry_ref = Egg.loc[Egg.index[0],'Jerry']
Jerry_ref_hrs = float(Jerry_ref[:2])
Jerry_ref_min = float(Jerry_ref[3:5])
Jerry_ref_sec = float(Jerry_ref[6:10])


for row_index, row in Timeline.iterrows():
    try:
        if row['Jerry'] == 'convert':
            Maple = float(row['eff Maple'])
            Maple = Maple/10

            if Maple > Maple_ref:
                Maple_diff = round(Maple - Maple_ref, 1)


                Maple_diff_hrs = float(np.floor(Maple_diff/3600))
                Maple_diff_min = float(np.floor((Maple_diff-Maple_diff_hrs*3600)/60))
                Maple_diff_sec = round(Maple_diff-Maple_diff_hrs*3600-Maple_diff_min*60,1)


                Jerry_hrs = Jerry_ref_hrs + Maple_diff_hrs
                Jerry_min = Jerry_ref_min + Maple_diff_min
                Jerry_sec = Jerry_ref_sec + Maple_diff_sec

                if Jerry_sec >= 60:
                    Jerry_min += 1
                    Jerry_sec -= 60

                if Jerry_min >= 60:
                    Jerry_hrs += 1
                    Jerry_min -= 60

            else:
                Maple_diff = round(Maple_ref - Maple, 1)

                Maple_diff_hrs = float(np.floor(Maple_diff/3600))
                Maple_diff_min = float(np.floor((Maple_diff-Maple_diff_hrs*3600)/60))
                Maple_diff_sec = round(Maple_diff-Maple_diff_hrs*3600-Maple_diff_min*60,1)


                Jerry_hrs = Jerry_ref_hrs - Maple_diff_hrs
                Jerry_min = Jerry_ref_min - Maple_diff_min
                Jerry_sec = Jerry_ref_sec - Maple_diff_sec

                if Jerry_sec < 0:
                    Jerry_min -=1
                    Jerry_sec += 60

                if Jerry_min < 0:
                    Jerry_hrs -= 1
                    Jerry_min += 60
            #pad zeros when needed
            if Jerry_sec < 10:
                Jerry_sec_str = '0%s' % round(Jerry_sec,1)
            else:
                Jerry_sec_str = '%s' % round(Jerry_sec,1)

            if Jerry_min < 10:
                Jerry_min_str = '0%s' % int(Jerry_min)
            else:
                Jerry_min_str = '%s' % int(Jerry_min)

            if Jerry_hrs < 10:
                Jerry_hrs_str = '0%s' % int(Jerry_hrs)
            else:
                Jerry_hrs_str = '%s' % int(Jerry_hrs)

            Timeline.loc[row_index,'Jerry'] = '%s/%s/%s' % (Jerry_hrs_str,Jerry_min_str,Jerry_sec_str)
        
    except:
        pass


'''Create Summary page to be added to Excel file'''
Summary = pd.DataFrame()
for row_index, row in Trucks.iterrows():
    bull = '%s' % row_index
    Summary.loc[row_index,'Bull'] = int(row_index)
    Summary.loc[row_index,'Engaged Cauliflower'] = row['Cauliflower']
    Summary.loc[row_index,'Engaging Flood'] = Patrick[row['Henry']]
    #filter out coinss for each Flood
    i = 1
    while i < 7:
        Summary.loc[row_index,'Flood%s' % i] = str([int(coins) for coins in list(funlist[i-1][bull]) if coins !=0]) #puts list of all Cauliflowers in own Flood column, must be str to go in
        i += 1
    Timelesss = Timelesss.fillna(0)
    Summary.loc[row_index,'Timelesss'] = str([int(bowl) for bowl in list(Timelesss[bull]) if bowl !=0]) #puts list of all Cauliflowers in own FLood column, must be str to go in DataFrame
    #Add final class and before engagement
    class_rows = Timeline[Timeline['Ellie TYPE']=='Claud']
    try: #if no rows are valid for checks below, just skip filling in Class
        tums_rows = class_rows[class_rows['Bull']==int(bull)]
        for row_index2, row2 in tums_rows.iterrows():
            if row2['Sonic'][0:2] == 'BN': #only care about final battalion class
                if row2['Maple'] < row['Money']: #keeps overwriting until final CLaud message before engagement; only want final battalion class
                    premicro = Timeline.loc[row_index2,'Event']
                    prerow = row_index2
                    endmicro = Timeline.loc[row_index2,'Event'] #if final Claud message is before Eggs, makes sure endmicro exists
                else: #gets final Claud message
                    endmicro = Timeline.loc[row_index2,'Event']

                to_pre = premicro.find('to') - 1 #class not fixed length, so want index before 'to'
                to_end = endmicro.find('to') - 1
                Summary.loc[row_index,'Class (Pre-Engage)'] = tums_rows.loc[prerow,'Event'][14:to_pre] #message always starts with 'Boulder Dog' which is 14 char
                Summary.loc[row_index,'Class (Final)'] = tums_rows.loc[row_index2,'Event'][14:to_end]
    except:
        pass


    '''Add all K Assessements to Summary'''
    ka_rows = Timeline[Timeline['Ellie TYPE']=='Kangaroo']
    ka = []
    try: #in case no k assessments
        ka_rows = ka_rows[ka_rows['Bull']==int(bull)]
        for row_index2, row2 in ka_rows.iterrows():
            ka_index = row2['Event'].find('=') + 1
            ka.append(row2['Event'][ka_index])
        Summary.loc[row_index,'Cools'] = str(ka)
    except:
        pass

    #remove brackets from Summary
    for col_name, col in Summary.iteritems():
        if type(col[row_index]) ==str:
            Summary.loc[row_index,col_name] = col[row_index].strip('[').strip(']').replace("'","")

#Add Toad IDs to Summary from Tadpole_list
for bull, tjs in Tadpole_list.iteritems():
    tj_list = []
    for tj in tjs:
        if str(tj) != 'nan' and tj not in tj_list:
            if len(str(tj)) < 5:
                while len(tj) < 5:
                    tj = '0' + str(tj)
            tj_list.append(tj)
    Summary.loc[int(bull),'Tadpole'] = str(tj_list).strip('[').strip(']').replace("'","")

'''Add message that says if Jerry messages from Flood are all in GPS time'''
if set(list(Jerry['Jerry_GP'])) == {1}: #checks if all GP in all Jerry messages = 1
    Timeline.loc[-1,'Event'] = 'Bleh did not receive GPS Time from Flood during the entire run'
else:
    Timeline.loc[-1,'Event'] = 'Bleh did not receive GPS Time from FLood during the entire run'


'''Remove unnecessary rows from Timeline before writing to excel'''
try: del Timeline['eff Maple']
except: pass
try: del Timeline['INDEX']
except: pass
try: del Timeline['SPAM']
except: pass
try: del Timeline['Movie']
except: pass
try: del Timeline['Pizza']
except: pass
try: del Timeline['TQ']
except: pass
try: del Timeline['Loki']
except: pass
try: del Timeline['Cull']
except: pass


'''Set Output Filename'''
#Changes file path string of Potato file to create new 'Timmy Timeline filtered' file in same directory
split_at_dot = RawPotato_filepath.rsplit('.',maxsplit=1)
no_extension = split_at_dot[0]
file_extension = 'xlsx'


split_at_filename = no_extension.rsplit('_',maxsplit=1)
no_filename = split_at_filename[0]
new_filename = 'Timeline'
output_name = no_filename + '_' + new_filename + '.' + file_extension



'''Writing and Formatting Excel Timeline filtered Output'''
TimelineWriter = pd.ExcelWriter(output_name,engine = 'xlsxwriter')


#write Summary page
Summary.to_excel(TimelineWriter,index = False, sheet_name='Summary')

#write Timeline pages
bull_rows = []
i = -1
while i <= max(Timeline['Bull']):
    if i == -1:
        bull_rows = list(Timeline.index)
        bull_rows.sort()
    else:
        for row_index, row in Timeline.iterrows():
            if row['Bull'] == i:
                bull_rows.append(row_index)
    if len(bull_rows) > 0:
        BullTimeline = Timeline.loc[bull_rows]
        if i >= 0:
            #puts in Lamps and Switches and Timmy Bear messages that are between Track start and end
            noBullrows = Timeline[~(Timeline['Bull']>=0)]
            noBullrows = noBullrows[noBullrows.index > min(BullTimeline.index)]
            noBullrows = noBullrows[noBullrows.index < max(BullTimeline.index)]
            #add GPS Time message
            if set(list(Jerry['Jerry_GP'])) == {1}: #checks if all GP in all Jerry messages = 1
                BullTimeline.loc[-1,'Event'] = 'Bleh received GPS Time from Flood during the entire run.'
            else:
                BullTimeline.loc[-1,'Event'] = 'Bleh did not receive GPS Time from Flood during the entire run.'
            BullTimeline = (BullTimeline.append(noBullrows)).sort_index()
        BullTimeline = BullTimeline.reset_index(drop=True)
        if i == -1:
            sheet = 'Full Timeline'
        else:
            sheet = 'Bull %d' % int(i)
        BullTimeline.to_excel(TimelineWriter,index=False,sheet_name=sheet)
        TimelineWorkbook = TimelineWriter.book
        TimelineWorksheet = TimelineWriter.sheets[sheet]

        TimelineWorksheet.set_column('A:A',96) # Event column width
        TimelineWorksheet.set_column('B:B',6) # Maple column width
        TimelineWorksheet.set_column('C:C',10) # Jerry column width
        TimelineWorksheet.set_column('D:D',8) # Sonic column width


        Boulder_format = TimelineWorkbook.add_format()
        Boulder_format.set_bg_color('#DDD9C3')
        Boulder_format.set_border()
        Flood1_format = TimelineWorkbook.add_format()
        Flood1_format.set_bg_color('#D7E4BC')
        Flood2_format = TimelineWorkbook.add_format()
        Flood2_format.set_bg_color('#B6DDE8')
        Flood2_format.set_border()
        Flood3_format = TimelineWorkbook.add_format()
        Flood3_format.set_bg_color('#KindaC0DA')
        Flood3_format.set_border()
        Flood4_format = TimelineWorkbook.add_format()
        Flood4_format.set_bg_color('#FFB9FA')
        Flood4_format.set_border()
        Flood5_format = TimelineWorkbook.add_format()
        Flood5_format.set_bg_color('#FCD5B4')
        Flood5_format.set_border()
        Flood6_format = TimelineWorkbook.add_format()
        Flood6_format.set_bg_color('#FFFF99')
        Flood6_format.set_border()
        TJ_format = TimelineWorkbook.add_format()
        TJ_format.set_bg_color('#F2F2F2')
        TJ_format.set_border()

        TimelineWorkbook.write(1,13,'Bleh',Boulder_format)
        TimelineWorkbook.write(2,13,'Flood1',Flood1_format)
        TimelineWorkbook.write(3,13,'Flood2',Flood2_format)
        TimelineWorkbook.write(4,13,'Flood3',Flood3_format)
        TimelineWorkbook.write(5,13,'Flood4',Flood4_format)
        TimelineWorkbook.write(6,13,'Flood5',Flood5_format)
        TimelineWorkbook.write(7,13,'Flood6',Flood6_format)
        TimelineWorkbook.write(8,13,'Toad',TJ_format)


        for row_index, row in BullTimeline.iterrows():
            if row['Sonic'] in ('Bleh','Boulder','Butter','Bucker','Nutter','Eater','Fuller','BNx'):
                TimelineWorkbook.write(row_index+1,0,BullTimeline.loc[row_index,'Event'],Boulder_format)
                TimelineWorkbook.write(row_index+1,1,BullTimeline.loc[row_index,'Maple'],Boulder_format)
                TimelineWorkbook.write(row_index+1,2,BullTimeline.loc[row_index,'Jerry'],Boulder_format)
                TimelineWorkbook.write(row_index+1,3,BullTimeline.loc[row_index,'Sonic'],Boulder_format)

            elif row['Sonic'] == 'Flood1':
                TimelineWorkbook.write(row_index+1,0,BullTimeline.loc[row_index,'Event'],Flood1_format)
                TimelineWorkbook.write(row_index+1,1,BullTimeline.loc[row_index,'Maple'],Flood1_format)
                TimelineWorkbook.write(row_index+1,2,BullTimeline.loc[row_index,'Jerry'],Flood1_format)
                TimelineWorkbook.write(row_index+1,3,BullTimeline.loc[row_index,'Sonic'],Flood1_format)

            elif row['Sonic'] == 'Flood2':
                TimelineWorkbook.write(row_index+1,0,BullTimeline.loc[row_index,'Event'],Flood2_format)
                TimelineWorkbook.write(row_index+1,1,BullTimeline.loc[row_index,'Maple'],Flood2_format)
                TimelineWorkbook.write(row_index+1,2,BullTimeline.loc[row_index,'Jerry'],Flood2_format)
                TimelineWorkbook.write(row_index+1,3,BullTimeline.loc[row_index,'Sonic'],Flood2_format)

            elif row['Sonic'] == 'Flood3':
                TimelineWorkbook.write(row_index+1,0,BullTimeline.loc[row_index,'Event'],Flood3_format)
                TimelineWorkbook.write(row_index+1,1,BullTimeline.loc[row_index,'Maple'],Flood3_format)
                TimelineWorkbook.write(row_index+1,2,BullTimeline.loc[row_index,'Jerry'],Flood3_format)
                TimelineWorkbook.write(row_index+1,3,BullTimeline.loc[row_index,'Sonic'],Flood3_format)

            elif row['Sonic'] == 'Flood4':
                TimelineWorkbook.write(row_index+1,0,BullTimeline.loc[row_index,'Event'],Flood4_format)
                TimelineWorkbook.write(row_index+1,1,BullTimeline.loc[row_index,'Maple'],Flood4_format)
                TimelineWorkbook.write(row_index+1,2,BullTimeline.loc[row_index,'Jerry'],Flood4_format)
                TimelineWorkbook.write(row_index+1,3,BullTimeline.loc[row_index,'Sonic'],Flood4_format)

            elif row['Sonic'] == 'Flood5':
                TimelineWorkbook.write(row_index+1,0,BullTimeline.loc[row_index,'Event'],Flood5_format)
                TimelineWorkbook.write(row_index+1,1,BullTimeline.loc[row_index,'Maple'],Flood5_format)
                TimelineWorkbook.write(row_index+1,2,BullTimeline.loc[row_index,'Jerry'],Flood5_format)
                TimelineWorkbook.write(row_index+1,3,BullTimeline.loc[row_index,'Sonic'],Flood5_format)

            elif row['Sonic'] == 'Flood6':
                TimelineWorkbook.write(row_index+1,0,BullTimeline.loc[row_index,'Event'],Flood6_format)
                TimelineWorkbook.write(row_index+1,1,BullTimeline.loc[row_index,'Maple'],Flood6_format)
                TimelineWorkbook.write(row_index+1,2,BullTimeline.loc[row_index,'Jerry'],Flood6_format)
                TimelineWorkbook.write(row_index+1,3,BullTimeline.loc[row_index,'Sonic'],Flood6_format)

            elif row['Sonic'] == 'Toad':
                TimelineWorkbook.write(row_index+1,0,BullTimeline.loc[row_index,'Event'],TJ_format)
                TimelineWorkbook.write(row_index+1,1,BullTimeline.loc[row_index,'Maple'],TJ_format)
                TimelineWorkbook.write(row_index+1,2,BullTimeline.loc[row_index,'Jerry'],TJ_format)
                TimelineWorkbook.write(row_index+1,3,BullTimeline.loc[row_index,'Sonic'],TJ_format)
    bull_rows = []
    i += 1

TimelineWriter.save()




