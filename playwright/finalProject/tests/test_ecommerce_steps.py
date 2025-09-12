from pytest_bdd import given, when, then, scenarios, parsers
from pages.login_page import LoginPage

scenarios("features/ecommerce_workflow.feature")


@given('I am logged in to the e-commerce site', target_fixture='inventory_page')
async def login_to_site(page):
    login_page = LoginPage(page)
    await login_page.navigate("https://www.saucedemo.com/")
    return await login_page.login("standard_user", "secret_sauce")


@when(parsers.parse('I search for the product "{product_name}"'))
async def search_product(inventory_page, product_name):
    await inventory_page.search_for_product(product_name)


@when(parsers.parse('I add the product "{product_name}" to the cart'))
async def add_to_cart(inventory_page, product_name):
    await inventory_page.add_product_to_cart(product_name)


@when('I proceed to the cart', target_fixture='cart_page')
async def go_to_cart(inventory_page):
    return await inventory_page.go_to_cart()


@when('I start checkout', target_fixture='checkout_page')
async def start_checkout(cart_page):
    return await cart_page.proceed_to_checkout()


@then(parsers.parse('I should see the product "{product_name}" in the checkout summary'))
async def verify_in_summary(checkout_page, product_name):
    await checkout_page.verify_item_in_summary(product_name)
