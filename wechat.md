Python自动化测试工具箱：从A到Z

背景

几个月前，一篇题为《Python实用技能: 从A到Z》的文章在网络上刷屏了。在文章中，作者介绍了26个首字母分别是A到Z的Python实用工具。不过，这些工具都是面向Python基础知识的。

大家知道，Python具有广泛应用。Python的重要应用之一就是自动化软件测试。这里，我借鉴上述文章的手法，针对自动化测试这一专门领域，精选一套首字母分别是A到Z的Python工具箱，分享给大家。

说明

这个工具箱所包含的26个Python工具，覆盖自动化测试的方方面面。总的来说，包括三种类型：
1. 面向Python语言本身的白盒测试工具，
2. 面向通用测试领域，基于Pytho实现的黑盒测试工具，
3. Python生态系统中广泛应用于自动化测试脚本的库。

下面就逐一简要介绍这26个工具。文中的代码示例全部收集在Github项目中：https://github.com/slxiao/python-test-automation-AtoZ。欢迎大家下载使用。

逐一介绍

**assert**

在软件测试中，一个普遍的需求就是比较被测对象的实际输出与期望输出是否相同。如果相同，测试继续执行；如果不相同，测试就会因失败而终止。Python中有一个内置的关键字，正好可以满足这一需求。它就是assert。

assert语句可以跟两个参数。其中第一个参数是必须的，表示判断条件，如果条件不为True，那么assert语句会报错，并且抛出"AssertionError"异常。第二个参数是可选的，表示当assert失败时，提示的错误消息。

例如，

actual, expected = 1, 2
assert actual == expected # 抛出异常
assert actual == expected, "actual result is not same as expected" #抛出异常并且提示错误消息

**behave**

behave是一种Python实现的行为驱动开发(Behavior-driven development, BDD)框架。在BDD框架中，测试用例被分为前端和后端两部分。前端用例由自然语言编写，负责描述；后端用例由Python编写，负责执行。

behave的安装命令为：

pip install behave

下面是一个测试用例示例。用例的前端部分是自然语言，为：

Feature: Showing off behave

  Scenario: Run a simple test
    Given we have behave installed
     When we implement 5 tests
     Then behave will test them for us!

后端为Python实现：
from behave import given, when, then, step

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0

执行结果为：
$ behave
Feature: Showing off behave # features/example.feature:2

  Scenario: Run a simple test          # features/example.feature:4
    Given we have behave installed     # features/steps/example_steps.py:4
    When we implement 5 tests          # features/steps/example_steps.py:8
    Then behave will test them for us! # features/steps/example_steps.py:13

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined

**Coverage.py**
代码覆盖率是软件测试度量的重要手段之一。Python中用于度量代码覆盖率的重要工具就是Coverage.py。它计算哪些Python代码被执行到，哪些Python代码没有被执行到，并输出覆盖率报告。

安装命令为：
pip install coverage

假设存在一个源文件myprogram.py，其代码为：
import sys

if int(sys.argv[1]) > 1:
    print("success")
else:
    print("fail")

执行coverage run myprogram.py 0命令，调用Python程序，并且生成执行数据，存储在当前目录下的.coverage文件。

然而，执行命令coverage report，生成覆盖率报告。在这个示例中，代码覆盖率为75%。

coverage report
Name           Stmts   Miss  Cover
----------------------------------
myprogram.py       4      1    75% 

**doctest**

doctest是Python内置的功能，能够实现代码注释驱动的自动化测试。在定义Python函数时，可以在注释中插入特定格式的表示测试用例的内容。doctest会自动从注释中提取和识别测试用例，并提供执行用例的接口。

