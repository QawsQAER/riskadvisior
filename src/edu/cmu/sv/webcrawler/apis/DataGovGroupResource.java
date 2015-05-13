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
import edu.cmu.sv.webcrawler.util.PackageCrawler;


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
	public DataGovViewReport getTopDatasetsByTag(@PathParam("groupName") String groupName, @PathParam("num") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		PackageCrawler packageCrawler = new PackageCrawler(groupName, "group");
		if (num < 0) {
			return null;
		}
		List<TagCloudEntry> content = packageCrawler.getTopPackages(num);
		int count = packageCrawler.getRealDataPackages().size();
		return new DataGovViewReport(content, count);
	}
	@GET
	@Path("/{groupName}/topTags/{num}")
	@Produces(MediaType.APPLICATION_JSON)
	public DataGovViewReport getTopTagsByTag(@PathParam("groupName") String groupName, @PathParam("num") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		PackageCrawler packageCrawler = new PackageCrawler(groupName, "group");
		if (num < 0) {
			return null;
		}
		List<TagCloudEntry> content = packageCrawler.getTopTags(num);
		int count = packageCrawler.getRealTags().size();
		return new DataGovViewReport(content, count);
	}

}
