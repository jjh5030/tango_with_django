import json
import urllib, urllib2
import sys

def run_query(search_terms):
	# Specify the base
	root_url = 'https://api.datamarket.azure.com/Bing/Search/'
	source = 'Web'

	results_per_page = 10
	offset = 0

	query = "'{0}'".format(search_terms)
	query = urllib.quote(query)

	# https://api.datamarket.azure.com/Bing/Search/v1/Web?Query=%27rango%27

	search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
		root_url,
		source,
		results_per_page,
		offset,
		query)
	
	# Setup authentication with the Bing servers.
	# The username MUST be a blank string, and put in your API key!
	username = ''
	bing_api_key = '60keZmgZ3yi2IfEbuNPAVcY1HfBC4Q9JixPexD9GyYA'

	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None, search_url, username, bing_api_key)

	results = []

	try:
		handler = urllib2.HTTPBasicAuthHandler(password_mgr)
		opener = urllib2.build_opener(handler)
		urllib2.install_opener(opener)

		response = urllib2.urlopen(search_url).read()

		json_response = json.loads(response)

		for result in json_response['d']['results']:
			results.append({
				'title': result['Title'],
				'link': result['Url'],
				'summary': result['Description']
				})
	except urllib2.URLError, e:
		print "Error when querying the Bing API: ", e
	except:
		print "Some error happened: ", sys.exc_info()[0]

	return results

def main():
	# Query, get the results and create a variable to store rank.
	query = raw_input("Please enter a query: ")
	results = run_query(query)
	rank = 1
	
	# Loop through our results.
	for result in results:
		# Print details.
		print "Rank {0}".format(rank)
		print result['title']
		print result['link']
		print
		
		# Increment our rank counter by 1.
		rank += 1

if __name__ == '__main__':
	main()