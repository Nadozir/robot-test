*** Settings ***
Library           Selenium2Library
Library           C:/****/robottest.py
Library           PageLoaded

*** Test Cases ***
    ${result} =    Run test_check_button
    stdout={C:/*****}/stdout.txt
    Terminate test_check_button   ${handle}
    ${result} =    Wait For test_check_button	timeout=20 secs
    Should Be Equal As Integers  ${result.rc}	0

