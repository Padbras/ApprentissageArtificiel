#include <fstream>
#include <vector>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include "Point.hpp"

int generationfichiers()
{
  std::vector<Point> apprentissage;
  std::vector<Point> validation;
  srand(time(NULL));

  for(int i = 0; i<10; i++)
    {
      Point tmpval;
      Point tmpapr;
      apprentissage.push_back(tmpapr);
      validation.push_back(tmpval);
    }

  std::ofstream fichier("apprentissage.txt", std::ios::app);
  std::ofstream fichier2("validation.txt", std::ios::app);

  if(fichier)
    {
      for(int i = 0; i < apprentissage.size(); i++)
	{
	  fichier << apprentissage[i].get_x1() << " "  << apprentissage[i].get_x2() << " " << apprentissage[i].get_etiquette()  << std::endl; // Entrée dans le fichier	   
	}
    }

  if(fichier2)
    {
      for(int i = 0; i < validation.size(); i++)
	{
	  fichier2 << validation[i].get_x1() << " "  << validation[i].get_x2() << " " << validation[i].get_etiquette()  << std::endl; // Entrée dans le fichier
	   
	}   
    }

  fichier.close();
  fichier2.close();
  return 0;
}

