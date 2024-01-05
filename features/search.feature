Feature: Get Stakeholder Requirements From Database Through Search Bar
    In order to understand what skills I should have to keep up with the industries
    As a Fresh graduate from university 
    I want to get the stakeholder requirements for a major by finding it on search bar

    Scenario: User gets the stakeholder requirements from the database based on the user major input
        Given I am on "/search"
        When I fill in "Information Systems" for "input-box"
        And I press enter
        Then I should be on "output page" with the url should match "/history/getByHistory/"
        And I should see "Information Systems" in the "major_name_output" element

    Scenario: User submits an invalid major and sees an error popup
        Given I am on "/search"
        When I fill in "yessirrr" for "input-box"
        And I press enter
        Then I should see "Your input is not on the list of majors. Please input a valid major." as an error in the "swal2-html-container" element

    Scenario: User submits major that has not been scraped and sees an error popup
        Given I am on "/search"
        When I fill in "Dental Engineering" for "input-box"
        And I press enter
        Then I should see "No history found for the specified major. Please input the major in the search field." as an error in the "swal2-html-container" element
