from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta


def get_date(date: str):
    today = datetime.today().date()
    if ":" in date:
        return today
    elif date.count(".") == 1:
        return datetime.strptime(str(today.year) + "." + date, "%Y.%m.%d").date()
    elif date.count(".") == 2:
        return datetime.strptime("20" + date, "%Y.%m.%d").date()

if __name__ == "__main__":
    url = "https://gall.dcinside.com/mgallery/board/lists/?id=sunshine&exception_mode=recommend&page="
    url_prefix = "https://gall.dcinside.com/"
    high_recommend_list = []

    minus_day = 1
    today = datetime.today().date()
    limit_day = today - timedelta(days = minus_day)
    not_see_limit_day = True
    page = 1
    while not_see_limit_day:
        req = Request(url + str(page), headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'})
        webpage = urlopen(req)
        soup = BeautifulSoup(webpage, features="html.parser")
        table = soup.find("table", {"class": "gall_list"})
        for tr in table.find("tbody").find_all("tr", {"data-type": "icon_recomimg"}):
            recommand = int(tr.find("td", {"class": "gall_recommend"}).text)
            d = {}
            title_a = tr.find("td", {"class": "gall_tit"}).find("a")
            d["recommend"] = int(tr.find("td", {"class": "gall_recommend"}).text)
            d["count"] = int(tr.find("td", {"class": "gall_count"}).text)
            d["title"] = title_a.text
            d["url"] = url_prefix + title_a["href"]
            d["id"] = int(tr.find("td", {"class": "gall_num"}).text)
            d["gall_date"] = get_date(str(tr.find("td", {"class": "gall_date"}).text))
            if d["id"] < 4000000:
                continue
            if d["gall_date"] <= limit_day:
                not_see_limit_day = False
                break
            if d["recommend"] > 35:
                high_recommend_list.append(d)
        time.sleep(0.1)
        page += 1
    high_recommend_list.sort(key=lambda x: -x["recommend"])
    print(*high_recommend_list, sep='\n')
    print(len(high_recommend_list))
