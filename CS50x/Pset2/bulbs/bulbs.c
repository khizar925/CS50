#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
void char_to_binary(char msg);
int main(void)
{
    // TODO
    string msg = get_string("Message : ");
    int N = strlen(msg);
    for (int i = 0; i < N; i++)
    {
        char_to_binary(msg[i]);
        printf("\n");
    }
}
void char_to_binary(char msg)
{
    int temp;
    int binary[BITS_IN_BYTE];
    for (int i = 0; i < BITS_IN_BYTE; i++)
    {
        binary[i] = 0;
    }
    temp = msg;
    for (int j = BITS_IN_BYTE - 1; j > 0; j--)
    {
        binary[j] = temp % 2;
        temp = temp / 2;
    }
    for (int i = 0; i < BITS_IN_BYTE; i++)
    {
        print_bulb(binary[i]);
    }
}
void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
