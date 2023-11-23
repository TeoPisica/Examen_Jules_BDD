Feature: Jules add person features

   Background:
      Given Sign in: I navigate to sign in page
      When Sign in: I write my email
      When Sign in: I write my password
      When Menu: I am a user on search page

   @person
   Scenario: Login and add new person
      When Menu: I click on add page
      When Add page: I click on the person button
      When Add person page: I set first name "John"
      When Add person page: I set last name "Smith"
      When Add person page: I click save
      When Add person page: I verify success message
      Then Add person page: I click finish button

