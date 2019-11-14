
(图片：urip@unsplash，字数: 6800，时间: 7分钟)



正文开始前，先推广下肖哥新开的知识星球"速度之上的质量"，目前5折特惠，欢迎同学们加入。点击这里了解星球的建立背景。另外，本文末有优惠券可领。



前言



年初的时候，一篇题为《Python实用技能: 从A到Z》的文章在网络上刷屏了。在文中，作者介绍了26个首字母分别从A到Z的Python实用工具。不过，这些工具都是面向Python基础编程的。



大家知道，Python最大的优势是应用面广，其中一个重要的应用是自动化软件测试。这里，我借鉴上述文章的手法，针对Python自动化测试这一专门领域，整理出一套首字母分别从A到Z的工具箱，分享给大家。



这26个Python工具覆盖自动化测试的方方面面。概况地说，可以分为三种类型：(1) 面向Python代码的白盒测试工具，(2) 面向通用测试领域，基于Python实现的黑盒测试工具，和(3) Python生态系统中在自动化测试中频繁使用的通用库。



接着就来逐一介绍它们。文中代码收集在Github项目中: https://github.com/slxiao/python-test-

automation-AtoZ。欢迎大家下载体验。结合实例学习，效果会更好。



提醒：文章很长，可以收藏之后慢慢看。



assert



在软件测试中，一个普遍需求是比较被测对象的实际输出与期望输出是否相同。如果相同，测试继续执行；如果不相同，测试就会失败并且终止。Python中有一个内置关键字，正好可以满足这一需求。它就是assert。



assert后面可以跟两个参数。第一个参数表示判断条件，是必须的。如果条件不为True，那么assert语句会报错，并且抛出"AssertionError"异常；第二个参数是可选的，表示当assert失败时，提示的错误消息。



举例如下：

actual, expected = 1, 2 
# 抛出异常
assert actual == expected 
#抛出异常并且提示错误消息
assert actual == expected, "actual result is not same as expected"


behave



behave是一种Python编写的，面向行为驱动开发(Behavior-driven development, BDD)模式的测试框架。在behave框架中，测试用例被分为前端和后端两部分。前端用例由自然语言编写，负责描述测试内容；后端用例由Python编写，负责执行测试步骤。



behave的安装命令为：

pip install behave


下面是一个简单的测试用例。用例的前端部分为：

Feature: Showing off behave 
  Scenario: Run a simple test  
    Given we have behave installed 
     When we implement 5 tests 
     Then behave will test them for us!


用例的后端部分为：

from behave import given, when, then, step 
​
@given('we have behave installed')
def step_impl(context):
    pass
    
@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number
​
@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0


执行结果如下：

$ behave 
Feature: Showing off behave # features/example.feature:2 
​
  Scenario: Run a simple test          # features/example.feature:4
    Given we have behave installed     # features/steps/example_steps.py:4
    When we implement 5 tests          # features/steps/example_steps.py:8
    Then behave will test them for us! # features/steps/example_steps.py:13
​
1 feature passed, 0 failed, 0 skipped 
1 scenario passed, 0 failed, 0 skipped 
3 steps passed, 0 failed, 0 skipped, 0 undefined


Coverage.py



代码覆盖率是测试度量的重要手段之一。Python中用于计算代码覆盖率的重要工具就是Coverage.py。它通过跟踪Python解释器工作情况，分析出哪些Python代码被执行到，哪些Python代码没有被执行到，并输出覆盖率报告。



其安装命令为：

pip install coverage


下面演示其使用方法。构造一个名为myprogram.py的文件，内容为：

import sys
​
if int(sys.argv[1]) > 1: 
   print("success")
else: 
    print("fail")


执行命令:

coverage run myprogram.py 0


将执行上述程序，并获取执行细节存储在当前目录下的.coverage文件中。然后，执行命令: 

coverage report


即可生成覆盖率报告如下。在这个示例中，代码覆盖率为75%。

coverage report 
Name           Stmts   Miss  Cover 
----------------------------------
myprogram.py       4      1    75%


doctest



doctest是Python内置功能，能够实现"文档即用例"模式的自动化测试。具体来说，在定义Python函数时，可以在函数注释中插入特定格式的表示测试用例的内容。doctest会自动从函数注释中识别和提取测试用例，并执行这些用例。



