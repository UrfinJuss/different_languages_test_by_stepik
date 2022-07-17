from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button(browser):
    browser.get(link)
    browser.implicitly_wait(30)
    ans = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert ans.is_displayed(), 'Sorry, you cant'
