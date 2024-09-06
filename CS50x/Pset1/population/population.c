#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start, end;
    do
    {
        printf("Start Size: ");
        start = get_string("Start Size :")
    }
    while (start < 9);

    do
    {
        printf("End Size: ");
        end = get_string ("End size : ");
    }
    while (end < start);

    int temp = start, year = 0, newBorn, died;

    if (start != end)
    {
        while (temp < end)
        {
            newBorn = temp / 3;
            died = temp / 4;
            temp = temp + newBorn - died;
            year++;
        }
    }

    printf("Years: %d\n", year);

    return 0;
}
