sudo apt update -y
sudo apt install python3-pip -y
pip install eluci_data/requirements.txt -y
sudo apt install npm -y
cd eluci-data-frontend 
npm i
npm run build
