Feature: Get Stakeholder Requirements From Database Through Major List
    In order to understand what skills I should have to keep up with the industries
    As a Fresh graduate from university 
    I want to get the stakeholder requirements for a major by clicking on the list of existing 

Scenario: Successfully Obtaining Relevant Skills for the Chosen Major from the List
    Given I am in in "/history/major"
    When I select "English Language and Literature" from "form_major"
    And I press "Click"
    Then I should be on "output page" with the url should match "/history/getByHistory/"
    And I should see "English Language and Literature" in the "major_name_output" element

Scenario: Failed Obtaining Relevant Skills for the Chosen Major from the List
    Given I am on "/history/major"
    When I select "Antropology" from the provided list from "form_major"
    And I press "Click"
    Then I should be on "output page" with the url should match "/history/getByHistory/"
    And I should see "Your input is not on the list of majors. Please input a valid major."
    And I should be on "search page" with the url should match "/search"


