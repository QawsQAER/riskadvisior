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
	<div>
		<h4>Add Keyword Here</h4>
		<form>
			Category: <input type="text" id="add_category"><br>
			Keyword: <input type="text" id="add_keyword"><br>
			<button onclick="addKeyword()">add this!</button>
		</form>
	</div>
	
	<div>
		<h4>Delete Keyword Here</h4>
		<form>
			Category: <input type="text" id="del_category"><br>
			Keyword: <input type="text" id="del_keyword"><br>
			<button onclick="deleteKeyword()">delete this!</button>
		</form>
	</div>
	
	<script>
		function addKeyword(){
			var url = location.href;
			var host = url.substring(0, url.lastIndexOf("/"));
			var category = document.getElementById("add_category");
			var keyword = document.getElementById("add_keyword");
			console.log("add keyword based on " + category + ", " + keyword);
			$.ajax({
				type:"GET",
				url:host + "/api/category/addKeyword?category="+category+"&keyword="+keyword,
				success:function(data){console.log(data);}
			});
		}
		
		function deleteKeyword(){
			var url = location.href;
			var host = url.substring(0, url.lastIndexOf("/"));
			var category = document.getElementById("del_category");
			var keyword = document.getElementById("del_keyword");
			console.log("delete keyword based on " + category + ", " + keyword);
			$.ajax({
				type:"GET",
				url:host + "/api/category/deleteKeyword?category="+category+"&keyword="+keyword,
				success:function(data){console.log(data);}
			});
		}
	</script>
	<%@  include file="./templates/footer.jsp"%>
</body>
</html>