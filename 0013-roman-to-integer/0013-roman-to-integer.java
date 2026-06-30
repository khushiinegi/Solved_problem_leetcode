class Solution {
    public int romanToInt(String s) 
    {
        int num = 0;
        for (int i = 0; i < s.length(); i++) {
            int value = 0;

            // get value of current character
            if (s.charAt(i) == 'I') value = 1;
            else if (s.charAt(i) == 'V') value = 5;
            else if (s.charAt(i) == 'X') value = 10;
            else if (s.charAt(i) == 'L') value = 50;
            else if (s.charAt(i) == 'C') value = 100;
            else if (s.charAt(i) == 'D') value = 500;
            else if (s.charAt(i) == 'M') value = 1000;

            // if next character exists and is bigger → subtract
            if (i + 1 < s.length()) {
                int nextValue = 0;
                if (s.charAt(i + 1) == 'I') nextValue = 1;
                else if (s.charAt(i + 1) == 'V') nextValue = 5;
                else if (s.charAt(i + 1) == 'X') nextValue = 10;
                else if (s.charAt(i + 1) == 'L') nextValue = 50;
                else if (s.charAt(i + 1) == 'C') nextValue = 100;
                else if (s.charAt(i + 1) == 'D') nextValue = 500;
                else if (s.charAt(i + 1) == 'M') nextValue = 1000;

                if (value < nextValue) {
                    num -= value; 
                    continue;
                }
            }

            num += value; // otherwise, add
        }

        return num;
    }
}