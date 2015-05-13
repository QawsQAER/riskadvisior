package edu.cmu.sv.webcrawler.apis;

import java.io.IOException;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.json.JSONException;

import edu.cmu.sv.webcrawler.models.GroupList;
import edu.cmu.sv.webcrawler.util.GroupListCrawler;


@Path("/groupList")
public class GroupListResource {

	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public GroupList getGroupList() throws IOException, JSONException {
		GroupListCrawler groupListCrawler = new GroupListCrawler();
		return new GroupList(groupListCrawler.getGroupList());
	}
}