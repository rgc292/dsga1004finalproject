var margin = {top: 100, right: 20, bottom: 30, left: 50},
width = 800 - margin.left - margin.right,
height = 600 - margin.top - margin.bottom;

/* 
* value accessor - returns the value to encode for a given data object.
* scale - maps value to a visual display encoding, such as a pixel position.
* map function - maps from data value to display value
* axis - sets up axis
*/ 

var formatDate = d3.time.format("%Y-%m-%d %X");

var x = d3.time.scale()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .ticks(d3.time.months)
    .tickFormat(d3.time.format("%B"));

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var line = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.Rides); })
    .interpolate("linear");;

var svg = d3.select("#svgCont").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


d3.csv("file1.csv",type, function(error, csv) { 
    if (error) return console.warn(error);
    data = csv

    $('#update').click(function(){
        svg.selectAll("*").remove();
        draw(data);
    });

});

function type(d) {
    d.date = formatDate.parse(d.Date_and_Hour);
    d.month = d.date.getMonth();
    d.day = d.date.getDate();
    d.hours = d.date.getHours();

    d.Temp = +d.Temp;
    d.Rides = +d.Rides;
    d.Dewp = +d.Dewp;

    if(d.Sd!="**") {
        d.Sd = +d.Sd;
    }
    if(d.Pcp01!="*****") {
        d.Pcp01 = +d.Pcp01;
    }
    if(d.Pcp06!="*****") {
        d.Pcp06 = +d.Pcp06;
    }
    if(d.Pcp24!="*****") {
        d.Pcp24 = +d.Pcp24;
    }
    return d;
}


