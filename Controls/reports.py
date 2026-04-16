import Constants
import os


def create_report(report_name: str, content: str):
    path_to_file = Constants.REPORT_PATH + report_name
    if not os.path.exists(Constants.REPORT_PATH):
        os.mkdir(Constants.REPORT_PATH)

    with open(path_to_file, 'w+') as f:
        f.write(content)
    return
