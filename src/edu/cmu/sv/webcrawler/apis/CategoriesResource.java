package edu.cmu.sv.webcrawler.apis;

import java.util.Map;

import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;

import edu.cmu.sv.webcrawler.models.Categories;
import edu.cmu.sv.webcrawler.models.Keywords;

@Path("/category")
public class CategoriesResource {
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Categories getCategory(@PathParam("param") String symbol) {
        Categories c = new Categories();
        return c;
    }

    @GET
    @Path("/{param}")
    @Produces(MediaType.APPLICATION_JSON)
    public Map<String, Integer> getCategoryBySymbol(
            @PathParam("param") String symbol, @QueryParam("year") String year) {
        Keywords ks = new Keywords();
        Map<String, Integer> map = ks.getKeywords(symbol, year);
        Categories c = new Categories(map);
        return c.getMap();
    }
    
    @GET
    @Path("/frequency/{param}")
    @Produces(MediaType.APPLICATION_JSON)
    public Map<String, Integer> getCategoryBySymbolWithFrequency(
            @PathParam("param") String symbol, @QueryParam("year") String year) {
        Keywords ks = new Keywords();
        Map<String, Integer> map = ks.getKeywordsFrequency(symbol, year);
        Categories c = new Categories(map);
        return c.getMap();
    }

    @GET
    @Path("/addKeyword")
    @Produces(MediaType.APPLICATION_JSON)
    public String addSymbolByCategory(
            @QueryParam("category") String category, @QueryParam("keyword") String keyword) {
        if(category.length() == 0 || keyword.length() == 0)
        	return "empty category or keyword received";
    	//access add Keyword API using GET
        Categories c = new Categories();
        c.insert(category, keyword);
        return " category: " + category + ", added keyword:" + keyword;
    }

    @GET
    @Path("/deleteKeyword")
    @Produces(MediaType.APPLICATION_JSON)
    public String deleteSymbolByCategory(
            @QueryParam("category") String category, @QueryParam("keyword") String keyword) {
    	if(category.length() == 0 || keyword.length() == 0)
        	return "empty category or keyword received";
    	Categories c = new Categories();
        c.remove(category, keyword);
        return "category: " + category + ", removed keyword is " + keyword;
    }
}
