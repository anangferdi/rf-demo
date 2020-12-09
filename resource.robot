*** Settings ***
Documentation    A resource file with reusable keywords and variables
...
...              It utilize keywords provided by the imported SeleniumLibrary
Library          SeleniumLibrary

*** Variables ***
${SERVER}            localhost:7272
${LOGIN URL}         http://${SERVER}/
${BROWSER}           firefox
${DELAY}             0
${VALID USERNAME}    demo
${VALID PASSWORD}    mode
${WELCOME URL}       http://${SERVER}/welcome.html

*** Keywords ***
Open browser to login page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login page should be open

Login page should be open
    Title Should Be    Login Page

Input username
    [Arguments]    ${username}
    Input Text    username_field    ${username}

Input password
    [Arguments]    ${password}
    Input Text    password_field    ${password}

Submit credential
    Click Button    login_button

Welcome page should be open
    Location Should Be    ${WELCOME URL}
    Title Should Be    Welcome Page
