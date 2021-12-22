*** Settings ***
Documentation   В либе используем декоратор @keywords и смотрим что в аллюре
Library    library.user_test_library.UserTestLibrary  WITH NAME   Foo
Library    library.user_test_library.UserTestLibrary  WITH NAME   Boo
Test Setup       Boo.Открыть браузер
Test Teardown    Foo.Закрыть браузер

*** Test Cases ***
Manual test case
    [Tags]      allure.manual
    Boo.Неимплементированный кейвод
    Foo.Кейворд с ошибкой
    Foo.Что-то делаем еще ....  один    два
