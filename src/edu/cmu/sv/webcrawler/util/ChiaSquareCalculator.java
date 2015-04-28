package edu.cmu.sv.webcrawler.util;

import com.mongodb.*;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

/**
 * Created by bluebyte60 on 4/7/15.
 */
public class ChiaSquareCalculator {
    MongoHelper mongoHelper;
    DBCollection categoriesCollection = null;
    DBCollection webcrawlerCollection = null;
    DBCollection featureCollection=null;
    //store all the key words
    HashSet<String> vocabulary = new HashSet<String>();
    //store the key word set of each categor
    protected HashMap<String, HashSet<String>> c_t_map = new HashMap<>();
    //use the category name and key word name as key value, store the occurance of the keyword in this category
    protected HashMap<String, Float> t_c_matrix = new HashMap<String, Float>();
    //use the keyword as key,  store the occurance of the keyword in this category
    protected HashMap<String, Float> t_matrix = new HashMap<String, Float>();
    //use the keyword as key,  store the occurance of the keyword in this category
    protected HashMap<String, Float> c_matrix = new HashMap<String, Float>();
    //store the occurance of the keyword in this category
    protected float N = 0;

    /**
     * This class is very complicated, do not touch if you like solving problem, especially mess problem....
     */
    public ChiaSquareCalculator() {
        //Get db collection
        mongoHelper = new MongoHelper();
        categoriesCollection = mongoHelper.getDb().getCollection("categories");
        webcrawlerCollection = mongoHelper.getDb().getCollection("webcrawler");
        featureCollection=mongoHelper.getDb().getCollection("features");
        //Calculation 1
        preCalculation();
        //Calculation 2
        calculation();
        //Feature selection weight calculation
        FeatureSelection featureSelection=new FeatureSelection(vocabulary,c_t_map.keySet(),t_c_matrix,  t_matrix,c_matrix, c_t_map,N);
        featureSelection.initialize();
        List<Term> termList=featureSelection.getFeatures("CHI");
        for(Term term:termList) System.out.println(term);
        //Save to DB
        store(termList);
        //store into DB
    }

    private void preCalculation() {
        BasicDBObject doc = new BasicDBObject();
        DBCursor cursor = this.categoriesCollection.find(doc);
        try {
            while (cursor.hasNext()) {
                DBObject obj = cursor.next();
                for (String key : obj.keySet()) {
                    if (key.equals("_id")) continue;//ignore _id;
                    c_t_map.put(key, new HashSet<String>());
                    c_matrix.put(key, 0f);
                    BasicDBList terms = (BasicDBList) obj.get(key);
                    for (Object s : terms) {
                        String term=s.toString().toLowerCase();
                        vocabulary.add(term);
                        c_t_map.get(key).add(term);
                        t_c_matrix.put(key + term, 0f);
                        t_matrix.put(term, 0f);
                    }
                }
            }
            cursor.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void calculation() {
        BasicDBObject doc = new BasicDBObject();
        DBCursor cursor = this.webcrawlerCollection.find(doc);
        try {
            while (cursor.hasNext()) {
                DBObject obj = cursor.next();
                for (String key : obj.keySet()) {
                    if (!key.equals("keywords")) continue;
                    BasicDBList terms = (BasicDBList) obj.get(key);
                    for (String index : terms.keySet()) {
                        String tokon = terms.get(index).toString();
                        String[] data = parse(tokon);
                        put(data);
                    }
                }
            }
            cursor.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void put(String[] data) {
        String term = data[0].toLowerCase();
        float fre = Float.valueOf(data[1]);
        for(String category:c_t_map.keySet()){//traversal each category
            if(!c_t_map.get(category).contains(term))continue;
            N+=fre;
            t_c_matrix.put(category+term,t_c_matrix.get(category+term)+fre);
            t_matrix.put(term,t_matrix.get(term)+fre);
            c_matrix.put(category,c_matrix.get(category)+fre);
        }
    }

    private void store(List<Term> list){
        BasicDBObject doc = new BasicDBObject();
        featureCollection.remove(doc);
        for(Term term:list){
            BasicDBObject obj = new BasicDBObject();
            obj.put("key",term.key);
            obj.put("weight",term.weight);
            obj.put("category",term.category);
            featureCollection.insert(obj);
        }
    }


    /**
     * Parse the token
     *
     * @param tokon
     * @return
     */
    private String[] parse(String tokon) {
        tokon = tokon.substring(1, tokon.length() - 1);
        String[] data = tokon.split(":");
        String term = data[0];
        term = term.trim();
        term = term.substring(1, term.length() - 1);
        String fre = data[1].trim();
        return new String[]{term, fre};
    }

    public static void main(String[] args) {
        new ChiaSquareCalculator();
    }
}
