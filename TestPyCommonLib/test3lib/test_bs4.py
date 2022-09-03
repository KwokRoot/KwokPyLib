# pip install bs4
from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>test_bs4</title>
    </head>
    <body>
        <p class="title">
            <b>html_doc</b>
        </p>
        <p class="p_class">
            <a href="http://example.com/one" class="a_class" id="link1">One</a>
            <a href="http://example.com/two" class="a_class" id="link2">Two</a>
            <a href="http://example.com/six" class="a_class" id="link3">Six</a>
        </p>
        <p class="p_class">Best Wishes To You .</p>
    </body>
</html>
"""


res = BeautifulSoup(html_doc, 'lxml')

print(res.a)
print(res.a.text)
print(res.a.attrs.get('href'))

# 通过标签名、属性值获取标签
print(res.find_all("a", {"id": "link2", "class": "a_class"}))

# 通过`css选择器`获取标签
print(res.select(".a_class"))


