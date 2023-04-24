#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512

int jpeg_found = 0;
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        printf("File could not be opened.\n");
        return 1;
    }
    // Define buffer:
    unsigned char buffer[BLOCK_SIZE];

    // Define img:
    FILE *img = NULL;
    while (fread(&buffer, BLOCK_SIZE, 1, file) == 1)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (jpeg_found == 0)
            {
                char filename[8];
                sprintf(filename, "%03i.jpg", jpeg_found);
                img = fopen(filename, "w");
                fwrite(&buffer, BLOCK_SIZE, 1, img);
                jpeg_found++;
            }
            else
            {
                fclose(img);
                char filename[8];
                sprintf(filename, "%03i.jpg", jpeg_found);
                img = fopen(filename, "w");
                fwrite(&buffer, BLOCK_SIZE, 1, img);
                jpeg_found++;
            }
        }
        else
        {
            if (jpeg_found > 0)
            {
                fwrite(&buffer, BLOCK_SIZE, 1, img);
            }
        }
    }

    fclose(file);

    return 0;
}