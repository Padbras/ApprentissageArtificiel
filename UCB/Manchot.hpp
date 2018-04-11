#ifndef MANCHOT_HPP
#define MANCHOT_HPP

#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <math.h>

class Manchot {
protected:
  double _esperance;
  double _variance;

public:
  Manchot(double esperance, double variance);
  Manchot();
  void to_string();
  double tirer_bras();
  
};
#endif
