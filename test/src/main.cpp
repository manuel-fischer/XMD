#include <stdio.h>

int greet(const char* str)
{
    printf("Hello %s\n", str);
    return 42;
}

int main()
{
    greet("World");
}
