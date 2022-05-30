from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_FIELD = (By.NAME, "search_query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button#search-icon-legacy>yt-icon")


class MainPageLocators:
    VIDEO_IMG = (By.CSS_SELECTOR, "#primary ytd-rich-grid-renderer>#contents #img.style-scope.yt-img-shadow")
    MOVIE_PLAYER = (By.ID, "inline-preview-player")
    VIDEO_LINE = (By.CSS_SELECTOR, "#inline-preview-player>.ytp-progress-bar-container")
    INLINE_PREVIEW = (By.CSS_SELECTOR, "#inline-preview-player .ytp-inline-preview-scrim.ytp-inline-preview-scrim-clear")


class ResultsPageLocators:
    RESULT_VIDEO = (By.CSS_SELECTOR, "Дельфин - Имя")


class VideoPageLocators:
    MOVIE_PLAYER = (By.ID, "movie_player")
    VIDEO_LINE = (By.CSS_SELECTOR, ".style-scope.ytd-page-manager.hide-skeleton .ytp-timed-markers-container")
