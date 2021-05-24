// Created by: shyraffy
// Recursive and iterative implementation of the binary search algorithm in Java

public class BinarySearch {
	
	public static int binarySrch(int[] v, int t){
		
	    int left = 0;
	    int right = v.length - 1;
	    int m;
	    int result = -1;
	    boolean found = false;

	    while (left <= right && !found){
	      m = (int) Math.floor((left + right) / 2.0); //Gets the middle point

	      if (t > v[m]) //The target number is on the right
	        left = m + 1; //"Sub-array" that goes from the position 0 to m-1

	      else if(t < v[m]) // The target number is on the left
	        right = m - 1; //"Sub-array" that goes from the position m to v's length

	      else{ //m is the target 
	        result = m;
	        found = true;
	      }
	    }

	    return result;
	}

	public static int binarySearchRecursive(int[] v, int t, int left, int right){
		if (left > right) // Base case, the number was not found
	      return -1;

	    else{
	    	
	      int m = (int) Math.floor((left + right) / 2.0);
	      if (t > v[m])
	        return binarySearchRecursive(v, t, m + 1, right);
	      else if(t < v[m])
	        return binarySearchRecursive(v, t, left, m - 1);
	      else
	        return m;
	    }
	}

	public static void main(String[] args) {
	    int[] v = {1, 3, 5, 8, 15};

	    //int result = binarySrch(v, 15);
	    int result = binarySearchRecursive(v, 15, 0, v.length - 1);

	    if (result == -1)
	      System.out.println("Search unsuccessful. If the item is really in the array, verify the array is sorted.");
	    else
	      System.out.println("Item found at position " + result);
	}
}
