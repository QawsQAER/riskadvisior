package edu.cmu.sv.webcrawler.apis;

import java.util.HashMap;
import java.util.Map;

import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;

import com.google.gson.Gson;

import edu.cmu.sv.webcrawler.models.Categories;
import edu.cmu.sv.webcrawler.models.Keywords;
import edu.cmu.sv.webcrawler.services.FeatureWeighting;

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
            @PathParam("param") String symbol, @QueryParam("year") String year, @QueryParam("docType") String docType) {
        Keywords ks = new Keywords();
        Map<String, Integer> map;
        if (docType == null || docType.isEmpty()){
        	map = ks.getKeywords(symbol, year);
        }
        else if (year == null || year.isEmpty()) {
        	map = ks.getKeywords(symbol, null, docType);
        }
        else {
        	map = ks.getKeywords(symbol, year, docType);
        }
        if (map == null){
            map = new HashMap<String, Integer>();
            map.put("Error",0);
            return map;
        }
        	
        Categories c = new Categories(map);
        return c.getMap();
    }

    @GET
    @Path("/frequency/{param}")
    @Produces(MediaType.APPLICATION_JSON)
    public Map<String, Double> getCategoryBySymbolWithFrequency(
            @PathParam("param") String symbol, @QueryParam("year") String year, @QueryParam("docType") String docType) {
        Keywords ks = new Keywords();
        Map<String, Integer> map = ks.getKeywordsFrequency(symbol, year, docType);
        Categories c = new Categories(map);
        Map<String, Integer> imap = c.getMap();
        Map<String, Double> dmap = new HashMap<String, Double>();
        for (String key : imap.keySet()) {
            Double d = imap.get(key) / 100.0;
            dmap.put(key, d);
        }
        return dmap;
    }

    @GET
    @Path("/addKeyword")
    @Produces(MediaType.APPLICATION_JSON)
    public String addSymbolByCategory(
            @QueryParam("category") String category, @QueryParam("keyword") String keyword) {
        if (category.length() == 0 || keyword.length() == 0)
            return "empty category or keyword received";
        //access add Keyword API using GET
        Categories c = new Categories();
        c.insert(category, keyword);
        //managing return json
        Map<String, String> m = new HashMap<String, String>();
        m.put("status", "success");
        m.put("category", category);
        m.put("keyword", keyword);
        Gson gson = new Gson();
        return gson.toJson(m);
    }

    @GET
    @Path("/deleteKeyword")
    @Produces(MediaType.APPLICATION_JSON)
    public String deleteSymbolByCategory(
            @QueryParam("category") String category, @QueryParam("keyword") String keyword) {
        if (category.length() == 0 || keyword.length() == 0)
            return "empty category or keyword received";
        Categories c = new Categories();
        c.remove(category, keyword);
        //managing return json
        Map<String, String> m = new HashMap<String, String>();
        m.put("status", "success");
        m.put("category", category);
        m.put("keyword", keyword);
        Gson gson = new Gson();
        return gson.toJson(m);
    }
}
