import unittest
import day4.recipes


class RecipeTestCase(unittest.TestCase):
    def setUp(self):

        pass

    def test_get_procedure(self):
        noodles_process = day4.recipes.fav_foods["noodles_list"]
        chapatis_process = day4.recipes.fav_foods["chapatis_list"]

        self.assertListEqual(
            day4.recipes.fav_foods["noodles_list"], noodles_process)
        self.assertListEqual(
            day4.recipes.fav_foods["chapatis_list"], chapatis_process)

    def test_get_ingredient(self):
        noodles_1 = day4.recipes.ingredients["noodles_ingredients"]
        chapatis_1 = day4.recipes.ingredients["chapatis_ingredients"]
        self.assertListEqual(
            day4.recipes.ingredients["noodles_ingredients"], noodles_1)
        self.assertListEqual(
            day4.recipes.ingredients["chapatis_ingredients"], chapatis_1)


if __name__ == "__main__":
    unittest.main()
