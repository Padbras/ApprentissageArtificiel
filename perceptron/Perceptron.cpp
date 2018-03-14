#include <fstream>
#include <vector>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include "Point.hpp"
#include "Neurone.hpp"

int main (int argc, char **argv){
  
  if (argc != 2){
    std::cout << "Pas assez d'arguments, entrez sous la forme ./a.out taille_appr taille_test" << std::endl;
  }
  
  std::vector<Point> apprentissage;
  std::vector<Point> validation;
  Neurone neurone(2);
  int nb_erreurs = 0;
  int cptIterations = 0;
  bool stop = false ;

  srand(time(NULL));

  // TEMPORAIRE? LECTURE DE FICHIERS? 
  for(int i = 0; i< atoi(argv[1]); i++){
    Point tmpapr;
    apprentissage.push_back(tmpapr);
  }

  for(int j = 0; j< atoi(argv[2]); j++){
    Point tmpval;
    validation.push_back(tmpval);
  }
  
  while(cptIterations++ != 100 && stop == false)
    {
      for(int i = 0; i< apprentissage.size(); i++)
	{
	  neurone.calculer_sortie(apprentissage[i]);

	  if(neurone.get_sortie() != apprentissage[i].get_etiquette())
	    {
	      neurone.maj_neurone(apprentissage[i]);
	      nb_erreurs++;
	    }
	}
      std::cout << "NOMBRE D'ERREURS (app): " << nb_erreurs << std::endl;
      if(nb_erreurs == 0)
	{
	  stop = true;
	  std::cout << "ARRET A L'ITERATION: " << cptIterations << std::endl;
	 
	}
      else
	{
	  nb_erreurs = 0;
	}

    }

  for(int i = 0; i< validation.size(); i++)
    {
      neurone.calculer_sortie(validation[i]);

      if(neurone.get_sortie() != validation[i].get_etiquette())
	{
	  nb_erreurs++;
	}
    }
  std::cout << "NB ERREURS BASE VALIDATION: " << nb_erreurs << std::endl;
  
  return 0;
}
