import mysql.connector
from sqlalchemy import create_engine
import pymysql
import json
from flask import Flask
import pandas as pd
import os
from datetime import datetime
from dateutil import parser
import numpy as np
import xlrd


app = Flask(__name__)

# from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile36 as zipfile

# api = KaggleApi()
# api.authenticate()
# api.dataset_download_files('dannielr/marvel-superheroes')

# try:
#     if os.path.exists('./marvel-superheroes.zip'):
#         print('file already been downloaded')
#         pass
#     else:
try:
    with zipfile.ZipFile('marvel-superheroes.zip','r') as zip:
        zip.extractall('./datasets/')
except Exception as e:
    print(e)
else:
    print('file extracted')      

destination_folder= './outputfile/'
if os.path.exists(destination_folder):
    pass
else:
    os.mkdir(destination_folder)    

def write_df_to_db(df, table_name):
    try:
        print('inside write_df_to_db')
        host="mysqldb"
        user="root"
        password="p@ssw0rd1"
        database="outputdb"       
        engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format(user,password,host,database))
        df.to_sql(table_name, engine, index=False, if_exists="append")
    except Exception as e:
        print('error from write_df_to_db')
        print(e)
    else:
        print('write_df_to_db success')
    finally:
        engine.dispose()

def remove_duplicates(df):
    col=list(df.columns)
    df.drop_duplicates(col)
    return df

def read_file(filename):
    ext = filename.split('.')[2]
    try:
        print('reading file...')
        if ext == 'xlsx':
            df = pd.read_excel(filename)
        else:
            df = pd.read_csv(filename)
    except Exception as e:
        print("file cannot be read")
    else:
        print('done reading file '+filename)
        return df

def save_file_csv(folder, filename,df):
    path = folder+filename
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        print('failed to write file to {}'.format(path))
        print(e)
    else:
        print('file {} successfully saved'.format(filename))

    
# @app.route('/')
# def hello_world():
#   return 'Hello, Docker!'

# @app.route('/initdb')
# def db_init():
mydb = mysql.connector.connect(
host="mysqldb",
user="root",
password="p@ssw0rd1"
)
cursor = mydb.cursor()

cursor.execute("DROP DATABASE IF EXISTS outputdb;")
cursor.execute("CREATE DATABASE outputdb;")
cursor.close()

mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="outputdb"
)
cursor = mydb.cursor()
cursor.execute("CREATE TABLE `character_attributes` (`char_name` varchar(100) NOT NULL,`alignment` varchar(10) NULL,`intelligence` int NULL,`strength` int NULL,`speed` int NULL,`durability` int NULL,`power` int NULL,`combat` int NULL,`total` int NULL,`gender` varchar(20) NULL,`eyecolor` varchar(50) NULL,`race` varchar(50) NULL,`haircolor` varchar(20) NULL,`skincolor` varchar(20) NULL,`height` float NULL,`weight` float NULL);")
cursor.execute("CREATE TABLE `character_power_matrix` (`char_name` varchar(100) not null,`agility` varchar(10) null,`accelerated_healing` varchar(10) null,`lantern_power_ring` varchar(10) null,`dimensional_awareness` varchar(10) null,`cold_resistance` varchar(10) null,`durability` varchar(10) null,`stealth` varchar(10) null,`energy_absorption` varchar(10) null,`flight` varchar(10) null,`danger_sense` varchar(10) null,`underwater_breathing` varchar(10) null,`marksmanship` varchar(10) null,`weapons_master` varchar(10) null,`power_augmentation` varchar(10) null,`animal_attributes` varchar(10) null,`longevity` varchar(10) null,`intelligence` varchar(10) null,`super_strength` varchar(10) null,`cryokinesis` varchar(10) null,`telepathy` varchar(10) null,`energy_armor` varchar(10) null,`energy_blasts` varchar(10) null,`duplication` varchar(10) null,`size_changing` varchar(10) null,`density_control` varchar(10) null,`stamina` varchar(10) null,`astral_travel` varchar(10) null,`audio_control` varchar(10) null,`dexterity` varchar(10) null,`omnitrix` varchar(10) null,`super_speed` varchar(10) null,`possession` varchar(10) null,`animal_oriented_powers` varchar(10) null,`weapon-based_powers` varchar(10) null,`electrokinesis` varchar(10) null,`darkforce_manipulation` varchar(10) null,`death_touch` varchar(10) null,`teleportation` varchar(10) null,`enhanced_senses` varchar(10) null,`telekinesis` varchar(10) null,`energy_beams` varchar(10) null,`magic` varchar(10) null,`hyperkinesis` varchar(10) null,`jump` varchar(10) null,`clairvoyance` varchar(10) null,`dimensional_travel` varchar(10) null,`power_sense` varchar(10) null,`shapeshifting` varchar(10) null,`peak_human_condition` varchar(10) null,`immortality` varchar(10) null,`camouflage` varchar(10) null,`element_control` varchar(10) null,`phasing` varchar(10) null,`astral_projection` varchar(10) null,`electrical_transport` varchar(10) null,`fire_control` varchar(10) null,`projection` varchar(10) null,`summoning` varchar(10) null,`enhanced_memory` varchar(10) null,`reflexes` varchar(10) null,`invulnerability` varchar(10) null,`energy_constructs` varchar(10) null,`force_fields` varchar(10) null,`self-sustenance` varchar(10) null,`anti-gravity` varchar(10) null,`empathy` varchar(10) null,`power_nullifier` varchar(10) null,`radiation_control` varchar(10) null,`psionic_powers` varchar(10) null,`elasticity` varchar(10) null,`substance_secretion` varchar(10) null,`elemental_transmogrification` varchar(10) null,`technopath/cyberpath` varchar(10) null,`photographic_reflexes` varchar(10) null,`seismic_power` varchar(10) null,`animation` varchar(10) null,`precognition` varchar(10) null,`mind_control` varchar(10) null,`fire_resistance` varchar(10) null,`power_absorption` varchar(10) null,`enhanced_hearing` varchar(10) null,`nova_force` varchar(10) null,`insanity` varchar(10) null,`hypnokinesis` varchar(10) null,`animal_control` varchar(10) null,`natural_armor` varchar(10) null,`intangibility` varchar(10) null,`enhanced_sight` varchar(10) null,`molecular_manipulation` varchar(10) null,`heat_generation` varchar(10) null,`adaptation` varchar(10) null,`gliding` varchar(10) null,`power_suit` varchar(10) null,`mind_blast` varchar(10) null,`probability_manipulation` varchar(10) null,`gravity_control` varchar(10) null,`regeneration` varchar(10) null,`light_control` varchar(10) null,`echolocation` varchar(10) null,`levitation` varchar(10) null,`toxin_and_disease_control` varchar(10) null,`banish` varchar(10) null,`energy_manipulation` varchar(10) null,`heat_resistance` varchar(10) null,`natural_weapons` varchar(10) null,`time_travel` varchar(10) null,`enhanced_smell` varchar(10) null,`illusions` varchar(10) null,`thirstokinesis` varchar(10) null,`hair_manipulation` varchar(10) null,`illumination` varchar(10) null,`omnipotent` varchar(10) null,`cloaking` varchar(10) null,`changing_armor` varchar(10) null,`power_cosmic` varchar(10) null,`biokinesis` varchar(10) null,`water_control` varchar(10) null,`radiation_immunity` varchar(10) null,`vision_-_telescopic` varchar(10) null,`toxin_and_disease_resistance` varchar(10) null,`spatial_awareness` varchar(10) null,`energy_resistance` varchar(10) null,`telepathy_resistance` varchar(10) null,`molecular_combustion` varchar(10) null,`omnilingualism` varchar(10) null,`portal_creation` varchar(10) null,`magnetism` varchar(10) null,`mind_control_resistance` varchar(10) null,`plant_control` varchar(10) null,`sonar` varchar(10) null,`sonic_scream` varchar(10) null,`time_manipulation` varchar(10) null,`enhanced_touch` varchar(10) null,`magic_resistance` varchar(10) null,`invisibility` varchar(10) null,`sub-mariner` varchar(10) null,`radiation_absorption` varchar(10) null,`intuitive_aptitude` varchar(10) null,`vision_-_microscopic` varchar(10) null,`melting` varchar(10) null,`wind_control` varchar(10) null,`super_breath` varchar(10) null,`wallcrawling` varchar(10) null,`vision_-_night` varchar(10) null,`vision_-_infrared` varchar(10) null,`grim_reaping` varchar(10) null,`matter_absorption` varchar(10) null,`the_force` varchar(10) null,`resurrection` varchar(10) null,`terrakinesis` varchar(10) null,`vision_-_heat` varchar(10) null,`vitakinesis` varchar(10) null,`radar_sense` varchar(10) null,`qwardian_power_ring` varchar(10) null,`weather_control` varchar(10) null,`vision_-_x-ray` varchar(10) null,`vision_-_thermal` varchar(10) null,`web_creation` varchar(10) null,`reality_warping` varchar(10) null,`odin_force` varchar(10) null,`symbiote_costume` varchar(10) null,`speed_force` varchar(10) null,`phoenix_force` varchar(10) null,`molecular_dissipation` varchar(10) null,`vision_-_cryo` varchar(10) null,`omnipresent` varchar(10) null,`omniscient` varchar(10) null);")
cursor.execute("CREATE TABLE `character_comics` (`char_name` varchar(100) not null,`comics_title` varchar(150) null,`issue_number` int null,`description` varchar(3000) null);")
cursor.execute("CREATE TABLE `character_variation` (`name` varchar(100) null,`identity` varchar(50) null,`alignment` varchar(20) null,`eyecolor` varchar(20) null,`haircolor` varchar(20) null,`gender` varchar(20) null,`status` varchar(20) null,`appearances` int null,`firstappearance` datetime null,`year` int null,`universe` varchar(20) null,`char_name` varchar(100) null);")
cursor.close()

