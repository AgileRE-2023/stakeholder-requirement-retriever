Feature: User Story Get_Stakeholder_Requirements_From_Database_In_Search_Page
    As a user of the stakeholder requirement retrieval app
    I want to get the stakeholder requirements for a major
    So that I can understand what skills I should improve to keep up with the industries

  Feature: Get the stakeholder requirements from the database based on the user major input

    Scenario: User gets the stakeholder requirements from the database based on the user major input
        Given the user is on the search page with path of "/search"
        When the user type "Information Systems" as a value for input tag with id of "input-box"
        And the user press enter to submit the form that have the input tag with id of "input-box"
        Then the user should be on the output page with the path of "/history/getByHistory/"
        Then the user should see stakeholder requirements of "Information Systems" in the div with id of "major_name_output"

    Scenario: User submits an invalid major and sees an error popup
        Given the user is on the search page with path of "/search"
        When the user type "yessirrr" as a value for input tag with id of "input-box"
        And the user press enter to submit the form that have the input tag with id of "input-box"
        Then the user should see an error popup with the message "Your input is not on the list of majors. Please input a valid major." in the div with id of "swal2-html-container"

    Scenario: User submits major that has not been scraped and sees an error popup
        Given the user is on the search page with path of "/search"
        When the user type "Dental Engineering" as a value for input tag with id of "input-box"
        And the user press enter to submit the form that have the input tag with id of "input-box"
        Then the user should see an error popup with the message "No history found for the specified major. Please input the major in the search field." in the div with id of "swal2-html-container"