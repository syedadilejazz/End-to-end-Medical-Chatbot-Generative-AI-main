# End-to-end-Medical-Chatbot-Generative-AI-main
End-to-end-Medical-Chatbot-Generative-AI-main
How to run?
Steps:
1.Clone the repo
#Terminal-
(base) syedadilejaz@SYEDs-MacBook-Air ~ % git --version
git version 2.39.3 (Apple Git-145)
(base) syedadilejaz@SYEDs-MacBook-Air ~ % cd ~/Documents
(base) syedadilejaz@SYEDs-MacBook-Air Documents % pwd
/Users/syedadilejaz/Documents
(base) syedadilejaz@SYEDs-MacBook-Air Documents % git clone https://github.com/syedadilejazz/End-to-end-Medical-Chatbot-Generative-AI-main.git
(base) syedadilejaz@SYEDs-MacBook-Air Documents % cd End-to-end-Medical-Chatbot-Generative-AI-main
(base) syedadilejaz@SYEDs-MacBook-Air End-to-end-Medical-Chatbot-Generative-AI-main % ls
LICENSE		README.md

2. Create a conda environment
(base) syedadilejaz@SYEDs-MacBook-Air End-to-end-Medical-Chatbot-Generative-AI-main % conda create -n llama python=3.10 -y
conda activate llama

3. Integreate the environment in vscode
Press Cmd + Shift + P
Then search:Python: Select Interpreter
Your Conda environment is located at:/Users/syedadilejaz/anaconda3/envs/llama

4. Install the requirements
pip install -r requirements.txt

5.Create a .env file in the root directory and add your pinecone & openai credential as follow-
PINECONE_API_KEY="XXXXXXXXXXX"
OPENAI_API_KEY="XXXXXXXXXXXX"
#run the following command to store embeddings to pinecone
python store_index.py
#finally run the following command
python app.py

Now, open up localhost:

6. Git commit codes-
git add .
git commit -m "<Add your message here>"
git push origin main

7. Create a .env file in the root directory and add your Pinecone and OPenai credentials as follor:
PINECONE_API_KEY="XXXXX"
OPENAI_API_KEY="XXXX"
#RUN the below command
python store_index.py
#Run below
python app.py

Now, open local host:and continue to chat

#TechStack Used:
-Python
-langchain
-Flask
-GPT
-Pinecone
-GitHub


#AWS CICD-Deployment with Github-Actions
1.Login to AWS console.
2.Create IAM user for deployment
    #with specific access
    1.EC@ access:It is virtual machine
    2.ECR:Elastic Container registry to save your docker image in aws

    #Description ABout the deployment
    1. Build docker image of the source code
    2.Push your docker image to ECR
    3.launcg your EC@
    4. Pull your image from ECR to EC2
    5. launch your docker image in EC2
    #Policy:
    1.AmazonEC2ContainerRegistryFullAccess
    2.AmazonEC2FullAccess

3.#Create ECR repo to store/save docker image
    -Save the URL:970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot

4.Create EC@ machine(Ubuntu)

5.Open EC2 and Install docker in EC2 Machine:
    #Optional
    sudo apt-get update -y
    sudo apt-get upgrade
    #required
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker

 6. Configure EC2 as self-hosted runner:
    setting>action>new self runner>choose os>the run command one by one

7.Setup github secrets:
    -AWS_ACCESS_KEY_ID
    -AWS_SECRET-ACCESS_KEY
    -AWS_DEFAULT_REGION
    -ECR_REPO
    -PINECONE_API_KEY
    -OPENAI_API_KEY



