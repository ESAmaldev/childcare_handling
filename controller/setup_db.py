import sqlite3
import csv
from datetime import datetime

con=sqlite3.connect("childcare_data.db")
cur = con.cursor()

#You can drop tables in LIFO order due to foreign key dependancies
con.execute('DROP TABLE IF EXISTS inspection_data')
con.execute('DROP TABLE IF EXISTS location_data')

con.execute('CREATE TABLE location_data (PROVISION_TYPE TEXT,REG_DATE DATE,REG_STATUS TEXT,GOV_REGION TEXT,LOCAL_AUTHORITY TEXT,CONSTITUENCY TEXT,SECTOR TEXT,ORG_OWNER TEXT,EVENT_NUM INTEGER)')
con.execute('CREATE TABLE inspection_data (EVENT_TYPE TEXT,INSPECT_DATE DATE,PUBLISH_DATE DATE,EVENT_NUM INTEGER,OVERALL_EXP TEXT,HELP_CARE_EFF TEXT,ADMIN_EFF TEXT)')

with open('childcare_data.csv', newline='') as data:
    reader = csv.reader(data, delimiter=";")
    next(reader) # skip the header line
    errCount=0
    errlst=[]
    for row in reader:
        print(row)

        PROVISION_TYPE=row(0)
        REG_DATE= datetime.strptime(row(1),'%m-%d-%Y').date()
        REG_STATUS=row(2)
        GOV_REGION=row(3)
        LOCAL_AUTHORITY=row(4)
        CONSTITUENCY=row(5)
        SECTOR=row(6)
        ORG_OWNER=row(7)
        EVENT_TYPE=row(8)
        INSPECT_DATE=datetime.strptime(row(9),'%m-%d-%Y').date()
        PUBLISH_DATE=datetime.strptime(row(10),'%m-%d-%Y').date()
        EVENT_NUM=int(row(11))
        OVERALL_EXP=row(12)
        HELP_CARE_EFF=row(13)
        ADMIN_EFF=row(14)

        try:
            cur.execute('INSERT INTO location_data VALUES (?,?,?,?,?,?,?,?,?)', (PROVISION_TYPE ,REG_DATE ,REG_STATUS ,GOV_REGION ,LOCAL_AUTHORITY ,CONSTITUENCY ,SECTOR ,ORG_OWNER ,EVENT_NUM))
            conn.commit()
            cur.execute('INSERT INTO inspection_data VALUES (?,?,?,?,?,?,?)', (EVENT_TYPE ,INSPECT_DATE ,PUBLISH_DATE ,EVENT_NUM ,OVERALL_EXP ,HELP_CARE_EFF ,ADMIN_EFF))
            conn.commit()

        except:
            errCount=+1
            errCount.append(row(11))

    print(errCount," records were not inserted correctly")

con.close()   




