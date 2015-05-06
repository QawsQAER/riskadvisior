package edu.cmu.sv.webcrawler.apis;

import java.io.IOException;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.json.JSONException;

import com.google.gson.Gson;

import edu.cmu.sv.webcrawler.util.PackageCrawler;
import edu.cmu.sv.webcrawler.util.Common;


@Path("/groupName")
public class DataGovGroupResource {

	@GET
	@Path("/{groupName}")
	@Produces(MediaType.APPLICATION_JSON)
	public String getDatasetsByTag(@PathParam("groupName") String groupName) throws IOException, JSONException {
		PackageCrawler packageCrawler = new PackageCrawler(groupName, "group");
		Gson gson = new Gson();
		String json = gson.toJson(packageCrawler.getDataPackages());
		return json;
	}
	@GET
	@Path("/{groupName}/topDataset/{num}")
	@Produces(MediaType.APPLICATION_JSON)
	public String getTopDatasetsByTag(@PathParam("groupName") String groupName, @PathParam("num") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		PackageCrawler packageCrawler = new PackageCrawler(groupName, "group");
		if (num < 0) {
			return ("cannot be negative");
		}

		Gson gson = new Gson();
		String json = gson.toJson(packageCrawler.getTopPackages(num));
		int count = packageCrawler.getRealDataPackages().size();
		return (Common.formatCountJson(count,json));
	}
	@GET
	@Path("/{groupName}/topTags/{num}")
	@Produces(MediaType.APPLICATION_JSON)
	public String getTopTagsByTag(@PathParam("groupName") String groupName, @PathParam("num") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		PackageCrawler packageCrawler = new PackageCrawler(groupName, "group");
		if (num < 0) {
			return ("cannot be negative");
		}
		Gson gson = new Gson();
		String json = gson.toJson(packageCrawler.getTopTags(num));
		int count = packageCrawler.getRealTags().size();
		return (Common.formatCountJson(count,json));
	}

}
