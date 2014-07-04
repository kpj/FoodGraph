import argparse


def drawer_argparse():
	parser = argparse.ArgumentParser(
		description="Tool to generate static images from data"
	)

	parser.add_argument(
		"-s",
		"--sample",
		help="path to sample",
		type=str,
		metavar="<path to sample>",
		required=True
	)
	parser.add_argument(
		"-i",
		"--image",
		help="path to image",
		type=str,
		metavar="<path to image>",
		required=True
	)
	parser.add_argument(
		"-m",
		"--mode",
		help="Drawing mode to use",
		type=str,
		metavar="<drawing mode>",
		default='opacity'
	)

	return parser.parse_args()

def miner_argparse():
	parser = argparse.ArgumentParser(
		description="Tool to crawl the web and search for recipes"
	)

	parser.add_argument(
		"-f",
		"--food",
		help="type of food to search for",
		type=str,
		metavar="<food type>",
		required=True,
		nargs='+'
	)
	parser.add_argument(
		"-s",
		"--sample",
		help="path to sample",
		type=str,
		metavar="<path to sample>",
		required=True
	)
	parser.add_argument(
		"-n",
		"--number",
		help="Number of recipes to fetch",
		type=int,
		metavar="<recipe number>",
		default=10
	)

	return parser.parse_args()