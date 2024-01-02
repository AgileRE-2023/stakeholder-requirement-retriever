Feature: User Story See New Version of Stakeholder Requirement
    As a user of the stakeholder requirement retrieval app
    I want to get the latest stakeholder requirements for a major
    So that I can understand what skills I should improve to keep up with the industries

  Feature: Get the stakeholder requirements from the database based on the user major input

    Scenario: User gets the stakeholder requirements from the database based on the user major input
        Given the user is on the search page
        When the user submits the form with "Information Systems" as an input value
        Then the user should see stakeholder requirements of "Information Systems" in the output page

    Scenario: User submits an invalid major and sees an error popup
        Given the user is on the search page
        When the user submits the form with "yessir" as an input value
        Then the user should see an error popup with the message "Your input is not on the list of majors. Please input a valid major."

    Scenario: User submits major that has not been scraped and sees an error popup
        Given the user is on the search page
        When the user submits the form with "Mathematics" as an input value
        Then the user should see an error popup with the message "No history found for the specified major. Please input the major in the search field."