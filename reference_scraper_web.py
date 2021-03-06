# Importing the necessary modules
from urllib import urlopen
from xml.etree import ElementTree
import json

def get_all_references():
	"""
		get_all_movies()
		Scrapes a single page with a list of movies.
		Adds each movie to an array.
		And returns that array
	"""
	#
	# Scraping Settings
	#
	# Set the url of all the movies
	all_references_url = "http://wiki.tarantino.info/index.php/Kill_Bill_References_Guide/westerns"
	# Set the xpath for all titles
	titles_xpath = './/span[@class="mw-headline"]'


	# open (and load) the site, then read the html
	site = urlopen(all_references_url)
	html = site.read()
	
	# parse the html as an XML-tree
	tree = ElementTree.fromstring(html)
	
	# find all titles
	title_elements = tree.findall(titles_xpath)
	# print len(title_elements)
	
	# Create an empty array
	movies = []
	
	# Get the title and the link from the elements
	for elem in title_elements:
		
		# Create empty movie dictionary
		movie = {}
		
		# Get the <li> sub element
		sub_element_xpath = ".//li"
		li_elem = elem.find(sub_element_xpath)

		# Only try to get the li if there is one
		if li_elem is not None:
			
			# Only add the movie if the title is not None
			title = li_elem.text
			if title is not None:
				print title
				

				# Get the href as link
				#movie['link'] = li_elem.get('href')

				# Append the dict to the array
				#movies.append(movie)
			
	# Return the array
	return movies

def main():
	"""
		main()
		Main function with overall the recipe / strategy for scraping. 
	"""
	#
	# Get all the movies from the overview page
	movies = get_all_references()
	
	# Outputs the movies as JSON
	with open('tarantino_references.json', 'w') as outfile:
		json.dump(movies, outfile)
	
if __name__ == '__main__':
	main()
