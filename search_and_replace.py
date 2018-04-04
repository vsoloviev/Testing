import os
import sys
import argparse

def file_search():
	topdir = '.'
	extens = ['html', 'js', 'json', 'ts', 'map']
	found = {x: [] for x in extens}
	for dirpath, dirnames, files in os.walk(topdir):
		for name in files:
			ext = name.lower().rsplit('.', 1)[-1]
			if ext in extens:
				found[ext].append(os.path.join(dirpath, name))
	files_arr = []
	for search in found:
		files_arr = files_arr + found[search]
	return files_arr

def replace_var(file_replace, string_to_replace, string_replace_with):

	for f in file_replace:
		with open(f, 'r') as file:
			filedata = file.read()
		filedata = filedata.replace(string_to_replace, string_replace_with)
		with open(f, 'w') as file:
			file.write(filedata)

def main():
	parser = argparse.ArgumentParser()
	find_ver = parser.add_argument_group('Replace variables')
	find_ver.add_argument('-sr', '--string-to-replace', dest='strr', help='Enter string to replace.')
	find_ver.add_argument('-rs', '--string-to-replace-with', dest='strw', help='Enter string to replace with.')
	args = parser.parse_args()
	files=file_search()
	replace_var(files, args.strr, args.strw)

main()
