from Recommendations.main import Recommendations
import time

try:
    with Recommendations(teardown=False) as bot:

        bot.landYOUTUBE()

        time.sleep(2)

        finalResult = bot.getNBARecommendations()

        # bot.download_csv_report()

        bot.sendingMail(data=finalResult)


except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '   set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '   PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
