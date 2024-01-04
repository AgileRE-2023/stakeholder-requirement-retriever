Feature: Get latest requirements from button on the output page

    Scenario: User clicks on "see new version" button to get the latest requirements
        Given the user is on the major list page
        When the user clicks "Electrical Engineering"
        And the user sees the last updated date
        And the user clicks on the "see new version" button
        Then the user should see the latest stakeholder requirements in the output page by knowing that current date of requirement terms is newer than the previous one