from analyzer import RequestsAnalyzer
from util import FileIO, parse_args


def main():
    command_args = parse_args()
    analyze_requests = RequestsAnalyzer()
    analyze_requests_output = analyze_requests(
        input_path=command_args['input_path'],
        ignored_urls=command_args['ignored_urls'])
    FileIO.writefile(command_args['output_path'], analyze_requests_output)
    analyze_requests.console_print(analyze_requests_output)


if __name__ == '__main__':
    main()
