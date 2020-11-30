# -*- coding: UTF-8 -*-

# Import from standard library
import os
import baba
import pandas as pd
# Import from our lib
from baba.lib import clean_data
import pytest
from baba import lib
import datetime
import unittest
def test_clean_data():
    datapath = os.path.dirname(os.path.abspath(baba.__file__)) + '/data'
    df = pd.read_csv('{}/data.csv.gz'.format(datapath))
    first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (999, 142)
    out = clean_data(df)
    assert out.shape == (985, 119)

class TestWeather(unittest.TestCase):
    def test_search_city_for_paris(self):
        city = lib.search_city('Paris')
        self.assertEqual(city['title'], 'Paris')
        self.assertEqual(city['woeid'], 615702)

    def test_search_city_for_london(self):
        city = lib.search_city('London')
        self.assertEqual(city['title'], 'London')
        self.assertEqual(city['woeid'], 44418)

    # def test_search_city_for_unknown_city(self):
    #     city = lib.search_city('Rouen')
    #     self.assertEqual(city, None)

    def test_search_city_ambiguous_city(self):
        lib.input = lambda _: "1"
        city = lib.search_city('San')
        self.assertEqual(city['title'], 'San Francisco')

    # def test_weather_forecast(self):
    #     forecast = lib.weather_forecast(44418)
    #     self.assertIsInstance(forecast, None, "Did you select the `consolidated_weather` key?")
    #     self.assertEqual(forecast[0]['applicable_date'], datetime.date.today().strftime('%Y-%m-%d'))
