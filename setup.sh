sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv
sudo apt-get install -y python3-dev
sudo apt-get install -y python3-setuptools python3-numpy
sudo apt-get install -y python3-scipy libatlas-base-dev
sudo apt-get install -y python3-matplotlib

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt