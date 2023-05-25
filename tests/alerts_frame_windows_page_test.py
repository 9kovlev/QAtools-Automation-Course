from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindow:

    class TestBrowserWindow:
        def test_new_tab(self, driver):
            browser_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_window_page.open()
            result = browser_window_page.check_opened_new_tab()
            assert result == 'This is a sample page', "The new tab has not been opened "

        def test_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_window_page.open()
            result = browser_window_page.check_opened_new_tab()
            assert result == 'This is a sample page', "The new tab has not been opened "

