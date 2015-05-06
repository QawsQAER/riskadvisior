package edu.cmu.sv.webcrawler.models;

import java.util.List;

public class DataPackage {
	private String name;
	private String id;
	private String title;
	private long total;
	private long recent;
	private int hotDegree;
	private List<Tag> tags;
	
	public DataPackage(String name, String id, String title, long total, long recent,
			List<Tag> tags) {
		super();
		this.name = name;
		this.id = id;
		this.total = total;
		this.title = title;
		this.recent = recent;
		this.hotDegree = (int) ((double) (recent) * 0.4 + (double) (total) * 0.6);
		this.tags = tags;
	}

	public String getName() {
		return name;
	}

	public String getId() {
		return id;
	}

	public String getTitle() {
		return title;
	}

	public long getTotal() {
		return total;
	}

	public long getRecent() {
		return recent;
	}

	public int getHotDegree() {
		return hotDegree;
	}

	public List<Tag> getTags() {
		return tags;
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setId(String id) {
		this.id = id;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public void setTotal(long total) {
		this.total = total;
	}

	public void setRecent(long recent) {
		this.recent = recent;
	}

	public void setHotDegree(int hotDegree) {
		this.hotDegree = hotDegree;
	}

	public void setTags(List<Tag> tags) {
		this.tags = tags;
	}

	@Override
	public String toString() {
		return "DataPackage [name=" + name + ", id=" + id + ", title=" + title
				+ ", total=" + total + ", recent=" + recent + ", hotDegree="
				+ hotDegree + ", tags=" + tags + "]";
	}
	
}
