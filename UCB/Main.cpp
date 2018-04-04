#include <vector>
#include "Manchot.hpp"

double rechercheUCB(int nbIterations, std::vector<Manchot> manchots)
{
  std::vector<int> nbTirages;
  std::vector<double> scores;
  double test; 
  for(int i = 0; i< manchots.size(); i++)
    {
      nbTirages.push_back(0);
      scores.push_back(0);
    }
  
  for(int i = 0; i< manchots.size(); i++)
    {
      test = manchots[i].tirer_bras();
      nbTirages[i]++;
      
      
    }
}

double rechercheAleatoire(int nbIterations, std::vector<Manchot> manchots)
{
  double sommeGains = 0;
  for(int i = 0; i < nbIterations; i++)
    {
      sommeGains += manchots[rand()%manchots.size()].tirer_bras();
    }
  std::cout << "Gains totaux:" << sommeGains << std::endl;
}

double rechercheGloutonne(int nbIterations, std::vector<Manchot> manchots)
{
  double sommeGains = 0;
  double bestResult = -10000;
  int bestRank = -1;
  double tmpResult;
  for(int i = 0; i< manchots.size(); i++)
    {
      tmpResult = manchots[i].tirer_bras();
	if(tmpResult > bestResult)
	  {
	    bestResult = tmpResult;
	    bestRank = i ;
	  }
      sommeGains += tmpResult;
    }

  for(int j = manchots.size(); j< nbIterations; j++)
    {
      sommeGains += manchots[bestRank].tirer_bras();
    }

  std::cout << "Gains totaux:" << sommeGains << std::endl;
}

int main (int argc, char **argv)
{
  srand(time(NULL));
  Manchot m1(2,2);
  Manchot m2(3,3);
  Manchot m3(5,6);

  std::vector<Manchot> manchots;
  manchots.push_back(m1);
  manchots.push_back(m2);
  manchots.push_back(m3);

  m1.to_string();
  double test;
  test = m1.tirer_bras();

  std::cout << "Resultat test:" << test << std::endl;

  rechercheAleatoire(5, manchots);
  rechercheGloutonne(5, manchots);
  rechercheUCB(5, manchots);

  
 
  return 0;
}
