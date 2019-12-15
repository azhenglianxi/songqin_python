*** Settings ***
Library  SeleniumLibrary
Library  Collections

*** Keywords ***
login website
    [Arguments]   ${username}=auto   ${password}=sdfsdfsdf
    open browser  http://localhost/mgr/login/login.html  chrome
    set selenium implicit wait  10
    input text  id=username  ${username}
    input text  id=password  ${password}
    click element  tag=button
add course
    [Arguments]   ${name}   ${desc}  ${idx}
    click element   css=*[ng-click="showAddOne=true"]
    input text  css=*[ng-model="addData.name"]   ${name}
    input text  xpath=//div[@class="ng-scope"]//*[@ng-model="addData.desc"]  ${desc}
    input text  css=*[ng-model="addData.display_idx"]  ${idx}
    click element  css=*[ng-click="addOne()"]
    sleep  2
get course list
    ${lessons}=  create list
    ${eles}=    Get Webelements  css=tr>td:nth-child(2)
    :FOR   ${ele}   IN   @{eles}
       \   log to console    ${ele.text}
       \   append to list  ${lessons}  ${ele.text}
    [Return]   ${lessons}