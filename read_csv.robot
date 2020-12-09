*** Settings ***
Library    csv_library.py

*** Test Cases ***
Reading a csv file
    ${data}    Read Csv File    test.csv
    log    ${data}