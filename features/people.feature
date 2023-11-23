Feature: Jules people feature

   Background:
      Given Sign in: I navigate to sign in page
      When Sign in: I write my email
      When Sign in: I write my password
      When Menu: I am a user on search page


       @edit
   Scenario: I search for a person and I edit it
      When Menu: I click on people page
      When People page: I search for name "Mary"
      When People Page: I click on last name "Davis"
      When People page: I click edit button
      When People Page: I set middle name "Joe"
      When People Page: I set last name "Biden"
      When People Page: I click save button
      Then People Page: I verify success message

      @delete1
   Scenario: I want to delete one person
      When Menu: I click on people page
      When People page: I search for name "Mary"
      When People Page: I click on last name "Smith"
      When People Page: I click on ellipsis button
      When People page: I click delete person
      When People Page: I verify warning message
      When People Page: I confirm delete
      Then People Page: I verify success message

       @delete2
   Scenario: I want to delete multiple people
      When Menu: I click on people page
      When People page: I search for name "Jenner"
      When People Page: I click select all
      When People page: I click delete
      When People Page: I verify warning message
      When People Page: I confirm delete
      Then People Page: I verify success message