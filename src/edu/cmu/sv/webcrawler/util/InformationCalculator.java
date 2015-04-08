package edu.cmu.sv.webcrawler.util;

import com.mongodb.*;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

/**
 * Created by bluebyte60 on 4/7/15.
 */
public class InformationCalculator {
    MongoHelper mongoHelper;
    DBCollection categoriesCollection = null;
    DBCollection webcrawlerCollection = null;
    DBCollection featureCollection=null;
    //儲存所有詞彙
    HashSet<String> vocabulary = new HashSet<String>();
    //儲存所有類別名稱與相應的詞彙集合
    protected HashMap<String, HashSet<String>> c_t_map = new HashMap<String, HashSet<String>>();
    //以類別名稱還有詞彙名稱作為key值 將該詞彙在該類別出現的次數儲存在內
    protected HashMap<String, Float> t_c_matrix = new HashMap<String, Float>();
    //以詞彙名稱作為key值 將該詞彙在所有類別出現的次數儲存在內
    protected HashMap<String, Float> t_matrix = new HashMap<String, Float>();
    //以類別名稱作為key值 將該類別中所有詞彙出現的總次數儲存在內
    protected HashMap<String, Float> c_matrix = new HashMap<String, Float>();
    //所有詞彙在所有類別出現的總次數
    protected float N = 0;

    /**
     * This class is very complicated, do not touch if you like solving problem, especially mess problem....
     */
    public InformationCalculator() {
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
        FeatureSelection featureSelection=new FeatureSelection(vocabulary,c_t_map.keySet(),t_c_matrix,  t_matrix,c_matrix, N);
        featureSelection.initialize();
        List<Term> termList=featureSelection.getFeatures("CHI");
        //Save to DB
       // store(termList);
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
                    c_t_map.put(key, new HashSet<>());
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
            featureCollection.insert(obj);
        }
    }


    /**
     * Parse the tokon
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
        new InformationCalculator();
    }
}
