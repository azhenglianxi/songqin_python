*** Settings ***
Library  SeleniumLibrary
Library  Collections
Library  st
Resource  rc.robot


*** Test Cases ***
测试1
    [Setup]  deleteAllCourse
    [Teardown]  deleteAllCourse
    login website
    add course  初中化学  化学描述  5
    ${lesson}=   get course list
    should be true  $lesson==["初中化学"]
    close browser














