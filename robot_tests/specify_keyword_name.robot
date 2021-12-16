*** Settings ***
Documentation   В либе используем декоратор @keywords и смотрим что в аллюре
Library    library.user_name.UserName  WITH NAME   KeywordUserNameExample

*** Test Cases ***
Keyword without decorator invoked by func name
    KeywordUserNameExample.without_decorator

Keyword without decorator invoked by name
    KeywordUserNameExample.Without Decorator

Keyword with simple decorator
    KeywordUserNameExample.Ползовательское имя для кейворда

Keyword with simple by default name
    Skip    Так уже не работает!!!
    KeywordUserNameExample.With Simple Decorator

Keyword with name and placeholder
    Log     Плейсхолдер не работает для декоратора @keywords
    KeywordUserNameExample.Кейворд с аргументом {string}    Привет!
