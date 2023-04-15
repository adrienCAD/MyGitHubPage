import os
import subprocess

def update_and_push_console_output():
    # Copy console output to your GitHub Pages repository
    source_path = "/Users/adriencaudron/CODE/ALGOTRADING_Research/Coding_Experiments/Deployment/logfile.log"
    target_path = "/Users/adriencaudron/CODE/adrienCAD.github.io/logfile.log"
    subprocess.run(["cp", source_path, target_path])

    # Change directory to your GitHub Pages repository
    os.chdir("/Users/adriencaudron/CODE/adrienCAD.github.io")

    # Add the updated file to Git
    subprocess.run(["git", "add", "logfile.log"])

    # Commit the changes
    subprocess.run(["git", "commit", "-m", "Update logfile.log"])

    # Push the changes to GitHub
    subprocess.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    update_and_push_console_output()
