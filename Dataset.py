import os
import pandas as pd




def get_data(data_group):
    DATA_DIR='SemEval2018-Task1-all-data/English/EI-oc/'
    MAIN_FILE=os.path.join(DATA_DIR,data_group)
    TXT_FILES=os.listdir(MAIN_FILE)
    data=pd.DataFrame()
    for file in TXT_FILES:
        file_loc=os.path.join(MAIN_FILE,file)
        df=pd.read_csv(file_loc, delimiter='\t')
        data=pd.concat([data,df], ignore_index=True)
     
    return data


    

