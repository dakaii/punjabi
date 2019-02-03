import unittest
from collections import defaultdict

from analyzer import RequestsAnalyzer

_MOCK_INPUT_PATH = 'tests/mock_files/mock_data.log'
_MOCK_INPUT_PATH_EMPTY = 'tests/mock_files/mock_data_empty.log'


class TestRequestsAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = RequestsAnalyzer()

    def tearDown(self):
        del self.analyzer

    def test_analyze_returns_correct_values(self):
        output = self.analyzer.analyze(
            input_path=_MOCK_INPUT_PATH,
            ignored_urls=('.gif'))
        correct_values = [
            '/articles.html?id=1004',
            '/articles.html?id=46',
            '/articles.html?id=0',
            '/vendor/bootstrap.min.js',
            '/vendor/bootstrap.min.css',
            '/articles.html?id=72',
            '/articles.html?id=74',
            '/articles.html?id=4',
            '/articles.html?id=21',
            '/articles.html?id=24']
        self.assertEqual(output, correct_values)

    def test_analyze_returns_10_items(self):
        output = self.analyzer.analyze(
            input_path=_MOCK_INPUT_PATH,
            ignored_urls=('.gif'))
        correct_values = [
            '/articles.html?id=1004',
            '/articles.html?id=46',
            '/articles.html?id=0',
            '/vendor/bootstrap.min.js',
            '/vendor/bootstrap.min.css',
            '/articles.html?id=72',
            '/articles.html?id=74',
            '/articles.html?id=4',
            '/articles.html?id=21',
            '/articles.html?id=24']
        self.assertEqual(len(output), 10)

    def test_empty_log_results_in_empty_list(self):
        output = self.analyzer.analyze(
            input_path=_MOCK_INPUT_PATH_EMPTY,
            ignored_urls=('.gif'))
        correct_values = []
        self.assertEqual(output, correct_values)

    def test_calculates_average_correctly(self):
        output = self.analyzer._calculate_and_sort(
            defaultdict(list),
            [{
                'url': '/articles.html?id=24',
                'response_time': 2.0,
                'response_status': 200
            }, {
                'url': '/articles.html?id=24',
                'response_time': 1.0,
                'response_status': 200
            }],
            ('.gif'))
        self.assertEqual(output[0][1], 1.5)

    def test_urls_are_case_insensitive(self):
        test_input = [
            '/articles.html?id=1004, 1.00s, Status Code: 200',
            '/ARTICLES.html?id=1004, 2.00, Status Code: 200']
        cleaned_log = self.analyzer._clean_input(test_input)
        output = self.analyzer._calculate_and_sort(
            defaultdict(list), cleaned_log, ('.gif'))
        self.assertEqual(output[0][1], 1.5)
    
    def test_specified_urls_are_ignored(self):
        test_input = [
            '/articles.html?id=1004, 1.00s, Status Code: 200',
            '/ARTICLES.html?id=1004, 2.00, Status Code: 200']
        cleaned_log = self.analyzer._clean_input(test_input)
        output = self.analyzer._calculate_and_sort(
            defaultdict(list), cleaned_log, ('.html'))
        self.assertEqual(output, [])


if __name__ == '__main__':
    unittest.main()
