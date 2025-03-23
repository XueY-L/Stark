from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/home/yuanxue/Stark-main/data/got10k_lmdb'
    settings.got10k_path = '/home/yuanxue/data/OpenDataLab___GOT-10k/raw/GOT-10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_lmdb_path = '/home/yuanxue/Stark-main/data/lasot_lmdb'
    settings.lasot_path = '/home/yuanxue/data/OpenDataLab___LaSOT/raw/LaSOT'
    settings.network_path = '/home/yuanxue/Stark-main/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/home/yuanxue/Stark-main/data/nfs'
    settings.otb_path = '/home/yuanxue/data/OpenDataLab___OTB100/raw'
    settings.prj_dir = '/home/yuanxue/Stark-main'
    settings.result_plot_path = '/home/yuanxue/Stark-main/test/result_plots'
    settings.results_path = '/home/yuanxue/Stark-main/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/home/yuanxue/Stark-main'
    settings.segmentation_path = '/home/yuanxue/Stark-main/test/segmentation_results'
    settings.tc128_path = '/home/yuanxue/Stark-main/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tpl_path = ''
    settings.trackingnet_path = '/home/yuanxue/data/OpenDataLab___TrackingNet/raw'
    settings.uav_path = '/home/yuanxue/Stark-main/data/UAV123'
    settings.vot_path = '/home/yuanxue/Stark-main/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

