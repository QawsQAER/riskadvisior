package edu.cmu.sv.webcrawler.models;

import edu.cmu.sv.webcrawler.services.Get10K;

public class Crawler {
	
	/**
	 * 
	 * @param symbol, 
	 * 				the CIK symbol for certian company
	 * @return 1 when Download10KbyCIK success, 
	 * 			-1 when Download10KbyCIK fail
	 */
	public int crawl(String symbol){
		//should try to call different crawling function here
		Get10K g=new Get10K();
		return g.Download10KbyCIK(symbol, false);
	}
	
	/**
	 * 
	 * @param symbol, 
	 * 				the CIK symbol for certian company
	 * @param docType,
	 * 				the documentType being crawled
	 * @return 1 when Download10KbyCIK success, 
	 * 			-1 when Download10KbyCIK fail
	 */
	public int crawl(String symbol, String docType){
		return 1;
	}
}
