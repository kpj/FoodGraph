import sys

import url_handler, stats_handler, file_handler


if len(sys.argv) != 3:
	print('Usage: %s <food type> <path to sample>' % sys.argv[0])
	sys.exit(1)

food_type = sys.argv[1]
sample_file = sys.argv[2]

stats = stats_handler.StatsHandler()
filer = file_handler.FileHandler(sample_file)

u = url_handler.AlastraHandler(food_type, 10)
content = u.parse_content()

for e in content:
	stats.add_entry(e)

#stats.info()

filer.save(stats._core, stats.ingredient_num)