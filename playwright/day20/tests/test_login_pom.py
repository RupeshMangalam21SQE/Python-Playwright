from pages.login_page import LoginPage

def test_login_pom(page):  # 'page' is provided automatically
    # Create LoginPage object
    login_page = LoginPage(page)

    # Navigate to login
    login_page.navigate("https://the-internet.herokuapp.com/login")

    # Login and move to HomePage
    home_page = login_page.login("tomsmith", "SuperSecretPassword!")

    # Verify welcome message
    home_page.verify_welcome_message("You logged into a secure area!")
