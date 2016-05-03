# -*- coding: utf-8 -*-

import os
import sys
import glob
try:
    import json
except ImportError:
    import simplejson as json


class BrowserCookieError(Exception):
    pass


class Chrome:
    def __init__(self, cookie_file=None):
        if sys.platform == 'darwin':
            self.cookie_file = cookie_file or os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Cookies')

        elif sys.platform.startswith('linux'):
            self.cookie_file = cookie_file or os.path.expanduser('~/.config/google-chrome/Default/Cookies') or \
                                         os.path.expanduser('~/.config/chromium/Default/Cookies')
        elif sys.platform == 'win32':
            self.cookie_file = cookie_file or os.path.join(os.getenv('APPDATA', ''), '..\Local\Google\Chrome\User Data\Default\Cookies')
        else:
            raise BrowserCookieError('Unsupported operating system: ' + sys.platform)

    def run(self):
        return self.cookie_file
    # def __str__(self):
    #     return 'chrome'


class Firefox:
    def __init__(self, cookie_file=None):
        self.cookie_file = cookie_file or self.find_cookie_file()
        # current sessions are saved in sessionstore.js

    def find_cookie_file(self):
        if sys.platform == 'darwin':
            cookie_files = glob.glob(os.path.expanduser('~/Library/Application Support/Firefox/Profiles/*.default/cookies.sqlite'))
        elif sys.platform.startswith('linux'):
            cookie_files = glob.glob(os.path.expanduser('~/.mozilla/firefox/*.default*/cookies.sqlite'))
        elif sys.platform == 'win32':
            cookie_files = glob.glob(os.path.join(os.getenv('PROGRAMFILES', ''), 'Mozilla Firefox/profile/cookies.sqlite')) or \
                           glob.glob(os.path.join(os.getenv('PROGRAMFILES(X86)', ''), 'Mozilla Firefox/profile/cookies.sqlite')) or \
                           glob.glob(os.path.join(os.getenv('APPDATA', ''), 'Mozilla/Firefox/Profiles/*.default/cookies.sqlite'))
        else:
            raise BrowserCookieError('Unsupported operating system: ' + sys.platform)
        if cookie_files:
            return cookie_files[0]
        else:
            raise BrowserCookieError('Failed to find Firefox cookie')

    def run(self):
        return self.find_cookie_file()


def chrome(cookie_file=None):
    """Returns a cookiejar of the cookies used by Chrome
    """
    return Chrome(cookie_file)


def firefox(cookie_file=None):
    """Returns a cookiejar of the cookies and sessions used by Firefox
    """
    return Firefox(cookie_file)

