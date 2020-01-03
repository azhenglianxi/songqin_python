*** Settings ***
Documentation    Suite description
Library  SeleniumLibrary
Library  Collections
Library  st
*** Keywords ***
loginwebsite
        [Arguments]   ${username}=auto   ${password}=sdfsdfsdf
        open browser   http://localhost/mgr/ps/mgr/index.html  chrome
        set selenium implicit wait    10

        input text    id=username    ${username}
        input text    id=password    ${password}
        click element   tag=button


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
        ${eles}=   Get Webelements  css=tr>td:nth-child(2)
        ${lessons} =  create list
        :FOR   ${ele}   IN   @{eles}
           \   log to console    ${ele.text}
           \   append to list    ${lessnons}      ${ele.text}

        [Return]   ${lessons}


*** Test Cases ***
测试1
        [Setup]     deleteAllCourse
        [Teardown]   deleteAllCourse
        loginwebsite   auto  sdfsdfsdf
        add course   初中化学   初中化学操作   4
        ${lesson}=   get course list
        should be true  $lessons==["初中化啥的学"]
         close browser
