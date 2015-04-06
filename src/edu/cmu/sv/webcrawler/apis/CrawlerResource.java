package edu.cmu.sv.webcrawler.apis;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Response;

import edu.cmu.sv.webcrawler.models.Symbols;
import edu.cmu.sv.webcrawler.models.Crawler;

@Path("/crawl")
public class CrawlerResource {

	@GET
	@Path("/{param}")
	public Response crawlBySymbol(@PathParam("param") String symbol, @QueryParam("docType") String docType) {
		String output = "Crawl the risk factors of the company with the symbol " 
							+ symbol + ",docType " + docType;
		String fail_output = "Fail to crawl the risk factor for company with symbol " 
							+ symbol + ",docType " + docType;
		Crawler c = new Crawler();
		if(c.crawl(symbol) < 0)
			return Response.status(200).entity(fail_output).build();
	
		return Response.status(200).entity(output).build();
	}

	@GET
	public Response crawlAll() {
		String output = "Crawl the risk factors of all companies";
		String fail_output = "Fail to crawl risk factor for company ";
		Crawler c = new Crawler();
		Symbols ss = new Symbols();
		for (String symbol : ss.getSymbols()) {
			if(c.crawl(symbol) < 0)
				return Response.status(200).entity(fail_output + symbol).build();
		}
		return Response.status(200).entity(output).build();
	}
}
