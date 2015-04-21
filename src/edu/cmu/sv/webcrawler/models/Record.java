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
	String sha256;

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

	public void setSha256(String sha256) {
		this.sha256 = sha256;
	}
	
	public String getSha256() {
		return this.sha256;
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
				", wordCount=" + wordCount + ", sha256=" + this.sha256 + "]";
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
		System.out.printf("Saving from record\n");
		doc.put("riskFactor", this.riskFactor);
		System.out.printf("Saving done from record\n");
		doc.put("keywords", list);
		doc.put("url", url);
		doc.put("document", document);
		doc.put("SIC", SIC);
		doc.put("SICName", SICName);
		doc.put("wordCount", wordCount);

		this.sha256 = Hex.encodeHexString(DigestUtils.sha256(this.riskFactor));
		System.out.printf("[Debug]: Record save() calculated hash value %s\n", this.sha256);
		doc.put("sha256", this.sha256);

		//this will add extra work load for database, could think about any other way to check redundancy.
		List<Record> recordList = this.searchBySha256(this.symbol, this.sha256);

		//if there is no matching document in the MongoDB, insert the doc
		if(recordList.size() == 0) {
			System.out.printf("[Debug] Current doc with sha256 %s not existed in DB\n",this.sha256);
			db.insert(doc);
		}
		else
			System.out.printf("[Debug] Current doc with sha256 %s already existed in DB\n",this.sha256);

		this.keywords = map;
		return true;
	}

	/*
		TODO debug this function, currently not working
	 */
	public static List<Record> searchBySha256(String symbol, String sha256){
		System.out.printf("[Debug] searchBySha256(%s,%s)\n",symbol,sha256);
		DBCollection db = MongoHelper.getCollection();
		BasicDBObject query = new BasicDBObject();
		query.put("symbol", symbol);
		query.put("sha256", sha256);
		DBCursor cursor = db.find(query);
		int docCnt = 0;
		List<Record> recordList = new ArrayList<Record>();
		try{
			while(cursor.hasNext()){
				System.out.printf("[Debug] searchBySha256() find a doc\n");
				docCnt++;
				if(docCnt > 1){
					System.out.printf("[WARNING]: searchBySha256() hash value collision happen\n");
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
		String sha256 = (String) obj.get("sha256");

		BasicDBList keywords = (BasicDBList) obj.get("keywords");
		Map<String, Integer> map = Keywords.getMap(keywords);
		Record record = new Record(docType, riskFactor, symbol, year, map);
		record.setCompanyName(companyName);
		record.setSIC(SIC);
		record.setSICName(SICName);
		record.setUrl(url);
		record.setWordCount(wordCount);
		record.setSha256(sha256);
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

	public static List<Record> search(String symbol, String year) {
		List<Record> records = new ArrayList<Record>();
		DBCollection db = MongoHelper.getCollection();
		BasicDBObject doc = new BasicDBObject();
		doc.put("symbol", symbol);
		doc.put("year", year);
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
		doc.put("year", year);
		doc.put("document", docType);
		DBCursor cursor = db.find(doc);
		try {
			while (cursor.hasNext()) {
				DBObject obj = cursor.next();
				Record record = getRecordFromDBObject(obj);
				System.out.printf("[Debug]: Record Search() Find one %s record for %s %s sha256=%s!\n",
						docType, symbol, year,record.getSha256());
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
		/*
		List<Record> results;
		results = test.searchBySha256("IBM","7a940b5d42a954438df76bd05358771c3c08477cb26032271e68455ea0c4de02");
		for(Record record : results){
			System.out.printf("%s\n",record.toString());
		}*/
		test.searchBySha256("IBM","e1c93ee40e9d1ba2d13e885d86d7a8f9a8a80f72e98a4c75ad411ce20d9d8379");
	}
}
