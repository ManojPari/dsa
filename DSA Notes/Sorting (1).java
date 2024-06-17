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
	
	static int inversion = 0;
	public static int[] merge(int a[], int b[]) {
		int res[] = new int[a.length + b.length];
		int i = 0, j = 0, k = 0;
		
		while(i < a.length && j < b.length) {
			if(a[i] <= b[j]) {
				res[k++] = a[i++];
			}else {
				res[k++] = b[j++];
				inversion += a.length - i;
			}
		}
		
		while(i < a.length) {
			res[k++] = a[i++];
		}
		
		while(j < b.length) {
			res[k++] = b[j++];
		}
		return res;
	}
	
	public static int[] mergeSort(int arr[], int low, int high) {
		if(low == high) {
			return new int[]{arr[low]};
		}
		
		int mid = (low + high)/ 2;
		int arr1[] = mergeSort(arr, low, mid);
		int arr2[] = mergeSort(arr, mid + 1, high);
		
		return merge(arr1, arr2);
		
	}
	
	public static void main(String[] args) {
		int arr[] = {9,6,7,3,1,2,5};
		
		int a[] = {1, 3, 4, 7};
		int b[] = {2, 5, 6, 7, 8, 9, 10};
//		print(arr);
//		bubbleSort(arr);
//		selectionSort(arr);
//		insertionSort(arr);
//		print(arr);
		int arr2[] = {8, 5, 3, 4, 1, 6, 2};
		mergeSort(arr2, 0, arr2.length - 1);
		System.out.println(inversion);
//		print(merge(a, b));
		
	}

}
