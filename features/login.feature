Feature: Jules login features

    @login
   Scenario: Login with valid credentials
      Given Sign in: I navigate to sign in page
      When Sign in: I write my email
      When Sign in: I write my password
      Then menu: I am a user on search page

