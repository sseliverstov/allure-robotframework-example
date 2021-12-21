*** Settings ***
Documentation   В либе используем декоратор @keywords и смотрим что в аллюре
Library    library.user_name.UserName  WITH NAME   KeywordUserNameExample

*** Test Cases ***
Manual test case
    [Tags]      allure.label=manual
    KeywordUserNameExample.Печальный кейворд    1
    KeywordUserNameExample.Ручной кейворд