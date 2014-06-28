from unittest import TestCase

import stats_handler
import recipe_parser


class Test_StatsHandler(TestCase):
	def test_basic_example(self):
		foo = [
			['water', 'salt', 'pepper'],
			['water', 'pepper'],
			['salt', 'pepper'],
			['honey']
		]

		s = stats_handler.StatsHandler()

		for e in foo:
			s.add_entry(e)

		self.assertEqual(
			s._core,
			{
				'honey': {},
				'pepper': {'salt': 2, 'water': 2},
				'salt': {'pepper': 2, 'water': 1},
				'water': {'pepper': 2, 'salt': 1}
			}
		)
		self.assertEqual(
			s.ingredient_num,
			8
		)

class Test_RecipeParser(TestCase):
	def test_basic_example(self):
		text = '1 tblsp salt\n2 lb pepper'

		self.assertEqual(
			recipe_parser.AlastraParser.parse(text),
			['salt', 'pepper']
		)

	def test_another_example(self):
		text ="""2 medium heads romaine
1/2 seedless cucumber
2 celery ribs, thinly sliced
3 tablespoons extra-virgin olive oil
1 1/2 tablespoons fresh lemon juice
1 teaspoon mild honey
1 teaspoon Dijon mustard"""

		self.assertListEqual(
			sorted(recipe_parser.AlastraParser.parse(text)),
			sorted([
				'seedless cucumber',
				'celery ribs thinly sliced',
				'extra virgin olive oil',
				'fresh lemon juice',
				'mild honey',
				'Dijon mustard',
				'heads romaine'
			])
		)