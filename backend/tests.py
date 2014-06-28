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
			sorted(recipe_parser.AlastraParser.parse(text)),
			sorted(['salt', 'pepper'])
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

	def test_big_example(self):
		text = """Lemon Cheesecake With Greek Yoghurt & Honey     : 

175 grams digestive biscuits, crushed (6oz)
75 grams unsalted butter, melted (23/4oz)
25 grams demerara sugar, (1oz)

200 g full fat soft cheese
60 milliliters greek honey, (4tbsp)
150 g strained yoghurt
juice and zest of 2 lemons
142 ml double cream

Lightly grease the base of a 20cm (8") round loose-bottomed cake
tin.   Make the cheesecake base by combining the biscuit crumbs,
butter and  demerara sugar.  Press the mixture evenly over the base
of the tin with the back of a spoon.  Leave in the refrigerator to
chill whilepreparing  the cheesecake topping. Place the soft cheese,
honey and yoghurt in a bowl and beat well, using an electric hand
whisk or balloon whisk, until the mixture isthoroughly  combined.
Stir in the lemon juice and zest. Add the cream and continue whisking
carefully at a low speed until the  mixture becomes the consistency
of lightly whipped cream.  Pour the  mixture over the biscuit base
and leave in the refrigerator for atleast 4 hours, or overnight,
until the cheesecake has set. Transfer to a serving plate and
decorate simply with shavings of lemon zest or seasonal fruit"""

		self.assertListEqual(
			sorted(recipe_parser.AlastraParser.parse(text)),
			sorted([
				'digestive biscuits crushed',
				'unsalted butter melted',
				'demerara sugar',
				'full fat soft cheese',
				'greek honey',
				'strained yoghurt',
				'juice and zest of lemons',
				'double cream'
			])
		)

	def test_big_example2(self):
		text = """

Kahlua Cheesecake

1 1/4 cups graham cracker crumbs
1/4 cup sugar
1/4 cup cocoa
1/3 cup butter or margarine, melted
2 8-oz pkgs cream cheese, softened
3/4 cup sugar
1/2 cup cocoa
2 eggs
1/4 cup strong coffee
1/4 cup kahlua
1 teaspoon vanilla extract
1 cup sour cream
2 tablespoons sugar
1 teaspoon vanilla
6 chocolate curls 

Combine graham cracker crumbs, 1/4 cup sugar, cocoa and butter or
margarine.  Mix well.  Press mixture into bottom of a 9-inch spring
form pan.  Bake at 325 F for 5 minutes.  Cool.  Beat cream cheese
with mixer until light and fluffy; gradually add 3/4 cup sugar,
mixing well.  Beat in 1/2 cup cocoa. Add eggs, one at a time,
beating well after each addition.  Stir in coffee, Kahlua and 1
teaspoon vanilla extract.  Pour into prepared pan.  Bake at 375
for 25 minutes.  Combine sour cream, 2 tablespoons sugar and 1
teaspoon vanilla; spread over hot cheesecake.  Bake 425  for 5 to
7 minutes.  Let cool at room temperature on a wire rack.  Chill 8
hours or overnight. Remove side of spring form pan.  To garnish,
place 3 chocolate curls in the center of cheesecake; gently break
the remaining chocolate curls and sprinkle over cheesecake if
desired."""

		self.assertListEqual(
			sorted(recipe_parser.AlastraParser.parse(text)),
			sorted([
				'graham cracker crumbs',
				'sugar',
				'cocoa',
				'butter',
				'margarine melted',
				'cream cheese softened',
				'sugar',
				'cocoa',
				'eggs',
				'strong coffee',
				'kahlua',
				'vanilla extract',
				'sour cream',
				'sugar',
				'vanilla',
				'chocolate curls'
			])
		)