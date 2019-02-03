
# How to run the program

In order to run the tests, run the following command.

``` shell
cd src
python -m unittest tests.test
```

Also run the following command in the top root directory to run the program to see the results.
You can specify the path to the log file to analyze with the --input_path flag.

```shell
python main.py --input_path txts/sample.log
```

# Comments

    - This project doesn't contain the requirement.txt file since I did not use any external libraries.
    - The program is written in Python 3.
    - The function analyze_requests mentioned in the assignment description is renamed analyze for better scalability.