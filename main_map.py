#interactive map
#jaylen ho luc
from turtle import width
from zipfile import ZipFile
from io import BytesIO
from urllib.request import urlopen
import folium
import pandas as pd
import api_mod as api
import time
from folium.plugins import MousePosition
import time
from folium.plugins import Search
import requests
import json
import branca
import pycountry
start1 = time.time()

main_map = folium.Map(
    location=[39.9042, 116.4074],   
    max_bounds = True,
    zoom_start = 3
)

formatter_lat = "function(num) {return L.Util.formatNum(num, 3) + ' º '+'N';};"
formatter_long = "function(num) {return L.Util.formatNum(num, 3) + ' º '+'E';};"


MousePosition(
    position="topright",
    separator=" | ",
    empty_string="NaN",
    lng_first=True,
    num_digits=20,
    prefix="Coordinates:",
    lat_formatter=formatter_lat,
    lng_formatter=formatter_long,
).add_to(main_map)

add = '/tile/{z}/{y}/{x}'

#add more map textures later

maps = dict(Grey='https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer',
            Divisional='https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer',
            Topographical='https://services.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer',
            Terrain= 'https://services.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer'
            )







#mcg = folium.plugins.MarkerCluster(control=False).add_to(main_map)
#main_map.add_child(mcg)
#cap = folium.plugins.MarkerCluster(name='Capitals',show=False).add_to(main_map)
# https://leafletjs.com/reference-1.7.1.html#path
colors = ''
fillColors = ''

cc = folium.FeatureGroup(name='General Country Data')


#class to fetch api information
country_object = api.server_fetch()
try:
    csvfile = pd.read_csv('worldcities.csv')
except:
    resp = urlopen('https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.75.zip')
    zipfiles = ZipFile(BytesIO(resp.read()), 'r')
    csvfile = pd.read_csv(zipfiles.open('worldcities.csv'))

#for line in zipfiles.open(zipfile).readlines():
#    print(line.decode('utf-8'))

#for i in zipfile.open(file).readlines()
#   unzipped.extractall(str(pathlib.Path(__file__).parent.resolve()))
#filecsv = ''

#for i in pathlib.Path(__file__).parent.resolve().iterdir():
#    if i.name == 'worldcities.csv': 
#        filecsv = i
#        break
#HARDED-------TESTABLE-------------------------------------------------------------------
# '''
# tt = country_object.news['articles'][100]['title']
# dd = country_object.news['articles'][99]['description']
# yy = country_object.news['articles'][99]['url']
# ll = country_object.news['articles'][99]['urlToImage']
# '''
# scroll = '<style> .tt_custom_sm{overflow-y: scroll !important;max-height: 100px} </style>  '
#scroll = '<style> html{scrollbar-width:normal; scrollbar-color: #777 #555;} html::-webkit-scrollbar{width 10px;} </style>'
#center = '<style> .center {text-align: center}</style>'


