#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Get the amount of change owed from the user
    int cents = get_cents();

    // Calculate the number of each coin required
    int quarters = calculate_quarters(cents);
    int dimes = calculate_dimes(cents % 25);
    int nickels = calculate_nickels(cents % 25 % 10);
    int pennies = calculate_pennies(cents % 25 % 10 % 5);

    // Print the total number of coins required
    int total_coins = quarters + dimes + nickels + pennies;
    printf("%i\n", total_coins);

    return 0;
}

int get_cents(void)
{
    int cents;

    // Prompt the user for a positive number of cents
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    return cents;
}

int calculate_quarters(int cents)
{
    // Calculate the number of quarters
    return cents / 25;
}

int calculate_dimes(int cents)
{
    // Calculate the number of dimes
    return cents / 10;
}

int calculate_nickels(int cents)
{
    // Calculate the number of nickels
    return cents / 5;
}

int calculate_pennies(int cents)
{
    // Calculate the number of pennies
    return cents;
}
