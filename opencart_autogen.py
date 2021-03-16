from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to http://opencart.abstracta.us/
    page.goto("http://opencart.abstracta.us/")
    # Click [placeholder="Search"]
    page.click("[placeholder=\"Search\"]")
    # Fill [placeholder="Search"]
    page.fill("[placeholder=\"Search\"]", "iphone")
    # Click text=Your Store 0 item(s) - $0.00 Your shopping cart is empty! >> button
    page.click("text=Your Store 0 item(s) - $0.00 Your shopping cart is empty! >> button")
    # assert page.url == "http://opencart.abstracta.us/index.php?route=product/search&search=iphone"
    # Click a:has-text("iPhone")
    page.click("a:has-text(\"iPhone\")")
    # assert page.url == "http://opencart.abstracta.us/index.php?route=product/product&product_id=40&search=iphone"
    # Click text=Add to Cart
    page.click("text=Add to Cart")
    # Click button:has-text("1 item(s) - $123.20")
    page.click("button:has-text(\"1 item(s) - $123.20\")")
    # Click text=View Cart
    page.click("text=View Cart")
    # assert page.url == "http://opencart.abstracta.us/index.php?route=checkout/cart"
    # ---------------------
    context.close()
    browser.close()
    
with sync_playwright() as playwright:
    run(playwright)

