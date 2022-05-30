import pytest
from tests.pages.base_page import BasePage
from tests.pages.locators import MainPageLocators
from tests.pages.main_page import MainPage


class TestHoverAndPlayByIndex:

    @pytest.mark.parametrize('video_segment', [None, 1/3, 4/5])
    def test_playing_hover_video_by_index(self, browser, video_segment, index=0):
        link = "https://www.youtube.com/"
        page = BasePage(browser, link)
        page.open()
        page.hover_video_by_index(index)
        main_page = MainPage(browser, browser.current_url)
        main_page.rewind_hovered_video(video_segment)
        assert main_page.check_hovered_video_is_playing() is True, "Video is not playing"

    @pytest.mark.parametrize('video_segment', [None, 1/3, 4/5])
    def test_hover_and_play_video_by_index(self, browser, video_segment, index=0):
        link = "https://www.youtube.com/"
        page = BasePage(browser, link)
        page.open()
        page.hover_video_by_index(index)
        video_preview = browser.find_element(*MainPageLocators.INLINE_PREVIEW)
        video_preview.click()
        page.rewind_video(video_segment)
        assert page.check_video_is_playing() is True, "Video is not playing"
