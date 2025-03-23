class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/yuanxue/Stark-main'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/yuanxue/Stark-main/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/yuanxue/Stark-main/pretrained_networks'
        self.lasot_dir = '/home/yuanxue/data/OpenDataLab___LaSOT/raw/LaSOT'
        self.got10k_dir = '/home/yuanxue/data/OpenDataLab___GOT-10k/raw/GOT-10k/train'
        self.lasot_lmdb_dir = '/home/yuanxue/Stark-main/data/lasot_lmdb'
        self.got10k_lmdb_dir = '/home/yuanxue/Stark-main/data/got10k_lmdb'
        self.trackingnet_dir = '/home/yuanxue/data/OpenDataLab___TrackingNet/raw'
        self.trackingnet_lmdb_dir = '/home/yuanxue/Stark-main/data/trackingnet_lmdb'
        self.coco_dir = '/home/yuanxue/data/COCO'
        self.coco_lmdb_dir = '/home/yuanxue/Stark-main/data/coco_lmdb'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/yuanxue/Stark-main/data/vid'
        self.imagenet_lmdb_dir = '/home/yuanxue/Stark-main/data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
