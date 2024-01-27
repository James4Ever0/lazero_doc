#define TERM_WORD_CHARS "-./?%&#_=+@~()"
#include <stdio.h>
#include <string.h>
// maybe you just want some chars.
// does not include extra shits.
// blanks are omitted.
// get all things from stdin
// just saying.
int cmp0(char a, char b[])
{
    for (int i = 0; i < strlen(b); i++)
    {
        if (a == b[i])
        {
            return 1;
        }
    }
    return 0;
}
int cmp(char a[])
{
    for (int i = 0; i < strlen(a); i++)
    {
        if (cmp0(a[i], TERM_WORD_CHARS))
        {
            return 1;
        }
    }
    return 0;
}
int main()
{
    char a[500];
    fgets(a, 500, stdin);
    // printf("%s", a);
    for (int i = 0; i < strlen(a); i++)
    {
        if (cmp0(a[i], TERM_WORD_CHARS))
        {
            printf("\\");
        }
        printf("%c", a[i]);
    }
}
// does this works?
// damn I will try shit out. all fucking shit in one.
// it is your learning, whatever it takes.
// shit. man i do not know what to say.
// just keep working. whatever shit it is going to be.