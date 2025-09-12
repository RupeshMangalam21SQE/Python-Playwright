Feature: E-Commerce End-to-End Workflow
  As a shopper
  I want to search, add items to cart, and checkout
  So that I can complete a purchase

  Scenario Outline: Search, add to cart, and verify during checkout
    Given I am logged in to the e-commerce site
    When I search for the product "<product_name>"
    And I add the product "<product_name>" to the cart
    And I proceed to the cart
    And I start checkout
    Then I should see the product "<product_name>" in the checkout summary

    Examples:
      | product_name         |
      | Sauce Labs Backpack  |
      | Sauce Labs Bike Light|
      | Invalid Product      |
