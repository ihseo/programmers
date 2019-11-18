package problem_10815;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		HashSet<String> h = new HashSet<String>(); 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < n; i++) {
			h.add(st.nextToken());
		}

		int j = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		 for (int i = 0; i < j; i++) {
	         if (h.contains(st.nextToken())) {
	        	 sb.append("1 ");
	         }
	         else {
	        	 sb.append("0 ");
	         }
	      }
		 System.out.println(sb);
		 
	     
	}
}