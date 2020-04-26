from locators.locators import Locators


class HomePage:

    def __init__(self, context):
        self.context = context.browser

    def verify_dashboard_tab(self):
        self.context.find_element_by_css_selector(Locators.dashboardTab).is_displayed()
