# YOLOv8
1. 更新顯示卡驅動程式 要支援CUDA 11.7或11.8
2. 安裝顯示卡驅動 CUDA 11.7或11.8
3. 查詢 CUDA 版本  命令列輸入 nvidia-smi
4. 安裝 PyTorch 至 https://pytorch.org/ 找到 PyTorch2.0 選取對應的環境選項
5. 虛擬環境下輸入 pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
6. 複製YOLOv8專案 虛擬環境下輸入 pip install ultralytics
7. 安裝 opencv-python 套件
-------要跑影音串流才安裝以下套件--------
8. 安裝 pafy 套件
9. 安裝 youtube-dl 套件
10. 變更 youtube-dl 套件版本 pip install youtube-dl==2020.12.02