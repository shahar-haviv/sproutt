from datetime import datetime

from dto.request import ReturnToClient

# from db.db import db

from datetime import datetime, tzinfo, timezone

def _read_from_file_logss_and_avrg(type:str ,formadate:str , todate:str) ->ReturnToClient:
 counter = 0
 entitymass=0
 entity_mass_avg=0
 with open(f'xg-{type}-1min-avg.log') as logs_document:
        lines = logs_document.readlines()
        for line in lines:
            if (formadate <= datetime.fromtimestamp(float(line.split(",")[0])) <= todate):
                counter += 1
                entitymass += float(line.split(",")[2])
        if counter > 0 :
            entity_mass_avg= entitymass/counter
 return ReturnToClient(type , entity_mass_avg , counter)
 

# didnt finish
# def _read_from_db_logss_and_avrg(type:str ,formadate:str , todate:str) ->ReturnToClient:
#     print(formadate)
#     logs = db.planets_tests_dev.find(
#         {'logTime': {
#         '$gte': datetime(2019, 1, 1, 0, 0, 0, tzinfo=timezone.utc), 
#         '$lt': datetime(2019, 9, 2, 0, 0, 0, tzinfo=timezone.utc)
#     }, 
#     'name': 'earth'
# }
#     )
#     print(logs)
    # return ReturnToClient(type , entity_mass_avg , counter)



def read_logss(type:str ,froma:str , to:str ):
    formadate = datetime.fromisoformat(froma)
    todate = datetime.fromisoformat(to)
    return _read_from_file_logss_and_avrg(type , formadate , todate) 
