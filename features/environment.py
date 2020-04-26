from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os


def before_all(context):
    print("Executing before all")


def before_feature(context, feature):
    print("Before feature\n")


# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    print("Before scenario\n")


def after_scenario(context, scenario):
    print("Scenario status is {}".format(scenario.status))
    if scenario.status == "failed":
        if not os.path.exists("failed_tests"):
            os.makedirs("failed_tests")
        os.chdir("failed_tests")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    context.browser.quit()
    print("After scenario\n")


def after_feature(context, feature):
    print("\nAfter feature")


def after_all(context):
    print("Executing after all")
