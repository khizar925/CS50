#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text, int N);
int count_sentences(string text, int N);
int count_words(string text, int N);
int main(void)
{
    string text = get_string("Text : ");
    int N = strlen(text);
    int letters = count_letters(text, N);
    int sentences = count_sentences(text, N);
    int words = count_words(text, N);
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}
int count_letters(string text, int N)
{
    char temp;
    int letters = 0;
    for (int i = 0; i < N; i++)
    {
        temp = text[i];
        temp = toupper(temp);
        if (temp >= 65 && temp <= 90)
        {
            letters++;
        }
    }
    return letters;
}
int count_sentences(string text, int N)
{
    char temp, sentences = 0;
    for (int i = 0; i < N; i++)
    {
        temp = text[i];
        if (temp == '.' || temp == '?' || temp == '!')
        {
            sentences++;
        }
    }
    return sentences;
}
int count_words(string text, int N)
{
    char temp;
    int words = 1;
    for (int i = 0; i < N; i++)
    {
        temp = text[i];
        if (temp == ' ')
        {
            words++;
        }
    }
    return words;
}
