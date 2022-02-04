# Two_Grains_Output

Data, Plots and Code for Curve Fitting of Magnetic Force Between Two Identical Paramagnetic Particles in Uniform Magnetic Field

More Data can be found at: https://docs.google.com/spreadsheets/d/1fKWJL0KRET4cCD3GnCUX3TCXCahcP3Il6l8_Q8eH0-0/edit?usp=sharing

## Procedure

1. First fitting on individual suspetibility data is done to get parameters of the inverse polynomial function. {scipy_curvefit.py}
2. Based on the plots of each parameter with suscpetibilty a curve is fitted for parameters. (Power law for parallel case and cubic polynomial for perpendicular case) {param_curvefit}
3. Now, with the new curves known for susceptibility dependence, complete curve fitting is checked for each susceptibility and complete R-square value is computed. {complete_function_fit}
4. The parameters for the complete function are computed by complete curve with the initial guess found before. 
5. These parameters found from initial guess are considered the final results.
6. Stability of the complete model function is checked.
