document.addEventListener("DOMContentLoaded", function () {
  var termsAndScore = document.querySelectorAll(".scoreHidden");
  var words = [];

  // Find the minimum and maximum quantity values
  const minQuantity = Math.min(
    ...Array.from(termsAndScore, (element) =>
      parseFloat(element.value.split("_")[1])
    )
  );
  const maxQuantity = Math.max(
    ...Array.from(termsAndScore, (element) =>
      parseFloat(element.value.split("_")[1])
    )
  );

  termsAndScore.forEach((element) => {
    const word = element.value.split("_")[0];
    const quantity = parseFloat(element.value.split("_")[1]);

    // Convert quantity to the 0-100 range using linear scaling
    const scaledQuantity =
      ((quantity - minQuantity) / (maxQuantity - minQuantity)) * (100 - 0) + 0;

    // Create an object and push it into the words array
    words.push({ word: word, quantity: scaledQuantity });
  });

  console.log(words); // or do something else with the words array

  // Function to generate a random color
  function getRandomColor() {
    const letters = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  const width = 500;
  const height = 450;

  const svg = d3
    .select("section")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  const layout = d3.layout
    .cloud()
    .size([width, height])
    .words(
      words.map((word) => ({
        text: word.word,
        size: word.quantity * 1,
      }))
    )
    .padding(2)
    .rotate(0)
    .fontSize((d) => d.size)
    .spiral("rectangular")
    .on("end", draw);

  layout.start();

  function draw(words) {
    svg.selectAll("*").remove();

    svg
      .append("g")
      .attr("transform", `translate(${width / 2}, ${height / 2})`)
      .selectAll("text")
      .data(words)
      .enter()
      .append("text")
      .style("font-size", (d) => d.size + "px")
      .style("fill", () => getRandomColor())
      .attr("text-anchor", "middle")
      .attr("transform", (d) => `translate(${[d.x, d.y]})rotate(${d.rotate})`)
      .text((d) => d.text);
  }

  console.log(words);
});
