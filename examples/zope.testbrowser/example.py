from zope.testbrowser.ftests.wsgitestapp import WSGITestApplication
from zope.testbrowser.wsgi import Browser

wsgi_app = WSGITestApplication()

browser = Browser('http://localhost/@@/testbrowser/simple.html', wsgi_app=wsgi_app)
print(browser.url)
