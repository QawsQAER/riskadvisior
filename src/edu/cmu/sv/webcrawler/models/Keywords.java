package edu.cmu.sv.webcrawler.models;

import com.mongodb.*;
import edu.cmu.sv.webcrawler.util.MongoHelper;

import java.util.*;

public class Keywords {

	private DBCollection collection;

	public Keywords() {
		MongoHelper helper = new MongoHelper();
		this.collection = helper.getDb().getCollection("keywords");
	}

	public void insert(String line) {
		BasicDBObject obj = new BasicDBObject();
		obj.put("value", line);
		collection.insert(obj);
	}

	public Set<String> getKeywords() {
		Set<String> set = new HashSet<String>();
		DBCursor cursor = collection.find();
		try {
			while (cursor.hasNext()) {
				DBObject obj = cursor.next();
				String tmp = (String) obj.get("value");
				set.add(tmp);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return set;
	}

	public void removeAll() {
		BasicDBObject doc = new BasicDBObject();
		collection.remove(doc);
	}

	public Map<String, Integer> getKeywords(String symbol,String year) {
        Map<String, Integer> result=new HashMap<String,Integer>();
		BasicDBObject doc = new BasicDBObject();
		doc.put("symbol", symbol);
		doc.put("year", year);
		DBCursor cursor = MongoHelper.getCollection().find(doc);
		Map<String, Integer> map = null;
		while (cursor.hasNext()) {
			DBObject obj = cursor.next();
			BasicDBList keywords = (BasicDBList) obj.get("keywords");
			map = getMap(keywords);
            merge(result, map);
			/*break;*/
		}
		return result;
	}
	
	public Map<String, Integer> getKeywords(String symbol, String year, String docType) {
		BasicDBObject doc = new BasicDBObject();
		Map<String, Integer> result=new HashMap<String,Integer>();
		doc.put("symbol", symbol);
		doc.put("year", year);
		doc.put("document", docType);
		DBCursor cursor = MongoHelper.getCollection().find(doc);
		Map<String, Integer> map = null;
		while (cursor.hasNext()) {
			DBObject obj = cursor.next();
			BasicDBList keywords = (BasicDBList) obj.get("keywords");
			map = getMap(keywords);
			merge(result, map);
			/*break;*/
		}
		return result;
	}
	
	public Map<String, Integer> getKeywordsFrequency(String symbol, String year, String docType) {
		BasicDBObject doc = new BasicDBObject();
		Map<String, Integer> result=new HashMap<String,Integer>();
		doc.put("symbol", symbol);
		doc.put("year", year);
		doc.put("document", docType);
		DBCursor cursor = MongoHelper.getCollection().find(doc);
		Map<String, Integer> map = null;
		String wordCount;
		while (cursor.hasNext()) {
			DBObject obj = cursor.next();
			BasicDBList keywords = (BasicDBList) obj.get("keywords");
			wordCount = (String) obj.get("wordCount");
			map = getFrequencyMap(keywords, wordCount);
			merge(result, map);
		}
		return result;
	}

    private void merge( Map<String, Integer> a,  Map<String, Integer> b){
        for(String key:b.keySet()){
            int v_b=b.get(key);
            if(a.containsKey(key)){
                int v_a=a.get(key);
                a.put(key,v_a+v_b);
            }
            else a.put(key,v_b);
        }

    }


	public static Map<String, Integer> getMap(BasicDBList keywords) {
		Map<String,Integer> map = new HashMap<String,Integer>();
		for (Iterator<Object> it = keywords.iterator(); it.hasNext();) {
			BasicDBObject dbo = (BasicDBObject) it.next();
			for (String s : dbo.keySet()) {
				map.put(s, dbo.getInt(s));
			}
		}
		return map;
	}
	
	public static Map<String, Integer> getFrequencyMap(BasicDBList keywords, String wordCount) {
		Map<String, Integer> map = new HashMap<String, Integer>();
		int wc = Integer.parseInt(wordCount);
		for (Iterator<Object> it = keywords.iterator(); it.hasNext();) {
			BasicDBObject dbo = (BasicDBObject) it.next();
			for (String s : dbo.keySet()) {
				map.put(s, (dbo.getInt(s)*100000 / wc));
			}
		}
		return map;
	}
}
