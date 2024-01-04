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
        event.preventDefault();
        searchForm.submit();
    });

    
  inputBox.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
      // Prevent the default behavior (form submission)
      event.preventDefault();
      searchForm.submit();
    }
  });

  inputBox.addEventListener("click", function () {
    var inputValue = this.value.trim().toLowerCase();
    var matchingResults = majors.filter(function (major) {
      return major.toLowerCase().includes(inputValue);
    });
  
    displayResults(matchingResults);
  });


    inputBox.addEventListener("input", function () {
      resetButton.style.display = inputBox.value.trim() !== '' ? 'block' : 'none';
      var query = this.value.trim().toLowerCase();
      
      // Filter majors that start with the query
      var matches = majors.filter(function (major) {
        return major.toLowerCase().startsWith(query);
      });
    
      displayResults(matches);
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
    
    results.sort();

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

});
