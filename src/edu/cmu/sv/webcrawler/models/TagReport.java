package edu.cmu.sv.webcrawler.models;

import java.util.List;

public class TagReport {
	
	private List<Tag> tags;
	private int count;
	public TagReport(List<Tag> tags) {
		super();
		this.tags = tags;
		this.count = tags.size();
	}
	public List<Tag> getTags() {
		return tags;
	}
	public int getCount() {
		return count;
	}
	public void setTags(List<Tag> tags) {
		this.tags = tags;
	}
	public void setCount(int count) {
		this.count = count;
	}
	@Override
	public String toString() {
		return "TagReport [count=" + count + "]";
	}
	

}
