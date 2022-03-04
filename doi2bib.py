import os
import re
import yaml
import urllib
import requests
from itertools import groupby

import argparse

def ris2dict(ris):
	records = [ (line[0:2],line[6:]) for line in ris.split('\n') if line ]
	def _group_to_value(g):
		values = list(map(lambda xs: xs[1], g))
		return values if len(values) > 1 else values[0]
	key_map = { 'TY' : 'type'
	          , 'AU' : 'authors'
	          , 'PY' : 'print_year'
	          , 'DA' : 'submission_date'
	          , 'TI' : 'title'
	          , 'SP' : 'SP'
	          , 'EP' : 'EP'
	          , 'VL' : 'volume'
	          , 'IS' : 'IS'
	          , 'AB' : 'abstract'
	          , 'SN' : 'SN'
	          , 'UR' : 'url'
	          , 'DO' : 'doi'
	          , 'ID' : 'cite_id'
	          , 'JO' : 'journal'
	          , 'ER' : 'ER' }
	d = { key_map[key]:_group_to_value(group) for key, group in groupby(records,lambda xs: xs[0]) }
	return d


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('config_files', metavar='doi_files', type=str, nargs='+', help='doi yaml files')
	args = parser.parse_args()
	
	if not args.config_files:
		print('No configuration file given')
		exit(1)

	for config_file in args.config_files:
		config = yaml.safe_load(open(config_file,'r'))
		for doi in config['dois']:
			doi_resolution = requests.get(f'https://doi.org/{doi}')
			url = doi_resulotion.url
			if 'www.nature.com' in url:
				citation_query = requests.get(f'https://citation-needed.springer.com/v2/references/{doi}')
				citation = citation_query.text




