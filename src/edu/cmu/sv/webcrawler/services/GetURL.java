package edu.cmu.sv.webcrawler.services;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;

/* This class retrives the urls of the annual reports in the website that belongs
 * to the company that is to be searched
 */

public class GetURL {
	private ArrayList<String> URLs;
	private StringBuffer sBuffer;
	
	public GetURL() {
		sBuffer = new StringBuffer();
		URLs = new ArrayList<String>();
	}
	
	private void ParseURLs(boolean isCurrent) {
		int startIndex = 0, endIndex = 0;
		
		int theCounter = 0;
		
		while(true) {
			startIndex = sBuffer.indexOf("/Archives/edgar/data", endIndex);
			if(startIndex == -1) {
				return;
			}
			endIndex = sBuffer.indexOf("\"", startIndex);
			String str = sBuffer.substring(startIndex, endIndex);
			String year = "";
			if(isCurrent == false) {
				int index = str.indexOf("-");
				year = str.substring(index+1, index+3);
			}
			str = "http://www.sec.gov" + str;
			URLs.add("http://www.sec.gov" + this.ParseIntoURLs(str)+year);
			
			
			
			theCounter++;
			
			if (theCounter == 3) break;
			
			if(Integer.parseInt(year) <= 11) {
				break;
			}
		}
	}
	
	private String ParseIntoURLs(String urlStr) {
		StringBuffer sb = Get10kSearchPage(urlStr);
		String str = "";
		int startIndex = 0, endIndex = 0;
		while(true) {
			startIndex = sb.indexOf("/Archives/edgar/data", endIndex);
			if(startIndex == -1) {
				break;
			}
			endIndex = sb.indexOf("\"", startIndex);
			str = sb.substring(startIndex, endIndex);
			int index = str.lastIndexOf('.');
			if(index != -1) {
				break;
			}
		}
		return str;
	}
	
	public ArrayList<String> GetURLwithCIK(String CIK, boolean isCurrent, String documentType) {
		String queryURL;
		if(isCurrent == false) {
			queryURL = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=" + documentType + "&CIK=";
			this.sBuffer = Get10kSearchPage(queryURL + CIK);
		}
		else {
			queryURL = "http://www.sec.gov/cgi-bin/current.pl?q1=1&q2=0";
			this.sBuffer = Get10kSearchPage(queryURL);
		}				
		ParseURLs(isCurrent);
		
		return URLs;
	}
	
	/**
	 * This function must be called after GetURLwithCIK()
	 * @return the companyName
	 */
	public String GetCompanyNameFromsBuffer(){
		String companyName = null;
		
		int startIndex = sBuffer.indexOf("companyName") + 13;     // the start index is end of "<span class="companyName">"
		int endIndex = sBuffer.indexOf("<acronym");               // the end index is start of "<acronym title="
		
		companyName = sBuffer.substring(startIndex, endIndex).trim();
		return companyName;
	}
	
	/**
	 * This function must be called after GetURLwithCIK()
	 * @return the SIC of the company
	 */
	public String GetSICFromsBuffer(){
		String SIC = null;
		String SICKeyword = "SIC</acronym>";
		String tmp = this.sBuffer.toString();
		//Currently it's a very stupid implementation of getting SIC of the company.
		int idxOfSIC = tmp.indexOf(SICKeyword);
		String tmp2 = tmp.substring(idxOfSIC + SICKeyword.length());
		String tmp3 = tmp2.substring(tmp2.indexOf(">") + 1,tmp2.indexOf("</a>"));
		SIC = tmp3;
		return SIC;
	}
	

	public String GetSICNameFromsBuffer(){
		String SICName = null;
		String SICKeyword = "SIC</acronym>";
		String tmp = this.sBuffer.toString();
		//Currently it's a very stupid implementation of getting SICName of the company.
		int idxOfSIC = tmp.indexOf(SICKeyword);
		String tmp2 = tmp.substring(idxOfSIC + SICKeyword.length());
		String tmp3 = tmp2.substring(tmp2.indexOf("</a>") + 7);
		String tmp4 = tmp3.substring(0,tmp3.indexOf("<br"));
		SICName = tmp4;
		return SICName;
	}

	private StringBuffer Get10kSearchPage(String urlStr)
    {
        /** the length of input stream */
        int chByte = 0;
        
        URL url = null;
        
        /** HTTP connection */
        HttpURLConnection httpConn = null;
        
        InputStream in = null;
        
        StringBuffer sb = new StringBuffer("");

        try
        {
        	//int len = 0;
            url = new URL(urlStr);
            httpConn = (HttpURLConnection) url.openConnection();
            HttpURLConnection.setFollowRedirects(true);
            httpConn.setRequestMethod("GET"); 
            
            in = httpConn.getInputStream();
            
            chByte = in.read();
            while (chByte != -1)
            {
            	//len++;
            	sb.append((char)chByte);
                chByte = in.read();
            }
            System.out.println();
        }
        catch (MalformedURLException e)
        {
            e.printStackTrace();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                in.close();
                httpConn.disconnect();
            }
            catch (Exception ex)
            {
                ex.printStackTrace();
            }
        }
        return sb;
    }
	
	public static void main(String Args[]){
		GetURL tester = new GetURL();
		tester.GetURLwithCIK("IBM",false,"10-K");
		tester.GetCompanyNameFromsBuffer();
		return ;
	}
}