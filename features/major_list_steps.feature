Feature: Get Stakeholder Requirements From Database Through Major List
    As a user of the stakeholder requirement retrieval app
    I want to get the stakeholder requirements for a major by clicking on the list of existing major 
    So that I can understand what skills I should improve to keep up with the industries

Scenario: Successfully Obtaining Relevant Skills for the Chosen Major from the List
    Given I am on the Major List Page
    When I click a "English Language and Literature" from the provided list
    Then I see a display of skills that are relevant to the "English Language and Literature" major

Scenario: Failed Obtaining Relevant Skills for the Chosen Major from the List
    Given I am on the Major List Page
    When I click a "Antropology" from the provided list
    Then I should see an error popup with the message "Your input is not on the list of majors. Please input a valid major."


