echo "****************** Installing pytorch ******************"
conda install -y pytorch==1.7.0 torchvision==0.8.1 cudatoolkit=11.0 -c pytorch

echo ""
echo ""
echo "****************** Installing yaml ******************"
pip install PyYAML

echo ""
echo ""
echo "****************** Installing easydict ******************"
pip install easydict

echo ""
echo ""
echo "****************** Installing cython ******************"
pip install cython

echo ""
echo ""
echo "****************** Installing opencv-python ******************"
pip install opencv-python==4.3.0.38

echo ""
echo ""
echo "****************** Installing pandas ******************"
pip install pandas

echo ""
echo ""
echo "****************** Installing tqdm ******************"
conda install -y tqdm

echo ""
echo ""
echo "****************** Installing coco toolkit ******************"
pip install pycocotools

echo ""
echo ""
echo "****************** Installing jpeg4py python wrapper ******************"
apt-get install libturbojpeg
pip install jpeg4py

echo ""
echo ""
echo "****************** Installing tensorboard ******************"
pip install tb-nightly

echo ""
echo ""
echo "****************** Installing tikzplotlib ******************"
pip install tikzplotlib

echo ""
echo ""
echo "****************** Installing thop tool for FLOPs and Params computing ******************"
# pip install --upgrade git+https://github.com/Lyken17/pytorch-OpCounter.git

echo ""
echo ""
echo "****************** Installing colorama ******************"
pip install colorama

echo ""
echo ""
echo "****************** Installing lmdb ******************"
pip install lmdb

echo ""
echo ""
echo "****************** Installing scipy ******************"
pip install scipy

echo ""
echo ""
echo "****************** Installing visdom ******************"
pip install visdom

echo ""
echo ""
echo "****************** Installing vot-toolkit python ******************"
# pip install git+https://github.com/votchallenge/vot-toolkit-python

echo ""
echo ""
echo "****************** Installing onnx and onnxruntime-gpu ******************"
pip install onnx onnxruntime-gpu==1.6.0

echo ""
echo ""
echo "****************** Installing timm ******************"
pip install timm==0.3.2

echo ""
echo ""
echo "****************** Installing tensorboardX yacs ******************"
pip install tensorboardX
pip install yacs

echo ""
echo ""

echo "****************** Installation complete! ******************"
