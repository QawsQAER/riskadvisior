package edu.cmu.sv.webcrawler.servlets;

import java.io.*;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import edu.cmu.sv.webcrawler.models.Categories;
import edu.cmu.sv.webcrawler.models.Keywords;
import edu.cmu.sv.webcrawler.util.MongoHelper;

@WebServlet("/dummy")
public class DummyServlet extends HttpServlet {

	private static final long serialVersionUID = 6271606642838193911L;

	@Override
	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		insertSymbols(request, response);
		insertKeywords(request, response);
		insertCategories(request, response);
		
	}

	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		req.getRequestDispatcher("./error.jsp").forward(req, resp);
	}
	
	private void insertCategories(HttpServletRequest request,
			HttpServletResponse response) {
		Categories c=new Categories();
		InputStream is = getServletContext().getResourceAsStream("category.json");
		c.load(is);
	}

	private void insertKeywords(HttpServletRequest request,
			HttpServletResponse response) {
		try {
			PrintWriter out = response.getWriter();
			String filename = "keywords.txt";
			
			Keywords kw = new Keywords();
			kw.removeAll();
			InputStream is = getServletContext().getResourceAsStream(filename);
			if (is != null) {
				InputStreamReader isr = new InputStreamReader(is);
				BufferedReader reader = new BufferedReader(isr);
				String text = "";
				while ((text = reader.readLine()) != null) {
					out.println(text);
					kw.insert(text);
					System.out.println(text);
				}
			}
		} catch (Exception e) {

		}
	}
	
	private void insertSymbols(HttpServletRequest request, HttpServletResponse response) {
		try {
			String filename = "stocksymbol";
			InputStream is = getServletContext().getResourceAsStream(filename);
			PrintWriter out = response.getWriter();
			MongoHelper helper = new MongoHelper();
			if (is != null) {
				InputStreamReader isr = new InputStreamReader(is);
				BufferedReader reader = new BufferedReader(isr);
				String text = "";
				while ((text = reader.readLine()) != null) {
					out.println(text);
					helper.insertCompanySymbol(text);
					System.out.println(text);
				}
			}
		}
		catch (IOException e) {
		}
	}

}
