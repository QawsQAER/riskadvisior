package edu.cmu.sv.webcrawler.models;

import java.util.List;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import edu.cmu.sv.webcrawler.util.MongoHelper;

public class Symbols {

	List<String> symbols;
	public Symbols(){
		MongoHelper helper=new MongoHelper();
		this.symbols=helper.getAllSymbols();
	}
	/**
	 * @return the symbols
	 */
	public List<String> getSymbols() {
		return symbols;
	}
	/**
	 * @param symbols the symbols to set
	 */
	public void setSymbols(List<String> symbols) {
		this.symbols = symbols;
	}
	
	//TODO: finish this loadFromJSONFile function.
	/**
	 * @param filepath is the path to the json file
	 * @return this function will load the symbols from the json file
	 */
	public void loadFromJSONFile(String filepath){
		
	}
}
