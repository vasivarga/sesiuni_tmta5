from behave import *

@given('You are on the sign up page')
def step_impl(context):
    context.signup_page.sign_up_page()

@when('I fill in the form "{name}", "{email}"')
def step_impl(context, name, email):
    context.signup_page.fill_in_name(name)
    context.signup_page.fill_in_email(email)
    context.signup_page.click_button()

@then('I receive error message "{error_message}"')
def step_impl(context, error_message):
    context.signup_page.acceptable_error()
    context.signup_page.check_error_message(error_message)