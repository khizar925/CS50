#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512
typedef uint8_t BYTE;

bool isJPEG(BYTE buffer[]);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *raw_file = fopen(argv[1], "r");
    if (raw_file == NULL)
    {
        printf("File cannot be opened.\n");
        return 1;
    }

    int count = 0;
    FILE *image = NULL;
    // char filename[8];

    BYTE buffer[BLOCK_SIZE];
    while (fread(buffer, BLOCK_SIZE, 1, raw_file) == 1)
    {
        if (isJPEG(buffer))
        {
            if (count != 0)
            {
                fclose(image);
            }

            // Allocate memory for the filename dynamically
            char *filename = malloc(8 * sizeof(char));
            if (filename == NULL)
            {
                printf("Memory allocation failed.\n");
                return 1;
            }

            sprintf(filename, "%03i.jpg", count++);
            image = fopen(filename, "w");
            free(filename); // Free allocated memory after using it

            if (image == NULL)
            {
                printf("Error opening image file.\n");
                return 1;
            }

            fwrite(buffer, BLOCK_SIZE, 1, image);
        }
        else if (count > 0)
        {
            fwrite(buffer, BLOCK_SIZE, 1, image);
        }
    }

    // Close the last image file
    if (image != NULL)
    {
        fclose(image);
    }

    fclose(raw_file);

    return 0;
}

bool isJPEG(BYTE buffer[])
{
    return (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0);
}
