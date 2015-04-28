package edu.cmu.sv.webcrawler.models;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import com.mongodb.BasicDBList;
import com.mongodb.BasicDBObject;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;

import com.sun.org.apache.xpath.internal.operations.Bool;
import edu.cmu.sv.webcrawler.services.KeywordExtractor;
import edu.cmu.sv.webcrawler.services.KeywordsService;
import edu.cmu.sv.webcrawler.util.MongoHelper;
import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.digest.DigestUtils;

public class Record {

	String companyName;
	String year;
	String riskFactor;
	String symbol;
	String document;
	String url;
	String SIC;
	String SICName;
	String wordCount;
	//hash value for the riskFactor string

	Map<String, Integer> keywords;
	Map<String, Integer> categories;
	
	public Record() {
		
	}
	
	public Record(String document, String riskFactor, String symbol, String year,
			Map<String, Integer> keywords) {
		this.year = year;
		this.riskFactor = riskFactor;
		this.symbol = symbol;
		this.keywords = keywords;
		this.document = document;
	}
	
	/**
	 * @return the keywords
	 */
	public Map<String, Integer> getKeywords() {
		return keywords;
	}

	/**
	 * @param keywords
	 *            the keywords to set
	 */
	public void setKeywords(Map<String, Integer> keywords) {
		this.keywords = keywords;
	}

	/**
	 * @return the companyName
	 */
	public String getCompanyName() {
		return companyName;
	}

	/**
	 * @param companyName
	 *            the companyName to set
	 */
	public void setCompanyName(String companyName) {
		this.companyName = companyName;
	}
	
	/**
	 * @return the SIC
	 */
	public String getSIC() {
		return SIC;
	}

	/**
	 * @param SIC
	 *            the SIC to set
	 */
	public void setSIC(String SIC) {
		this.SIC = SIC;
	}
	
	/**
	 * @return the SICName
	 */
	public String getSICName() {
		return SICName;
	}

	/**
	 * @param SICName
	 *            the SICName to set
	 */
	public void setSICName(String SICName) {
		this.SICName = SICName;
	}
	
	/**
	 * @return the url
	 */
	public String getUrl() {
		return url;
	}

	/**
	 * @param url
	 *            the url to set
	 */
	public void setUrl(String url) {
		this.url = url;
	}

	/**
	 * @return the year
	 */
	public String getYear() {
		return year;
	}

	/**
	 * @param year
	 *            the year to set
	 */
	public void setYear(String year) {
		this.year = year;
	}

	/**
	 * @return the riskFactor
	 */
	public String getRiskFactor() {
		return riskFactor;
	}

	/**
	 * @param riskFactor
	 *            the riskFactor to set
	 */
	public void setRiskFactor(String riskFactor) {
		this.riskFactor = riskFactor;
	}

	/**
	 * @return the symbol
	 */
	public String getSymbol() {
		return symbol;
	}

	/**
	 * @param symbol
	 *            the symbol to set
	 */
	public void setSymbol(String symbol) {
		this.symbol = symbol;
	}
	
	/**
	 * @return the wordCount
	 */
	public String getWordCount() {
		return wordCount;
	}

	/**
	 * @param wordCount
	 *            the wordCount to set
	 */
	public void setWordCount(String wordCount) {
		this.wordCount = wordCount;
	}
	
	/**
	 * @return the document
	 */
	public String getDocument() {
		return document;
	}

	
	/*
	 * (non-Javadoc)
	 * 
	 * @see java.lang.Object#toString()
	 */
	@Override
	public String toString() {
		return "Record [companyName" + companyName + ", year=" + year + ", riskFactor=" + riskFactor
				+ ", symbol=" + symbol + ", url=" + url + ", SIC=" + SIC + ", SICName=" + SICName +
				", wordCount=" + wordCount + "]";
	}

	/**
	 * Save the record into MongoDB
	 * 
	 * @param companyName
	 * @param year
	 * @param symbol
	 * @return
	 */
	public boolean save() {
		DBCollection db = MongoHelper.getCollection();
		BasicDBObject doc = new BasicDBObject();
		
		KeywordsService ks = new KeywordExtractor(riskFactor);
		
		Map<String, Integer> map = ks.getKeywordsBySymbol();
		this.wordCount = String.valueOf(ks.getWordTotalCount());
		
		BasicDBList list = new BasicDBList();
		
		for (String s : map.keySet()) {
			DBObject tmp = new BasicDBObject();
			tmp.put(s, map.get(s));
			list.add(tmp);
		}
		
		//System.out.println("wordcount in record: " + wordCount);
		
		doc.put("symbol", symbol);
		doc.put("companyName", companyName);
		doc.put("year", year);
		doc.put("riskFactor", this.riskFactor);
		doc.put("keywords", list);
		doc.put("url", url);
		doc.put("document", document);
		doc.put("SIC", SIC);
		doc.put("SICName", SICName);
		doc.put("wordCount", wordCount);
		System.out.printf("[Debug] saving %s\n",url);


		//this will add extra work load for database, could think about any other way to check redundancy.
		List<Record> recordList = this.searchByUrl(this.symbol,this.url);

		//if there is no matching document in the MongoDB, insert the doc
		if(recordList.size() == 0) {
			System.out.printf("[Debug] Current doc with url %s not existed in DB\n",this.url);
			db.insert(doc);
		}
		else
			System.out.printf("[Debug] Current doc with url %s already existed in DB\n",this.url);

		this.keywords = map;
		return true;
	}


