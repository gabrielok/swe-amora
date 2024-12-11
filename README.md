# swe-amora

Back end challenge for aMORA.
   
## Using Conda
Since this project utilizes conda for package management, you have to use the provided 
terminal (Anaconda Prompt) to run commands. This will ensure you use the proper version
of python and packages. Here's a step-by-step:
1. Install Conda (if not installed): https://docs.anaconda.com/miniconda/
2. Open the Anaconda Prompt app.
3. Navigate to the project directory.
   1. First time: create the environment.
   ```bash
   conda env create -f environment.yml
   ```
   2. Next time(s): activate the environment.
   ```bash
   conda activate swe-amora
   ```

## Running the project

1. Install and run postgres locally.
2. Run psql on the terminal and create the database:
```postgresql
CREATE DATABASE amora;
```
3. Create a .env file with DB_USER and DB_PASSWORD entries.
4. Run the setup file:
   ```bash
   python src/setup.py
   ```