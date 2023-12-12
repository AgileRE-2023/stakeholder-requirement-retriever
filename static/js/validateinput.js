var inputBox = document.getElementById("input-box");
var searchForm = document.getElementById("search-form");
var resetButton = document.getElementById("reset-button");

// Optional: Hide the reset button initially
resetButton.style.display = 'none';

function convertStringToArray(stringArray) {
  const replacedString = stringArray.replace(/'/g, '"');
  return JSON.parse(replacedString);
}
document.addEventListener("DOMContentLoaded", function () {
  const listMajor = document.querySelector("#prodiList")
  if (listMajor) {
    console.log(listMajor.value)
    var majors = convertStringToArray(listMajor.value)
  } else {
    var majors = []
  }

  var searchButton = document.getElementById("search-button");
    searchButton.addEventListener("click", function (event) {
        // Prevent the default button behavior (page reload)
        event.preventDefault();
        // Validate the input value before submitting the form
        var inputValue = inputBox.value;
        if (inputValue && majors.includes(inputValue)) {
        // Input is not empty and matches a major, submit the form
        searchForm.submit();
        } else {
        // Display an error message
        showNotification("No history found for the specified major. Please input the major in the search field.");
        }
    });

    

  inputBox.addEventListener("input", function () {
    resetButton.style.display = inputBox.value.trim() !== '' ? 'block' : 'none';
    var query = this.value.toLowerCase();
    var matches = majors.filter(function (major) {
      // Split the major into words
      var words = major.toLowerCase().split(" ");

      // Check if any word or the major itself matches the query
      return words.some(function (word) {
        return word.startsWith(query) || major.toLowerCase().startsWith(query);
      });
    });

    displayResults(matches);
  });

  inputBox.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      // Prevent the default behavior (form submission)
      event.preventDefault();
      // Validate the input value before submitting the form
      var inputValue = inputBox.value;
      if (inputValue && majors.includes(inputValue)) {
        // Input is not empty and matches a major, submit the form
        searchForm.submit();
      } else {
        // Display an error message
        showNotification("No history found for the specified major. Please input the major in the search field.")
      }
    }
  });

  

  function displayResults(results) {
    var resultList = document.getElementById("result-list");
    resultList.innerHTML = "";

    resetButton.addEventListener("click", function () {
      // Set the selected result as the value of the input-box
      resetButton.style.display = 'none';
      resultList.innerHTML = "";
      inputBox.value = "";
  
    });

    results.forEach(function (result) {
      var listItem = document.createElement("li");
      var link = document.createElement("li");
      link.textContent = result;
      listItem.appendChild(link);
      resultList.appendChild(listItem);

      // Add click event listener to each link
      link.addEventListener("click", function () {
        // Set the selected result as the value of the input-box
        inputBox.value = result;
      });
      
    });

    if (results.length === 0) {
      var noResultItem = document.createElement("p");
      noResultItem.textContent = "No matching majors found.";
      noResultItem.style.padding = "10px 70px";
      resultList.appendChild(noResultItem);
    }
  }

  function showNotification(message) {
    // Displaying a notification from preventing the default action of the "Enter" button
    Swal.fire({
      icon: 'error',
      title: 'Error!',
      text: message,
  });
  }
});
