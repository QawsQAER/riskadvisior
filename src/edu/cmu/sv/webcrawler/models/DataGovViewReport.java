package edu.cmu.sv.webcrawler.models;

import java.util.List;

public class DataGovViewReport {
	List<TagCloudEntry> content;
	int count;

	public List<TagCloudEntry> getContent() {
		return content;
	}

	public int getCount() {
		return count;
	}

	public void setContent(List<TagCloudEntry> content) {
		this.content = content;
	}

	public void setCount(int count) {
		this.count = count;
	}

	public DataGovViewReport(List<TagCloudEntry> content, int count) {
		super();
		this.content = content;
		this.count = count;
	}

	@Override
	public String toString() {
		return "DataGovViewReport [content=" + content + ", count=" + count
				+ "]";
	}
}
