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
