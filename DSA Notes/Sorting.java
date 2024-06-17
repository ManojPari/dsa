package InterviewQuestions;

public class Sorting {
	
	public static void swap(int arr[], int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	
	public static void bubbleSort(int arr[]) {
		boolean swapped = false;
		for(int pass = 1; pass < arr.length; pass++) {
			swapped = false;
			for(int curr = 0; curr < arr.length - pass; curr++) {
				if(arr[curr] > arr[curr + 1]) {
					swap(arr, curr, curr+1);
					swapped = true;
				}
			}
			if(swapped == false) break;
		}
	}
	
	public static void selectionSort(int arr[]) {
		for(int usi = 0; usi < arr.length - 1; usi++) {
			int min_idx = usi;
			for(int i = usi + 1; i < arr.length; i++) 
				if(arr[i] < arr[min_idx]) 
					min_idx = i;
			
			swap(arr, usi, min_idx);
		}
	}
	
	public static void insertionSort(int arr[]) {
		for(int usi = 1; usi < arr.length; usi++) {
			int key = arr[usi];
			int i;
			for(i = usi - 1; i >= 0 && key < arr[i]; i--) {
				arr[i + 1] = arr[i];
			}
			arr[i+1] = key;
		}
	}
	
	public static void print(int arr[]) {
		for(int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}
	
	public static void main(String[] args) {
		int arr[] = {9,6,7,3,1,2,5};
		print(arr);
//		bubbleSort(arr);
//		selectionSort(arr);
		insertionSort(arr);
		print(arr);
		
	}

}
