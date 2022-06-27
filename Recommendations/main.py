import time
from selenium import webdriver
import os
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import By
from prettytable import PrettyTable
from Recommendations import resources
from Recommendations.finalReport import finalReport
import pandas as pd
from Recommendations.smtp import ManagingMails

class Recommendations(webdriver.Chrome):
    def __init__(self, driver_path=r"D:\webdrivers", teardown=False):
        self.driver_path = driver_path

        #   Teardown to know when to let the window get closed
        self.teardown = teardown

        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Recommendations, self).__init__(options=options)

        #   Adding implicitly waiting time for every process
        self.implicitly_wait(8)

        #   To maximise the window as soon as we fetch it.
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    #   Load the youtube webpage
    def landYOUTUBE(self):
        self.get(resources.YOUTUBE_RESOURCE_URL)

    def getNBARecommendations(self):
        VideosListdiv = self.find_element(
            By.ID,
            resources.overall_lists_div_id
        )
        report = finalReport(ListSectionElement=VideosListdiv)
        table = PrettyTable(
            ["Video Title", "Views", "Channel"]
        )
        table.add_rows(report.pull_videos_attributes())
        return table

    def download_csv_report(self):
        nbarecomFinal = self.getNBARecommendations()
        finalData_df = pd.DataFrame(nbarecomFinal)
        finalData_df.to_csv('NBAtrending.csv',index=None)

    def sendingMail(self, data):
        manager = ManagingMails()
        manager.sendMail(data=data)


