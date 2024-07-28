'''To install Python packages from the Python Package Index (PyPI) into Visual Studio Code, you typically use the integrated terminal within VS Code itself. Here’s a step-by-step guide:

Open Visual Studio Code: Launch VS Code on your computer.

Open the Integrated Terminal:

You can open the integrated terminal in VS Code by pressing Ctrl+ (backtick) or by navigating to View > Terminal from the top menu.
Install the Package:

In the terminal that opens at the bottom of the VS Code window, use pip, the Python package installer, to install packages from PyPI. Here's the general command format:
pip install 'package_name'


Replace package_name with the name of the package you want to install.

For example, to install the requests package, you would type:
pip install requests

Confirm Installation:

Once you enter the command, pip will download and install the package along with any dependencies it requires. You should see output in the terminal indicating the progress and success of the installation.
Verify Installation (if necessary):

If you want to verify that the package was installed correctly, you can check by running the following command in the terminal:
pip show package_name

Use the Package:

Now that the package is installed, you can import and use it in your Python code within VS Code. Remember to import the package at the beginning of your script:
import package_name

By following these steps, you can easily install Python packages from PyPI into Visual Studio Code and start using them in your projects.
'''

from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
my_table.add_column("Type", ["Electric", "Water", "Fire"])
my_table.align = "l"
print(my_table)

