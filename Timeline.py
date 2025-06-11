

import pandas as pd
import numpy as np
#import tkinter as tk
from tkinter import *
import os
import pdb

RawPotato_filepath = r'.doc'
Tomato_filepath = r'.xlsx'
Greenery_filepath = r'.doc'
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
                







