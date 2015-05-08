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

import edu.cmu.sv.webcrawler.models.DataPackage;
import edu.cmu.sv.webcrawler.models.DataPackageReport;
import edu.cmu.sv.webcrawler.models.Tag;
import edu.cmu.sv.webcrawler.models.TagReport;
import edu.cmu.sv.webcrawler.util.HealthCrawler;
import edu.cmu.sv.webcrawler.util.PackageCrawler;



@Path("/backend")
public class DataGovBackendResource {
	//group
	@GET
	@Path("/groupName/{groupName}")
    @Produces(MediaType.APPLICATION_JSON)
	public DataPackageReport backendGetDatasetsByGroup(@PathParam("groupName") String groupName) throws IOException, JSONException {
		PackageCrawler packageCrawler = new PackageCrawler(groupName, "group");
		Gson gson = new Gson();
		DataPackageReport dataPackageReport = new DataPackageReport(packageCrawler.getRealDataPackages());
		return dataPackageReport;
	}
	@GET
	@Path("/groupName/{groupName}/topDataset/{num}")
	@Produces(MediaType.APPLICATION_JSON)
	public DataPackageReport backendGetTopDatasetsByGroup(@PathParam("groupName") String groupName, @PathParam("num") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		PackageCrawler packageCrawler = new PackageCrawler(groupName, "group");
		if (num < 0) {
			return null;
		}

		Gson gson = new Gson();
		List<DataPackage> dataPackages = packageCrawler.getRealTopPackages(num);
		DataPackageReport dataPackageReport = new DataPackageReport(dataPackages);
		return dataPackageReport;
	}
	@GET
	@Path("/groupName/{groupName}/topTags/{num}")
	@Produces(MediaType.APPLICATION_JSON)
	public TagReport backendGetTopTagsByGroup(@PathParam("groupName") String groupName, @PathParam("num") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		PackageCrawler packageCrawler = new PackageCrawler(groupName, "group");
		if (num < 0) {
			return null;
		}
		Gson gson = new Gson();
		List<Tag> tags = packageCrawler.getRealTopTags(num);
		TagReport tagReport = new TagReport(tags);
		return tagReport;
	}
	//tag
	@GET
	@Path("/tagName/{tagName}")
	@Produces(MediaType.APPLICATION_JSON)
	public DataPackageReport backendGetDatasetsByTag(@PathParam("tagName") String tagName) throws IOException, JSONException {
		PackageCrawler packageCrawler = new PackageCrawler(tagName, "tag");
		Gson gson = new Gson();
		DataPackageReport dataPackageReport = new DataPackageReport(packageCrawler.getRealDataPackages());
		return dataPackageReport;
	}
	@GET
	@Path("/tagName/{tagName}/topDataset/{num}")
	@Produces(MediaType.APPLICATION_JSON)
	public DataPackageReport backendGetTopDatasetsByTag(@PathParam("tagName") String tagName, @PathParam("num") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		PackageCrawler packageCrawler = new PackageCrawler(tagName, "tag");
		if (num < 0) {
			return null;
		}

		Gson gson = new Gson();
		List<DataPackage> dataPackages = packageCrawler.getRealTopPackages(num);
		DataPackageReport dataPackageReport = new DataPackageReport(dataPackages);
		return dataPackageReport;
	}
	@GET
	@Path("/tagName/{tagName}/topTags/{num}")
	@Produces(MediaType.APPLICATION_JSON)
	public TagReport backendGetTopTagsByTag(@PathParam("tagName") String tagName, @PathParam("num") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		PackageCrawler packageCrawler = new PackageCrawler(tagName, "tag");
		if (num < 0) {
			return null;
		}
		Gson gson = new Gson();
		List<Tag> tags = packageCrawler.getRealTopTags(num);
		TagReport tagReport = new TagReport(tags);
		return tagReport;
	}
	//health
	@GET
	@Path("/groupName1/health")
    @Produces(MediaType.APPLICATION_JSON)
	public DataPackageReport backendGetDatasetsByHealth() throws IOException, JSONException {
		HealthCrawler healthCrawler = new HealthCrawler();
		Gson gson = new Gson();
		DataPackageReport dataPackageReport = new DataPackageReport(healthCrawler.getRealDataPackages());
		return dataPackageReport;
	}
	@GET
	@Path("/groupName1/health/topDataset/{num}")
	@Produces(MediaType.APPLICATION_JSON)
	public DataPackageReport backendGetTopDatasetsByGroup(@PathParam("num") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		HealthCrawler healthCrawler = new HealthCrawler();
		if (num < 0) {
			return null;
		}

		Gson gson = new Gson();
		List<DataPackage> dataPackages = healthCrawler.getRealTopPackages(num);
		DataPackageReport dataPackageReport = new DataPackageReport(dataPackages);
		return dataPackageReport;
	}
	@GET
	@Path("/groupName1/health/topTags/{num}")
	@Produces(MediaType.APPLICATION_JSON)
	public TagReport backendGetTopTagsByGroup(@PathParam("num") String number) throws IOException, JSONException {
		int num = Integer.parseInt(number);
		HealthCrawler healthCrawler = new HealthCrawler();
		if (num < 0) {
			return null;
		}
		Gson gson = new Gson();
		List<Tag> tags = healthCrawler.getRealTopTags(num);
		return new TagReport(tags);
	}
}