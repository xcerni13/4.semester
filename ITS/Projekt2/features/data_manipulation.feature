Feature: Admin account manipulating with Use Case data

Scenario: Use can log in
Given User is logged out
When User logs in
Then User can look at all content

Scenario: Create Use Case
Given Use cases home page open
When a new Use Case is created
Then it is visible on the page

Scenario: Delete Use Case
Given a Use Case is available
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



