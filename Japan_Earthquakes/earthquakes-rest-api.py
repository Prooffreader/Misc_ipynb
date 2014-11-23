# A Python script to download and create a pandas dataframe out of IRIS earthquake data

#VARIABLES

start_time = '1980-01-01T00:00:00'
end_time = '1989-12-31'
min_latitude = '30'
max_latitude = '40'
min_longitude = '-100'
max_longitude = '-90'

import urllib2
import xmltodict
import pandas as pd

url = 'http://service.iris.edu/fdsnws/event/1/query?starttime=' + start_time +'&endtime=' + end_time
url += '&minlatitude='+min_latitude+'&maxlatitude='+max_latitude+'&minlongitude='+min_longitude+'&maxlongitude='+max_longitude
xmlresponse = urllib2.urlopen(url).read()
quakedict = xmltodict.parse(xmlresponse)

quakes = pd.DataFrame()
for event in quakedict['q:quakeml'][u'eventParameters']['event']:
    cdate = event['origin']['time']['value']
    cmonth = int(cdate[5:7])
    cyear = int(cdate[:4])
    clat = event['origin']['latitude']['value']
    clon = event['origin']['longitude']['value']
    try:
        cmagnitude = event['magnitude']['mag']['value']
    except:
        cmagnitude = 0
    try:
        cevent_type = event['type']
    except:
        cevent_type = ''
    try:
        cdesc = event['description']
    except:
        cdesc = ''
    try:
        cmagid = event['preferredMagnitudeID']
    except:
        cmagid = ''
    try:
        corid = event['preferredOriginID']
    except:
        corid = ''
    try:
        cmagtype = event['magnitude']['type']
    except:
        cmagtype = ''        
    try:
        cdepth = event['origin']['depth']
    except:
        cdepth = ''        
    try:
        ccreatinfo = event['origin']['creationInfo']
    except:
        ccreatinfo = ''
    try:
        ccontrib = event['origin']['@iris:contributor']
    except:
        ccontrib = ''  
    try:
        ccat = event['origin']['@iris:catalog']
    except:
        ccat = ''  
    try:
        cctoi = event['origin']['@iris:contributorOriginId']
    except:
        cctoi = ''  
        
    tempdf = pd.DataFrame({'year':[cyear],
                            'month':[cmonth],
                            'date':[cdate],
                            'lat': [clat],
                            'lon': [clon],
                            'mag_type':[cmagtype],
                            'pref_mag_id':[cmagid],
                            'pref_orig_id':[corid],
                            'description':[cdesc],
                            'event_type':[cevent_type],
                            'depth':[cdepth],
                            'creation_info':[ccreatinfo],
                            'contributor':[ccontrib],
                            'catalog':[ccat],
                            'contributor_origin_id':[cctoi],
                            'magnitude': [cmagnitude] }, dtype=float)
    quakes = quakes.append(tempdf)

quakes = quakes[quakes.magnitude != 0]
quakes[['year', 'month']] = quakes[['year', 'month']].astype(int)