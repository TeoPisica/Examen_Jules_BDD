Feature: Jules add property features

   Background: Scenario: Login and add new person
      Given Sign in: I navigate to sign in page
      When Sign in: I write my email
      When Sign in: I write my password
      When Menu: I am a user on search page

    @add
   Scenario: Add new property
      When Menu: I click on add page
      When Add page: I click on the property button
      When Add property page: I set property name "test1"
      When Add property page: I click the continue button
      When Add property page: I fill property parcel number "12345"
      When Add property page: I fill property address "test address"
      When Add property page: I click save button
      When Add property page: I verify success message
      Then Add property page: I click finish button