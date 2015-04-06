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
		<div class="col-sm-4">
		<h4> Add Keyword Here</h4>
		<label for="category" class="control-label">Category:</label> 
		<input type="text" id="add_category" class="form-control col-sm-4"><br>
		<label for="keyword" class="control-label">Keyword:</label>
		<input type="text" id="add_keyword" class="form-control col-sm-4"><br>		
		<button value="add this!" onclick="addKeyword()" class="btn btn-default">Add</button>
		</div>	
	</div>

	<div class="container">
		<div class="col-sm-4">
		<h4> Delete Keyword Here</h4>
		<label for="category" class="control-label">Category:</label>
		<input type="text" id="del_category" class="form-control col-sm-4"><br>
		<label for="keyword" class="control-label">Keyword:</label> 
		<input type="text" id="del_keyword" class="form-control col-sm-4"><br>
		<button value="delete this!" onclick="deleteKeyword()" class="btn btn-default">Delete</button>
		</div>
	</div>
	
	<div class="container" class="col-sm-4">
		<h4>Category</h4>
		<table id="CategoryTable" class="table table-striped table-hover table-bordered table-striped">
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
			var tr = document.createElement("tr");
			var td1 = document.createElement("td");
			var td2 = document.createElement("td");
			td1.innerHTML = "Category";
			td2.innerHTML = "Keyword";
			tr.appendChild(td1);
			tr.appendChild(td2);
			table.appendChild(tr);
			var categories = data.initMap;
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
			var td1 = document.createElement("td");
			td1.innerHTML = categoryName;
			var td2 = document.createElement("td");
			td2.innerHTML = keyword;
			tr.appendChild(td1);
			tr.appendChild(td2);
			table.appendChild(tr);
			return ;
		}
		
		function addKeyword(){
			var url = location.href;
			var host = url.substring(0, url.lastIndexOf("/"));
			var category = document.getElementById("add_category").value;
			var keyword = document.getElementById("add_keyword").value;
			console.log("add keyword based on " + category + ", " + keyword);
			
			$.ajax({
				type:"GET",
				url:host + "/api/category/addKeyword?category="+category+"&keyword="+keyword,
				success:function(data){
					console.log(data);
					getKeywords();
				}
			});
			
		}
		
		function deleteKeyword(){
			var url = location.href;
			var host = url.substring(0, url.lastIndexOf("/"));
			var category = document.getElementById("del_category").value;
			var keyword = document.getElementById("del_keyword").value;
			console.log("delete keyword based on " + category + ", " + keyword);
			
			$.ajax({
				type:"GET",
				url:host + "/api/category/deleteKeyword?category="+category+"&keyword="+keyword,
				success:function(data){
					console.log(data);
					getKeywords();
				}
			});
			
		}
	</script>
	<%@  include file="./templates/footer.jsp"%>
</body>
</html>
