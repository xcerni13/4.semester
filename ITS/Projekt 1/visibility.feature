Feature: Admin account manipulating with Use Case dependencies

Background:
Given Admin is logged in
And Use Case exists
And Requirement which are each covered by a Test Case exist

Scenario: Make Use Case public
Given Use Case is private
And home page of the use case is open
When it is published
Then any user can see this Use Case

Scenario: Make Use Case private
Given Use Case is public for all users
When Use Case is made private
Then it is visible to admin and not to other users

Scenario: Make a Requirement private
Given Use Case is public
And it has some Requirement
When the Requirement is made private
Then it is no longer visible to non-admin users
And the Use Case is visible
And its public Requirements are visible

Scenario: Make a Tool public
Given Tool is private
When it is made public
Then it is available to non-admin users

Scenario: Delete a public Method
Given Method is public
When it is Deleted
Then it is no longer available for any user