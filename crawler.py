def cseSeminar():
    import requests
    from bs4 import BeautifulSoup
    import re
    import datetime
    from dateutil.parser import parse
    from snumap.models import Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post
    req = requests.get('https://cse.snu.ac.kr/seminars')
    if not req.ok:
        print("Error: request to cseSeminar has failed")
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    thisYearSeminars = soup.select(
        '#block-system-main > div > div > div > div:nth-child(1)'
    )[0]
    year = thisYearSeminars.find('h2').text
    seminarList = thisYearSeminars.select('ul > li')
    for seminar in seminarList:
        divs = seminar.select('li > div')
        title = divs[2].text.strip()
        link = "https://cse.snu.ac.kr"+divs[2].find('a')['href']
        try:
            existing_seminar = Seminar.objects.get(link=link)
        except Seminar.DoesNotExist:
            pass
        else:
            continue
        detailReq = requests.get(link)
        detailHtml = detailReq.text
        detailSoup = BeautifulSoup(detailHtml, 'html.parser')
        detailContents = detailSoup.select('div.content div.content')[0].select('div.field-items > div.even')
        talkerData = detailContents[0].select('div.content')[0]
        talker = talkerData.find(text=True)
        talkerFrom = talkerData.find('div')
        for br in talkerFrom.find_all("br"):
            br.replace_with("-")
        if talkerFrom.text is not None:
            talker = talker+"-"+talkerFrom.text
        ttime = detailContents[1].text
        where = detailContents[2].text
        description = detailContents[4].text
        codePattern = re.compile('\d+')
        codeMatch = codePattern.search(where)
        code = ""
        if codeMatch:
            code = codeMatch.group()
        else:
            print("no code is found in where information")
        try:
            building = Building.objects.get(code__startswith=code)
        except Building.DoesNotExist:
            print("error: no such a Building code:"+code+"/")
        except Building.MultipleObjectsReturned:
            print("error: ther is duplicated Building that has the code:"+code)
        temptime = ttime.split('-')
        timepattern = re.compile("\d+| \d+|[a-z:A-Z_]+")
        temptime2 = timepattern.findall(temptime[0])
        timett1 = ''
        num1 = 0
        for i in temptime2:
            num1 = num1 + 1
            if(num1 == 4) :
                continue
            timett1 = timett1 + i
        timett1 = timett1 + ' ' + temptime2[3]
        time = parse(timett1).strftime('%Y %m %d %H:%M') + ' ~ '
        if(len(temptime) > 1) :
            temptime3 = timepattern.findall(temptime[1])
            timett2 = ''
            num2 = 0
            for i in temptime3:
                num2 = num2 + 1
                if(num2 == 4) :
                    continue
                timett2 = timett2 + i
            timett2 = timett2 + ' ' + temptime3[3]
            tttime = parse(timett2).strftime('%H:%M')
            time = time + tttime
        Seminar(
            title=title,
            talker=talker,
            description=description,
            building=building,
            where=where,
            time=time,
            link=link
        ).save()
cseSeminar()

def econSeminar():
    import requests
    from bs4 import BeautifulSoup
    import re
    import datetime
    from dateutil.parser import parse
    from snumap.models import Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post
    req = requests.get('http://econ.snu.ac.kr/research/seminars/list-view')
    if not req.ok:
        print("Error: request to econSeminar has failed")
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    Seminars = soup.select(
        '#zcmsprogram'
    )[0]
    seminarList = Seminars.select('div.seminarlist.clearfix')
    for seminar in seminarList:
        link = "http://econ.snu.ac.kr"+seminar.select('a')[0]['href']
        try:
            existing_seminar = Seminar.objects.get(link=link)
        except Seminar.DoesNotExist:
            pass
        else:
            continue
        detailReq = requests.get(link)
        detailReq.encoding = 'UTF-8'
        detailHtml = detailReq.text
        detailSoup = BeautifulSoup(detailHtml, 'html.parser')
        detailContents = detailSoup.select('div.seminarview')[0]
        title = detailContents.find('h3').text
        talker = detailContents.select('div')[2].text[9:]
        ttime = detailContents.select('div')[1].text[6:]
        where = detailContents.select('div')[3].text[10:]
        description = "No description."
        codePattern = re.compile('\d+')
        codeMatch = codePattern.search(where)
        code = ""
        if codeMatch:
            code = codeMatch.group()
        else:
            print("no code is found in where information")
        try:
            building = Building.objects.get(code=code)
        except Building.DoesNotExist:
            print("error: no such a Building code:"+code+"/")
        except Building.MultipleObjectsReturned:
            print("error: ther is duplicated Building that has the code:"+code)
        temptime = ttime.split(',')
        temptime2 = parse(temptime[2] + temptime[1]).strftime("%Y %m %d")
        time = temptime2 + temptime[3]
        Seminar(
            title=title,
            talker=talker,
            description=description,
            building=building,
            where=where,
            time=time,
            link=link
        ).save()

econSeminar()