from unittest import TestCase

import stats_handler
import recipe_parser


class TestUtils(TestCase):
	def test_stats_handler(self):
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

	def test_parser(self):
		text = '1 tblsp salt\n2 lb pepper'

		self.assertEqual(
			recipe_parser.AlastraParser.parse(text),
			['salt', 'pepper']
		)