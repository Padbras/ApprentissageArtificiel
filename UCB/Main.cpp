#include <vector>
#include "Manchot.hpp"


double rechercheUCB(int nbIterations, std::vector<Manchot> manchots, double k)
{
  double nbTirages[manchots.size()] = {0};
  double scoresUCB[manchots.size()] = {0};
  double scoresTotaux[manchots.size()] = {0};
  double test = 0;
  double sommeGains = 0; 
  int tmpIndice = -1;
  double tmpUCB = -100000;

  for(int i = 0; i< manchots.size(); i++) // Premier tirage de chaque machine
    {
      test = manchots[i].tirer_bras();
      nbTirages[i]++;
      scoresTotaux[i] += test; // Scores de gains
      sommeGains += test;
    }

  for(int i = 0; i< manchots.size(); i++) 
    {
      scoresUCB[i] = (scoresTotaux[i]/nbTirages[i]) + k * (sqrt(log(manchots.size())/nbTirages[i])); // MàJ tableau UCB
    }

  test = 0;
  for(int i = 0; i<nbIterations-manchots.size(); i++) // Boucle principale
    {        
      for(int j = 0; j< manchots.size(); j++) 
	{
	  if(scoresUCB[j]> tmpUCB)
	    {
	      tmpUCB = scoresUCB[j];
	      tmpIndice = j; 
	    }
	}
      test = manchots[tmpIndice].tirer_bras();
      sommeGains += test;
      scoresTotaux[tmpIndice] = scoresTotaux[tmpIndice]+test;
      nbTirages[tmpIndice]++;

      for(int h = 0; h< manchots.size(); h++) 
	{
	  scoresUCB[h] = (scoresTotaux[h]/nbTirages[h]) + k * (sqrt(log((manchots.size()+i))/nbTirages[h]));
	}
  

      tmpIndice = -1;
      tmpUCB = -100000;
      test = 0;
    }

  std::cout << "Gains totaux (UCB):" << sommeGains << std::endl;


  std::cout << "Répartition des itérations" << std::endl;

  for(int i = 0; i< manchots.size(); i++) 
    {
      std::cout << nbTirages[i] << " " ;
    }

  std::cout << std::endl;

}


double rechercheAleatoire(int nbIterations, std::vector<Manchot> manchots)
{
  double sommeGains = 0;
  for(int i = 0; i < nbIterations; i++)
    {
      sommeGains += manchots[rand()%manchots.size()].tirer_bras();
    }
  std::cout << "Gains totaux (aleatoire):" << sommeGains << std::endl;
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

  std::cout << "Gains totaux (glouton):" << sommeGains << std::endl;
}

int main (int argc, char **argv)
{

  if(argc!=2)
    {
      std::cout << "Pas assez d'arguments, entrez sous la forme ./a.out nb_manchots" << std::endl;
    }
  std::vector<Manchot> manchots;
  srand(time(NULL));

  for(int i = 0; i< atoi(argv[1]); i++){
    Manchot tmp_manchots;
    manchots.push_back(tmp_manchots);
  }


  rechercheAleatoire(150000, manchots);
  rechercheGloutonne(150000, manchots);
  rechercheUCB(150000, manchots, 2);

  
 
  return 0;
}