function draw(data) {
    // APPLYING FILTERS ON GRAPH
    data = data.filter(function(d) {
        if( (d.month >= $('#mon-min').val()-1)&&(d.month <= $('#mon-max').val()-1)&&(d.day >= $('#day-min').val())&&(d.day <= $('#day-max').val())&&((d.hours+((d.day-1)*24)) >= $('#hrs-min').val())&&( (d.hours+((d.day-1)*24)) <= $('#hrs-max').val()) ) {
            return true;
        }
        return false;
    })
    console.log(data);
    x.domain([d3.min(data,function(d) { return d.date; }), d3.max(data,function(d) { return d.date; })]);

    // x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain(d3.extent(data, function(d) { return d.Rides; }));

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
      .append("text")
	    .attr("x", width)
	    .attr("y", 20)
	    .style("text-anchor", "end")
        .text("Date and Hour");

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Rides");

    var selectType = $('#graph-type').val();

    if (selectType=="sd") {
        var dataGroup = data.map(function (d, index, arr) {
            var next = arr[index + 1],
            prev = arr[index - 1];
            var color = "";
            if( d.Sd == "**" ) {
                color = "black";
            }
            else if( d.Sd >0) {
                console.log(d);
                color = "red";
            }
            else {
                //default color
                color = "black";
            }

            return {
                x: x(d.date),
                y: y(d.Rides),
                x1: x(d.date),
                y1: y(d.Rides),
                data: d,
                color:color,
                x2: (next) ? x(next.date) : x(prev.date),
                y2: (next) ? y(next.Rides) : y(prev.Rides)
            };
        });

	    // drawing each line segments
	    $.each(dataGroup,function(i,val){
	    	console.log(val);
	    	svg.append('line')
	        .attr('x1', val.x1)
	        .attr('y1', val.y1)
	        .attr('x2', val.x2)
	        .attr('y2', val.y2)
	        .attr("stroke", val.color)
	        .attr("fill", "none")
	        .attr("stroke-width", 1);
	    });

        var legendsMap = [
            {
                name: "Sd > 0",
                color: "red",
            },
            {
                name: "Default",
                color: "black",
            }
        ];

        // draw legend
        var legend = svg.append("g")
            .attr("class", "legend");

        legendsMap.forEach(function(val,i){
            legend.append("rect")
                .attr("x", width - margin.right)
                .attr("y", - margin.top + margin.bottom -15 + i*20)
                .attr("width", 15)
                .attr("height", 15)
                .style("fill", val.color);

            legend.append("text")
                .attr("x", width - margin.right - 5)
                .attr("y", -margin.top + margin.bottom -10  + i*20)
                .attr("dy", ".35em")
                .style("text-anchor", "end")
                .text(val.name);
        });

    }


	else if (selectType=="pcp01") {
        var dataGroup = data.map(function (d, index, arr) {
            var next = arr[index + 1],
            prev = arr[index - 1];
            var color = "";
            if( d.Pcp01 == "*****" ) {
                color = "black";
            }
            else if( d.Pcp01 >0) {
                console.log(d);
                color = "red";
            }
            else {
                //default color
                color = "black";
            }

            return {
                x: x(d.date),
                y: y(d.Rides),
                x1: x(d.date),
                y1: y(d.Rides),
                data: d,
                color:color,
                x2: (next) ? x(next.date) : x(prev.date),
                y2: (next) ? y(next.Rides) : y(prev.Rides)
            };
        });

	    // drawing each line segments
	    $.each(dataGroup,function(i,val){
	    	console.log(val);
	    	svg.append('line')
	        .attr('x1', val.x1)
	        .attr('y1', val.y1)
	        .attr('x2', val.x2)
	        .attr('y2', val.y2)
	        .attr("stroke", val.color)
	        .attr("fill", "none")
	        .attr("stroke-width", 1);
	    });

        var legendsMap = [
            {
                name: "Pcp01 > 0",
                color: "red",
            },
            {
                name: "Default",
                color: "black",
            }
        ];

        // draw legend
        var legend = svg.append("g")
            .attr("class", "legend");

        legendsMap.forEach(function(val,i){
            legend.append("rect")
                .attr("x", width - margin.right)
                .attr("y", - margin.top + margin.bottom -15 + i*20)
                .attr("width", 15)
                .attr("height", 15)
                .style("fill", val.color);

            legend.append("text")
                .attr("x", width - margin.right - 5)
                .attr("y", -margin.top + margin.bottom -10  + i*20)
                .attr("dy", ".35em")
                .style("text-anchor", "end")
                .text(val.name);
        });

    }



	else if (selectType=="pcp06") {
        var dataGroup = data.map(function (d, index, arr) {
            var next = arr[index + 1],
            prev = arr[index - 1];
            var color = "";
            if( d.Pcp06 == "*****" ) {
                color = "black";
            }
            else if( d.Pcp06 >0) {
                console.log(d);
                color = "red";
            }
            else {
                //default color
                color = "black";
            }

            return {
                x: x(d.date),
                y: y(d.Rides),
                x1: x(d.date),
                y1: y(d.Rides),
                data: d,
                color:color,
                x2: (next) ? x(next.date) : x(prev.date),
                y2: (next) ? y(next.Rides) : y(prev.Rides)
            };
        });

	    // drawing each line segments
	    $.each(dataGroup,function(i,val){
	    	console.log(val);
	    	svg.append('line')
	        .attr('x1', val.x1)
	        .attr('y1', val.y1)
	        .attr('x2', val.x2)
	        .attr('y2', val.y2)
	        .attr("stroke", val.color)
	        .attr("fill", "none")
	        .attr("stroke-width", 1);
	    });

        var legendsMap = [
            {
                name: "Pcp06 > 0",
                color: "red",
            },
            {
                name: "Default",
                color: "black",
            }
        ];

        // draw legend
        var legend = svg.append("g")
            .attr("class", "legend");

        legendsMap.forEach(function(val,i){
            legend.append("rect")
                .attr("x", width - margin.right)
                .attr("y", - margin.top + margin.bottom -15 + i*20)
                .attr("width", 15)
                .attr("height", 15)
                .style("fill", val.color);

            legend.append("text")
                .attr("x", width - margin.right - 5)
                .attr("y", -margin.top + margin.bottom -10  + i*20)
                .attr("dy", ".35em")
                .style("text-anchor", "end")
                .text(val.name);
        });

    }



	else if (selectType=="pcp24") {
        var dataGroup = data.map(function (d, index, arr) {
            var next = arr[index + 1],
            prev = arr[index - 1];
            var color = "";
            if( d.Pcp24 == "*****" ) {
                color = "black";
            }
            else if( d.Pcp24 >0) {
                console.log(d);
                color = "red";
            }
            else {
                //default color
                color = "black";
            }

            return {
                x: x(d.date),
                y: y(d.Rides),
                x1: x(d.date),
                y1: y(d.Rides),
                data: d,
                color:color,
                x2: (next) ? x(next.date) : x(prev.date),
                y2: (next) ? y(next.Rides) : y(prev.Rides)
            };
        });

	    // drawing each line segments
	    $.each(dataGroup,function(i,val){
	    	console.log(val);
	    	svg.append('line')
	        .attr('x1', val.x1)
	        .attr('y1', val.y1)
	        .attr('x2', val.x2)
	        .attr('y2', val.y2)
	        .attr("stroke", val.color)
	        .attr("fill", "none")
	        .attr("stroke-width", 1);
	    });

        var legendsMap = [
            {
                name: "Pcp24 > 0",
                color: "red",
            },
            {
                name: "Default",
                color: "black",
            }
        ];

        // draw legend
        var legend = svg.append("g")
            .attr("class", "legend");

        legendsMap.forEach(function(val,i){
            legend.append("rect")
                .attr("x", width - margin.right)
                .attr("y", - margin.top + margin.bottom -15 + i*20)
                .attr("width", 15)
                .attr("height", 15)
                .style("fill", val.color);

            legend.append("text")
                .attr("x", width - margin.right - 5)
                .attr("y", -margin.top + margin.bottom -10  + i*20)
                .attr("dy", ".35em")
                .style("text-anchor", "end")
                .text(val.name);
        });

    }



    else if(selectType=="dewp") {  

    // getting coordinated of next and grouping data into line segments and colors
    var dataGroup = data.map(function (d, index, arr) {
        var next = arr[index + 1],
        prev = arr[index - 1];
        var color = "";
        if( d.Dewp <= 32 ) {
            color = "blue";
        }
        else if( d.Dewp > 32 && d.Dewp <= 50) {
            color = "green";
        }
        else if( d.Dewp >50 && d.Dewp <= 60 ) {
            color = "orange";
        }
        else if ( d.Dewp >60){
            color = "red";
        }
        else {
            //default color
            color = "black";
        }
        // console.log(x(d.date),x(next.date));
        return {
            x: x(d.date),
            y: y(d.Rides),
            x1: x(d.date),
            y1: y(d.Rides),
            data: d,
            color:color,
            x2: (next) ? x(next.date) : x(prev.date),
            y2: (next) ? y(next.Rides) : y(prev.Rides)
        };
    });

    console.log(dataGroup,dataGroup.length);

    // drawing each line segments
    $.each(dataGroup,function(i,val){
    	console.log(val);
    	svg.append('line')
        .attr('x1', val.x1)
        .attr('y1', val.y1)
        .attr('x2', val.x2)
        .attr('y2', val.y2)
        .attr("stroke", val.color)
        .attr("fill", "none")
        .attr("stroke-width", 1);
    });

    var legendsMap = [
        {
            name: "Default",
            color: "black",
        },
        {
        	name:" Dewp <= 32",
        	color:"blue",
        },
        {
            name: "32 < Dewp <= 50",
            color: "green",
        },
        {
            name: "50 < Dewp <= 60",
            color: "orange",
        },
        {
            name: "Dewp > 60",
            color: "red",
        }
    ];
    // draw legend
    var legend = svg.append("g")
        .attr("class", "legend");

    legendsMap.forEach(function(val,i){
        legend.append("rect")
            .attr("x", width - margin.right)
            .attr("y", - margin.top + margin.bottom -15 + i*20)
            .attr("width", 15)
            .attr("height", 15)
            .style("fill", val.color);

        legend.append("text")
            .attr("x", width - margin.right - 5)
            .attr("y", -margin.top + margin.bottom -10  + i*20)
            .attr("dy", ".35em")
            .style("text-anchor", "end")
            .text(val.name);
    });

    }



    else if(selectType=="temp") {  

    // getting coordinated of next and grouping data into line segments and colors
    var dataGroup = data.map(function (d, index, arr) {
        var next = arr[index + 1],
        prev = arr[index - 1];
        var color = "";
        if( d.Temp <= 32 ) {
            color = "blue";
        }
        else if( d.Temp > 32 && d.Temp <= 50) {
            color = "green";
        }
        else if( d.Temp >50 && d.Temp <= 60 ) {
            color = "orange";
        }
        else if ( d.Temp >60){
            color = "red";
        }
        else {
            //default color
            color = "black";
        }
        // console.log(x(d.date),x(next.date));
        return {
            x: x(d.date),
            y: y(d.Rides),
            x1: x(d.date),
            y1: y(d.Rides),
            data: d,
            color:color,
            x2: (next) ? x(next.date) : x(prev.date),
            y2: (next) ? y(next.Rides) : y(prev.Rides)
        };
    });

    console.log(dataGroup,dataGroup.length);

    // drawing each line segments
    $.each(dataGroup,function(i,val){
    	console.log(val);
    	svg.append('line')
        .attr('x1', val.x1)
        .attr('y1', val.y1)
        .attr('x2', val.x2)
        .attr('y2', val.y2)
        .attr("stroke", val.color)
        .attr("fill", "none")
        .attr("stroke-width", 1);
    });

    var legendsMap = [
        {
            name: "Default",
            color: "black",
        },
        {
        	name:" Temp <= 32",
        	color:"blue",
        },
        {
            name: "32 < Temp <= 50",
            color: "green",
        },
        {
            name: "50 < Temp <= 60",
            color: "orange",
        },
        {
            name: "Temp > 60",
            color: "red",
        }
    ];
    // draw legend
    var legend = svg.append("g")
        .attr("class", "legend");

    legendsMap.forEach(function(val,i){
        legend.append("rect")
            .attr("x", width - margin.right)
            .attr("y", - margin.top + margin.bottom -15 + i*20)
            .attr("width", 15)
            .attr("height", 15)
            .style("fill", val.color);

        legend.append("text")
            .attr("x", width - margin.right - 5)
            .attr("y", -margin.top + margin.bottom -10  + i*20)
            .attr("dy", ".35em")
            .style("text-anchor", "end")
            .text(val.name);
    });

    }
};



