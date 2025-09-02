import os
import pandas as pd
from datetime import datetime

class overRideIngest:
    df_rate_overrides=None
    df_extra_person_charges=None
    def __init__(self,df_which_ones,override_dir,output_dir):
        self.df_which_ones=df_which_ones
        self.override_dir=override_dir
        self.output_dir=output_dir
    def read_overrides(self):
        all_overrides=[]
        all_extra_cahrges=[]
        for file in os.listdir(self.override_dir):
            all_overrides.append(pd.read_excel(os.path.join(self.override_dir,file),sheet_name='BARRates_DateRange'))
            all_extra_cahrges.append(pd.read_excel(os.path.join(self.override_dir,file),sheet_name='BARates_Form'))
            self.df_rate_overrides=pd.concat(all_overrides)
            self.df_extra_person_charges=pd.concat(all_extra_cahrges)
    def produce_file_for_IT(self):
        df_which_one=self.df_which_ones
        out_all=self.df_rate_overrides.copy()
        out_all.rename(columns={'inncode':'propCode','RoomTypeCode':'RoomType'
          },inplace=True)
        dow=['Sun','Mon','Wed','Thu','Fri','Sat']
        df_ext_per_chg=self.df_extra_person_charges.copy()
    #This line is for demo
