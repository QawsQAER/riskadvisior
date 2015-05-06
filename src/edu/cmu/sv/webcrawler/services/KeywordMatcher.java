package edu.cmu.sv.webcrawler.services;

import edu.cmu.sv.webcrawler.models.Keywords;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class KeywordMatcher {
	private Set<String> keywords;
	public KeywordMatcher(){
		/*keywords = new HashSet<String>();
		BufferedReader buff;
		try {
			buff = new BufferedReader(new FileReader("keywords.txt"));
			boolean eof = false;
			String line = buff.readLine();
			while (!eof) {
				line = buff.readLine();
				if (line == null)
					eof = true;
				else{
					//System.out.println(line);//for test only
					keywords.add(line);
				}
			}
			buff.close();*/
		keywords=new Keywords().getKeywords();
		/*} catch (IOException e) {
			e.printStackTrace();
		}*/
		keywords = new HashSet<String>();

		Keywords key = new Keywords();
		keywords = (HashSet<String>)key.getKeywords();
//		BufferedReader buff;
//		try {
//			buff = new BufferedReader(new FileReader("keywords.txt"));
//			boolean eof = false;
//			String line = buff.readLine();
//			while (!eof) {
//				line = buff.readLine();
//				if (line == null)
//					eof = true;
//				else{
//					//System.out.println(line);//for test only
//					keywords.add(line);
//				}
//			}
//			buff.close();
//		} catch (IOException e) {
//			e.printStackTrace();
//		}

	}
	
	public HashMap<String, Integer> getKeywordMatch(String riskfactor){
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		
		for (String str : keywords) {
			int count = 0;
			int index = -1;
			while (true) {
				index = riskfactor.indexOf(str, index + 1);
			    if (index > 0) {
			    	count++;
			    } else {
			    	map.put(str, count);
			    	break;
			    }
			}
		}
//		used for test
//		for (String key : map.keySet()) {
//			   System.out.println("key= "+ key + " and value= " + map.get(key));
//		}
		return map; 
	}
	
	// test code
	public static void main(String[] args){
		KeywordMatcher keywordmatcher = new KeywordMatcher();
		keywordmatcher.getKeywordMatch("loss of business, yes today loss of business as kjsd");
	}
}
