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
	

	<div class="container">
		<h3> Add Keyword Here</h3>
		<form class="form-horizontal" role="form">
			<div class="form-group">
				<div class="col-sm-4">
				<label for="category" class="control-label">Category:</label> 
				<input type="text" id="add_category" class="form-control col-sm-4"><br>
				<label for="keyword" class="control-label">Keyword:</label>
				<input type="text" id="add_keyword" class="form-control col-sm-4"><br>	
				</div>	
			</div>	
			<button value="add this!" onclick="addKeyword()" class="btn btn-default">Add</button>
		</form>
	</div>
	<br>
	<div class="container">
		<h4>Category</h4>
		<table class="table table-striped table-hover table-bordered table-striped" >
			<thead>
			<tr>
				<th>Category</th>
				<th>Keyword</th>
				<th>Action</th>
			</tr>
			</thead>
			<tbody id="CategoryTable">
			</tbody>
		</table>
	</div>
	
	<script>
		getKeywords();
		function getKeywords(){
			var url = location.href;
			var host = url.substring(0, url.lastIndexOf("/"));
			console.log(host + "/api/category");
			$.ajax({
				type:"GET",
				url:host + "/api/category",
				success:function(data){renderKeywords(data);}
			})
		}
		
		function renderKeywords(data){
			console.log(data);
			var table = document.getElementById("CategoryTable");
			table.innerHTML = "";
			var categories = JSON.parse(data);
			console.log(categories);
			for(var category in categories){
				console.log(category);
				if(categories.hasOwnProperty(category)){
					for(var idx in categories[category]){
						addTableRow(table,category,categories[category][idx]);
					}
				}
			}
		}
		
		function addTableRow(table,categoryName,keyword){
			console.log("addTableRow(" + table + ", " + categoryName + ", " + keyword);
			var tr = document.createElement("tr");
			tr.className = "success";
			var td1 = document.createElement("td");
			td1.innerHTML = categoryName;
			var td2 = document.createElement("td");
			td2.innerHTML = keyword;
			var td3 = document.createElement("td");
			var button = document.createElement("button");
			button.className = "btn btn-danger";
			button.innerHTML = "Delete";
			$(button).click({category:categoryName,keyword:keyword},deleteKeywordByParam);
			td3.appendChild(button);
			tr.appendChild(td1);
			tr.appendChild(td2);
			tr.appendChild(td3);
			table.appendChild(tr);
			return ;
		}
		
		function addKeyword(){
			var url = location.href;
			var host = url.substring(0, url.lastIndexOf("/"));
			var category = document.getElementById("add_category").value;
			var keyword = document.getElementById("add_keyword").value;

			$.ajax({
				type: "GET",
				url: host + "/api/category/addKeyword?category=" + category + "&keyword=" + keyword,
				success: function (data) {
					console.log("Success in addKeyword Ajax");
				},
				error: function(xhr, status, error){
					console.log("Error in addKeyword Ajax");
					console.log(xhr);
					console.log(status);
					console.log(error);
				}
			}).done(function(){
				getKeywords();
			});
			
		}
		
		function deleteKeyword(){
			var category = document.getElementById("del_category").value;
			var keyword = document.getElementById("del_keyword").value;
			deleteKeywordByParam(category,keyword);
		}

		function deleteKeywordByParam(event){
			var url = location.href;
			var host = url.substring(0, url.lastIndexOf("/"));
			var category = event.data.category;
			var keyword = event.data.keyword;
			$.ajax({
				type:"GET",
				url:host + "/api/category/deleteKeyword?category="+category+"&keyword="+keyword,
				success:function(data){
					console.log("Success in deleteKeyword Ajax");
				},
				error:function(xhr,status,error){
					console.log("Error in deleteKeyword Ajax");
					console.log(xhr);
					console.log(status);
					console.log(error);
				}
			}).done(function(){
				getKeywords();
			});
		}
	</script>
	<%@  include file="./templates/footer.jsp"%>
</body>
</html>
