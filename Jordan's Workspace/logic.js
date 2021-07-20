// var link = "tweets_csvs/tweets.json";

// Chart Params
var svgWidth = 960;
var svgHeight = 500;

var margin = { top: 20, right: 40, bottom: 60, left: 50 };

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3
  .select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import data from an external CSV file
d3.csv("../tweet_csvs/super.csv").then(function(tweetData) {
  console.log(tweetData);
//   console.log([tweetData]);

  // Create a function to parse date and time
  var parseTime = d3.timeParse("%d-%b-%Y");

  // Format the data
  tweetData.forEach(function(data) {
    data.date = parseTime(data.date);
    data.sentiment = +data.sentiment;
  });

  // Create scaling functions
  var xTimeScale = d3.scaleTime()
    .domain(d3.extent(tweetData, d => d.date))
    .range([0, width]);

  var yLinearScale = d3.scaleLinear()
    .domain([0, d3.max(tweetData, d => d.sentiment)])
    .range([height, 0]); 
    
  // Create axis functions
  var bottomAxis = d3.axisBottom(xTimeScale)
    .tickFormat(d3.timeFormat("%d-%b-%Y"));
  var leftAxis = d3.axisLeft(yLinearScale);

  // Add x-axis
  chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  // Add y-axis to the left side of the display
  chartGroup.append("g")
  // Define the color of the axis text
  .classed("green", true)
  .call(leftAxis); 

  // Line generators for line
  var line = d3.line()
    .x(d => xTimeScale(d.date))
    .y(d => yLinearScale(d.sentiment));

  // Append a path for line1
  chartGroup.append("path")
    .data([tweetData])
    .attr("d", line)
    .classed("line green", true);

  //Append axes titles
  chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 37})`)
    .classed("tweet text", true)
    .text("Twitter Sentiment");
}).catch(function(error) {
  console.log(error);
});