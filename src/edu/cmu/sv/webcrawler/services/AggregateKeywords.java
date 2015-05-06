package edu.cmu.sv.webcrawler.services;

import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class AggregateKeywords {
	
	public HashMap<String, Integer> aggregate(List<RequiredInfo> type){
		HashMap<String, Integer> results = new HashMap<String, Integer>();
		
		for(RequiredInfo requiredInfo: type){
			HashMap<String, Integer> keywords = new HashMap<String, Integer>();
			keywords = requiredInfo.getKeywords();
			Iterator<?> iter = keywords.entrySet().iterator();
			while (iter.hasNext()) {
				@SuppressWarnings("rawtypes")
				Map.Entry entry = (Map.Entry) iter.next();
				String key = (String)entry.getKey();
				int val = (int)entry.getValue();
				if(results.containsKey(key)){
					int old = results.get(key);
					results.put(key, old+val);
				}
				else{
					results.put(key, val);
				}
			}			
		}
		return results;
	}
}
