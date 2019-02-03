import json
import sys
from collections import defaultdict
from pprint import pprint

from util import FileIO


class Analyzer(object):

    def __init__(self):
        pass

    def __call__(self, **kargs):
        return self.analyze(**kargs)

    def analyze(self):
        raise NotImplementedError

    def console_print(self, data):
        pprint(data)


class RequestsAnalyzer(Analyzer):

    def __init__(self):
        self.max_items = 10

    def analyze(self, **kargs):
        parsed_log = FileIO.parse_input(kargs['input_path'])
        cleaned_log = self._clean_input(parsed_log)
        output = self._calculate_and_sort(
                defaultdict(list), cleaned_log, kargs['ignored_urls'])
        return [x[0] for x in output][:self.max_items]
    
    def _calculate_and_sort(self, times_by_urls, cleaned_log, ignored_urls):
        self._filter_input(times_by_urls, cleaned_log, ignored_urls)
        output = self._calculate_avg(times_by_urls)
        output.sort(key=lambda x: x[1], reverse=True)
        return output

    def _filter_input(self, times_by_urls, inputted_data, ignored_urls):
        for data in inputted_data:
            url_without_query_str = data['url'].split('?')[0]
            if data['response_status'] == 200 and \
                    not url_without_query_str.endswith(ignored_urls):
                times_by_urls[data['url']].append(data['response_time'])
    
    def _calculate_avg(self, times_by_urls):
        output = []
        for url, processing_times in times_by_urls.items():
            ave_processing_time = sum(processing_times) / float(len(processing_times))
            output.append((url, ave_processing_time))
        return output
    
    def _clean_input(self, txt_input):
        data = []
        for vals in txt_input:
            url, response_time, response_status = vals.split(',')
            data.append({
                'url': url.lower(),
                'response_time': float(response_time.replace('s', '')),
                'response_status': int(response_status.split(':')[1])
            })
        return data
