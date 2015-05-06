package edu.cmu.sv.webcrawler.apis;

import java.util.ArrayList;
import java.util.List;

import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import edu.cmu.sv.webcrawler.models.Record;

@Path("/results")
public class ResultsResource {

	@GET
	@Path("/{param}")
	@Produces(MediaType.APPLICATION_JSON)
	public Records getResult(@PathParam("param") String symbol,
			@QueryParam("year") String year, @QueryParam("docType") String docType) {
		Records records = new Records();
		List<Record> list = null;
		if (year == null && docType == null) {
			list = Record.search(symbol);
			records.setRecords(list);
			return records;
		}
		if (year == null || year.isEmpty()){
			list = Record.search(symbol, null, docType);
		}
		else if (docType == null || docType.isEmpty()) {
			list = Record.search(symbol, year, null);
		}
		else {
			list = Record.search(symbol, year, docType);
		}
		records.setRecords(list);
		return records;
	}

	@DELETE
	@Path("/{param}")
	public Response removeResult(@PathParam("param") String symbol,
			@QueryParam("year") String year, @QueryParam("docType") String docType) {
		Record record = new Record(docType, null, symbol, year, null);
		record.remove(symbol, year, docType);
		return Response.status(200).entity("Remove a result with the symbol "+symbol).build();
	}
	
	//delete all records
	@DELETE
	public Response removeAllResult(){
		Record.removeAll();
		return Response.status(200).entity("Remove all result.").build();
		
	}
}

class Records {
	List<Record> records;

	/**
	 * @return the records
	 */
	public List<Record> getRecords() {
		return records;
	}

	/**
	 * @param records
	 *            the records to set
	 */
	public void setRecords(List<Record> records) {
		this.records = new ArrayList<Record>(records);
	}

}