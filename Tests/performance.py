from ceic_api_client.pyceic import Ceic
from ceic_api_client.api_client import ApiClient
from ceic_api_client.apis.dictionary_api import DictionaryApi
from ceic_api_client.apis.series_api import SeriesApi
from ceic_api_client.apis.insights_api import InsightsApi
from  datetime import datetime
from Common import config
from Common.config import *
from Common.html_report import *

#import urllib3
#http = urllib3.HTTPConnectionPool('https://insights.ceicdata.com/Untitled-insight', maxsize=1500)

seriesid ="407208797,406677387,407019287,407896007,407723377,407174517,408009637,406629517,408012897,406599267,407317997,407485777,407782107,407395457,407083757,407680277,407869007,407963787,406973777,407841127,407054077,406846197,407847937,408042347,407217797,407670077,407159687,407975817,407036127,407652447,406855157,407129167,406797997,407777567,407057677,407964797,407595607,407473467,406984717,406938367,407363997,407209927,406528137,407413867,408074047,407455287,417797147,407093497,407705587,406773627,407171857,407132377,406778927,407693287,407772547,406564267,406817917,407633037,406826197,407843507,406686297,407436737,407237577,406714107,406710037,407510727,407886597,406666487,407705727,407578197,407338427,407577137,407679947,407828327,406962307,407655747,407884927,407137187,407215357,407807667,407307457,407814687,407135677,407769707,407041107,406971867,407685977,407333797,406977597,407126217,407599797,407090887,407635597,407872597,407783557,407567867,407803037,407715017,406731657,406791827,407089697,407238697,407086987,407159577,406973707,417799307,407570517,406787907,407145217,407769317,407296647,407093767,407176567,406986267,407986407,407400817,408029367,407293697,407592187,406603347,406533927,406966247,407891307,407325947,407758957,407152567,406691557,406919617,406830027,408039097,406603287,407100617,407178877,406685797,407327287,406866967,407675517,406717627,407626457,407656417,406991167,407437817,407060327,407253417,407153227,407125307,407382127,406610327,406966317,407505447,407684437,407616837,406975397,417798027,407169877,407088727,406641697,407713457,407586657,407022927,407825277,406693367,407207927,407287527,407347697,407080007,417797637,407547457,407449887,406681487,406747697,406639007,407551207,406981467,406833067,407560727,407320067,406927517,407640017,406777787,407347497,406907587,407972637,407493817,407808227,407017607,407206317,417798177,406831907,407354987,407259297,407507967,406892597,407164737,406993957,406631967,406820117,407853697,406757977,406773997,417798947,407885057,407504837,407922587,406744677,407509157,407369187,407461287,407322827,406745297,407490657,408028137,407219117,406608567,407152817,406799557,407020797,407475167,406945347,407058697,407705987,406900387,407684847,407225397,408055597,407903197,407830457,406637327,407357867,407765627,407742577,407665847,406893717,407492927,408057907,406672437,407165547,407881647,406784967,406579527,407659487,406545577,407483947,407631977,407426167,408013767,407226657,407464667,407045417,407152867,407087217,407968627,406789307,408011197,407861317,407206917,406794097,407129857,407628287,407171617,407903877,407375827,406784667,407716437,417798237,407362047,407518297,406580447,406980297,407321977,406818137,407961707,407508277,408080287,406778747,407819927,407105797,406555587,408050187,407247607,406969267,407003397,406671247,407322047,407619597,406933997,407440867,407843567,407505617,407616257,407950767,407867747,406771537,407467907,406595507,407419817,407274977,407768357,407347977,407647307,407402657,407484477,407231697,406780757,407494527,407293587,406938037,407307227,407560857,406821867,407597667,408061097,407974617,407400567,407538257,407450307,407000117,406830367,406920207,406970447,407030687,407120277,406782817,417797037,407835237,407056577,407412447,408037497,407465377,407283827,407374037,406816237,406618177,407212187,407838247,407482507,407404337,406564307,407901377,407255507,406602027,407590877,407720757,407342937,406861367,406631587,406869887,406671077,407882047,406831477,407445047,407977287,406600697,407411187,406678507,407887837,407617977,406801077,407399457,407250687,407292087,407440587,407165007,407213067,406648847,406796987,407338217,407955837,407428647,407243817,417799257,406899987,407357177,406908467,407983127,407646347,406984407,406536557,406655527,407397337,407018907,407385587,406811067,417797947,407734577,407714717,408049067,407018637,406905707,407364087,406942007,406567377,407523067,407151537,406966647,407375627,406610677,407157227,407098237,407698567,407457087,407836927,406741387,407395867,417797847,406643387,407618147,406991087,407695217,406931357,407203907,407032767,408020447,407011067,407567717,406948407,406715007,417797677,407923817,407692037,407883637,406791307,407696447,407322747,407179037,407054567,406784267,407537247,407403037,406642977,406969677,275055102,275239102,275306802,275076502,275096402,275259402,275114402,275127802,275143602,275162202,275181002,341780102,298229102,275218702,274911302,274932402,274953502,275013002,275034102,274993002,275286902,275326902,275346802,274448202,264537702,266346602,386845687,386848317,264517702,386840427,386843057,264707202,266361502,386856207,386858837,264687202,386850947,386853577,224281801,224282101,224282001,224282301,224281901,275381102,274469002,275538402,275720902,275788702,275559802,275579802,275741202,275597402,275609702,275626102,275645002,275663502,275682502,298287002,275700502,275395502,275416602,275437702,275496402,275517502,275476702,275768802,335161202,275866002,224282201"
access_token ="y6vaX4hIhKHAXFew1izyljHzQvPFBArvHTgTJ8dcz3pea5ZfGKHuC9y4VXImQZZhjIOWWzgvZG0lR1ooHCm0i15FdsG2HkbduSNBwiMc50eITbhdyEV5gai7FG7uejM6"
api_client = ApiClient( header_name="Authorization", header_value=access_token )
series_api = SeriesApi( api_client=api_client )
id = seriesid.split(",")
newseriesid =""
dict = []
p= 0
r= 0


def update_without_overwriting(d, x):
    dict.update({k: v for k, v in x.items() if k not in d})

#for i in range (len(id)): print id[i]

for num in range(1, len(id)+1):
    newseriesid = newseriesid +"," +id[r]
    p +=1
    r +=1
    if p%100 == 0:
        newseriesid = newseriesid[1:]
        series_metadata_result = series_api.get_series_metadata( id=newseriesid ).to_dict()
        dict.append(series_metadata_result)
        newseriesid = ""
        p = 0
        #print("#######################")

        #print("#######################")

        # print (p)
        # print (r)
        # print("#######################")
        # print (newseriesid)

        #break
print dict
import dicttoxml
xml_data = dicttoxml.dicttoxml( dict, attr_type=False, root=True )
file_path = "C:\\Users\\rchethana\\Documents\\SDK_Automation\\XML-ActualData\Metadata\chethana.xml"

f = open(file_path, 'w' )
f.write( xml_data )
f.close()
#return file_path




