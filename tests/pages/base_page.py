import time
from selenium.webdriver import ActionChains
from tests.pages.locators import BasePageLocators, VideoPageLocators, MainPageLocators
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def search_video(self, search_name):
        search_field = self.browser.find_element(*BasePageLocators.SEARCH_FIELD)
        search_button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON)
        search_field.send_keys(search_name)
        search_button.click()

    def check_video_is_playing(self):
        player = self.browser.find_element(*VideoPageLocators.MOVIE_PLAYER)
        atr = player.get_attribute("class")
        if 'playing-mode' in atr:
            return True
        else:
            return False

    def rewind_video(self, video_segment):
        if video_segment is not None:
            line = self.browser.find_element(*VideoPageLocators.VIDEO_LINE)
            line_width = line.size['width']
            x_coordinate = line_width * video_segment
            action = ActionChains(self.browser)
            action.move_to_element_with_offset(line, x_coordinate, 1)
            action.click()
            action.perform()
        else:
            pass

    def hover_video_by_index(self, index):
        images = self.browser.find_elements(*MainPageLocators.VIDEO_IMG)
        videos = []
        for i in images[0::2]:
            videos.append(i)
        video = videos[index]
        action = ActionChains(self.browser)
        action.move_to_element(video).perform()

    def choose_target_video(self, video_name):
        while True:
            height = self.browser.execute_script("return document.body.scrollHeight")
            time.sleep(1)
            self.browser.find_element_by_tag_name('body').send_keys(Keys.END)
            if int(height) == 0:
                break
        target_video = self.browser.find_element_by_css_selector(f"[title='{video_name}']")
        target_video.click()
