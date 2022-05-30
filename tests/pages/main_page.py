from selenium.webdriver import ActionChains
from tests.pages.base_page import BasePage
from tests.pages.locators import MainPageLocators


class MainPage(BasePage):

    def check_hovered_video_is_playing(self):
        player = self.browser.find_element(*MainPageLocators.MOVIE_PLAYER)
        atr = player.get_attribute("class")
        if 'playing-mode' in atr:
            return True
        else:
            return False

    def rewind_hovered_video(self, video_segment):
        if video_segment is not None:
            line = self.browser.find_element(*MainPageLocators.VIDEO_LINE)
            line_width = line.size['width']
            x_coordinate = line_width * video_segment
            action = ActionChains(self.browser)
            action.move_to_element_with_offset(line, x_coordinate, 1)
            action.click()
            action.perform()
        else:
            pass
