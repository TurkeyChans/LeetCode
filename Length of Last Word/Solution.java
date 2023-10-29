public class Solution {
    public int lengthOfLastWord(String s) {
        char a = ' ';
        int ans = 0;
        int save = 0;
        boolean alert = true;
        for(int i = 0; i < s.length(); ++i) {
            a = s.charAt(i);
            if(a == ' ' && alert) {
                save = ans;
                ans = 0;
                alert = false;
            }
            else if(alert == false) {
                if(a != ' ') {
                    ans++;
                    save = ans;
                    alert = true;
                }   
            }
            else {
                ans++;
                save = ans;
            }

        }
        return save;
    }
    /*public static void main(String[] args) {
        Solution Test = new Solution();
        String number1 = "Hello World";
        String number2 = "  a  ";
        String number3 = "  I  love  me  some  java!!!  ";
        System.out.println("1st Test: " + Test.lengthOfLastWord(number1));
        System.out.println("2nd Test: " + Test.lengthOfLastWord(number2));
        System.out.println("2nd Test: " + Test.lengthOfLastWord(number3));
    }*/
}