	public static List<Record> searchByUrl(String symbol, String url){
		System.out.printf("[Debug] searchByUrl(%s,%s)\n",symbol,url);
		DBCollection db = MongoHelper.getCollection();
		BasicDBObject query = new BasicDBObject();
		query.put("symbol", symbol);
		query.put("url", url);
		DBCursor cursor = db.find(query);
		int docCnt = 0;
		List<Record> recordList = new ArrayList<Record>();
		try{
			while(cursor.hasNext()){
				System.out.printf("[Debug] searchByUrl() find a doc\n");
				docCnt++;
				if(docCnt > 1){
					System.out.printf("[WARNING]: searchByUrl() collision happen\n");
				}
				DBObject obj = cursor.next();
				Record record = getRecordFromDBObject(obj);
				recordList.add(record);
			}
		}catch (Exception e){
			e.printStackTrace();
		}
		return recordList;
	}

	public static Record getRecordFromDBObject(DBObject obj){
		String symbol = (String) obj.get("symbol");
		String year = (String) obj.get("year");
		String riskFactor = (String) obj.get("riskFactor");
		String companyName = (String) obj.get("companyName");
		String SIC = (String) obj.get("SIC");
		String SICName = (String) obj.get("SICName");
		String url = (String) obj.get("url");
		String wordCount = (String) obj.get("wordCount");
		String docType = (String) obj.get("document");

		BasicDBList keywords = (BasicDBList) obj.get("keywords");
		Map<String, Integer> map = Keywords.getMap(keywords);
		Record record = new Record(docType, riskFactor, symbol, year, map);
		record.setCompanyName(companyName);
		record.setSIC(SIC);
		record.setSICName(SICName);
		record.setUrl(url);
		record.setWordCount(wordCount);
		return record;
	}

	public static List<Record> search(String symbol) {
		List<Record> records = new ArrayList<Record>();
		DBCollection db = MongoHelper.getCollection();
		BasicDBObject doc = new BasicDBObject();
		doc.put("symbol", symbol);
		DBCursor cursor = db.find(doc);
		try {
			while (cursor.hasNext()) {
				DBObject obj = cursor.next();
				Record record = getRecordFromDBObject(obj);
				records.add(record);
			}
		} catch (Exception e) {
		}
		return records;
	}
	
	public static List<Record> search(String symbol, String year, String docType) {
		List<Record> records = new ArrayList<Record>();
		DBCollection db = MongoHelper.getCollection();
		BasicDBObject doc = new BasicDBObject();
		doc.put("symbol", symbol);
		if (year != null)
			doc.put("year", year);
		if (docType != null)
			doc.put("document", docType);
		DBCursor cursor = db.find(doc);
		try {
			while (cursor.hasNext()) {
				DBObject obj = cursor.next();
				Record record = getRecordFromDBObject(obj);
				System.out.printf("[Debug]: Record Search() Find one %s record for %s %s\n",
						docType, symbol, year);
				records.add(record);
			}
		} catch (Exception e) {
		}
		return records;
	}

	public void remove(String symbol, String year) {
		DBCollection db = MongoHelper.getCollection();
		BasicDBObject doc = new BasicDBObject();
		doc.put("symbol", symbol);
		if (year != null && !year.isEmpty()) {
			doc.put("year", year);
		}
		db.remove(doc);
	}
	
	public void remove(String symbol, String year, String docType) {
		DBCollection db = MongoHelper.getCollection();
		BasicDBObject doc = new BasicDBObject();
		doc.put("symbol", symbol);
		if (year != null && !year.isEmpty()) {
			doc.put("year", year);
		}
		if (docType != null && !docType.isEmpty()) {
			doc.put("document", docType);
		}
		db.remove(doc);
	}

	public static void removeAll() {
		DBCollection db = MongoHelper.getCollection();
		BasicDBObject doc = new BasicDBObject();
		db.remove(doc);
	}

	public static void main(String argv[]){
		Record test = new Record();
		
	}
}
