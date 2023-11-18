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

  document.getElementById("input-box").addEventListener("input", function () {
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

  document
    .getElementById("input-box")
    .addEventListener("keydown", function (event) {
      if (event.key === "Enter") {
        event.preventDefault(); // Preventing the default action of the "Enter" button
        showNotification(
          "Please select a major from the recommendation list below."
        );
      }
    });

  function displayResults(results) {
    var resultList = document.getElementById("result-list");
    resultList.innerHTML = "";

    results.forEach(function (result) {
      var listItem = document.createElement("li");
      var link = document.createElement("a");
      link.href = result.replace(/\s+/g, "-").toLowerCase();
      link.textContent = result;
      listItem.appendChild(link);
      resultList.appendChild(listItem);
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
    alert(message);
  }
});
