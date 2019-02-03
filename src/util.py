import argparse
import json
import sys

from settings import INPUT_PATH, OUTPUT_PATH, IGNORED_URLS


def parse_args():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--input_path", help="input file path")
    argparser.add_argument("--output_path", help="output file path")
    argparser.add_argument("--ignored_urls", help="urls to be ignored")
    paths = argparser.parse_args()
    return {
        'input_path': paths.input_path or INPUT_PATH,
        'output_path': paths.output_path or OUTPUT_PATH,
        'ignored_urls': paths.ignored_urls or IGNORED_URLS
    }

class FileIO:
    @staticmethod
    def writefile(fname, data):
        '''
        When the file is not found, this function create a new file
        and writes to it.
        '''
        with open(fname, 'w') as f:
            json.dump(data, f, ensure_ascii=False)


    @staticmethod
    def parse_input(fpath):
        try:
            with open(fpath) as f:
                return [x.strip() for x in f.readlines()]
        except IOError as err:
            sys.exit("The required file {0} was not found.".format(fpath))
