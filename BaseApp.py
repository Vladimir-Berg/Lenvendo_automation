class BaseApp:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://HR:test@qa.digift.ru'

    def open_base_page(self):
        wd = self.driver
        wd.get(self.base_url)
        wd.set_window_size(1289, 817)
