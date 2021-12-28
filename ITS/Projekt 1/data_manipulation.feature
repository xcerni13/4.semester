Feature: Admin account manipulating with Use Case data

Background:
Given Admin is logged in

Scenario: Create Use Case
Given Use cases home page open
When a new Use Case is created
Then it is visible on the page

Scenario: Delete Use Case
Given a Use Case is available
And Use Case to be deleted is open
When use Actions Delete
Then Use Case is no longer available

Scenario: Add Evaluation Scenario to Use Case
Given Use cases home page open
When a new Evaluation Scenario is created
Then it is possible to open and edit it

Scenario: Add Requirement
Given Use cases home page open
When a Requirement is created
Then it is available on the home page

Scenario: Add Requirement to an Evaluation Scenario
Given a Use Case with an Evaluation Scenario exists
And specific Use Case page is open
When a Requirement is created
And it is added to the Evaluation Scenarios List
Then it is available in the List
And it is available on the Use Case's page

Scenario: Add Test Case to a Requirement
Given Requirement exists
And its' page is open
When a Test Case is created
And it is added to Requirement's Test Cases list
Then it is visible in the list and on the page

