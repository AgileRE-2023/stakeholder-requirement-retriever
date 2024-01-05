Feature: User Story Get Latest Requirements From Button On Output Page
    In order to understand what skills I should have to keep up with the industries
    As a Fresh graduate from university 
    I want to get the latest stakeholder requirements for a major by clicking on the see new version button

    Scenario: User clicks on "see new version" button to get the latest requirements
        Given I am on "/history/major"
        When I select "Information System" 
        And I see "last updated date"
        And I press "see new version"
        Then I should see "the latest stakeholder requirements" in the output page
        And the current date of requirement terms is newer than the previous one