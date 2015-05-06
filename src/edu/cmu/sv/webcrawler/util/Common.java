package edu.cmu.sv.webcrawler.util;

public class Common {
	public static final String DATE_PATTERN = "yyyy-MM-dd'T'HH:mm:ssz";
	public static String formatCountJson(int count, String json)
	{
		return ("{\"count\":"+count+",\"content\":"+json+"}");
	}
}
