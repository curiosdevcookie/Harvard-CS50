#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through each row — y-axis:
    for (int i = 0; i < height; i++)
    {
        // Loop through each pixel in the row — x-axis:
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtRed == 0 && image[i][j].rgbtGreen == 0 && image[i][j].rgbtBlue == 0)
            {
                // Change the colors to rebecca purple:
                image[i][j].rgbtRed = 102;
                image[i][j].rgbtGreen = 51;
                image[i][j].rgbtBlue = 153;
            }
        }
    }
}
