Today in this article we will discuss the program to generate all combinations of balanced parentheses in C++ programming language. We are given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of well-formed(balanced) parentheses.

All Combinations of Balanced Parentheses in C++
While loop in C

----------------------------------------------------Method 1:----------------------------------------------------

Generate a recursive function that accepts a string (s), count of opening brackets (o) and count of closing brackets (c) and the value of n.
If the value of opening bracket and closing bracket is equal to n then print the string and return.
If the count of opening bracket is greater than count of closing bracket then call the function recursively with the following parameters String s + “}”, count of opening bracket o, count of closing bracket c + 1, and n.
If the count of opening bracket is less than n then call the function recursively with the following parameters String s + “{“, count of opening bracket o + 1, count of closing bracket c, and n.
Method 1 :Code in C++
Run
#include <bits/stdc++.h>
using namespace std;
vector<string> generateParenthesis(int n)
{
    vector<string> two;
    vector<string> ans;
    if (n == 1) {
        two.push_back("{}");
        return two;
    } 
    if (n == 2) {
        two.push_back("{{}}");
        two.push_back("{}{}");
        return two;
    }
 
    two = generateParenthesis(n - 1);
    
    for (int i = 0; i < two.size(); i++) {
        string buf = "{", bug = "{", bus = "{";
        buf = buf + two[i] + "}";
        bug = bug + "}" + two[i];
        bus = two[i] + bus + "}";
        ans.push_back(buf);
        ans.push_back(bus);
        ans.push_back(bug);
    }
 
    ans.pop_back();
 
    return ans;
}
int main()
{
    vector<string>ff; 
    int n = 2;
    ff = generateParenthesis(n); 
 
    for (int i = 0; i < ff.size(); ++i) {
        cout << ff[i] << endl; 
    }
}
Output :
{{}}
{}{}
While loop in C
Method 2 :
In this method we use the implementation of the same algorithm in a slightly different, simple and concise way.

----------------------------------------------------Method 2 :Code in C++----------------------------------------------------


#include <bits/stdc++.h>
using namespace std;

void generateParenthesis(int n, int open, int close, string s, vector<string> &ans){
    if(open==n && close==n){
        ans.push_back(s);
        return;
    } 

    if(open<n){
        generateParenthesis(n, open+1, close, s+"{", ans);
    }

    if(close<open){
        generateParenthesis(n, open, close+1, s+"}", ans);
    }
       
}
int main() {
    int n = 3;
    
    vector<string> ans;
    generateParenthesis(n,0,0,"",ans);
     
    for(auto s:ans){
        cout<<s<<endl;
    }
    return 0;
}
Output :
{{{}}}
{{}{}}
{{}}{}
{}{{}}
{}{}{}
