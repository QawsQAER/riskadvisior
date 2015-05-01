package edu.cmu.sv.webcrawler.apis;

import java.io.IOException;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.json.JSONException;

import com.google.gson.Gson;

import edu.cmu.sv.webcrawler.util.HealthCrawler;




@Path("/groupName1/health")
public class DataGovGroupHealthResource {
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public String getDatasetsByHealth() throws JSONException, IOException {
		HealthCrawler healthCrawler = new HealthCrawler();
		Gson gson = new Gson();
		String json = gson.toJson(healthCrawler.getDataPackages());
		return (json);
	}
	
	@GET
	@Path("/topTags/{number}")
	@Produces(MediaType.APPLICATION_JSON)
	public String getTopTagsByHealth(@PathParam("number") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		HealthCrawler healthCrawler = new HealthCrawler();
		if (num < 0) {
			return ("cannot be negtive");
		}
		Gson gson = new Gson();
		String json = gson.toJson(healthCrawler.getTopTags(num));
		int count = healthCrawler.getRealTags().size();
		return ("{"+count+"}"+json);
	}
	
	@GET
	@Path("/topDataset/{number}")
	@Produces(MediaType.APPLICATION_JSON)
	public String getTopDatasetsByHealth(@PathParam("number") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		HealthCrawler healthCrawler = new HealthCrawler();
		if (num < 0) {
			return ("cannot be negtive");
		}
		Gson gson = new Gson();
		String json = gson.toJson(healthCrawler.getTopPackages(num));
		int count = healthCrawler.getRealTags().size();
		return ("{"+count+"}"+json);
	}
	
}
