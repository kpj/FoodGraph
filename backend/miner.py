import url_handler, stats_handler, file_handler


stats = stats_handler.StatsHandler()
filer = file_handler.FileHandler('../data/sample3.js')

u = url_handler.AlastraHandler('german', 10)
content = u.parse_content()

for e in content:
	stats.add_entry(e)

#stats.info()

filer.save(stats._core, stats.ingredient_num)