package edu.cmu.sv.webcrawler.util;

import java.util.Comparator;
 public class TermComparator implements Comparator {

    public int compare(Object o1, Object o2) {

        float t1 = ((Term) o1).weight;
        float t2 = ((Term) o2).weight;

        // 比較得分 (遞減排列)
        if (t1 < t2)
            return 1;
        else if (t1 > t2)
            return -1;
        else
            return 0;
    }
}
