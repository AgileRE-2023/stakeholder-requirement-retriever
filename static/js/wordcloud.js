let words = [
    {word: "skill-1", quantity: 95},
    {word: "skill-2", quantity: 85},
    {word: "skill-3", quantity: 75},
    {word: "skill-4", quantity: 65},
    {word: "skill-5", quantity: 60},
    {word: "skill-6", quantity: 55},
    {word: "skill-7", quantity: 45},
    {word: "skill-8", quantity: 35},
    {word: "skill-9", quantity: 19},
    {word: "skill-10", quantity: 10},
   
];

let colors = ["#4169E1","#6941e1", "#b9e141","#e141b9", "#41e169", "#dbc970", "#b98e68", "	#af4035", "#88d8c0" ];

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
            text :word.word,
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
    .style("fill", (d, i)=>{
        return colors[i % colors.length];
    })
    .attr("text-anchor", "middle")
    .attr("transform", (d)=>`translate(${[d.x, d.y]})rotate(${d.rotate})`)
    .text((d) => d.text);
}

console.log(words);