sudo apt update -y && sudo apt upgrade -y
sudo apt install python3-pip -y
pip3 install eluci_data/requirements.txt -y
sudo apt install npm -y
npm i create-react-app
cd eluci-data-frontend 
npm i
npm run build
sudo apt install serve -y
