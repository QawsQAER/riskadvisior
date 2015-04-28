package edu.cmu.sv.webcrawler.apis;

import java.util.List;
import java.util.Map;
import java.util.HashMap;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import com.google.gson.Gson;
import edu.cmu.sv.webcrawler.models.Record;
import edu.cmu.sv.webcrawler.models.Symbols;
import edu.cmu.sv.webcrawler.models.Crawler;
import edu.cmu.sv.webcrawler.services.RequiredInfo;

@Path("/crawl")
public class CrawlerResource {

    /**
     * @param symbol
     * @param docType
     * @return this function will crawl the company with SIC symbol as symbol, docType as docType
     */
    @GET
    @Path("/{param}")
    @Produces(MediaType.APPLICATION_JSON)
    public String crawlBySymbol(@PathParam("param") String symbol, @QueryParam("docType") String docType) {
        String output = "Crawl the risk factors of the company with the symbol "
                + symbol + ",docType " + docType;
        String fail_output = "Fail to crawl the risk factor for company with symbol "
                + symbol + ",docType " + docType;
        Crawler c = new Crawler();
        List<RequiredInfo> result = c.crawl(symbol, docType);
        //create a mapping from "docType" to "numOfDocument"
        Map<String,Integer> m = new HashMap<String,Integer>();
        //add a status field
        m.put("size", result.size());
        for(RequiredInfo info : result){
            String key = info.getDocumentType();
            if(m.containsKey(key)){
                m.put(key,m.get(key)+1);
            }else{
                m.put(key,1);
            }
        }
        Gson gson = new Gson();
        return gson.toJson(m);
    }


    /**
     * @return this function will crawl the 10-K document of all companies in records
     */
    @GET
    public Response crawlAll() {
        String output = "Crawl the risk factors of all companies";
        String fail_output = "Fail to crawl risk factor for companies";
        Crawler c = new Crawler();
        Symbols ss = new Symbols();
        /*for (String symbol : ss.getSymbols()) {
			if(c.crawl(symbol) < 0)
				return Response.status(200).entity(fail_output + symbol).build();
		}*/
        for (String symbol : ss.getSymbols()) {
            if (c.crawl(symbol) < 0)
                System.out.println(Response.status(200).entity(fail_output + symbol).build());
        }
        return Response.status(200).entity(output).build();
    }
}
