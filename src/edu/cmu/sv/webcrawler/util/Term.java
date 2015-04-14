package edu.cmu.sv.webcrawler.util;


public class Term {
    public String key = "";
    public float weight;
    public String category;
    public Term(String s) {
        this.key = s;
    }
    public String toString(){return category+": "+key+" weight:"+weight;}
}


