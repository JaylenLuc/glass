from urllib import response
import requests
import time
import json
import pandas as pd
import io
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
import http.client, urllib.parse
import pycountry
from selenium import webdriver
from selenium.webdriver.common.by import By


newsapi = NewsApiClient(api_key='9d00f1ed20454836b2b1b30b5f84530a')

class server_fetch:
    fetch_time = 0
    response = ''
    news= '' #NOT USED UNLESS CACHE
    hdi = ''
    co2 = ''
    exports = ''
#------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        try: 
            with open('restcountries.json') as open_f: server_fetch.response = json.loads(open_f.read())
        except: server_fetch.response = requests.get('https://restcountries.com/v3.1/all').json()
        #server_fetch.news = requests.get('https://newsapi.org/v2/everything?domains=aljazeera.com,apnews.com,reuters.com,cfr.org,foreignpolicy.com&apiKey=9d00f1ed20454836b2b1b30b5f84530a').json()
        server_fetch.hdi=pd.read_csv(io.StringIO(requests.get(BeautifulSoup(requests.get('https://hdr.undp.org/data-center/documentation-and-downloads').text,\
            'html.parser').find_all(text='HDI and components time-series')[0].parent['href']).content.decode('utf-8')))

        try:
            with open(r'owid-co2-data.json') as open_f: server_fetch.co2 = json.loads(open_f.read())
        except:
            server_fetch.co2 = json.loads((requests.get(BeautifulSoup(requests.get('https://github.com/owid/co2-data').text,\
                'html.parser').find_all(text='JSON')[0].parent['href']).content.decode('utf-8')))
        #store csv file and web scrape        
        try:
            server_fetch.exports = pd.read_csv(r'csvData.csv')
        except:
            driver = webdriver.Chrome(executable_path=b"C:\Users\Jaylen\Downloads\chromedriver_win32 (1)\chromedriver.exe")

            driver.get("https://worldpopulationreview.com/country-rankings/exports-by-country")

            driver.find_element(By.LINK_TEXT,  'CSV').click()