以下面的代码为例，针对函数factorial(n)，在注释中定义了两个测试用例。一个是正常测试用例，[factorial(n) for n in range(6)]；另一个是异常测试用例，factorial(30.1)。

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    """
    import math
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    result, factor = 1, 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

执行命令"python example.py  -v"命令，结果如下，两个测试用例都是pass的。
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

**elasticsearch**
自动化测试的一个热点技术是测试监控(或质量监控)。对于监控类应用来说，ELK是首选的技术栈。Python中的elasticsearch库，提供了与elasticsearch进行交付的API，可以用于向elasticsearch推送测试数据，以及从elasticsearch查询测试数据。

elasticsearch的安装命令为：
pip install elasticsearch

elasticsearch的简单示例为：
from elasticsearch import Elasticsearch
es = Elasticsearch() #默认连接到localhost:9200

#查询索引为test-index的记录
print(es.search(index="test-index", body={"query": {"match_all": {}}})) 

**ftplib**
在测试FTP类应用时，经常需要使用Python标准库中的ftplib模块。它实现了FTP客户端协议，能够与FTP服务端进行交付，用于测试FTP服务端的功能。

一个基于ftplib的简单示例为：
from ftplib import FTP

ftp = FTP('ftp.debian.org')     # connect to host, default port
ftp.login()                     # user anonymous, passwd anonymous@
ftp.cwd('debian')               # change into "debian" directory
ftp.retrlines('LIST')           # list directory contents

with open('README', 'wb') as fp:
    ftp.retrbinary('RETR README', fp.write)

ftp.quit()

**gauge-python**
gauge是ThoughtWorks的一个免费和开源的自动化测试框架，其主要特点是可以减少测试脚本数量，从而较低测试维护成本。gauge-python则是Python语言的gauge执行器。

gauge-python的执行依赖于gauge, python和pip。其安装命令为：
gauge install python

创建一个gauge-python项目的命令为：
gauge init python

执行测试用例的命令为：
gauge run specs

一个面向UI自动化的gauge-python项目示例为：https://github.com/kashishm/gauge-example-python

**html**

解析HTML文件，从中提取感兴趣的内容是自动化测试中的一个常见需求。Python标准库中提供了html模块，能够帮助实现对HTML和XHTML文件的解析。

一个简单的HTML解析示例为：
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

输出结果如下：
Encountered a start tag: html
Encountered a start tag: head
Encountered a start tag: title
Encountered some data  : Test
......
Encountered an end tag : html

**ipython**

ipython想必大家都非常熟悉交互式Python开发工具。ipython一个典型的用途就是来高效地调试和验证程序。

据我观察，许多大牛在写Python程序之前，都会在ipython上敲一敲命令，快速熟悉API的用法，并验证想法是否可行。在ipython上基本验证过之后，才开始写程序。这比写代码->保存->切换窗口->执行脚本->继续改代码的流程简单多了。

在自动化测试中，我们也可以使用类似的方式，高效地调整测试脚本，或者定位某一个错误。例如，在下面的例子中，我们快速验证被测软件的接口：

**json**
json可以是一种家喻户晓的数据交换格式了。在自动化测试中，我们经常需要处理json格式的数据。Python中的json库，提供了序列化和反序列化json对象的方法。

import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
#'["foo", {"bar": ["baz", null, 1.0, 2]}]'
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
#['foo', {'bar': ['baz', None, 1.0, 2]}]

**kubernetes**
在云原生和微服务日益普及的趋势下，基于Kubernetes的测试环境变得越来常见。Python的kubernetes库，提供了管理和控制Kunernetes namespace, pod, node的接口API。

安装命令为：
pip install kubernetes

下面这个示例，获取kubernetes中所有的POD的IP地址：
from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

**locust**

locust是Python编写的，可扩展的压力测试工具。它主要用在性能测试用，目的是验证系统(不仅仅是UI系统)能够承受的最大并发用户数量。locust通过gevent实现事件驱动，能够在单台机器上模拟海量的用户行为。

locust的安装方式为：
pip install locustio

下面的例子中
from locust import HttpLocust, TaskSet

def login(l):
    l.client.post("/login", {"username":"ellen_key", "password":"education"})

def logout(l):
    l.client.post("/logout", {"username":"ellen_key", "password":"education"})

def index(l):
    l.client.get("/")

def profile(l):
    l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

执行命令为：locust --host=http://example.com

然后用浏览器打开http://127.0.0.1:8089/，就可以开发并发测试了。

**mock**
mock是Python标准库中的一个模块，它用于替换程序中的属性和接口，并返回预定义的结果。mock主要用于Python单元测试。当然，对于Python实现的高级别测试用例，在被测对象还不可用的时候，可以用mock来调试测试用例。


下面是一个mock示例。示例中，ProductionClass类的method方法被mock掉，并且返回值设置为3。这样，当调用method方法时，就不会真的去执行它，而直接范围3。

from unittest.mock import MagicMock
thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key='value')
thing.method.assert_called_with(3, 4, 5, key='value')

**nose2**
nose2是Python的单元测试框架"三剑客"之一。另两个分别是unittest和pytest，后面会有介绍。我之前也写过一篇比较这三个框架的文章《三种最流行的Python测试框架，我该用哪一个？》。

nose2安装命令为：

pip install nose2

nose2的主要目的是扩展python的标准单元测试库unittest，因此它的定位是“带插件的unittest”。nose2提供的插件，例如测试用例加载器，覆盖度报告生成器，并行测试等内置插件和第三方插件，让单元测试变得更加完善。

一个简单的nose单元测试示例如下：

import nose2
 
def test_example ():
    pass
 
if __name__ == '__main__':
    nose2.runmodule()

执行结果：

...
---------------------
Ran1 tests in 0.000s
OK

**os**

操作系统是我们在自动化测试过程经常需要打交道的一个对象。Python标准库中的os模块，提供了调用操纵系统接功能的接口，包括但不限于工作路径切换，文件夹处理，环境变量，进程信息，文件描述符操作等。

下面是几个使用os模块的简单示例：

import os

print(os.getcwd())

print(os.listdir())

os.chdir('Population_Data/New York')

os.mkdir('testdir')

**pytest**
刚才介绍了，pytest是Python单元测试框架三剑客之一。事实上，pytest不仅让单元测试变得更容易，并且也能扩展到支持应用层面复杂的功能测试。甚至在nose2 Github主页上，都推荐大家使用pytest，而不是nose2。

pytest的特性有：

1）支持用简单的assert语句实现丰富的断言，无需复杂的self.assert*函数
2）自动识别测试模块和测试函数
3）兼容unittest和nose测试集
4）支持Fixture形式的测试setup/teardown，这一点我的文章《什么是Fixture？》中有详细介绍。
5）丰富的插件生态，已有300多个各式各样的插件，和活跃的社区

pytest一个简单的示例如下：

definc(x):
    return x +1
 
deftest_answer():
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
 
test_sample.py:5: AssertionError
========================== 1 failed in 0.04 seconds===========================

**Queue**

**Robot Framework**
Robot Framework是重要的功能自动化测试框架。它是完全基于Python编写的。Robot Framework的作者是芬兰人Pekka Laukkanen，其设计思想源于Pekka在2006年提交的，题为"Data-Driven and Keyword-Driven Test Automation Frameworks"的硕士论文。在同年，Robot Framework有了第一个版本。2008年，Robot Framework v2.0正式在Github上开源。Robot Framework最新版本是今年5月发布的v3.1.2。

Robot Framework有三大特点：通用(general)，关键词驱动(keyword-driven)和模块化(modular)。基于Robot Framework编写测试用例，使用的是Robot语法。这是一种领域专用语言(DSL)。十分接近自然语言，因此适合开发基础薄弱的测试人员转型自动化。

安装命令为：
pip install robotframework

一个简单的示例为：
*** Settings ***
Documentation     A test suite with a single test for valid login.
Resource          resource.txt

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    demo
    Input Password    mode
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser

这里测试用例中的步骤，可以基于Robot Framework标准库或第三方库来实现，也可以自己用Python或者Java语言来实现。

**selenium**
Python中的selenium库提供了一系列简洁的API来与Selenium Webdriver进行交互，实现UI自动化测试。

selenium的安装命令为：pip install selenium

由于python selenium库并不直接操作浏览器，而是通过Webdriver。因此还需要安装一个可用的Webdriver，并且配置。不同浏览器需要安装不同的Webdriver，一般都能在浏览器官方上下载到。

下面是一个使用selenium的简单例子。例子中，调用Fixfox浏览器， 打开网址http://www.python.org，然后找到搜索框，输入pycon，回车得到搜索结果。在过程中，利用assert做了一些中间结果的判断。

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()




更多示例

总结与互动