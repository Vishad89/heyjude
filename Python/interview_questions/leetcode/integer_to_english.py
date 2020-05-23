"""
273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five
"""
def intger_to_english_word(digit):
    singles = ["","One","Two", "Three","Four","Five","Six","Seven","Eight","Nine"]
    doubles = ["ten","Eleven","Twelve", "Thirteen","fourteen","Fifteen", "Sixteen", "Seventeen","Eighteen","Nineteen"]
    tens = ["","","Twenty", "Thirty", "Fourty", "fifty", "Sixty", "Seventy","Eighty", "Ninety"]
    #rest = ["", "hundred", "thousand", "million", "billion"]
    
    if digit < 10:
        return singles[digit]
    elif digit < 20:
        return doubles[digit%10]
    elif digit < 100:
        return (tens[digit // 10] + " " +  singles[digit % 10]).strip()
    elif digit < 1000:
        return (singles[digit // 100] + " hundred " + intger_to_english_word(digit % 100)).strip()
    elif digit < 1000000:
        return ((intger_to_english_word(digit // 1000)) + " thousand " + (intger_to_english_word(digit % 1000))).strip()
    elif digit < 1000000000:
        return ((intger_to_english_word(digit // 1000000)) + " million " + (intger_to_english_word(digit % 1000000))).strip()
    else:
        return ((intger_to_english_word (digit // 1000000000)) + " billion " + (intger_to_english_word(digit % 1000000000))).strip() 

print(intger_to_english_word(int(input("Enter a number: "))))