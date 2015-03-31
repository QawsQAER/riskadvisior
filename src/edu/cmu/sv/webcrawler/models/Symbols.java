package edu.cmu.sv.webcrawler.models;

import java.util.HashSet;
import java.util.Set;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import com.mongodb.BasicDBObject;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;

import edu.cmu.sv.webcrawler.util.MongoHelper;

public class Symbols {

	private DBCollection collection;
	
	public Symbols(){
		MongoHelper helper = new MongoHelper();
		this.collection = helper.getDb().getCollection("companysymbols");
	}
	
	public void insert(String symbol) {
		BasicDBObject doc = new BasicDBObject();
		doc.put("symbol", symbol);
		collection.insert(doc);
	}
	
	public void removeAll() {
		BasicDBObject doc = new BasicDBObject();
		collection.remove(doc);
	}
	
	/**
	 * @return the symbols
	 */
	public Set<String> getSymbols() {
		Set<String> symbols = new HashSet<String>();
		DBCursor cursor = collection.find();
		try {
			while (cursor.hasNext()) {
				DBObject obj = cursor.next();
				String tmp = (String) obj.get("symbol");
				symbols.add(tmp);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return symbols;
	}
	
	/**
	 * @param symbols the symbols to set
	 */
//	public void setSymbols(List<String> symbols) {
//		this.symbols = symbols;
//	}
	
	//TODO: finish this loadFromJSONFile function.
	/**
	 * @param filepath is the path to the json file
	 * @return this function will load the symbols from the json file
	 */
	public void loadFromJSONFile(String filepath){
		
	}
}
