/* Counting Leafs */
/* 
   You are given a tree with N nodes numbered from 0 to N-1 . 
   You are also given a node X which you are supposed to delete. 
   You have to tell the number of leaf nodes in the tree after deleting the given node. 
   Note that deleting a node deletes all the nodes in its subtree. 
*/

import java.io.*;
import java.util.*;
import static java.lang.System.out;

public class CountingLeafs {
   public static void main(String args[] ) throws Exception {

	//Write code here

        Scanner scan = new Scanner(System.in);
        
        int arrlen = Integer.parseInt(scan.nextLine());
        
        if(arrlen > 0) {

            StringTokenizer token = new StringTokenizer(scan.nextLine());
            
            // making a heap, skipping first element for simplicity
            int[] arr = new int[token.countTokens() + 1];
            
            int i = 1;
            while (token.hasMoreElements()) {
                String s = (String)token.nextElement();
                arr[i++] = Integer.parseInt(s);
            }
            
            int delindex = Integer.parseInt(scan.nextLine()) + 1; // adding 1 because first index is skipped
            
            if(delindex < arr.length) {
                
                arr[delindex] = Integer.MIN_VALUE;
                
                int mid = (int)Math.floor((arr.length - 1) / 2) + 1;
                
                int count = 0;
                for (int j = mid; j < arr.length; j++) {
                    count += checkIfParentDeleted(arr, j) ? 0 : 1;
                }
                
                System.out.println(count);
            }
        }

   }
   
   static boolean checkIfParentDeleted(int[] arr, int j) {
       
       if (arr[j] == Integer.MIN_VALUE) {
           return true;
       }
       
       if (arr[j] == -1 || j < 1) {
           return false;
       }
       
       return checkIfParentDeleted(arr, (int)(j / 2));
       
   }
   
}
