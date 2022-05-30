import pytest
from tests.pages.base_page import BasePage


class TestSearchAndPlayByName:

    @pytest.mark.parametrize('video_segment', [None, 1/3, 4/5])
    def test_playing_video_by_search_bar_and_video_name(self, browser, video_segment,
                                                        search_value='тюбинг', video_name='Тюбинг.Ташлы. Уфа'):
        link = "https://www.youtube.com/"
        page = BasePage(browser, link)
        page.open()
        page.search_video(search_value)
        page = BasePage(browser, browser.current_url)
        page.choose_target_video(video_name)
        page.rewind_video(video_segment)
        assert page.check_video_is_playing() is True, "Video is not playing"
