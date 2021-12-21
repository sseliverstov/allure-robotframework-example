*** Settings ***
Documentation   Попытка сделать динамические имена для ручных
Library    .library.dynamic_name.DynamicName  WITH NAME   KeywordDynamincrNameExample

*** Test Cases ***
Keyword without decorator invoked by name
    KeywordDynamincrNameExample.My Keyword

