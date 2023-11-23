Feature: Jules search features

   Background:
      Given Sign in: I navigate to sign in page
      When Sign in: I write my email
      When Sign in: I write my password
      When Menu: I am a user on search page

   @search
   Scenario: I search for added property
      When Menu: I type in search field "test"
      Then Menu: I select item "test1"

