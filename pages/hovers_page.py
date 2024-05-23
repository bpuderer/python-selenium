from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HoversPage():

    FIGURE_BOX = (By.CLASS_NAME, "figure")
    BOX_CAPTION = (By.CLASS_NAME, "figcaption")

    def __init__(self, driver):
        self.driver = driver

    def hover_over_figure(self, index):
        # pass in 1 based index
        figure_element = self.driver.find_elements(*HoversPage.FIGURE_BOX)[index - 1]
        ac = ActionChains(self.driver)
        ac.move_to_element(figure_element).perform()
        figcaption_element = figure_element.find_element(*HoversPage.BOX_CAPTION)
        return {
            "is_displayed": figure_element.is_displayed(),
            "header": figcaption_element.find_element(By.TAG_NAME, "h5").text,
            "link_text": figcaption_element.find_element(By.TAG_NAME, "a").text,
            "link": figcaption_element.find_element(By.TAG_NAME, "a").get_attribute(
                "href"
            ),
        }
