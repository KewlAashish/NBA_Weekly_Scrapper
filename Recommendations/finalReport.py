from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.remote.webelement import WebElement


class finalReport:
    def __init__(self, ListSectionElement: WebElement):
        self.ListSectionElement = ListSectionElement
        self.videosList = self.pull_videos_elements()

    def pull_videos_elements(self):
        return self.ListSectionElement.find_elements(
            By.CSS_SELECTOR,
            'ytd-video-renderer[class="style-scope ytd-item-section-renderer"]'
        )

    '''def parse_data(self,video):
        video_title = video.find_element(
            By.CSS_SELECTOR,
            'yt-formatted-string[class="style-scope ytd-video-renderer"]'
        ).get_attribute(
            'innerHTML'
        ).strip()

        views_count = video.find_element(
            By.CSS_SELECTOR,
            'span[class="style-scope ytd-video-meta-block"]'
        ).get_attribute(
            'innerHTML'
        ).strip()

        uploaded_BY = video.find_element(
            By.CSS_SELECTOR,
            "a[class='yt-simple-endpoint style-scope yt-formatted-string']"
        ).get_attribute(
            'innerHTML'
        ).strip()

        return {
            'Video Title' : video_title,
            'View count' : views_count,
            'Channel' : uploaded_BY
        }'''

    def pull_videos_attributes(self):
        collection = []

        # videos_data = [self.parse_data(video) for video in self.videosList[:20]]
        for video in self.videosList:
            video_title = video.find_element(
                By.CSS_SELECTOR,
                'yt-formatted-string[class="style-scope ytd-video-renderer"]'
            ).get_attribute(
                'innerHTML'
            ).strip()

            views_count = video.find_element(
                By.CSS_SELECTOR,
                'span[class="style-scope ytd-video-meta-block"]'
            ).get_attribute(
                'innerHTML'
            ).strip()

            uploaded_BY = video.find_element(
                By.CSS_SELECTOR,
                "a[class='yt-simple-endpoint style-scope yt-formatted-string']"
            ).get_attribute(
                'innerHTML'
            ).strip()
            collection.append(
                [video_title, views_count, uploaded_BY]
            )

        return collection
