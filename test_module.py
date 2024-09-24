import unittest
import sea_level_predictor
import numpy as np
import matplotlib.pyplot as plt


# the test case
class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Rise in Sea Level'")
    
    def test_plot_labels(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'Year'")
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'Sea Level (inches)'")
        actual = self.ax.get_xticks().tolist()
        expected = [1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]
        self.assertEqual(actual, expected, "Expected x tick labels to be '1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0'")

    def test_plot_data_points(self):
        actual = self.ax.get_children()[0].get_offsets().data.tolist()
        expected = [[1880.0, 0.0], [1881.0, 0.22047244100000002], [1882.0, -0.440944881], [1883.0, -0.232283464], [1884.0, 0.590551181], [1885.0, 0.531496062], [1886.0, 0.43700787399999996], [1887.0, 0.216535433], [1888.0, 0.299212598], [1889.0, 0.362204724], [1890.0, 0.440944881], [1891.0, 0.374015748], [1892.0, 0.499999999], [1893.0, 0.6850393690000001], [1894.0, 0.303149606], [1895.0, 0.767716535], [1896.0, 0.46850393700000004], [1897.0, 0.6732283459999999], [1898.0, 1.043307086], [1899.0, 1.338582676], [1900.0, 1.125984251], [1901.0, 1.1102362190000001], [1]]

if __name__ == "__main__":
    unittest.main()
