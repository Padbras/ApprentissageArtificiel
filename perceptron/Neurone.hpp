#ifndef NEURONE_HPP
#define NEURONE_HPP

#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include "Point.hpp"


#define PAS_APPRENTISSAGE 0.01

class Neurone {
protected:
  double biais;
  std::vector<double> poids;
  int sortie;
public:
  Neurone(int taille);
  void to_string();
  void calculer_sortie(Point exemple);
  void maj_neurone(Point exemple);
  int get_sortie();
    
           
	

		
};
#endif
