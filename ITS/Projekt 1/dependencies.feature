Feature: Admin account manipulating with Use Case dependencies

Background:
Given Admin is logged in
And Use Case exists

Scenario: Deleting Use Case with dependencies
Given Use Case has Evaluation Scenarios
And Use Case page is open
When Use Case is deleted
Then it is no longer available
And elements under this Use Case are deleted
And these elements are not available to other Use Cases

Scenario: Deleting specific Evaluation Scenarios
Given Use Case has Evaluation Scenarios
And an Evaluation Scenario is open
When this scenario is deleted
Then it is not available to this or other Use Case
And all Requirements and Test Cases tied to it are deleted

Scenario: Deleting Requirement from Use Case
Given Use Case has Evaluation Scenarios with Requirements
And this Requirement is in Use Case Contents
When the Requirement is deleted through the Contents list
Then it is not available there
And it is not available in the Evaluation Scenarios it belonged to

Scenario: Organisation is Deleted
Given Use Case has a Partner listed
And page of this Organisation is open
When the Organisation is deleted
Then it no longer exists
And the partnership is no longer listed

Scenario: Deleting Test Case
Given a Test Case exists
And it is linked to a Method and Requirement
When it is deleted
Then it is no longer available
And its' links in the Method and Requirement are deleted