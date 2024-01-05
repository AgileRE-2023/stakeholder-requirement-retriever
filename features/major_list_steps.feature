Feature: Get Stakeholder Requirements From Database Through Major List
    In order to understand what skills I should have to keep up with the industries
    As a Fresh graduate from university 
    I want to get the stakeholder requirements for a major by clicking on the list of existing 

Scenario: Successfully Obtaining Relevant Skills for the Chosen Major from the List
    Given I am on "/history/major"
    When I select "English Language and Literature"
    Then I should be on "output page" with the url should match "/history/getByHistory/"
    And I should see "English Language and Literature" in the "major_name_output" element

Scenario: Failed Obtaining Relevant Skills for the Chosen Major from the List
    Given I am on "/history/major"
    When I select "Dental Engineering"
    Then I should be on "output page" with the url should match "/history/getByHistory/"
    And I should see "No history found for the specified major. Please input the major in the search field." as an error in the "swal2-html-container" element



