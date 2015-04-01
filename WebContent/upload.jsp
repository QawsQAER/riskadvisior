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
		<form action="./api/category/addKeyword" method="GET">
			Category: <input type="text" id="Add_input_category"><br>
			Keyword: <input type="text" id="Add_input_keyword"><br>
			<input type="submit" value="add this!">
		</form>
	</div>
	
	<div>
		<h4>Delete Keyword Here</h4>
		<form action="./api/category/deleteKeyword" method="GET">
			Category: <input type="text" id="Del_input_category"><br>
			Keyword: <input type="text" id="Del_input_keyword"><br>
			<input type="submit" value="delete this!">
		</form>
	</div>
	
	<%@  include file="./templates/footer.jsp"%>
</body>
</html>