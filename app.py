import os
import sys

sys.path.append(os.path.join(sys.path[0],'Hybrid','chatbot'))#Set the csv file directory
path = "./Hybrid/chatbot"
os.chdir( path )

import test_hybrid as hy

hy.app.run()