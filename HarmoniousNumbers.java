/*Fergus Farrell
 * Etude 9 - Harmonious Numbers
 */

import java.util.*;

public class HarmoniousNumbers{
  
  private static int calculation(int num){
   int divisor = (int)Math.sqrt(num);
   int total = 0;
   
   for(int i = 2; i < divisor+1; i++){
     if(num % i == 0){
      int value = num/i;
      if(value != i){
       total += value; 
      }
      total += i;
     }
   }
   return total;
  }
  
  public static void main(String [] args){
    int max = 2000000;
    Map<Integer, Integer> numbers = new HashMap<Integer, Integer>();
    
    for(int i = 2; i < max; i++){
     int numOne = calculation(i);
     int numTwo = calculation(numOne);
     //System.out.println(numOne + " " + numTwo);
     
     if (numbers.get(numOne) == null){
       if(numOne != i && numTwo == i){
         if(numOne < numTwo){
          numbers.put(numOne, numTwo); 
          System.out.println(numOne + " " + numTwo);
         } else {
          numbers.put(numTwo, numOne);
          System.out.println(numTwo + " " + numOne);
         }
       } 
     }
    }
  }
}