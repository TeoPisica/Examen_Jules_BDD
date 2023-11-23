Feature: Sign up feature

  Background:
    Given Sign in: I navigate to sign in page

  @smoke
  Scenario Outline: Validate error message for invalid email
    When Sign in: I click on sign up link
    When Sign up: I select personal option
    When Sign up: I complete first and last name inputs
    When Sign up: I complete email input "<email>"
    Then Sign up: I validate error message is as expected "Please enter a valid email address."

    Examples:
    | email       |
    | noemail.com |
    | itfactory   |


    @smoke
  Scenario: Validate error message for existing email
    When Sign in: I click on sign up link
    When Sign up: I select personal option
    When Sign up: I complete first and last name inputs
    When Sign up: I complete email input "p.iuuliana@gmail.com"
    Then Sign up: I validate error message is as expected "e-mail address is already in use"





