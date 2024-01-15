import gspread
import config
import pandas as pd

gc = gspread.service_account(filename=config.name_json)
sh= gc.open_by_url("https://docs.google.com/spreadsheets/d/11af795c73hBh9kCRuT8dqc51fXvrVBX2tknP2QqWNMQ/edit#gid=0")
worksheet = sh.sheet1
df = pd.DataFrame(worksheet.get_all_records())

def free_hours(date:str)-> list:
    return list(df.loc[df[date]=='']['Время/Дата'])

def record_user(date:str,hour:str,user_name:str):
    c=worksheet.find(date).col
    r=worksheet.find(hour).row
    worksheet.update_cell(r, c, user_name)
    pass