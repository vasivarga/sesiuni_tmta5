from browser import Browser
from pages.home_page import HomePage
from pages.signup_page import SignUp

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.signup_page = SignUp()


def after_all(context):
    context.browser.close()