# return 'init database'

# @app.route('/loaddb')
# def process_data():

#path and filenames
filename1 = './datasets/marvel_dc_characters.xlsx'
filename2 = './datasets/superheroes_power_matrix.csv'
filename3 = './datasets/marvel_characters_info.csv'
filename4 = './datasets/comics.csv'
filename5 = './datasets/charcters_stats.csv'
filename6 = './datasets/charactersToComics.csv'
filename7 = './datasets/characters.csv' 


#character variation table
#from the file filter characters from Marvel Universe 
marvel_chars = read_file(filename1)
print('total records: {} in {}'.format(len(marvel_chars.index),filename1))
marvel_chars = marvel_chars[marvel_chars['Universe']=='Marvel']
print('total records: {} after filtering universe = Marvel'.format(len(marvel_chars.index)))

#data cleansing for 1st file
marvel_chars['FirstAppearance']=pd.to_datetime(marvel_chars.FirstAppearance)
marvel_chars['Year'] = marvel_chars['FirstAppearance'].dt.strftime('%Y')
marvel_chars['char_name'] = marvel_chars['Name'].str.partition("(")[0]
character_variation_df = remove_duplicates(marvel_chars)
print('total records: {} after dedup'.format(len(character_variation_df.index)))
character_variation_df=character_variation_df.drop(columns=['ID']).rename(str.lower,axis='columns')

#write as a csv file
save_file_csv(destination_folder, 'character_variation.csv',character_variation_df)

#load df to db
write_df_to_db(character_variation_df, "character_variation")



#character power matrix
char_power_matrix = pd.read_csv(filename2)
print('total records: {} in {}'.format(len(char_power_matrix.index),filename2))

#data cleansing:
char_power_matrix_df = remove_duplicates(char_power_matrix)
print('total records: {} after dedup'.format(len(char_power_matrix_df.index)))
char_power_matrix_df = char_power_matrix_df.rename(str.lower, axis='columns').rename(columns={'name':'char_name'}).rename(columns=lambda s: s.replace(' ','_'))

#write as a csv file
save_file_csv(destination_folder, 'char_power_matrix.csv',char_power_matrix_df)

#load df to db
write_df_to_db(char_power_matrix_df, "character_power_matrix")



#character attributes
char_attribute1 = pd.read_csv(filename5) #char_stats
print('total records: {} in {}'.format(len(char_attribute1.index),filename5))

#char attribute1 data cleansing
char_attribute1.fillna(0)
char_attribute1['Total'] = char_attribute1.iloc[:,2:8].sum(axis=1)
char_attribute1_df = remove_duplicates(char_attribute1)
print('total records: {} after dedup'.format(len(char_attribute1_df.index)))
char_attribute2 = read_file(filename3) #marvel_chars_info
print('total records: {} in {}'.format(len(char_attribute2.index),filename3))

#char attribute2 data cleansing
char_attribute2 = char_attribute2[char_attribute2['Publisher']=='Marvel Comics'].drop(columns=['ID','Alignment','Publisher']).replace('-',np.NaN)
print('total records after filtering publisher = Marvel Comics: ', len(char_attribute2.index))
char_attribute2_df = remove_duplicates(char_attribute2)
print('total records: {} after dedup'.format(len(char_attribute2_df.index)))

#merge and create a character attributes file
print('merging {} and {}'.format(filename3,filename5))
char_attributes_df = char_attribute1_df.merge(char_attribute2_df, how='left', on='Name') \
                    .drop_duplicates(subset=['Name'], keep='first')
char_attributes_df = char_attributes_df.rename(str.lower,axis='columns').rename(columns={'name':'char_name'})
print('done!')
print(len(char_attributes_df.index),' rows')

#write as a csv file
save_file_csv(destination_folder, 'char_attributes.csv',char_attributes_df)

#load df to db
write_df_to_db(char_attributes_df, "character_attributes")



#comics and characters
comics = read_file(filename4) #comics.csv
characters = read_file(filename7) #characters.csv
char_to_comics = read_file(filename6) #charactersToComics.csv

print('total records: {} in {}'.format(len(comics.index),filename4))
print('total records: {} in {}'.format(len(characters.index),filename7))
print('total records: {} in {}'.format(len(char_to_comics.index),filename6))

#map characters and comics to char_to_comics
char_to_comics_df = char_to_comics.merge(characters, how='left', on='characterID')
char_to_comics_df = char_to_comics_df.merge(comics, how='left', on='comicID')

#data cleansing
character_comics_df = char_to_comics_df.drop(columns=['comicID','characterID']).rename(columns={'name':'char_name','title':'comics_title','issueNumber':'issue_number'}).rename(str.lower, axis='columns')
character_comics_df = remove_duplicates(character_comics_df)
print(len(character_comics_df.index),' rows')

#write as a csv file
save_file_csv(destination_folder, 'character_comics.csv',character_comics_df)

# #load df to db
write_df_to_db(character_comics_df, "character_comics")


if __name__ == "__main__":
    app.run(host ='0.0.0.0') 
