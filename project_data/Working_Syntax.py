import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
import pandas as pd
from scipy.integrate import odeint #this is the module  we need later to numerically solve differential equations

# Load in dataset from the folder
Total_data=pd.read_csv("../Bio165_FinalProject/data/composition_data/Bio165_InfluenzaAIGG_Assay.csv")
