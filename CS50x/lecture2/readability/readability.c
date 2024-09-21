#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");
    int letter = 0;
    int space = 1;
    int sentences = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        text[i] = toupper(text[i]);
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            letter++;
        }
    }
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == ' ')
        {
            space++;
        }
    }
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '!' || text[i] == '.' || text[i] == '?')
        {
            sentences++;
        }
    }
    float L = (float) letter/space * 100;
    float S = (float) sentences/space * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    if (index >= 1 && index <= 16)
    {
        printf("Grade %.0f\n", index);
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }

}
