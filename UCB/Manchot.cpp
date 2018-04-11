#include "Manchot.hpp"


Manchot::Manchot(double esperance, double variance)
{
  _esperance = esperance;
  _variance = variance;
}


Manchot::Manchot()
{
  _esperance = (double)(rand()%20-10);
  _variance = (double)(rand()%10);
}

void Manchot::to_string()
{
  std::cout << "Esperance : " << _esperance <<std::endl;
  std::cout << "Variance : " << _variance << std::endl;
}

double Manchot::tirer_bras()
{
  double rand1 = ((rand() / (double) RAND_MAX ));
  double rand2 = ((rand() / (double) RAND_MAX ));
  return _variance*sqrt(-2.0*log(rand1))*cos(2*M_PI*rand2)+_esperance;
}
