package edu.cmu.sv.webcrawler.services;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.StringReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.apache.commons.codec.binary.Base64;
import org.apache.http.NameValuePair;
import org.apache.http.client.fluent.Executor;
import org.apache.http.client.fluent.Request;
import org.apache.http.client.utils.URLEncodedUtils;
import org.apache.http.entity.ContentType;
import org.apache.http.message.BasicNameValuePair;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;

import com.firebase.client.Firebase;

import net.htmlparser.jericho.Source;
import edu.cmu.sv.webcrawler.models.*;

public class GetRiskFactor {

	private StringBuffer GetContent(String urlStr) {
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
	 * @param documentType
	 */
	public List<RequiredInfo> DownloadByCIKAndType(String symbol, boolean isCurrent,
			String documentType) {
		GetURL gURL = new GetURL();
		List<RequiredInfo> resultList = new ArrayList<RequiredInfo>();
		
		
		ArrayList<String> URLs = gURL.GetURLwithCIK(symbol, isCurrent,
				documentType);
		String companyName = gURL.GetCompanyNameFromsBuffer();
		String SIC = gURL.GetSICFromsBuffer();
		String SICName = gURL.GetSICNameFromsBuffer();
		System.out.printf("companyName is %s, SIC is %S, SICName is %s\n",companyName,SIC,SICName);
		Iterator<String> it = URLs.iterator();

		while (it.hasNext()) {
			RequiredInfo result = new RequiredInfo();
			result.setDocumentType(documentType);
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
				// if(url != null){
				// System.out.println(url);
				// continue;
				// }
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

			// DownLoad10K(url, fileName);

			StringBuffer sb = GetContent(url);

			String s = null;
			ExtractAllTextByType exall = new ExtractAllTextByType();
			if (ext.equals(".txt")) {
				s = sb.toString();
			} else if (sb != null) {
				if (documentType.equals("10-K"))
					s = exall.extractAllText10K(sb.toString());
				else if (documentType.equals("10-Q"))
					s = exall.extractAllText10Q(sb.toString());
				else if (documentType.equals("20-F"))
					s = exall.extractAllText20F(sb.toString());
				else if (documentType.equals("8-K"))
					s = exall.extractAllText8K(sb.toString());
			}
			if(s != null)
				System.out.println("Finish one Crawl for:"+documentType);
			String[] sp = s.split(" ");
			int count = sp.length;
			result.setRiskFactor(s);
			result.setSIC(SIC);
			result.setSICName(SICName);
			//result.setSymbo(symbo);
			result.setYear(year);
			KeywordMatcher mat = new KeywordMatcher();
			result.setKeywords(mat.getKeywordMatch(s));
			result.setWordCount(count);
			result.setUrl(url);
			resultList.add(result);
			save(result);

			// BigInsights bigInsights = new BigInsights();
			//
			// String json = null;
			// try {
			// json = bigInsights.runApp(s_10K);
			// } catch (Exception e) {
			// e.printStackTrace();
			// }
			//
			// StringBuffer sb_10K_2 = new StringBuffer();
			// sb_10K_2.append(". ");
			//
			// String lines[] = json.split("}");
			//
			// for (String line : lines) {
			// String tokens[] = line.split(":|,");
			//
			// int count = Integer.parseInt(tokens[1].trim());
			// String word = tokens[3].split("}")[0].split("\"")[1];
			//
			// for (int i = 0; i < count; ++i) {
			// sb_10K_2.append(word);
			// sb_10K_2.append(". ");
			// }
			// }
			//
			// String s_10K_2 = sb_10K_2.toString();
			//
			// output(s_10K_2, year, symbol);

			// output(s_10K, year, symbol);

			// System.out.println(fileName);
		}
		return resultList;
	}

	public void save(RequiredInfo result){
		
		String documentType = result.getDocumentType();
		String riskFactor = result.getRiskFactor();
		String symbol = result.getSymbo();
		String year = result.getYear();
		Record record = new Record(documentType, riskFactor, symbol, year, null);
		record.remove(symbol, year);
		
		record.setCompanyName(result.getCompanyName());
		record.setSIC(result.getSIC());
		record.setSICName(result.getSICName());
		record.setUrl(result.getUrl());
		record.setKeywords(result.getKeywords());
		record.setWordCount(result.getWordCount()+"");
		record.save();
	}
	/**
	 * 
	 * Output all the s_10k into MongoDB
	 * 
	 * @param s_10K
	 * @param year
	 * @param symbol
	 */
	private void output(String s_10K, String year, String symbol) {
		if (s_10K == null || s_10K.isEmpty()) {
			return;
		}
		//TODO: modify this so that it matches the latest Record format
		//Record record = new Record(s_10K, symbol, year, null);
		//record.save();
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
				// Download10KbyCIK(str, false, "10-K");
				str = br.readLine();
			}
			br.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	// Main
	public static void main(String[] args) {
		System.out.println("Start crawling from www.sec.gov...");
		String CIK = "CX"; // "ABIO"
		GetRiskFactor getRisk = new GetRiskFactor();
		List<RequiredInfo> l = getRisk.DownloadByCIKAndType(CIK,false,"20-F");
		for(RequiredInfo info : l){
			getRisk.save(info);
		}
		// g10K.Download10KbyCIKList("stocksymbol");
		System.out.println("Finished crawling.");
	}
}