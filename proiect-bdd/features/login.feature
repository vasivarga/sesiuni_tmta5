Feature: Login Page

  Background: Open login page
  Given I am on the Login Page

  # Scenariul 1 fara parametru
  Scenario: Log in with unregistered email
    When I enter an unregistered email
    When I enter a password
    When I click the Login button
    Then I should see "No customer account found" message

  # Scenariul 1 cu parametru
  Scenario: Log in with unregistered email (with param)
    When I enter "tmta5@itfactory.ro" in the email input
    When I enter "alabalaportocala" in the password input
    When I click the Login button
    Then I should see "No customer account found" message

  # Scenariul 1 cu alt parametru
  Scenario: Log in with unregistered email (with param)
    When I enter "tmta6@itfactory.ro" in the email input
    When I enter "lalala" in the password input
    When I click the Login button
    Then I should see "No customer account found" message

  # Scenariul 1 cu alt parametru
  Scenario: Log in with unregistered email (with param)
    When I enter "tmta7@itfactory.ro" in the email input
    When I enter "parolagrea" in the password input
    When I click the Login button
    Then I should see "No customer account found" message

  @regression
  Scenario: Log in with empty email
    When I click the Login button
    Then I should see "Please enter your email" error message

  @regression @smoke
  # Invalid email cu click pe login button
  Scenario: Validate invalid email format
    When I enter "tmta5_email" in the email input
    When I click the Login button
    Then I should see "Wrong email" error message

  # Invalid email cu defocusare prin apasarea tastei TAB
  @interes @smoke @regression
  Scenario: Validate invalid email format
    When I enter "tmta5_email" in the email input
    When I defocus from the email input
    Then I should see "Wrong email" error message

  @interes
  Scenario: Check that the URL is correct
    Then The URL of the page is "https://demo.nopcommerce.com/login"