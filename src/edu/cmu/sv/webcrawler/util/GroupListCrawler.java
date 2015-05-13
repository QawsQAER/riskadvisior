package edu.cmu.sv.webcrawler.util;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class GroupListCrawler {
	private static String GET_GROUP_LIST = "http://catalog.data.gov/api/3/action/group_list";
	private List<String> groupList;

	private static String readAll(Reader rd) throws IOException {
		StringBuilder sb = new StringBuilder();
		int cp;
		while ((cp = rd.read()) != -1) {
			sb.append((char) cp);
		}
		return sb.toString();
	}

	public static JSONObject readJsonFromUrl(String url) throws IOException,
			JSONException {
		InputStream is = new URL(url).openStream();
		try {
			BufferedReader rd = new BufferedReader(new InputStreamReader(is,
					Charset.forName("UTF-8")));
			String jsonText = readAll(rd);
			JSONObject json = new JSONObject(jsonText);
			return json;
		} finally {
			is.close();
		}
	}

	public GroupListCrawler() throws IOException, JSONException {
		List<String> groupList = new ArrayList<String>();
		JSONObject json = readJsonFromUrl(GET_GROUP_LIST);
		JSONArray result = json.getJSONArray("result");
		for (int i = 0; i < result.length(); i++) {
			String cur = result.getString(i);
			groupList.add(cur);
		}
		this.groupList = groupList;
	}

	public List<String> getGroupList() {
		return groupList;
	}

	public void setGroupList(List<String> groupList) {
		this.groupList = groupList;
	}

}
