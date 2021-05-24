from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_title(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url"))
    wait = WebDriverWait(browser, 5, poll_frequency=0.5)
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/head/title")))
    assert browser.title == "Your Store"


def test_main_page(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url"))
    wait = WebDriverWait(browser, 2, poll_frequency=0.5)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))

    main_search_group = browser.find_element_by_css_selector(".input-group:first-child")
    main_search_group.find_element_by_css_selector("[type=text]")
    main_search_group.find_element_by_css_selector("[type=button]")

    browser.find_element_by_css_selector(".swiper-viewport:first-child")


def test_catalog_desktops(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url") + "/index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 2, poll_frequency=0.5)

    catalog_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-category")))

    catalog_container.find_element_by_css_selector(".breadcrumb")
    catalog_container.find_element_by_css_selector(".list-group")
    catalog_container.find_elements_by_css_selector(".product-thumb")

    browser.find_element_by_css_selector("footer")


def test_product_page(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url") + "/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 2, poll_frequency=0.5)

    product_area = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-product")))
    product_area.find_element_by_css_selector(".thumbnail [title]")
    product_area.find_element_by_css_selector(".tab-content")
    product_area.find_element_by_css_selector(".rating")
    product_area.find_element_by_css_selector("#button-cart")


def test_customer_login_page(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url") + "/index.php?route=account/login")
    wait = WebDriverWait(browser, 2, poll_frequency=0.5)

    login_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#account-login")))

    new_customer, returning_customer = login_container.find_elements_by_css_selector(".col-sm-6")

    new_customer.find_elements_by_css_selector(".btn.btn-primary")
    returning_customer.find_elements_by_css_selector("#input-email")
    returning_customer.find_elements_by_css_selector("#input-password")


def test_admin_login_page(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url") + "/admin/")
    wait = WebDriverWait(browser, 2, poll_frequency=0.5)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-logo.navbar-header")))

    login_panel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel.panel-default")))
    login_panel.find_element_by_css_selector(".panel-title")

    username_form, password_form = login_panel.find_elements_by_css_selector(".form-group")
    username_form.find_elements_by_css_selector("#input-username")
    password_form.find_elements_by_css_selector("#input-password")
