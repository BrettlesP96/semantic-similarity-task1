## Building and Running the Docker Container

1. Clone the repository
git clone https://github.com/Brettlesp96/semantic-similarity.git


2. Navigate to the project folder:

cd semantic-similarity


3. Build the Docker image:


docker build -t semantic-similarity .


4. Run the Docker container:

docker run --rm semantic-similarity


The output should display the semantic similarities between the words "cat", "monkey", and "banana".
