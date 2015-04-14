package edu.cmu.sv.webcrawler.services;

import com.mongodb.*;
import edu.cmu.sv.webcrawler.util.MongoHelper;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by bluebyte60 on 4/8/15.
 */
public class FeatureWeighting {
    Map<String, Float> featureMap;

    public FeatureWeighting() {
        featureMap = readFromDB();
    }

    public float getWeight(String term) {
        if (!featureMap.containsKey(term)) return 1;
        else return featureMap.get(term);
    }

    public Map<String, Float> readFromDB() {
        Map<String, Float> map = new HashMap<>();
        MongoHelper helper = new MongoHelper();
        DBCollection featureCollection = helper.getDb().getCollection("features");
        BasicDBObject doc = new BasicDBObject();
        DBCursor cursor = featureCollection.find(doc);
        try {
            while (cursor.hasNext()) {
                DBObject obj = cursor.next();
                map.put(obj.get("key").toString(), Float.valueOf(obj.get("weight").toString()) + 1);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return map;
    }

    public static void main(String[] args) {
        System.out.println(new FeatureWeighting().getWeight("risk"));
    }
}
