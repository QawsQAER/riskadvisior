package edu.cmu.sv.webcrawler.util;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import edu.cmu.sv.webcrawler.models.DataPackage;
import edu.cmu.sv.webcrawler.models.Tag;
import edu.cmu.sv.webcrawler.models.TagCloudEntry;

public class PackageCrawler {
	private static String GET_PACKAGE_BY_TAG = "http://catalog.data.gov/api/3/action/tag_show";
	private static String GET_PACKAGE_BY_GROUP = "http://catalog.data.gov/api/3/action/group_package_show";
	private static String GET_MEMBER_BY_GROUP = "http://catalog.data.gov/api/3/action/member_list";
	private String tagName;
	private List<DataPackage> dataPackages;
	private HashMap<String, Integer> tagMap;
	private List<Tag> tags;

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

	public PackageCrawler(String tagName, String type) throws IOException, JSONException {
		this.tagName = tagName;
		JSONObject json = null;
		String url = null;
		int length = 0;
		if (type.equals("tag")) {
			url = GET_PACKAGE_BY_TAG;
		}
		else {
			JSONObject members = readJsonFromUrl(GET_MEMBER_BY_GROUP+"?id="+tagName);
			length = members.getJSONArray("result").length();
			System.out.println("the legth="+length);
			url = GET_PACKAGE_BY_GROUP;
		}
		ArrayList<DataPackage> packageList = new ArrayList<DataPackage>();
		JSONArray results = null;
		if (type.equals("tag")) {
			if (tagName == null || tagName.length() == 0) {
				json = readJsonFromUrl(url);
			} else {
				json = readJsonFromUrl(url + "?id=" + tagName);
			}
			results = json.getJSONObject("result").getJSONArray(
				"packages");
			for (int i = 0; i < results.length(); i++) {
				long total = results.getJSONObject(i)
						.getJSONObject("tracking_summary").getInt("total");
				long recent = results.getJSONObject(i)
						.getJSONObject("tracking_summary").getInt("recent");
				String name = results.getJSONObject(i).getString("name");
				String id = results.getJSONObject(i).getString("id");
				String title = results.getJSONObject(i).getString("title");
				List<Tag> tags = new ArrayList<Tag>();
				JSONArray tagsJson = results.getJSONObject(i).getJSONArray("tags");
				int num_tags = results.getJSONObject(i).getInt("num_tags");
				for (int j = 0; j < num_tags; j++) {
					tags.add(new Tag(tagsJson.getJSONObject(j).getString("name")));
				}
				DataPackage dataPackage = new DataPackage(name, id, title, total, recent,
						tags);
				packageList.add(dataPackage);
			}
		}
		else {
			json = readJsonFromUrl(url + "?id=" + tagName);
			results = json.getJSONArray("result");
			for (int i = 0; i < results.length(); i++) {
				long total = results.getJSONObject(i)
						.getJSONObject("tracking_summary").getInt("total");
				long recent = results.getJSONObject(i)
						.getJSONObject("tracking_summary").getInt("recent");
				String name = results.getJSONObject(i).getString("name");
				String id = results.getJSONObject(i).getString("id");
				String title = results.getJSONObject(i).getString("title");
				List<Tag> tags = new ArrayList<Tag>();
				JSONArray tagsJson = results.getJSONObject(i).getJSONArray("tags");
				int num_tags = results.getJSONObject(i).getInt("num_tags");
				for (int j = 0; j < num_tags; j++) {
					tags.add(new Tag(tagsJson.getJSONObject(j).getString("name")));
				}
				DataPackage dataPackage = new DataPackage(name, id, title, total, recent,
						tags);
				packageList.add(dataPackage);
			}
		}
		
		dataPackages = packageList;

		HashMap<String, Integer> hashmap = new HashMap<String, Integer>();
		for (int i = 0; i < packageList.size(); i++) {
			DataPackage curPackage = packageList.get(i);
			List<Tag> curTags = curPackage.getTags();
			for (int j = 0; j < curTags.size(); j++) {
				if (hashmap.containsKey(curTags.get(j))) {
					int cur = hashmap.get(curTags.get(j).getName());
					cur = cur + curPackage.getHotDegree();
					hashmap.put(curTags.get(j).getName(), cur);
				} else {
					hashmap.put(curTags.get(j).getName(),
							curPackage.getHotDegree());
				}
			}
		}

		this.tagMap = hashmap;
		this.tags = new ArrayList<Tag>();
		for (int i = 0; i < packageList.size(); i++) {
			DataPackage curPackage = packageList.get(i);
			List<Tag> curTags = curPackage.getTags();
			for (int j = 0; j < curTags.size(); j++) {
				curTags.get(j).setHotDegree(
						hashmap.get(curTags.get(j).getName()));
			}
		}

		for (String curTag : tagMap.keySet()) {
			int cur = hashmap.get(curTag);
			Tag tag = new Tag(curTag);
			tag.setHotDegree(cur);
			tags.add(tag);
		}
	}

