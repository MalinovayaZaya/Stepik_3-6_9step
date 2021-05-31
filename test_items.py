import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_add_to_cart_button_without_assert(browser):
    browser.get(link)
    # time.sleep(30)  # при необходимости можно раскоментить :В

    cart = None
    try:
        cart = browser.find_element_by_css_selector("button.btn-add-to-basket")
    except:
        assert cart != None, 'No such elements on page'
