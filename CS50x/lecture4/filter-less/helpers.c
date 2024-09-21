#include "helpers.h"
#include <math.h>
#include <cs50.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

// Convert image to grayscale -> Śmiga
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float a = image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue;
            int d = round (a / 3);
            image[i][j].rgbtRed = d;
            image[i][j].rgbtGreen = d;
            image[i][j].rgbtBlue = d;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int a = round (.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image [i][j].rgbtBlue);
            int b = round (.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int c = round (.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (a > 255)
            {a = 255;}
            if (b > 255)
            {b = 255;}
            if (c > 255)
            {c = 255;}

            image[i][j].rgbtRed = a;
            image[i][j].rgbtGreen = b;
            image[i][j].rgbtBlue = c;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int a = width / 2;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < a; j++)
        {
            RGBTRIPLE temp = image [i][j];
            int b = width - 1 - j;
            image [i][j] = image [i][b];
            image [i][b] = temp;
        }
    }
    return;
}

// Blur image 
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int a1 = 0;
    int b1 = 0;
    int c1 = 0;
    int a4 = 1;
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (i > 0)
            {
                a1 = a1 + image[i-1][j].rgbtRed;
                b1 = b1 + image[i-1][j].rgbtGreen;
                c1 = c1 + image[i-1][j].rgbtBlue;
                a4++;
            }
            if (i < height - 1)
            {
                a1 = a1 + image[i+1][j].rgbtRed;
                b1 = b1 + image[i+1][j].rgbtGreen;
                c1 = c1 + image[i+1][j].rgbtBlue;
                a4++;
            }
            if (j > 0)
            {
                a1 = a1 + image[i][j-1].rgbtRed;
                b1 = b1 + image[i][j-1].rgbtGreen;
                c1 = c1 + image[i][j-1].rgbtBlue;
                a4++;
            }
            if (j < width - 1)
            {
                a1 = a1 + image[i][j+1].rgbtRed;
                b1 = b1 + image[i][j+1].rgbtGreen;
                c1 = c1 + image[i][j+1].rgbtBlue;
                a4++;
            }
            if (i > 0 && j > 0)
            {
                a1 = a1 + image[i-1][j-1].rgbtRed;
                b1 = b1 + image[i-1][j-1].rgbtGreen;
                c1 = c1 + image[i-1][j-1].rgbtBlue;
                a4++;
            }
            if (i < height -1 && j < width - 1)
            {
                a1 = a1 + image[i+1][j+1].rgbtRed;
                b1 = b1 + image[i+1][j+1].rgbtGreen;
                c1 = c1 + image[i+1][j+1].rgbtBlue;
                a4++;
            }
            if (i > 0 && j < width - 1)
            {
                a1 = a1 + image[i-1][j+1].rgbtRed;
                b1 = b1 + image[i-1][j+1].rgbtGreen;
                c1 = c1 + image[i-1][j+1].rgbtBlue;
                a4++;
            }
            if (i < height - 1  && j > 0)
            {
                a1 = a1 + image[i+1][j-1].rgbtRed;
                b1 = b1 + image[i+1][j-1].rgbtGreen;
                c1 = c1 + image[i+1][j-1].rgbtBlue;
                a4++;
            }

            a1 = a1 + image[i][j].rgbtRed;
            float a2 = a1;
            float a3 = a2 / a4;

            b1 = b1 + image[i][j].rgbtGreen;
            float b2 = b1;
            float b3 = b2 / a4;

            c1 = c1 + image[i][j].rgbtBlue;
            float c2 = c1;
            float c3 = c2 / a4;

            int a = round (a3);
            int b = round (b3);
            int c = round (c3);

            temp[i][j].rgbtRed = a;
            temp[i][j].rgbtGreen = b;
            temp[i][j].rgbtBlue = c;
            a1 = 0;
            b1 = 0;
            c1 = 0;
            a4 = 1;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
    return;
}