#------------------------------------- -----------------------------------------------------------------------------------------------------------------

    def get_news(self,coun,apikey):
        #media stack 500 per month
        #-------------------------------------------------------------------------
        # conn = http.client.HTTPConnection('api.mediastack.com')

        # params = urllib.parse.urlencode({
        #     'access_key': f'{apikey}', #REPLACE
        #     'categories': 'general,-entertainment ,-health,-sports, -business',
        #     'sort': 'published_desc',
        #     'sources':'cfr', #new
        #     'languages': 'en',
        #     'limit': 5,
        #     'countries': str(iso2),
        #     })

        # conn.request('GET', f'/v1/news?{params}')

        # response_object = json.loads(conn.getresponse().read().decode('utf-8'))
        #VARIANT1--------------------------------------------------------------------------------------------------------------------------------------------------
        #f'https://newsapi.org/v2/everything?q=+{coun}&language=en&domains=cfr.org,brookings.edu,crisisgroup.org,csis.org&apiKey={apikey}'
        #at this point, play around with news api domain param and q param for more accurate and salient results*****************************
        #another thing is perhaps add a couple more things to the hover pop up such as biggest export and import , largest mineral deposits, geography, and breif description, and demographics and gov type
        response_object = requests.get(f'https://newsapi.org/v2/everything?q={coun}&language=en&domains=cfr.org,thediplomat.com,brookings.edu,aljazeera.com,crisisgroup.org,csis.org&apiKey={apikey}').json() #include aljazeera ????

        all_news = f'<h1 font-size:25px;>Current Events</h1><br><base target="_blank" ><br>'
        try:
            #print('TOTAL ARTICLE RESULTS: ',response_object['totalResults'])
            for i in response_object['articles']: 
                imageurl, title, descrip, urllink = i['urlToImage'],  i['title'],\
                i['description'], i['url']
                all_news += f'<img src="{imageurl}" style="width:130px;height:100px;"><br><b>\
                <h2 style="font-size:20px;">{title}</h2></b>{descrip}<br><a href="{urllink}">Article Link</a><br><br>'
        except: print('server response protocol message: ', response_object['message'])

        return all_news

        #NEWS API-------- exampl output
        # {
            #     "status": "ok",
            #     "totalResults": 8072,
            #     -"articles": [
            #     -{
            #     -"source": {
            #     "id": "the-verge",
            #     "name": "The Verge"
            #     },
            #     "author": "Justine Calma",
            #     "title": "Texas heatwave and energy crunch curtails Bitcoin mining",
            #     "description": "Bitcoin miners in Texas powered down to respond to an energy crunch triggered by a punishing heatwave. Energy demand from cryptomining is growing in the state.",
            #     "url": "https://www.theverge.com/2022/7/12/23205066/texas-heat-curtails-bitcoin-mining-energy-demand-electricity-grid",
            #     "urlToImage": "https://cdn.vox-cdn.com/thumbor/sP9sPjh-2PfK76HRsOfHNYNQWAo=/0x285:4048x2404/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/23761862/1235927096.jpg",
            #     "publishedAt": "2022-07-12T15:50:17Z",
            #     "content": "Miners voluntarily powered down as energy demand and prices spiked \r\nAn aerial view of the Whinstone US Bitcoin mining facility in Rockdale, Texas, on October 9th, 2021. The long sheds at North Ameri… [+3770 chars]"
            #     }, [....]
        #     ]
        # }
        #------------------------------------------------------------------------------------------------------------------------------------------------
            #         {
            #     "pagination": {
            #         "limit": 100,
            #         "offset": 0,
            #         "count": 100,
            #         "total": 293
            #     },
            #     "data": [
            #         {
            #             "author": "CNN Staff",
            #             "title": "This may be the big winner of the market crash",
            #             "description": "This may be the big winner of the market crash",
            #             "url": "http://rss.cnn.com/~r/rss/cnn_topstories/~3/KwE80_jkKo8/a-sa-dd-3",
            #             "source": "CNN",
            #             "image": "https://cdn.cnn.com/cnnnext/dam/assets/150325082152-social-gfx-cnn-logo-super-169.jpg",
            #             "category": "general",
            #             "language": "en",
            #             "country": "us",
            #             "published_at": "2020-07-17T23:35:06+00:00"
            #         },
            #         [...]
            #     ]
            # }
            #---------------------------------------------------------------------------------------------------------------------------------------------------

        
            #print(pycountry.countries.get(alpha_3=f'{iso3}').alpha_2.lower())
            #country_object.get_news(pycountry.countries.get(alpha_3=f'{iso3}').alpha_2.lower()) 
            #print(api.server_fetch.news)#try lower case if not working
            #tot = api.server_fetch.news['totalResults']
            #print('_---------------',int( api.server_fetch.news['totalResults']))
            

                
                    #print('in loop')
                    #print(i['properties']['ADMIN'])
                    #print(idx)
                    #print(ticker)
                #print('OUTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
                #print(ticker)
                #print(i['properties']['ADMIN'])
                #print(idx)
        #next order of business:: get the pop and try to do the images of flag


