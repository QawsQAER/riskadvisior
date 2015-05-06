package edu.cmu.sv.webcrawler.models;

/**
 * Created by raoli on 3/25/15.
 */
public class TagCloudEntry {
	String text;
	long weight;
	String link;
	
	public TagCloudEntry(Tag tag)
	{
		this.text = tag.getName();
		this.weight = tag.getHotDegree();
		this.link = "http://catalog.data.gov/dataset?tags="+tag.getName();
	}

	public TagCloudEntry(DataPackage pkg)
	{
		this.text = pkg.getTitle();
		this.link = "http://catalog.data.gov/dataset/" + pkg.getName();
		this.weight = pkg.getHotDegree();

	}
	public long getWeight() {
		return weight;
	}

	public void setWeight(long weight) {
		this.weight = weight;
	}

	public String getText() {
		return text;
	}

	public void setText(String text) {
		this.text = text;
	}

	public String getLink() {
		return link;
	}

	public void setLink(String link) {
		this.link = link;
	}

}
