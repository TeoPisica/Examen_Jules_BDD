Feature: Forgot password feature

  @test
  Scenario: Validate error message for wrong email
    Given Sign in: I navigate to sign in page
    When Sign in: I click on forgot password button
    When Forgot pass: I write my email "noemail.com"
    Then Forgot pass: I validate that send email button is NOT enabled




     @test
  Scenario: Validation message for valid email
    Given Sign in: I navigate to sign in page
    When Sign in: I click on forgot password button
    When Forgot pass: I write my email "p.iuuliana@gmail.com"
    Then Forgot pass: I validate that send email button is enabled