#------------------------------------------------------------------------------------------------------------------------------------------------------
    def form_str(self,code,ir):
        #most  ofthe time is taken here
        #print(']]]]]]]]  ',code)
        start = time.time()
        #income = self.get_income(code)
        #response = requests.get(f'https://restcountries.com/v3.1/alpha/{code}').json()
        end = time.time()
        
        #print(server_fetch.response)
        
        for i in range(250):
            #print(i)
            if server_fetch.response[i]['cca3'] == code:

                try:
                    color = ''
                    color_end = ''
                    style = ''
                    gin = float(list(server_fetch.response[i]['gini'].values())[0])
                    if gin < 30:
                        style = '<style>pr {color:#008000; display:inline;}</style> '
                        color = '<pr>'
                        color_end = '</pr>'
                    elif gin >= 30 and gin < 45:
                        style = '<style>pr {color:#FFA500; display:inline;}</style> '
                        color = '<pr>'
                        color_end = '</pr>'
                    elif gin >= 45 :
                        style = '<style>pr {color:#FF0000; display:inline;}</style> '
                        color = '<pr>'
                        color_end = '</pr>'
                    self.gini = style+ f'<b>Gini Income Inequality Index:</b> '+color+str(gin)+ color_end+' per ' + str(list(server_fetch.response[i]['gini'].keys())[0]) #gini index
                except(KeyError):
                    self.gini =style+ f'<b>Gini Income Inequality Index:</b> '+ 'N/A'
                
                try:
                    y = str(list(server_fetch.response[i]['currencies'].items())[0][1]['name'])
                    self.money = f'<b>Fiat Currency:</b> '+ y+ ' '+ str(list(server_fetch.response[i]['currencies'].items())[0][1]['symbol']) #currrency #currencu symb

                except(KeyError):
                    self.money = f'<b>Fiat Currency:</b> '+ 'N/A' #currrency #currencu symb
                t = 0
                lang = ''
                name= ''

                for k,v in server_fetch.response[i]['languages'].items():
                    if t == 1: lang += '<b>Other languages:</b> '
                    if not t == 0: lang += f'{v} / '
                    t+= 1
                lang = lang[0:-2]
                if code == 'ZWE': name = list(server_fetch.response[i]['name']['nativeName'].items())[0][1]['official']
                else:

                    for k,v in server_fetch.response[i]['name']['nativeName'].items():
                        name += v['official'] + ' / '

                    name = name[0:-2]
                try:
                    income = income[1][0]['incomeLevel']['value']
                except:
                    income = 'N\A'
                try:
                    capital = server_fetch.response[i]['capital'][0]
                except(KeyError):
                    capital = 'N/A'

                year = int(BeautifulSoup(requests.get('https://hdr.undp.org/data-center/documentation-and-downloads').text,'html.parser').find_all(text='HDI and components time-series')[0].parent['href'][46:50]) - 1
                
                #print(code)
                 
                hdi_og = server_fetch.hdi[(server_fetch.hdi['iso3'] == f'{code}')]
                if hdi_og.empty:
                    hdi = 'N/A'
                    ranked = 'N/A'
                    gni = 'N/A'
                    le = 'N/A'
                    mys = 'N/A'
                    eys = 'N/A'
                else:
                    hdi = [str(list(hdi_og[f'hdi_{year}'])[0]) if str(list(hdi_og[f'hdi_{year}'])[0]) != 'NaN' else 'N/A'][0]
                    ranked = [str(list(hdi_og[f'hdi_rank_{year}'])[0])[0:-2] if str(list(hdi_og[f'hdi_rank_{year}'])[0])[0:-2] != 'NaN' else 'N/A'][0]
                    gni = [str(list(hdi_og[f'gnipc_{year}'])[0]) if str(list(hdi_og[f'gnipc_{year}'])[0]) != 'NaN' else 'N/A'][0]
                    le = [str(list(hdi_og[f'le_{year}'])[0]) if str(list(hdi_og[f'le_{year}'])[0]) != 'NaN' else 'N/A'][0]
                    mys = [str(list(hdi_og[f'mys_{year}'])[0]) if str(list(hdi_og[f'mys_{year}'])[0]) != 'NaN' else 'N/A'][0]
                    eys = [str(list(hdi_og[f'eys_{year}'])[0]) if str(list(hdi_og[f'eys_{year}'])[0]) != 'NaN' else 'N/A'][0]
                    try: gni = float(gni)
                    except: pass
                #print(name)
                if not hdi_og.empty and hdi != 'N/A':
                    color = '<prh>'
                    color_end = '</prh>'
                    if float(hdi) >= .80: style = '<style>prh {color:#008000; display:inline;}</style> ' 
                    elif float(hdi) >= .7 and float(hdi) < .80: style = '<style>prh {color:#FFA500; display:inline;}</style> '  
                    elif float(hdi) >= .5 and float(hdi) < .7: style = '<style>prh {color:#FF5349; display:inline;}</style> '
                    elif float(hdi) < .5: style = '<style>prh {color:#FF0000; display:inline;}</style> '
                    hdi = style + color + hdi + color_end
                    ranked = style + color + ranked + color_end 
                if not hdi_og.empty and gni != 'N/A':
                    color = '<prg>'
                    color_end = '</prg>'
                    if float(gni) >= 13500: style = '<style>prg {color:#008000; display:inline;}</style> '
                    elif float(gni) >= 4500 and float(gni) < 13500: style = '<style>prg {color:#FFA500; display:inline;}</style> '
                    elif float(gni) >= 1200 and float(gni) < 4500: style = '<style>prg {color:#FF5349; display:inline;}</style> '
                    elif float(gni) < 1200: style = '<style>prg {color:#FF0000; display:inline;}</style> '
                    gni =  style + color + f'{gni:,}' + color_end
                if not hdi_og.empty and le != 'N/A':
                    color = '<prl>'
                    color_end = '</prl>'
                    if float(le) >= 80: style = '<style>prl {color:#008000; display:inline;}</style> '
                    elif float(le) >= 70 and float(le) < 80: style = '<style>prl {color:#FFA500; display:inline;}</style> '
                    elif float(le) >= 60 and float(le) < 70: style = '<style>prl {color:#FF5349; display:inline;}</style> '
                    elif float(le) < 60: style = '<style>prl {color:#FF0000; display:inline;}</style> '
                    le = style + color + str(le) + color_end
                if not hdi_og.empty and eys != 'N/A':
                    color = '<prey>'
                    color_end = '</prey>'
                    if float(eys) >= 14: style = '<style>prey {color:#008000; display:inline;}</style> '      
                    elif float(eys) >= 10 and float(eys) < 14: style = '<style>prey {color:#FFA500; display:inline;}</style> '
                    elif float(eys) < 10:style = '<style>prey {color:#FF0000; display:inline;}</style> '
                    eys = style + color + str(eys) + color_end
                if not hdi_og.empty and mys != 'N/A':
                    color = '<prm>'
                    color_end = '</prm>'
                    if float(mys) >= 12: style = '<style>prm {color:#008000; display:inline;}</style> '
                    elif float(mys) >= 8 and float(mys) < 12: style = '<style>prm {color:#FFA500; display:inline;}</style> '  
                    elif float(mys) < 8: style = '<style>prm {color:#FF0000; display:inline;}</style> '
                    mys = style + color + str(mys) + color_end
                if len(lang) != 0: lang += '</br>'
                #'<img src="data:image/jpeg;base64,{}">'
                #print(code)
                pop = server_fetch.response[i]['population']
                try:carbon = server_fetch.co2[ir['properties']['ADMIN']]['data'][-1]['co2']#Annual production-based emissions of carbon dioxide (CO2), measured in million tonnes. This is based on territorial emissions, which do not account for emissions embedded in traded goods.
                except KeyError:
                    try: carbon = server_fetch.co2[pycountry.countries.get(alpha_3=f'{code}').name]['data'][-1]['co2']
                    except Exception as e : carbon = 'N/A'
                   
                try:ccap = server_fetch.co2[ir['properties']['ADMIN']]['data'][-1]['co2_per_capita']
                except KeyError:
                    try: ccap = server_fetch.co2[pycountry.countries.get(alpha_3=f'{code}').name]['data'][-1]['co2_per_capita']
                    except Exception as e : ccap = 'N/A'

                if type(carbon) != str:
                    if float(carbon) > 500:style = '<style>prp {color:#FF0000; display:inline;}</style> '
                    elif float(carbon) <= 500 and float(carbon) > 150:style = '<style>prp {color:#FFA500; display:inline;}</style> '
                    elif float(carbon) <= 150 :style = '<style>prp {color:#008000 ; display:inline;}</style> '
                    carbon =  style + '<prp>' + str(carbon) + '</prp>'


                if type(ccap) != str:
                    if float(ccap) > 14:style = '<style>prx {color:#FF0000; display:inline;}</style> '
                    elif float(ccap) <= 14 and float(ccap) > 5:style = '<style>prx {color:#FFA500; display:inline;}</style> '
                    elif float(ccap) <= 5 :style = '<style>prx {color:#008000 ; display:inline;}</style> '
                    ccap =  style + '<prx>' + str(ccap) + '</prx>'

                try:subrr = server_fetch.response[i]['subregion']
                except: subrr = 'N/A'
                #print(pop)

                exp = server_fetch.exports[(server_fetch.exports['country'] == pycountry.countries.get(alpha_3=f"{code}").name)]

                bige = str(*[v for k,v in exp.to_dict().items()][4].values())
                
                #hard code "DR Congo" maybe i hate this 
                if not bige:
                    try:
                        exp = server_fetch.exports[(server_fetch.exports['country'] == pycountry.countries.get(alpha_3=f"{code}").common_name)]
                        bige = str(*[v for k,v in exp.to_dict().items()][4].values())
                        if not bige:
                            exp = server_fetch.exports[(server_fetch.exports['country'] == ir['properties']['ADMIN'])]
                            bige = str(*[v for k,v in exp.to_dict().items()][4].values())
                    except:
                        exp = server_fetch.exports[(server_fetch.exports['country'] == ir['properties']['ADMIN'])]
                        bige = str(*[v for k,v in exp.to_dict().items()][4].values())


                flag = server_fetch.response[i]['flags']['png']
                ret = f'<b>Autochthonous Name:</b> '+ name + '<br>'\
                        +f'<b>Anglophone Name:</b> '+server_fetch.response[i]['name']['common']+ '<br>'+f'<img src="{flag}" style="width:114px;height:60px;">'+'<br>'\
                            +str(f'<b>Administrative Center:</b> '+ capital) + '<br>'\
                                +str(f'<b>Subregion:</b> '+subrr)+ '<br>'\
                                    +  str( f'<b>Lingua Franca:</b> '+list(server_fetch.response[i]['languages'].items())[0][1])+ '<br>'\
                                        +lang + '<b>Population:</b> '+f'{pop:,}' + '<br>'\
                                                +str(f'<b>Timezone (UTC):</b> ' + server_fetch.response[i]['timezones'][0]) + '<br>'+self.gini + '<br>'+self.money + '<br>'\
                                                    +f'<b>Human Development Index ({year}):</b> '+hdi + '</br>'+\
                                                        '<b>HDI rank: </b>'+ranked+'<br>'+f'<b>Gross National Income Per Capita (PPP):</b> {gni}'+'<br>'+\
                                                            '<b>Life Expectancy at Birth:</b> '+ le+'<br>'+'<b>Expected Years of Schooling:</b> '+eys+'<br>'+\
                                                                '<b>Mean Years of Schooling:</b> '+ mys +'<br>'+'<b>Annual emissions of carbon dioxide (CO2) (million tonnes):</b> '+carbon+'<br>'+\
                                                                        '<b>Annual emissions of carbon dioxide (CO2) in tonnes per person:</b> '+str(ccap)+'<br>'\
                                                                            '<b>Biggest Exports: </b> '+str(bige) +'</div>'
                
                server_fetch.fetch_time += end-start
                break
            
        return ret




if __name__ == '__main__':
    y = server_fetch()
    print(y.form_str('chn'))
    
