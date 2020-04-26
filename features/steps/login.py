from behave import given, when, then
from pageobjects.loginPage import LoginPage
from pageobjects.homePage import HomePage
from values import parameters
import time


@given(u'I am on login page')
def step_impl(context):
    context.browser.get(parameters.base_url)
    time.sleep(5)


@when(u'I login with valid user credentials')
def step_impl(context):
    lp = LoginPage(context)
    lp.enter_valid_login("Admin", "admin123")


@then(u'I should be able to successfully login')
def step_impl(context):
    hp = HomePage(context)
    hp.verify_dashboard_tab()
