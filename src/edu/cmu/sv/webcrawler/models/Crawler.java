package edu.cmu.sv.webcrawler.models;

import edu.cmu.sv.webcrawler.services.Get10K;
import edu.cmu.sv.webcrawler.services.GetRiskFactor;
import edu.cmu.sv.webcrawler.services.RequiredInfo;
import java.util.List;

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
		GetRiskFactor g = new GetRiskFactor();
		List<RequiredInfo> l = g.DownloadByCIKAndType(symbol, false, docType);
		for(RequiredInfo info : l)
			g.save(info);
		return 1;
	}
}
