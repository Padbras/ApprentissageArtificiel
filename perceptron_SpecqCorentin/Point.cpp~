#include "Point.hpp"

Point::Point()
{


  x1 = (double)rand()/RAND_MAX;
  x2 = (double)rand()/RAND_MAX;

  if((x1+x2-1)>0)
  {
    etiquette = 1;
  }
  else
  {
    etiquette = 0; 
  }

}

void Point::to_string()
{
  std::cout << "----------------------------" << std::endl;
  std::cout << "x1:" << x1 << std::endl;
  std::cout << "x2:" << x2 << std::endl;
  std::cout << "etiquette:" << etiquette << std::endl;
  std::cout << "----------------------------" <<  std::endl;
}

double Point::get_x1()
{
return x1;
}
double Point::get_x2()
{
return x2;
}
int Point::get_etiquette()
{
return etiquette;
}
