## Police Stations

Toy project per request from a friend.  Uses Selenium and Chromedriver to scrape metadata about police stations in the US from mapdevelopers.com.

Simple implementation of the Extractor class.  Loads a list of police station abbreviations into a NumPy array for use by Extractor.  Iterates over each row of the np array, fetching the url with the abbreviation as the query parameter.  Extracts the metadata about the police station and updates the np array, or reinitializes the Exctractor instance and continues on search failure.  Dumps updated np array to an outfile.

