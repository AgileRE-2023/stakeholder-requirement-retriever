document.addEventListener("DOMContentLoaded", function () {
    var majors = [
      "Kebidanan",
      "Kedokteran",
      "Ilmu Hukum",
      "Akuntansi",
      "Manajemen",
      "Ekonomi Pembangunan",
      "Ekonomi Islam",
      "Farmasi",
      "Kedokteran Hewan",
      "Sosiologi",
      "Ilmu Komunikasi",
      "Ilmu Hubungan Internasional",
      "Ilmu Administrasi",
      "Antropologi",
      "Ilmu Informasi dan Perpustakaan",
      "Ilmu Politik",
      "Matematika",
      "Sistem Informasi",
      "Statistika",
      "Fisika",
      "Teknik Biomedis",
      "Kimia",
      "Biologi",
      "Teknik Lingkungan",
      "Kesehatan Masyarakat",
      "Ilmu Gizi",
      "Psikologi",
      "Ilmu Sejarah",
      "Sastra Jepang",
      "Sastra Indonesia",
      "Sastra Inggris",
      "Keperawatan",
      "Akuakultur",
      "Teknologi Hasil Perikanan",
      "Teknik Robotika dan Kecerdasan Buatan",
      "Teknik Elektro",
      "Teknik Industri",
      "Rekayasa Nano Teknologi",
      "Teknologi Sains Data",
    ];

    var inputBox = document.getElementById("input-box");
    var searchForm = document.getElementById("search-form");
    var resetButton = document.getElementById("reset-button");

    // Optional: Hide the reset button initially
    resetButton.style.display = 'none';
  
    inputBox.addEventListener("input", function () {
        // Toggle the visibility of the reset button based on the input value
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
        showNotification("Use the right spelling!");
        }
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
            showNotification("Use the right spelling!")
          }
        }
      });

      function displayResults(results) {
        var resultList = document.getElementById("result-list");
        resultList.innerHTML = "";
    
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

        if (results.length === 0 || !currentQuery) {
            // Display an error message
            displayError("No matching majors found.");
          }
        }
      
        function displayError(message) {
          var resultList = document.getElementById("result-list");
          var errorItem = document.createElement("p");
          errorItem.textContent = message;
          errorItem.style.padding = "10px 70px";
          resultList.appendChild(errorItem);
        }
      
  
    function showNotification(message) {
      // Displaying a notification from preventing the default action of the "Enter" button
      alert(message);
    }
  });