在下面的例子中，针对函数factorial(n)，在注释中定义了两个测试用例。一个是正常测试用例[factorial(n) for n in range(6)]，期望结果是[1, 1, 2, 6, 24, 120]；另一个是异常测试用例factorial(30.1)，期望结果是抛出ValueError异常。

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.
    >>> [factorial(n) for n in range(6)] 
    [1, 1, 2, 6, 24, 120] 
    >>> factorial(30.1) 
    Traceback (most recent call last): 
        ... 
    ValueError: n must be exact integer 
    """
​
    import math
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    result, factor = 1, 2
    while factor <= n:
        result *= factor
        factor += 1
    return result
​
if __name__ == "__main__":
    import doctest
    doctest.testmod()


执行命令:

python example.py  -v


doctest的执行过程如下，结果显示两个测试用例都是pass的：

# python example.py  -v 
Trying: 
    [factorial(n) for n in range(6)] 
Expecting: 
    [1, 1, 2, 6, 24, 120] 
ok 
Trying: 
    factorial(30.1) 
Expecting:
    Traceback (most recent call last): 
        ...
    ValueError: n must be exact integer 
ok
1 items had no tests: 
    __main__ 
1 items passed all tests: 
   2 tests in __main__.factorial 
2 tests in 2 items. 
2 passed and 0 failed. 
Test passed.


elasticsearch



自动化测试的一个热点技术是测试监控(或质量监控)。对于监控类应用来说，ELK已经成为优先的技术选择。Python的elasticsearch库，提供了与elasticsearch引擎进行交付的API。既可以向elasticsearch引擎推送格式化的测试数据，也可以从elasticsearch查询历史测试记录。



elasticsearch的安装命令为：

pip install elasticsearch


elasticsearch的简单示例如下：

from elasticsearch import Elasticsearch 
#默认连接到localhost:9200
es = Elasticsearch()  
#查询索引为test-index的记录 
print(es.search(index="test-index", body={"query": {"match_all": {}}}))


ftplib



在测试FTP类应用(FTP应用在传统IT行业依然广泛存在)时，经常需要使用Python标准库中的ftplib模块。它实现了FTP客户端协议，能够与FTP服务端进行交付，从而测试FTP服务端的功能。



一个基于ftplib的简单示例为：

from ftplib import FTP 
​
ftp = FTP('ftp.debian.org')     # 连接到FTP服务端
ftp.login()                     # 登陆
ftp.cwd('debian')               # 切换目录
ftp.retrlines('LIST')           # 获取文件列表
with open('README', 'wb') as fp:
    ftp.retrbinary('RETR README', fp.write) # 下载文件
ftp.quit() # 退出连接


gauge-python



gauge是ThoughtWorks提供的一个免费和开源自动化测试框架。它的主要特点是可以减少测试脚本数量，降低测试维护成本。gauge-python是Python语言的gauge执行器。



gauge-python的执行依赖于gauge, python和pip。其安装命令：

gauge install python


创建一个gauge-python项目的命令：

gauge init python


执行测试用例的命令：

gauge run specs


面向UI自动化测试的gauge-python示例项目为：https://github.com/ka shishm/gauge-example-python



html



解析HTML文件，从中提取感兴趣的内容是自动化测试中的一个常见操作。Python标准库中的html模块，能够帮助实现对HTML文件的解析。



一个解析HTML的例子如下：

from html.parser import HTMLParser 
​
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
​
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
​
    def handle_data(self, data):
        print("Encountered some data  :", data)
​
parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')


程序输出结果为：

Encountered a start tag: html 
Encountered a start tag: head 
Encountered a start tag: title 
Encountered some data  : Test 
......
Encountered an end tag : html


ipython



ipython想必大家都非常熟悉的Python交互式工具。ipython是用来快速调试或测试代码的不二选择。据我观察，大牛们在写Python程序前，都习惯在ipython上敲一敲，快速熟悉API的用法，验证想法是否可行。这比写代码->保存->切换窗口->执行脚本->继续改代码的过程简单多了。



在自动化测试中，我们也可以使用类似方式高效地调试测试脚本或定位某个具体错误。例如，在下面的例子中，我们快速验证接口在请求参数发生变化时，是否会报错：

In [18]: import requests
​
In [19]: requests.get("https://www.python.org/search/?q=").status_code
Out[19]: 200
​
In [20]: requests.get("https://www.python.org/search/?q=yes123").status_code
Out[20]: 200
​
In [21]: requests.get("https://www.python.org/search/?q=_______").status_code
Out[21]: 200


json



json可以是一种家喻户晓的数据交换格式了。在自动化测试中，我们经常需要处理json格式数据。Python标准库中的json模块，提供了序列化和反序列化json对象的方法。



例如：

import json 
​
# 序列化(编码)
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]) 
# 结果：'["foo", {"bar": ["baz", null, 1.0, 2]}]' 
# 反序列化(解码)
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
# 结果：['foo', {'bar': ['baz', None, 1.0, 2]}]


kubernetes



在云原生和微服务日益流行的趋势下，基于Kubernetes的测试环境变得越来常见。Python的kubernetes库，提供了管理和控制Kunernetes namespace, node, deployment, pod的接口API。



安装命令为：

pip install kubernetes


下面是一个获取kubernetes中所有pod的IP地址的例子：

from kubernetes import client, config 
​
config.load_kube_config() 
v1 = client.CoreV1Api() 
print("Listing pods with their IPs:") 
ret = v1.list_pod_for_all_namespaces(watch=False) 
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


locust



locust是Python编写的可扩展压力测试工具。它主要用在性能测试方面，目的是检验系统能够承受的最大并发用户数量。locust通过gevent和协程实现异步IO，能够在单台机器上模拟海量用户的行为。



locust的安装方式：

pip install locustio


locust的执行依赖于一个描述locust任务的文件，例如： 

from locust import HttpLocust, TaskSet 
​
def login(l):
    l.client.post("/login", {"username":"ellen_key", "password":"education"})
​
def logout(l):
    l.client.post("/logout", {"username":"ellen_key", "password":"education"})
​
def index(l):
    l.client.get("/")
​
def profile(l):
    l.client.get("/profile")
​
class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}
    
    def on_start(self):
        login(self)
​
    def on_stop(self):
        logout(self)
​
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000


执行命令，准备测试网址http://example.com：

locust --host=http://example.com


然后用浏览器打开http://127.0.0.1:8089/，就可以开发并发测试了:





mock



mock是Python标准库的一个模块，用于在单元测试中替换程序的部分方法，并返回预定义结果。



下面是一个mock示例。示例中，ProductionClass类的method方法被mock掉，并且返回值设置为3。这样，当调用method方法时，就不会去执行原始方法，而是直接返回3。

from unittest.mock import MagicMock 
​
thing = ProductionClass() 
thing.method = MagicMock(return_value=3) 
thing.method(3, 4, 5, key='value') 
thing.method.assert_called_with(3, 4, 5, key='value')


nose2



nose2是Python的单元测试框架"三剑客"之一，另两个分别是unittest和pytest。我写过一篇比较这三个框架的文章《三种最流行的Python测试框架，我该用哪一个》。



nose2安装命令为：

pip install nose2


unittest是Python标准库中的单元测试框架，nose2的定位是带插件的unittest。nose2提供的插件，例如测试用例加载器，覆盖度报告生成器，并行测试等内置插件和第三方插件，让单元测试变得更加完善。



一个简单的nose2单元测试示例如下：

import nose2 
​
def test_example (): 
    pass 
​
if __name__ == '__main__': 
    nose2.runmodule()


执行结果：

...
--------------------- 
Ran1 tests in 0.000s 
OK


os



操作系统是自动化测试经常需要打交道的一个对象。Python标准库中的os模块，提供了调用操纵系统功能的接口，包括但不限于路径切换，文件夹管理，环境变量，进程管理，文件描述符操作等。



下面是几个使用os模块的简单示例：

import os 
​
print(os.getcwd()) # 获取当前工作目录
print(os.listdir()) # 列举文件夹
os.chdir('Population_Data/New York') # 切换目录
os.mkdir('testdir') # 创建新目录


pytest



刚才介绍了，pytest是Python单元测试框架"三剑客"之一。事实上，pytest不仅让单元测试变得更容易，并且也能支持应用层面复杂的功能测试。因此，pytest可以说是通用框架。甚至在nose2的Github主页上，都推荐大家使用pytest，而不是nose2。



pytest的主要特性有：

1) 支持用简单的assert语句实现丰富的断言，无需复杂的self.assert*函数，

2) 兼容unittest和nose2测试集，

3) 支持Fixture形式的测试setup/teardown，其优势在文章《什么是Fixture？》中有详细描述，

4) 丰富的插件生态，已有300多个各式各样的插件，和活跃的社区。



pytest一个简单的示例如下：

def inc(x):
    return x +1 
​
def test_answer(): 
    assert inc(3) ==5


执行结果如下：

$ pytest 
============================= test session starts============================= 
collected 1 items  
test_sample.py F  
================================== FAILURES=================================== 
_________________________________ test_answer_________________________________
    def test_answer(): 
>       assert inc(3)== 5 
E       assert 4 == 5  
E        +  where 4 = inc(3)  
​
test_sample.py:5: AssertionError  
========================== 1 failed in 0.04 seconds===========================


q



你没看错，这个工具名字就是q。q是Python中一款适合"懒人"的快速调试工具。q的安装命令为：

pip install q


在调试代码时，如果用print打印变量var的值，那么语法是print(var)，而使用q完成同样任务，只需用q(var)。当然前提是要import q。比print更强大的是，q还能直接插入到表达式内部，例如：

file.write(q/prefix + (sep or '').join(items))


会在在执行代码时，打印prefix的值。另外q作为函数装饰器(@q)使用时，还能自动跟踪函数执行情况，打印函数的参数，返回值和运行时间。



Robot Framework



Robot Framework是一个主流的功能自动化测试框架。它基于Python编写。Robot Framework有三大特点：通用(general)，关键词驱动(keyword-driven)和模块化(modular)。基于Robot Framework编写测试用例，使用的是Robot语法。这是一种领域专用语言(DSL)，十分接近自然语言，有利于开发经验欠缺的测试人员使用。



安装命令：

pip install robotframework


一个简单的Robot用例为：

*** Settings *** 
Documentation     A test suite with a single test for valid login.
Resource          resource.txt
​
*** Test Cases *** 
Valid Login 
    Open Browser To Login Page
    Input Username    demo
    Input Password    mode
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser


这个用例中的步骤，既可以采用Robot Framework标准库或第三方库来实现，也可以通过Python或者Java程序来定义。



selenium



Python中的selenium库提供了一系列简洁的API来与Selenium Webdriver进行交互，从而完成UI自动化测试。



selenium的安装命令为：

pip install selenium


由于Python selenium库并不直接操作浏览器，因此还需要安装一个可用的webdriver，并进行配置。不同浏览器需要安装不同的webdriver，一般都能在浏览器官网上下载到。



下面是一个使用selenium的简单例子。例子中，调用Fixfox浏览器， 打开网址http://www.python.org，然后定位搜索框，输入"pycon"，回车得到搜索结果。在代码中中，利用assert语句针对部分中间结果做了校验。

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
​
driver = webdriver.Firefox() 
driver.get("http://www.python.org") 
assert "Python" in driver.title 
elem = driver.find_element_by_name("q") 
elem.clear() 
elem.send_keys("pycon") 
elem.send_keys(Keys.RETURN) 
assert "No results found." not in driver.page_source 
driver.close()


tox



在用Python做自动化测试开发时，开发环境的维护和外部依赖的管理常常是一个痛点，尤其是在需要支持多个Python版本的时候。tox工具就是针对这个痛点而出现的。它的愿景是让Python软件打包，测试和发布变得更容易。



tox的安装命令为：

pip install tox


使用tox，需要在项目根目录创建一个名为tox.ini的描述文件，例如：

# content of: tox.ini , put in same dir as setup.py 
[tox] 
envlist = py27,py36 
​
[testenv]
# install pytest in the virtualenv where commands will be executed
deps = pytest 
commands = 
    # NOTE: you can run any command line tool here - not just tests
    pytest


这时，执行命令tox，就可以同时完成python2.7和Python3.6两种环境下的测试：

[lots of output from what tox does] 
[lots of output from commands that were run]
​
__________________ summary _________________ 
  py27: commands succeeded
  py37: commands succeeded
  congratulations :)


unittest



unittest是Python标准库中的单元测试框架。unittest有时候也被称为PyUnit。就像JUnit是Java语言的标准单元测试框架一样，unittest(PyUnit)则是Python语言的标准单元测试框架。



unittest支持自动化测试，测试用例的初始化和关闭，测试用例的聚合等功能。unittest有一个很重要的特性：它通过类(class)的方式，将测试用例组织在一起。



一个简单unittest用例如下：

import unittest 
​
class TestStringMethods(unittest.TestCase): 
    def test_upper(self): 
        self.assertEqual('foo'.upper(), 'FOO') 
​
if__name__=='__main__': 
    unittest.main()


执行结果：

...
--------------------- 
Ran 1 tests in 0.000s 
OK


VCR.py



VCR是ruby中的一个著名工具，用来录制和回访HTTP消息交互过程。VCR.py，顾名思义，就是Python版本的VCR。



安装命令：

pip install vcrpy


在下面的例子中。第一次执行完代码片段后，VCR.py会把HTTP交互过程记录下来，保存到文件fixtures/vcr_cassettes/synopsis.yaml中。再次执行代码时，VCR.py将直接从该文件中获取reponse内容，而不需要发送真实的HTTP请求。

import vcr 
import urllib2 
​
with vcr.use_cassette('fixtures/vcr_cassettes/synopsis.yaml'): 
    response = urllib2.urlopen('http://www.iana.org/domains/reserved').read() 
    assert 'Example domains' in response


webbrowser



webrowser是Python标准库中的一个模块，提供直接打开浏览器的Python接口。例如：

import webbrowser
​
url = 'http://www.python.org/' 
​
# 在新标签中打开连接http://www.python.org/doc/
webbrowser.open_new_tab(url + 'doc/')


xml



与json一样，XML也是一种常见数据交换格式。许多自动化测试框架会输出xUnit标准测试报告，这种报告就是XML格式的。另外，一种标准代码覆盖率报告Cobertual，也是XML格式的。与XML文件打交道，在Python自动化测试是普遍的。而标准库中的xml模块，就提供了处理XML数据的接口。



例如，有下面这个名为country_data.xml的文件：

<?xml version="1.0"?> 
<data> 
    <country name="Liechtenstein"> 
        <rank>1</rank> 
        <year>2008</year> 
        <gdppc>141100</gdppc> 
        <neighbor name="Austria" direction="E"/> 
        <neighbor name="Switzerland" direction="W"/> 
    </country> 
</data>


解析它的Python脚本为：

import xml.etree.ElementTree as ET
​
tree = ET.parse('country_data.xml')  
root = tree.getroot()  
print(root.tag) # 'data'


yappi



从yappi这个名字可以猜到，它大概又是一个yet another xxx系统的工具。这里，yappi代表yet another python profier，主要用来分析Python代码性能。



安装命令为：

pip install yappi


示例略。



zope.testbrowser



zope.testbrowser是一个Python第三方库，它提供易用和可编程的web浏览器，能够用于UI测试。



安装命令为：

pip install zope.testbrowser




例如，下面的例子中，程序打开链接http://localhost，并从页面定位内容是"Link Text"的超链接元素：

from zope.testbrowser.wsgi import Browser
from zope.testbrowser.testing import demo_app
​
browser = Browser('http://localhost/', wsgi_app=demo_app)
link = browser.getLink('Link Text')


总结



这里简要介绍了26个应用于自动化测试的Python工具。仅仅看这26个工具，就可以了解到Python丰富的生态优势。基本上各种典型的测试场景，都能从Python中找到对应的自动化测试工具或框架。



当然，Python中可以应用于自动化测试工具远远不止这26个。真实数字可能是260个，甚至2600个。这里列举的工具只是抛砖引玉，大家来补充。欢迎在留言区写下自己在日常测试工作中经常使用的Python库。



另外，如果觉得文章有帮助，欢迎帮忙转发，谢谢！



最后，奉上星球"速度之上的质量"的限量特惠券，后面再也不会有这种优惠力度了。感兴趣的同学尽快加入哟。如果想了解详情，也可以戳这里。



