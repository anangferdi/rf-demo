*** Settings ***
Documentation   Robot Framework demo to handling valid login scenario
...
...             This test suites contains only one test case
Resource        resource.robot

*** Test Cases ***
Valid Login
    Open browser to login page
    Input username    ${VALID USERNAME}
    Input password    ${VALID PASSWORD}
    Submit credential
    Welcome page should be open 
    [Teardown]    Close Browser