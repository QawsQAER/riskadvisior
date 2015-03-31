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
		Get10K g=new Get10K();
		return g.Download10KbyCIK(symbol, false);
	}
}
