package edu.cmu.sv.webcrawler.services;

import edu.cmu.sv.webcrawler.models.Record;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Iterator;


import net.htmlparser.jericho.Source;

public class Get10K {

	private StringBuffer Get10kContent(String urlStr) {
		int chByte = 0;
		URL url = null;
		HttpURLConnection httpConn = null;
		InputStream in = null;
		StringBuffer sb = new StringBuffer("");

		try {
			// int len = 0;
			url = new URL(urlStr);
			httpConn = (HttpURLConnection) url.openConnection();
			HttpURLConnection.setFollowRedirects(true);
			httpConn.setRequestMethod("GET");

			in = httpConn.getInputStream();

			chByte = in.read();
			while (chByte != -1) {
				// len++;
				sb.append((char) chByte);
				chByte = in.read();
			}
			// System.out.println(len);
		} catch (MalformedURLException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				in.close();
				httpConn.disconnect();
			} catch (Exception ex) {
				ex.printStackTrace();
			}
		}
		return sb;
	}

	/**
	 * Download 10-k files for a given company using CIK or symbol
	 * 
	 * @param symbol
	 * @param isCurrent
	 *            true - download 10K for the day
	 * @return return 1 when no error(s) occurs, 
	 * 			return -1 when no URLs is fetched from the given symbol
	 */
	public int Download10KbyCIK(String symbol, boolean isCurrent) {
		GetURL gURL = new GetURL();
		
		ArrayList<String> urls = gURL.GetURLwithCIK(symbol, isCurrent,"10-K");
		if(urls.size() == 0)
			return -1;
		
		String companyName = gURL.GetCompanyNameFromsBuffer();
		String SIC = gURL.GetSICFromsBuffer();
		String SICName = gURL.GetSICNameFromsBuffer();
		
		Iterator<String> it = urls.iterator();
		while (it.hasNext()) {
			String str = it.next();
			int index0 = str.indexOf("data");
			int index1 = str.indexOf("/", index0 + 5);
			String CIK = str.substring(index0 + 5, index1);
			int index2 = str.lastIndexOf('.');
			if (index2 <= 14)
				continue;
			String year, url;
			if (isCurrent == false) {
				url = str.substring(0, str.length() - 2);
				year = str.substring(str.length() - 2);
				if (Integer.parseInt(year) < 60) {
					year = "20" + year;
				} else {
					year = "19" + year;
				}
			} else {
				year = "2014";
				url = str;
			}
			String ext = url.substring(index2);
			StringBuffer sb_10K = Get10kContent(url);
			String s_10K = null;
			if (ext.equals(".txt")) {
				s_10K = sb_10K.toString();
			} else if (sb_10K != null) {
				s_10K = extractAllText(sb_10K.toString());
			}
			
			System.out.printf("companyName = [%s], SIC = [%s],SICName = [%s]\n",companyName,SIC,SICName );
			output(s_10K, year, symbol, companyName, SIC, SICName, url);	
		}
		return 1;
	}

	/**
	 * 
	 * Output all the s_10k into MongoDB
	 * 
	 * @param s_10K
	 * @param year
	 * @param symbol
	 * @param companyName
	 * @param SIC
	 * @param SICName
	 * @param url
	 */
	private void output(String s_10K, String year, 
			String symbol, String companyName, 
			String SIC, String SICName, String url) {
		if (s_10K == null || s_10K.isEmpty()) {
			return;
		}
		Record record = new Record("10-K", s_10K, symbol, year, null);
		record.remove(symbol, year);
		record.setCompanyName(companyName);
		record.setSIC(SIC);
		record.setSICName(SICName);
		record.setUrl(url);	
		record.save();
	}

	/**
	 * 
	 * Download 10-k files for a list of companies
	 * 
	 * @param filename
	 */
	public void Download10KbyCIKList(String filename) {
		try {
			FileReader fr = new FileReader(filename);
			BufferedReader br = new BufferedReader(fr);
			String str = br.readLine();
			while (str != null) {
				Download10KbyCIK(str, false);
				str = br.readLine();
			}
			br.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public String extractAllText(String htmlText) {
		Source source = new Source(htmlText);
		String page = source.getTextExtractor().toString().toLowerCase();
		boolean flag = true;
		int start = 0, start_risk = 0, end = 0;
		while (flag) {
			start = page.indexOf("item 1a", start + 1);
			start_risk = page.indexOf("risk factors", start + 1);
			if (start == -1 || start_risk == -1) {
				return null;
			}
			if ((page.charAt(start - 1) != ' ' && page.charAt(start - 1) != '.')
					|| (page.charAt(start + 7) != ' ' && page.charAt(start + 7) != '.')
					|| (page.charAt(start_risk - 1) != ' ' && page
							.charAt(start_risk - 1) != '.')
					|| start_risk - start > 20) {
				continue;
			}
			page = page.substring(start);
			end = page.indexOf("unresolved staff comments");
			if (end > 100) {
				return page.substring(0, end + 10);
			}
		}
		return null;
	}

	// Main
	public static void main(String[] args) {
		System.out.println("Start crawling from www.sec.gov...");

		String CIK = "IBM";
		Get10K g10K = new Get10K();
		//test case where symbol is valid.
		if(g10K.Download10KbyCIK(CIK, false) < 0)
			System.out.printf("Errors when fetching for %s\n",CIK);
		System.out.printf("Test passed for valid symbol\n");
		
		CIK = "ThisDoesNotExist";
		//test case where symbol is not valid.
		if(g10K.Download10KbyCIK(CIK,false) < 0)
			System.out.printf("Errors when fetching for %s\n",CIK);
		System.out.printf("Test passed for invalid symbol\n");
		System.out.println("Finished Testing.");
	}
}