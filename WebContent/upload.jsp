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
			Keyword: <input type="text" name="add_keyword"><br>
			<button value="add this!" onclick="addKeyword()"></button>
		</form>
	</div>
	
	<div>
		<h4>Delete Keyword Here</h4>
		<form>
			Category: <input type="text" name="del_category"><br>
			Keyword: <input type="text" name="del_keyword"><br>
			<button value="delete this!" onclick="deleteKeyword()"></button>
		</form>
	</div>
	
	<script>
		function addKeyword(){
			var category = document.getElementById("add_category");
			var keyword = document.getElementById("add_keyword");
			$.ajax({
				type="GET",
				url="./api/category/addKeyword?category="+category+"&keyword="+keyword,
				success: function(data){console.log(data);}
			});
		}
		
		function deleteKeyword(){
			var category = document.getElementById("del_category");
			var keyword = document.getElementById("del_keyword");
			$.ajax({
				type="GET",
				url="./api/category/deleteKeyword?category="+category+"&keyword="+keyword,
				success: function(data){console.log(data);}
			});
		}
	</script>
	<%@  include file="./templates/footer.jsp"%>
</body>
</html>