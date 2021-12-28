Feature: Admin account manipulating with Use Case dependencies

Background:
Given Admin is logged in
And Use Case exists

Scenario: Deleting Use Case with dependencies
Given Use Case has Evaluation Scenarios
And Use Case page is open
When Use Case is deleted
Then it is no longer available


Scenario: Deleting specific Evaluation Scenarios
Given Use Case has Evaluation Scenarios
And an Evaluation Scenario is open
When this scenario is deleted
Then it is not available to this or other Use Case



