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
		<form id="crawlerform" class="form-horizontal" role="form"
			action="/crawl" method="post">
			<div class="form-group">
				<label for="companyname">Crawl records of a company</label>
				<input type="text" id="companyname" class="form-control col-sm-4"
					placeholder="Empty = crawl all companies"></input>
				<select id="docType_craw">
					<option value="all" selected="selected">all</option>
					<option value="10-K">10-K</option>
					<option value="20-F">20-F</option>
					<option value="8-K">8-K</option>
					<option	value="10-Q">10-Q</option>
					<option value="6-K">6-K</option>
				</select>
			</div>
			<div class="form-group">
				<button id="begincrawl" type="submit" class="btn btn-default">Crawl
					now!</button>
			</div>
			<div>
				<p class="bg-info" id="crawl-info"></p>
			</div>
			<label>Delete the records of a company</label>
			<select id="docType_delete">
				<option value="all" selected="selected">all</option>
				<option value="10-K">10-K</option>
				<option value="20-F">20-F</option>
				<option value="8-K">8-K</option>
				<option	value="10-Q">10-Q</option>
				<option value="6-K">6-K</option>
			</select>
			<div class="form-group">
				<input id="deletesymbol" type="text" class="form-control col-sm-4"
					placeholder="Empty = delete all records" />
				<button id="deleterecord" class="btn btn-default">Delete</button>
			</div>
			<div>
				<p class="bg-info" id="crawl-delete"></p>
			</div>
		</form>
	</div>


	<script>
	var url = location.href;
	var host = url.substring(0, url.lastIndexOf("/"));
		$("#begincrawl").click(
			function(event) {
				event.preventDefault();
				var symbol = $("#companyname").val();
				var docType = $("#docType_craw").val();
				var output = $("#crawl-info");
				var crawlurl = host+"/api/crawl/" + symbol + "?docType=" + docType;
				output.text("Trying to Crawl " + symbol);
				$.ajax({
					url : crawlurl,
					success : function(data) {
						if(data["size"] == 0){
							var msg = "No Document are crawlled";
							output.text(msg);
						}else{
							var msg = "Some documents are crawled: ";
							console.log(data);
							if("all" in data)
								msg += data["all"] + " all documents, ";
							if("10-K" in data)
								msg += data["10-K"] + " 10-K documents, ";
							if("20-F" in data)
								msg += data["20-F"] + " 20-F documents, ";
							if("8-K" in data)
								msg += data["8-K"] + " 8-K documents, ";
							if("10-Q" in data)
								msg += data["10-Q"] + " 10-Q documents, ";
							if("6-K" in data)
								msg += data["6-K"] + " 6-K documents, ";
							output.text(msg);
						}
					}
				});
		});

		$("#deleterecord").click(
			function(event) {
				event.preventDefault();
				var symbol = $("#deletesymbol").val();
				var output = $("#crawl-delete");
				var docType = $("#docType_delete").val();
				var deleteurl = host+"/api/results/" + symbol+ "?docType=" + docType;
				$.ajax({
					type : "DELETE",
					url : deleteurl,
					success : function(data) {
					output.text("Deleted the records of the company "
							+ symbol);
					}
				});
			});
	</script>


	<%@  include file="./templates/footer.jsp"%>
</body>
</html>