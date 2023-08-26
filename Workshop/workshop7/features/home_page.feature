Feature: Home Page verification


  Scenario: Navigate to website
    Given I introduce website url adress in browser
    When I press ENTER
    Then Home Page is displayed "https://automationexercise.com/"

  Scenario: Carousel page element is displayed
    Given I am on the Home Page
    When Page is loaded
    Then Carousel page element is displayed



