#include <fstream>
#include <vector>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include "Point.hpp"



int main (int argc, char **argv)
{
  std::vector<Point> apprentissage;
  std::vector<Point> validation;
    srand(time(NULL));

  for(int i = 0; i<10; i++)
  {
    Point tmpval;
    Point tmpapr;
     apprentissage.push_back(tmpapr);
     apprentissage.push_back(tmpval);
  }

  /*  for(int i = 0; i < points.size(); i++)
	 {
	   points[i].to_string();
	   }*/

   std::ofstream fichier("apprentissage.txt", std::ios::app);
   std::ofstream fichier("validation.txt", std::ios::app);

   if(fichier)
     {
       for(int i = 0; i < apprentissage.size(); i++)
	 {
	   fichier << apprentissage[i].get_x1() << " "  << apprentissage[i].get_x2() << " " << apprentissage[i].get_etiquette()  << std::endl; // Entrée dans le fichier
	 }
    
     }

   fichier.close();
  

  return 0;
}
