#include <iostream>
using namespace std;

void investigatePrime(int n)
{
    if (n < 2)
    {
        cout << "Not Prime" << endl;
        return;
    }
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            cout << "not prime" << endl;
            return;
        }
    }
    cout << "Prime" << endl;
}

int main()
{

    int n;
    cout << "Enter the Whole number: " << endl;
    cin >> n;

    investigatePrime(n);
    return 0;
}
