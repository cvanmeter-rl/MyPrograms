/*
 * Christian VanMeter
 * pawprint:cbvhkg
 * CS1050
 * Fall 2020
 * Lab 10 group E
 */

// includes
#include <stdio.h>
#include <ctype.h>

// Symbolic Constants
#define CLEARTEXT \
"It's Christmastime in Washington\a\nThe Democrats rehearsed \b\n"\
"Gettin' into gear for four more years\nThings not gettin' worse"\
"\"\\\?\n\n\t\t- Steve Earle"

// Prototypes
void Encrypt(char *s, int displacement);//encrypts the text by the displacement passed to the function
void Decrypt(char *s,int displacement);//decrypts the text by going back from the displacement

// Main
int main(void)
{
    char string[256] = {CLEARTEXT};
    printf("**** Original ****\n%s\n",string);

    printf("**** Encrypted ****\n");
    Encrypt(string,2);
    printf("%s\n\n",string);

    printf("**** Unecrypted ****\n");
    Decrypt(string,2);
    printf("%s\n\n",string);
}

// Function implementations
void Encrypt(char *s, int displacement)
{
    int c = 0;//holds the integer value of the character to be changed
    int i = 0;
    while(s[i] != '\0')//iterates through the entire array until it reaches the NULL terminator.
    {
        if(!(isspace(s[i])) && s[i] != '\b')//changes all characters that aren't a whitspace character
        {
            c = s[i];
            s[i] = c + displacement;
        }
        i++;
    }
}

void Decrypt(char *s,int displacement)
{
    int c = 0;//holds the integer value of the character to be changed
    int i = 0;
    while(s[i] != '\0')//interates through the entire array until it reaches the NULL terminator.
    {
        if(!(isspace(s[i])) && s[i] != '\b')//changes all characters that aren't a whitespace character
        {
            c = s[i];
            s[i] = c - displacement;
        }
        i++;
    }
}

