import pip
from subprocess import call

# List of packages to check
packages = [
    'pandas', 'numpy', 'statsmodels', 'pandas_datareader', 'matplotlib',
    'yfinance', 'pandas_ta', 'scikit-learn', 'pypfopt', 'pypfopt', 'cvxpy'
]

# Create an empty dictionary to store package versions
package_versions = {}

# Loop over each package and get its version
for package in packages:
    try:
        package_version = pip.__version__._get_metadata_lines(
            f'${package}$')[0].split(' ')[-1]
        package_versions[package] = package_version
    except Exception:
        package_versions[package] = 'Not Found'

# Print the package versions
for package, version in package_versions.items():
    print(f'{package}: {version}')

# Save package versions to a requirements.txt file
with open('requirements.txt', 'w') as file:
    for package, version in package_versions.items():
        file.write(f'{package}=={version}\n')

# Install the packages with specific versions from the requirements.txt file
call(["pip", "install", "-r", "requirements.txt"])
