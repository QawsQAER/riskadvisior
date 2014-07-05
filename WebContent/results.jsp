<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Web Crawler</title>
<%@  include file="./templates/includes.jsp"%></head>
<body>
	<%@  include file="./templates/header.jsp"%>
	<!-- Main part -->
	<div class="container">
		<label>Results</label>
		<form class="form-horizontal" role="form">
			<div class="form-group">
				<div class="col-sm-4">
					<label for="symbol" class="control-label">Symbol</label> <input
						type="text" class="form-control" id="symbol"
						placeholder="Input the company symbol you want to search" />
				</div>
			</div>
			<div class="form-group">
				<div class="col-sm-4">
					<label for="year" class="control-label">Year</label> <select
						id="year" class="form-control">
						<option>all</option>
						<option>2014</option>
						<option>2013</option>
						<option>2012</option>
						<option>2011</option>
					</select>
				</div>
			</div>
			<button id="searchrecords" class="btn btn-default">Search</button>
		</form>
	</div>

	<div id="result-output" style="display: none" class="bg-info">
		<table
			class="table table-striped table-hover table-bordered table-striped">
			<thead>
				<tr>
					<td>Symbol</td>
					<td>Year</td>
					<td>Risk Factors</td>
				</tr>
			</thead>
			<tbody>

			</tbody>
		</table>
	</div>

	<script>
		$("#searchrecords").click(
				function(event) {
					event.preventDefault();
					var symbol = $("#symbol").val();
					var year = $("#year option:selected").text();
					var crawlurl = "/crawler/api/results/" + symbol;
					if (year != "all") {
						crawlurl = crawlurl + "/?year=" + year;
					}
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
										$('<td>').text(v.riskFactor)));
							});
						}
					});
				});
	</script>

	<%@  include file="./templates/footer.jsp"%>
</body>
</html>