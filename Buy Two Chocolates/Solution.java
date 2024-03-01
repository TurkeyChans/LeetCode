class Solution {
    public void sort(int[] arrayToSort) {
        int i,j,k,temp;
        for(i = 0; i < arrayToSort.length-1; ++i) {
			k = i;
			for(j = i+1; j < arrayToSort.length; ++j) {
				if(arrayToSort[k] > arrayToSort[j]) {
					k = j;
				}
			}
			temp = arrayToSort[i];
			arrayToSort[i] = arrayToSort[k];
			arrayToSort[k] = temp;
		}
	}
    public int buyChoco(int[] prices, int money) {
        sort(prices);
        int buying = money - (prices[0] + prices[1]);
        if(buying >= 0) {
            return buying;
        }
        return money;
    }

    public static void main(String[] args) {
       Solution ts = new Solution();
       int[] prices = {98,54,6,34,66,63,52,39};
       int money = 62;
       System.out.print(ts.buyChoco(prices, money));
    }
}