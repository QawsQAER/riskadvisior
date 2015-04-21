<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Risk Advisor</title>
<%@  include file="./templates/includes.jsp"%></head>
<body>
	<%@  include file="./templates/header.jsp"%>
	<!-- Main part -->
	<div class="container">
		<h3>Show the results of a company in a given year.</h3>
		<form class="form-horizontal" role="form">
			<div class="form-group">
				<div class="col-sm-4">
					<label for="symbol" class="control-label">Stock symbol</label> <input
						type="text" class="form-control" id="symbol"
						placeholder="Input the company symbol you want to search" />
				</div>
			</div>
			<div class="form-group">
				<div class="col-sm-4">
					<label for="year" class="control-label">Year</label> <select
						id="year" class="form-control">
						<option>all</option>
						<option>2015</option>
						<option>2014</option>
						<option>2013</option>
						<option>2012</option>
						<option>2011</option>
					</select>
				</div>
			</div>
			<div class="form-group">
				<div class="col-sm-4">
					<label for="docType" class="control-label">DocType</label> <select
						id="docType" class="form-control">
						<option value="10-K">10-K</option>
						<option value="20-F">20-F</option>
						<option value="8-K">8-K</option>
						<option	value="10-Q">10-Q</option>
						<option value="6-K">6-K</option>
					</select>
				</div>
			</div>
			<button id="searchrecords" class="btn btn-default">Show results!</button>
		</form>
	</div>

	<div id="chartContainer1" style="height: 300px; width: 100%;"></div>
	<div id="chartContainer2" style="height: 300px; width: 100%;"></div>
	<div id="result-output" style="display: none" class="bg-info">
		<table
			class="table table-striped table-hover table-bordered table-striped">
			<thead>
				<tr>
					<td>Symbol</td>
					<td>Year</td>
					<td>Word Count</td>
					<td>Risk Factors</td>
				</tr>
			</thead>
			<tbody>

			</tbody>
		</table>
	</div>

	<script>
		var url = location.href;
		var host = url.substring(0, url.lastIndexOf("/"));
		$("#searchrecords").click(
			function(event) {
				event.preventDefault();
				var symbol = $("#symbol").val();
				var year = $("#year option:selected").text();
				var doc = $("#docType option:selected").text();
				var crawlurl = host+"/api/results/" + symbol;
				var categoryurl=host+"/api/category/" + symbol;
				if (year != "all") {
					crawlurl = crawlurl + "/?year=" + year;
					categoryurl = categoryurl+"/?year=" + year;
				}
				else {
					crawlurl = crawlurl + "/?year=2014";
					categoryurl = categoryurl+"/?year=2014"; 
				}
				crawlurl = crawlurl + "&docType=" + doc;
				categoryurl = categoryurl + "&docType=" + doc;
				//get the result from api provided by current website
				$.ajax({
					url : crawlurl,
					success : function(data) {
						var body = $("#result-output").find("tbody");
						$("#result-output").show();
						body.find('tr').remove();
						$.each(data.records, function(i, v) {
							body.append($('<tr>').append(
									$('<td>').text(v.symbol)).append(
									$('<td>').text(v.year)).append(
									$('<td>').text(v.wordCount)).append(
									$('<td>').text(v.riskFactor)));
						});
					}
				});
				
				//get the category from api provided by current website
				$.ajax({
					url: categoryurl,
					success : function(data){
						showData(data,"Risk Categories");
					}
				});
			});
		function showData(data,text) {
			var risks=data;
			//console.log(risks);

			var dataPoints = [];
			for (key in risks) {
				if(risks[key]<=0){
					continue;
				}
				dataPoints.push({
					label : key,
					y : risks[key]
				});
			}
			var chart1 = new CanvasJS.Chart("chartContainer1", {
				title : {
					text : text+" Histogram"
				},
				data : [//array of dataSeries              
				{ //dataSeries object

					/*** Change type "column" to "bar", "area", "line" or "pie"***/
					type : "column",
					dataPoints : dataPoints
				} ]
			});

			var chart2 = new CanvasJS.Chart("chartContainer2", {
				title : {
					text : text+" Components PieChart",
					fontFamily : "Impact",
					fontWeight : "normal"
				},

				legend : {
					verticalAlign : "bottom",
					horizontalAlign : "center"
				},
				data : [ {
					//startAngle: 45,
					indexLabelFontSize : 20,
					indexLabelFontFamily : "Garamond",
					indexLabelFontColor : "darkgrey",
					indexLabelLineColor : "darkgrey",
					indexLabelPlacement : "outside",
					type : "doughnut",
					dataPoints : dataPoints
				} ]
			});
			chart1.render();
			chart2.render();
			//}
		}
	</script>

	<%@  include file="./templates/footer.jsp"%>
</body>
</html>