	public List<TagCloudEntry> getTopPackages(int num) {
		List<TagCloudEntry> returnTags = new ArrayList<TagCloudEntry>();
		Collections.sort(dataPackages, new Comparator<DataPackage>() {
			@Override
			public int compare(DataPackage o1, DataPackage o2) {
				// TODO Auto-generated method stub
				return (o2.getHotDegree() - o1.getHotDegree());
			}
		});
		int count = (num > dataPackages.size()) ? dataPackages.size() : num;
		for (int i = 0; i < count; i++) {
			TagCloudEntry entry = new TagCloudEntry(dataPackages.get(i));
//			entry.setWeight(count-i);
			returnTags.add(entry);
		}
		return returnTags;
	}

	public List<TagCloudEntry> getTopTags(int num) {
		Collections.sort(tags, new Comparator<Tag>() {
			@Override
			public int compare(Tag t1, Tag t2) {
				return t2.getHotDegree() - t1.getHotDegree();
			}
		});
		List<TagCloudEntry> returnTags = new ArrayList<TagCloudEntry>();
		int count = (num > tags.size()) ? tags.size() : num;
		for (int i = 0; i < count; i++) {
			TagCloudEntry entry = new TagCloudEntry(tags.get(i));
			entry.setWeight(count-i);
			returnTags.add(entry);
		}
		return returnTags;
	}

	public List<TagCloudEntry> getDataPackages() {
		List<TagCloudEntry> returnTags = new ArrayList<TagCloudEntry>();
		for (DataPackage pkg : dataPackages)
		{
			returnTags.add(new TagCloudEntry(pkg));
		}
		return returnTags;
	}
	
	
	public String getTagName() {
		return tagName;
	}

	public List<DataPackage> getRealDataPackages() {
		return dataPackages;
	}
	public List<Tag> getRealTags() {
		return tags;
	}

	public List<DataPackage> getRealTopPackages(int num) {
		List<DataPackage> returnTags = new ArrayList<DataPackage>();
		Collections.sort(dataPackages, new Comparator<DataPackage>() {
			@Override
			public int compare(DataPackage o1, DataPackage o2) {
				// TODO Auto-generated method stub
				return (o2.getHotDegree() - o1.getHotDegree());
			}
		});
		int count = (num > dataPackages.size()) ? dataPackages.size() : num;
		for (int i = 0; i < count; i++) {
//			entry.setWeight(count-i);
			returnTags.add(dataPackages.get(i));
		}
		return returnTags;
	}
	public List<Tag> getRealTopTags(int num) {

		Collections.sort(tags, new Comparator<Tag>() {
			@Override
			public int compare(Tag t1, Tag t2) {
				return t2.getHotDegree() - t1.getHotDegree();
			}
		});
		List<Tag> returnTags = new ArrayList<Tag>();
		int count = (num > tags.size()) ? tags.size() : num;
		for (int i = 0; i < count; i++) {
			returnTags.add(tags.get(i));
		}
		return returnTags;
	}
}