class nation:
    classification = []
    style_func_time = 0
    c_cat = [(['MAC','HKG','CHN','PRK','KOR','JPN','TWN','SGP','VNM'],['#D12601',"Sinosphere"]),
    (['LAO','THA','MMR','KHM','PHL','MYS','IDN','TLS','BRN'],['#cc8899',"Indo China"]),
    (['IND','PAK','BGD','LKA','MDV'],['#654321',"Hindustan"]),
    (['IRN','IRQ','SYR','SYR','ISR','PSE','LBN',\
        'SAU','YEM','OMN','ARE','QAT','BHR','KWT','AFG','JOR'],['#009000',"Middle East"]),
    (['TKM','UZB','KAZ','KGZ','TJK','MNG'],['#09EBEE',"Turkistan"]),
    (['BMU','ALA','GIB','SMR','VAT','MLT','ESP','PRT','FRA','BEL','NLD','GBR','IRL',\
        'DEU','LUX','ITA','AND','CHE','AUT','DNK','NOR','SWE','FIN','EST','FRO','ISL',\
        'GRL','MCO','AUS','NZL','ATF','BLM','GGY','HMD','IMN','JEY','LIE','SGS','SHN','SPM','UMI'],['blue','The West']),
    (['POL','LTU','LVA','BLR','UKR','CZE','SVK','HUN'\
        'ROU','BGR','HRV','SVN','BIH','GRC','TUR','MKD','ALB','RUS','CYP',\
        'SRB','MNE','MDA','ROU','HUN'],['purple','The Orthodoxy']),
    (['ETH','ERI','SOM','DJI'],['#376550','Cushite']),
    (['CPV','CIV','GHA','NGA','BEN','TGO','BFA','LBR','SLE','GIN','SEN',\
        'GNB','MLI','NER','CMR','GNQ','GAB','GMB','STP'],['#ff8c00','West Africa']),
    (['CAF','COD','COG','UGA','KEN','TZA','ZMB','AGO','MWI',\
        'MOZ','ZWE','NAM','BWA','RWA','BDI','SWZ'],['#FBC490','Bantu']),
    (['ZAF','LSO'],['black','South Africa']),
    (['LBY','DZA','MAR','MRT','ESH','DZA','TUN','EGY','TCD'],['#00c300','North Africa']),
    (['SDN','SSD'],['#FFCC00','Sudan']),
    (['GEO','ARM','AZE'],['#75816b','Caucauses']),
    (['COM','MDG','MUS','IOT','SYC'],['#800020','Madagascar Indian Ocean']),
    (['PNG','SLB','VUT','NCL'],['#8da825','Melanesia']),
     (['FSM','MHL','MNP','GUM','PLW','NRU','KIR'],['#00008B','Micronesia']),
    (['PYF','WSM','TUV','WLF','NIU','TON','NFK','COK','PCN','FJI','ASM'],['#39FF14','Polynesia']),
    (['NPL','BTN'],['#ACD5F3','The Himilayas']),
     (['USA','CAN'],['#000080','Euro-North American Settler-Colonies']),
    (['MEX','BLZ','GTM','HND','SLV','NIC','CRI','PAN'],['#125454','Spanish-occupied Mexica']),
    (['GUY','SUR','BRA'],['#F36196','Portuguese-Occupied Tupi-Guarani']),
    (['ECU','PER','BOL','CHL'],['#C19A6B ','Spanish-Occupied Inca']),
   (['ARG','URY','PRY','FLK'],['#0d98ba ','Euro-Hispanic Occupied South-West America ']),
    (['VEN','COL'],['#C49102 ','Grand colombia']),
    (['CUB','DMA','HTI','TCA','DOM','BHS','JAM','PRI','ATG','MSR',\
        'KNA','VCT','TTO','BRB','GRD','LCA','CUW','ABW','AIA','CYM','MAF','SXM','VGB','VIR'],['#00A36C ','Caribbean'])]
    
    c_dict = {i : v  for (li,v) in c_cat for i in li}


    @staticmethod
    def style_func(colorsz,i,namez):
        colors = colorsz
        fillColors = colorsz
        bordersStyle={
            'color': f'{colors}',
            'weight':2,
            'fillColor':f'{fillColors}',
            'fillOpacity' : .2
        }
        #included in the tooltip popup::
         
        #print(i['properties']['ISO_A3'])
        

        #print(i['geometry']['coordinates'])

        st = time.time()
        #print(i['properties']['ISO_A3'])
        
        ht = country_object.form_str(i['properties']['ISO_A3'],i)

        en = time.time()
        
        html = f'<style>pz {{color:{colors}; display:inline;}}</style>'+f'<div style="white-space: normal"><b>Civilization</b>: \
            <pz>{namez}</pz><br>{ht}'
        geo = folium.features.GeoJson(
            i,
            #tooltip = folium.GeoJsonTooltip(fields=('ADMIN','ISO_A3',), aliases=('Nation-State','ALPHA3',)),
            tooltip= folium.Tooltip(text=folium.Html(html, script=True,width=500).render()),
            show = True,
            control = False,
            zoom_on_click = True,
            name = i['properties']['ADMIN'],
            style_function=lambda x:bordersStyle)
         #still need to test without scroll
        iso3 = i['properties']['ISO_A3']

        #---------REPLACE BASED ON API
        all_news  = country_object.get_news(pycountry.countries.get(alpha_3=f'{iso3}').name,'9d00f1ed20454836b2b1b30b5f84530a') #formated html for the news popup
        #all_news = ''
        #TESTER__________________________________________________________
        # temp = '<br><a href="https://www.brookings.edu/">Article Link</a>'
        # all_news += temp
        #<base target= '_blank'/> works forthte time being
        
        #media stack response object incldues the pagination and data object

        #print(f'survived for {iso3}')
        #all_news += ''
        popup = folium.Popup(branca.element.IFrame(html=all_news ,\
            width=500, height=400), max_width=500 ) #main thingy thing news api maybe maybe news api
        popup.add_to(geo)
        cc.add_child(geo)
        #main_map.add_child(geo)

        #geo.add_to(main_map)

        #.add_to(main_map)
        #nation.classification.append(new_country)
#web scrap the gepjson file
ugh = time.time()


try:
    with open(r'countries.geojson') as open_f: country_r = json.loads(open_f.read())
except:
    country_r = requests.get('https://datahub.io/core/geo-countries/r/countries.geojson').json()

ughe = time.time()
print(f'open file: {ughe-ugh}')
func_time = 0
start2 = time.time()

#each country code has a value which is the style function maybe maybe not so much of a pain in the ass

#make this a lot shorter and cleawner and less bopilerplate by making a dicitonary 
#optimize style_func


#reduce boilerplate #ALL DONE REDUCED LINES 

#ADD EVRYTHING COUNTRY YES


