#include<iostream>
using namespace std;

int main()
{
    string str, sub_str;
    getline(cin, str);

    int p = 0;
    char c = str[p++];

    while(p <= str.size())
    {
        if(c=='<')
        {
            cout << sub_str;
            sub_str = "";
            while(c!='>')
            {
                cout << c;
                c = str[p++];
            }
            cout << c;
        }
        else if(c==' ')
        {
            cout << sub_str << c;
            sub_str = "";
        }
        else
        {
            sub_str = c + sub_str;
        }
        c = str[p++];
    }

    cout << sub_str;
}