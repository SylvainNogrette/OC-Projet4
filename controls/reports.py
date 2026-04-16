import constants
import os


def create_report(report_name: str, content: str):
    path_to_file = constants.REPORT_PATH + report_name
    if not os.path.exists(constants.REPORT_PATH):
        os.mkdir(constants.REPORT_PATH)

    with open(path_to_file, 'w+') as f:
        f.write(content)
    return