for i in country_r['features']:  
    if i['properties']['ISO_A3'] != 'ATA' and i['properties']['ISO_A3']  != '-99': nation.style_func(nation.c_dict[i['properties']['ISO_A3']][0],i, nation.c_dict[i['properties']['ISO_A3']][1])

#findings: style func is quite fast but the for loop itself may be overbearing
end2 = time.time()
print(f'function fetch runtime: {func_time}')
print(f'breakpoint 2 runtime: {end2-start2} seconds')
#folium.GeoJsonTooltip(fields=['TYPE', 'R_STATEFP', 'L_STATEFP']).add_to(US_Geojson)

for map_name, url in maps.items():
    url+=add
    folium.TileLayer(
        url,
        name=map_name,
        attr='My attr').add_to(main_map)
#fg=folium.FeatureGroup(name='CIvilization', show=False)
#main_map.add_child(fg)

#adding cities to map
caps = folium.FeatureGroup(name='Capitals',show=False)
first = folium.FeatureGroup(name='First Level Admin Capital',show=False)
capitals = csvfile[(csvfile['capital'] == 'primary')]
fir = csvfile[(csvfile['capital'] == 'admin')]
#provinces = csvfile[(csvfile['capital'] == '')]
#popu = csvfile['population']
#icon = folium.features.CustomIcon('star.png',icon_size=(14, 14))
icon = "folium.Icon(color='red')" #High Population (>7,000,000)
icon2 = "folium.Icon(color='orange')"#'Medium Population (between 2,000,000 and 7,000,000)
icon3 = "folium.Icon(color='lightblue')"#Low Population (<2,000,000)
#icon_seach = "folium.Icon(color='lightblue')"
string1 = "first.add_child(folium.Marker("+\
        "location=[i['lat'], i['lng']],"+\
        "popup=folium.Popup(html=f'<style>pz {{color:{colors}; display:inline;}}</style>'+f'<b>First Level Admin Capital:</b> \
            {c}<br><b>Population:<b> <pz>{pop}</pz><br><b>Coordinates:</b>{long}º E / {lat}º N',"+\
        "max_width= 200),"+\
       " tooltip=f'<b>First subdivision Capital city:</b> {ci}',"


string2 = "caps.add_child(folium.Marker("+\
        "location=[v['lat'], v['lng']],"+\
        "popup=folium.Popup(html=f'<style>pz {{color:{colors}; display:inline;}}</style>'+f'<b>Capital city of:</b> \
            {vc}<br><b>Population:</b><pz> {vpop}</pz><br><b>Coordinates:</b>{vlong}º E / {vlat}º N',"+\
        "max_width= 200),"+\
       " tooltip=f'<b>Capital city:</b> {vci}',name=f'{vc}',"

#main_map.add_child(exec(FeatureGroupSubGroup(caps,string_cap,control=False)))
for (iind,i) in fir.iterrows():
    ci,c,pop,lat,long = i['city'],i['admin_name'],i['population'],i['lat'],i['lng']
    if float(pop) >= 7000000:
        colors = 'red'
        exec(string1 + f"icon= {icon}))")
    
    elif float(pop) < 7000000 and float(i['population']) >= 1000000 :
        colors = 'orange'
        exec(string1 + f"icon= {icon2}))")
    elif float(pop) < 1000000:
        colors = 'lightblue'
        exec(string1 + f"icon= {icon3}))")

        
for (vind, v) in capitals.iterrows():
    vci,vc,vpop,vlat,vlong = v['city'],v['country'],v['population'],v['lat'],v['lng']

    
    if float(vpop) >= 7000000:
        colors = 'red'
        exec(string2 + f"icon= {icon}))")
       
    elif float(vpop) < 7000000 and float(vpop) >= 1000000 :
        colors = 'orange'
        exec(string2 + f"icon= {icon2}))")

    elif float(vpop) < 1000000:
        colors = 'lightblue'
        exec(string2 + f"icon= {icon3}))")

    
#for i,d in capitals.iterrows():

    

main_map.add_child(cc)
main_map.add_child(caps)
main_map.add_child(first)



folium.TileLayer('Stamen Terrain').add_to(main_map)
folium.TileLayer('cartodbdark_matter').add_to(main_map)
folium.TileLayer('Stamen Toner').add_to(main_map)
folium.TileLayer('Stamen Water Color').add_to(main_map)
folium.TileLayer('cartodbpositron').add_to(main_map)




countryesearch = Search(
    layer = caps,
    geom_type = 'MultiPolygon',
    search_label='name',
    placeholder='Search for a country',
    collapsed=False,
    search_zoom=7
    
).add_to(main_map)

end1 = time.time()
print(f'System runtime: {end1-start1} seconds')
print(f'form_str func time: {func_time} seconds')
print(f'API fetching {country_object.fetch_time}')
folium.LayerControl().add_to(main_map)
main_map.save('output1.html')
#folium.GeoJson()

#folium.Marker(
#    location = []
#)