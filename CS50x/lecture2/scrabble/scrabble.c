#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int score[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    string s = get_string("Player 1: ");
    string d = get_string("Player 2: ");
    int x = 0;
    int z = 0;
    int x2 = 0;
    int z2 = 0;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        s[i] = toupper(s[i]);
        if (s[i] >= 'A' && s[i] <= 'Z')
        {
            int c  = s[i] - 65;
            x = score[c];
            z = x + z;
        }
    }
    for (int i = 0, n = strlen(d); i < n; i++)
    {
        d[i] = toupper(d[i]);
        if (d[i] >= 'A' && d[i] <= 'Z')
        {
            int c2  = d[i] - 65;
            x2 = score[c2];
            z2 = x2 + z2;
        }
    }
    if (z > z2)
    {
        printf("Player 1 wins!\n");
    }
    else if (z < z2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
