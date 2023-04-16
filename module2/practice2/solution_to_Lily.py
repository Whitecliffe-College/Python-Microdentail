import requests
import re

def save_website_title(url, filename):
    """grab the title of a website and save it to a file
    :return: True if success, False otherwise
    """
    try:
        resp = requests.get(url)
    except RequestException as e:
        print(f'save failed: unable to get page content: {e}')
        return False

    # below code doesn't need to be in try block
    # because even if it throws an exception, it will be caught by AttributeError
    obj = re.search(r'<title>(.*)</title>', resp.text)
    if not obj:
        print('save failed: title tag not found in page content')
        return False
    title = obj.group(1)

    try:
        with open(filename, 'w') as fp:
            fp.write(title)
    except IOError as e:
        print(f'save failed: unable to write to file {filename}: {e}')
        return False
    else:
        return True