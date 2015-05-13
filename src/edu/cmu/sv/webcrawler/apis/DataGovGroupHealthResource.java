package edu.cmu.sv.webcrawler.apis;

import java.io.IOException;
import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.json.JSONException;

import com.google.gson.Gson;

import edu.cmu.sv.webcrawler.models.DataGovViewReport;
import edu.cmu.sv.webcrawler.models.TagCloudEntry;
import edu.cmu.sv.webcrawler.util.Common;
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
	public DataGovViewReport getTopTagsByHealth(@PathParam("number") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		HealthCrawler healthCrawler = new HealthCrawler();
		if (num < 0) {
			return null;
		}
		List<TagCloudEntry> content = healthCrawler.getTopTags(num);
		int count = healthCrawler.getRealTags().size();
		return new DataGovViewReport(content, count);
	}
	
	@GET
	@Path("/topDataset/{number}")
	@Produces(MediaType.APPLICATION_JSON)
	public DataGovViewReport getTopDatasetsByHealth(@PathParam("number") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		HealthCrawler healthCrawler = new HealthCrawler();
		if (num < 0) {
			return null;
		}
		List<TagCloudEntry> content = healthCrawler.getTopPackages(num);
		int count = healthCrawler.getRealTags().size();
		return new DataGovViewReport(content, count);
	}
	
}
