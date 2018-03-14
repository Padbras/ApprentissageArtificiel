#include "Neurone.hpp"


Neurone::Neurone(int taille)
{
  
  sortie = 0;
  biais = 0.5;
  
  for(int i = 0; i < taille; i++)
    {
      poids.push_back((double)rand()/RAND_MAX); 
    }
  
}

void Neurone::to_string()
{
  std::cout << "Sortie:" << sortie << std::endl ;
  std::cout << "Biais:" << biais << std::endl;
  std::cout << "Vecteur de poids: " ;

  for(int i = 0 ; i < poids.size(); i++)
    {
      std::cout << " " << poids[i];
    }

  std::cout << std::endl;

}

void Neurone::calculer_sortie(Point exemple)
{
  sortie =  (exemple.get_x1()*poids[0] +  exemple.get_x2()*poids[1])-biais; 
}

void Neurone::maj_neurone(Point exemple)
{
  biais = biais + PAS_APPRENTISSAGE * (exemple.get_etiquette() * sortie) * -0.5;

  poids[0] =  poids[0] + PAS_APPRENTISSAGE * (exemple.get_etiquette() - sortie) * exemple.get_x1();
  poids[1] =  poids[1] + PAS_APPRENTISSAGE * (exemple.get_etiquette() - sortie) * exemple.get_x2();
  
}

int Neurone::get_sortie()
{
  return sortie;
}
