import requests
from lxml import etree

headers = {"Authorization": "Basic {}".format("YWRtaW46dms1dkEyZmo=")}
url = "http://10.10.87.91:1888/clusters/log_plantform_dev/consumers"

resp = requests.get(url, headers=headers)
# print(resp.text)

html = etree.HTML(resp.text)
tr_list = html.xpath("/html/body/div[1]/div/div/div[2]/table/tbody")

for tr in tr_list[0].iterfind("tr"):
    td_list = tr.findall("td")
    consumer = td_list[0].xpath("a//text()")
    topics = td_list[2].xpath("a//text()")
    values = td_list[2].xpath("span//text()")
    print(consumer[0])

