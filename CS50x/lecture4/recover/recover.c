// Śmiga

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;


int main(int argc, char *argv[])
{
    // Accept a single comand-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover File\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");

    // Create a buffer for a block of data
    BYTE buffer[512];
    char filename[8];

    // While there's still data left to read frotm the memory card
    int a = 0;
    FILE *img = NULL;
    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data
        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if(a == 0)
            {
                sprintf(filename, "%03i.jpg", a);
                img = fopen(filename, "w");
                fwrite(buffer, 1, 512, img);
                a = a + 1;
            }
            else if (a != 0)
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", a);
                img = fopen(filename, "w");
                fwrite(buffer, 1, 512, img);
                a = a + 1;
            }
        }
        else if (a > 0)
        {
            fwrite(buffer, 1, 512, img);
        }
    }
    fclose(card);
    fclose(img);
}
