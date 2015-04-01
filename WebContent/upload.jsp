<%@ page import="edu.cmu.sv.webcrawler.models.Categories" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
         pageEncoding="ISO-8859-1" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <title>Risk Advisor</title>
    <%@  include file="./templates/includes.jsp" %>
</head>
<body>
<%@  include file="./templates/header.jsp" %>
<h1>The page is reserved for user to add keyword or category</h1>
<%@  include file="./templates/footer.jsp" %>
<!-- Main part -->
<h1>APIs</h1>


<div class="apis">
    <table  class="table table-striped table-hover table-bordered table-striped">
        <tbody>
        <tr>
            <td>Category</td>
            <td>Keyword</td>
        </tr>

        <tr class="success">
            <td>This is Categoru</td>
            <td>This is Keyword</td>
        </tr>

        </tbody>
    </table>
</div>


</body>
</html>