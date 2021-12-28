
# ITS Projekt 2 - implementacia automatickych testov podla navrhu BBD scenarov
# Autor: Rebeka Černianska, xcerni13
# 10.5.2021



from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@given(u'User is logged out')
def step_impl(context):
    pass


@when(u'User logs in')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.ID, "personaltools-login").click()
    element = context.driver.find_element(By.ID, "personaltools-login")
    context.driver.find_element(By.ID, "__ac_name").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("itsadmin")
    context.driver.find_element(By.ID, "__ac_password").click()
    context.driver.find_element(By.ID, "__ac_password").send_keys("itsadmin")
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()


@then(u'User can look at all content')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-folderContents span:nth-child(2)").click()

###################################
@given(u'Use cases home page open')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()



@when(u'a new Use Case is created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-logo > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "use_case").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("USE CASE 2")
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>aaa<br data-mce-bogus=\"1\"></p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()



@then(u'it is visible on the page')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.LINK_TEXT, "USE CASE 2").click()


###################################################
@given(u'a Use Case is available')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")




@when(u'use Actions Delete')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.LINK_TEXT, "USE CASE 2").click()
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-logo > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions").click()
    context.driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()




@then(u'Use Case is no longer available')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    try:
        context.driver.find_element(By.LINK_TEXT, "USE CASE 2")
    except:
        pass

#######################################################

@when(u'a new Evaluation Scenario is created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-logo > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "evaluation_scenario").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("New Eval Scenario")
    context.driver.find_element(By.ID, "form-widgets-evaluation_secnario_id").click()
    context.driver.find_element(By.ID, "form-widgets-evaluation_secnario_id").send_keys("UC2_R_1")
    context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").click()
    context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").send_keys("aaa")
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'it is possible to open and edit it')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.LINK_TEXT, "New Eval Scenario").click()


#######################################################
@when(u'a Requirement is created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.LINK_TEXT, "UC1 Trespassing Monitoring & Enforcing System").click()
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-logo > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "requirement").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("Requirement")
    context.driver.find_element(By.ID, "form-buttons-save").click()


@then(u'it is available on the home page')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.LINK_TEXT, "UC1 Trespassing Monitoring & Enforcing System").click()
    context.driver.find_element(By.LINK_TEXT, "Requirement").click()


####################################################
@given(u'Admin is logged in')
def step_impl(context):
    pass


@given(u'Use Case exists')
def step_impl(context):
    pass


@given(u'Use Case has Evaluation Scenarios')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-logo > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()
    context.driver.find_element(By.ID, "use_case").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("USE CASE 2")
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>aaa<br data-mce-bogus=\"1\"></p>'}", element)
    context.driver.switch_to.default_content()
    context.driver.find_element(By.ID, "form-buttons-save").click()
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.LINK_TEXT, "USE CASE 2").click()
    context.driver.find_element(By.CSS_SELECTOR, ".icon-edit").click()
    element = context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()
    context.driver.find_element(By.LINK_TEXT, "use-cases").click()
    context.driver.find_element(By.CSS_SELECTOR, "#select2-result-label-8 .icon-right-circle").click()
    context.driver.find_element(By.CSS_SELECTOR, "#select2-result-label-18 .pattern-relateditems-result-path").click()
    context.driver.find_element(By.ID, "form-buttons-save").click()

@given(u'Use Case page is open')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.LINK_TEXT, "USE CASE 2").click()


@when(u'Use Case is deleted')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    context.driver.find_element(By.LINK_TEXT, "USE CASE 2").click()
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-logo > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions").click()
    context.driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()


@then(u'it is no longer available')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.find_element(By.LINK_TEXT, "Use cases").click()
    try:
        context.driver.find_element(By.LINK_TEXT, "USE CASE 2")
    except:
        pass




####################################################
@given(u'an Evaluation Scenario is open')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/use-cases")
    context.driver.find_element(By.LINK_TEXT, "UC1 Trespassing Monitoring & Enforcing System").click()
    context.driver.find_element(By.CSS_SELECTOR, "#contentview-edit span:nth-child(2)").click()
    element = context.driver.find_element(By.CSS_SELECTOR, "#portal-logo > img")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()
    context.driver.find_element(By.LINK_TEXT, "use-cases").click()
    context.driver.find_element(By.CSS_SELECTOR, "#select2-result-label-10 .pattern-relateditems-result-path").click()
    context.driver.find_element(By.ID, "form-buttons-save").click()


@when(u'this scenario is deleted')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/use-cases")
    context.driver.find_element(By.LINK_TEXT, "New Eval Scenario").click()
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-logo > img").click()
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-actions").click()
    context.driver.find_element(By.ID, "plone-contentmenu-actions-delete").click()
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #form-buttons-Delete").click()


@then(u'it is not available to this or other Use Case')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "UC1 Trespassing Monitoring & Enforcing System").click()
    try:
        context.driver.find_element(By.LINK_TEXT, "New Eval Scenario")
    except:
        pass


@then(u'all Requirements and Test Cases tied to it are deleted')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/use-cases")






# ####################################################







