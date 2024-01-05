Feature: User Story Get_Latest_Requirements_From_Button_On_Output_Page
    As a user of the stakeholder requirement retrieval app
    I want to view the latest stakeholder requirements for a major
    So that I can stay updated on the current requirements

  Feature: Get latest requirements from button on the output page

    Scenario: User clicks on "see new version" button to get the latest requirements
        Given I am on "/history/major"
        When I press "Electrical Engineering" 
        And I see "last updated date"
        And I press "see new version"
        Then I should see "the latest stakeholder requirements" in the output page
        And the current date of requirement terms is newer than the previous one