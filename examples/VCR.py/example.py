import vcr
import urllib2

with vcr.use_cassette('fixtures/vcr_cassettes/synopsis.yaml'):
    response = urllib2.urlopen('http://www.iana.org/domains/reserved').read()
    assert 'Example domains' in response