Feature: User Login
  As a user
  I want to log in with valid credentials
  So that I can access the secure area

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "tomsmith" and password "SuperSecretPassword!"
    And I submit the login form
    Then I should see the welcome message "You logged into a secure area!"

  Scenario Outline: Login with different user types
    Given I am on the login page
    When I enter username "<username>" and password "<password>"
    And I submit the login form
    Then I should see the message "<expected_message>"

    Examples: Valid and invalid users
      | username   | password             | expected_message                  |
      | tomsmith   | SuperSecretPassword! | You logged into a secure area!    |
      | invalid    | wrongpass            | Your username is invalid!         |
      | tomsmith   | wrongpass            | Your password is invalid!         |
