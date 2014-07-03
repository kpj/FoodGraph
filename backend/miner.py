import sys

import url_handler, stats_handler, file_handler
from arg_parser import miner_argparse as get_args


args = vars(get_args())

food_type = args['food']
sample_file = args['sample']
recipe_num = args['number']


stats = stats_handler.StatsHandler()
filer = file_handler.FileHandler(sample_file)

u = url_handler.AlastraHandler(food_type, recipe_num)
content = u.parse_content()

for e in content:
	stats.add_entry(e)

#stats.info()

filer.save(
	stats._core,
	{
		'inum': stats.ingredient_num,
		'ftype': food_type
	}
)