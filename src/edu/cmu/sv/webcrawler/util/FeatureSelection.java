package edu.cmu.sv.webcrawler.util;

import java.util.*;

/**
 * Created by bluebyte60 on 4/7/15.
 */
public class FeatureSelection {
    //儲存所有詞彙
    Set<String> vocabulary = new HashSet<String>();
    //儲存所有類別名稱
    Set<String> categories = new HashSet<String>();
    protected HashMap<String, HashSet<String>> c_t_map = new HashMap<>();
    //以類別名稱還有詞彙名稱作為key值 將該詞彙在該類別出現的次數儲存在內
    protected Map<String, Float> t_c_matrix = new HashMap<String, Float>();
    //以詞彙名稱作為key值 將該詞彙在所有類別出現的次數儲存在內
    protected Map<String, Float> t_matrix = new HashMap<String, Float>();
    //以類別名稱作為key值 將該類別中所有詞彙出現的總次數儲存在內
    protected Map<String, Float> c_matrix = new HashMap<String, Float>();
    //所有詞彙在所有類別出現的總次數
    protected float N = 0;
    //總亂度
    public float uncondition_entropy;

    private FeatureSelection() {

    }

    public FeatureSelection(Set<String> vocabulary, Set<String> categories, Map<String, Float> t_c_matrix, Map<String, Float> t_matrix, Map<String, Float> c_matrix, HashMap<String, HashSet<String>> c_t_map, float N) {
        this.c_t_map = c_t_map;
        this.vocabulary = vocabulary;
        this.categories = categories;
        this.c_matrix = c_matrix;
        this.N = N;
        this.t_c_matrix = t_c_matrix;
        this.t_matrix = t_matrix;

    }

    public void initialize() {
        float temp = 0;
        Iterator<String> it = categories.iterator();
        while (it.hasNext()) {
            String cat = it.next();
            float a = c_matrix.get(cat);
            float prob_c = a / N;
            //System.out.println(prob_c*(Math.log(prob_c)/Math.log(2))) ;
            temp -= (prob_c * (Math.log(prob_c) / Math.log(2)));
        }
        uncondition_entropy = temp;
    }

    public ArrayList<Term> getFeatures(String type) {
        ArrayList<Term> data = new ArrayList<Term>();
        for (String cat : categories) {
            for (String term : c_t_map.get(cat)) {
                float weight = 0;
                if (t_c_matrix.get(cat + term) != null && t_c_matrix.get(cat + term) > 0) {
                    if (type.equals("CHI"))
                        weight = calculateCHI(term, cat);
                    if (Double.isNaN(weight))
                        weight = 0;
                    if (Double.isInfinite(weight))
                        weight = 0;
                }
                Term t=new Term(term);
                t.weight=weight;
                t.category=cat;
                data.add(t);
            }

        }
        Collections.sort(data, new TermComparator());
        return data;
    }

/*    public float calculateIG(String term, String cat) {
        float c = t_matrix.get(term);
        float d = N - c;
        float prob_t = c / N;
        float prob_t_comp = 1 - prob_t;
        float temp1 = 0, temp2 = 0;

        float a = c_matrix.get(cat);
        float a00 = t_c_matrix.get(cat + term);
        float a10 = a - a00;
        float prob_t_c = (a00 + 1) / (c + vocabulary.size());
        float prob_t_c_comp = (a10 + 1) / (d + vocabulary.size());
        temp1 += prob_t_c * (Math.log(prob_t_c) / Math.log(2));
        temp2 += prob_t_c_comp * (Math.log(prob_t_c_comp) / Math.log(2));
        temp1 *= prob_t;
        temp2 *= prob_t_comp;
        float total = uncondition_entropy + temp1 + temp2;
        // System.out.println(total);
        return total;
    }*/

    public float calculateCHI(String term, String cat) {
        float c = t_matrix.get(term);
        float d = N - c;
        double temp = 0;
        float a = c_matrix.get(cat);
        float a00 = t_c_matrix.get(cat + term);
        float a10 = a - a00;
        float b = N - a;
        float a01 = c - a00;
        float a11 = b - a01;
        double child = a00 * a11 - a10 * a01;
        temp = Math.pow(child, 2) / (a * b * c * d);
        return (float) temp;
    }
}
