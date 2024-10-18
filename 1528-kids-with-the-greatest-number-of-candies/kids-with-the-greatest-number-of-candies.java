class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        //boolean[] res = new boolean[candies.length];
        ArrayList<Boolean> res = new ArrayList<Boolean>(candies.length);
		int max=0;
		for(int i:candies){
		    if(i>max){
		        max=i;
		    }
		}
		for(int i=0; i<candies.length; i++){
		    if(candies[i]+extraCandies>=max){
		        res.add(true);
		    }
		    else{
		        res.add(false);
		    }
		}
        return res;
    }
}