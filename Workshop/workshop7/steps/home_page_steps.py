from behave import *

@given('I introduce website url adress in browser')
def step_impl(context):
    context.home_page.open_website()

@when('I press ENTER')
def step_impl(context):
    context.home_page.navigate_to_website()

@then('Home Page is displayed "{expected_url}"')
def step_impl(context, expected_url):
    context.home_page.check_home_page(expected_url)

@given('I am on the Home Page')
def step_impl(context):
    context.home_page.open_website()
    context.home_page.navigate_to_website()

@when('Page is loaded')
def step_impl(context):
    context.home_page.loaded_home_page()

@then('Carousel page element is displayed')
def step_impl(context):
    context.home_page.carousel_is_visible()