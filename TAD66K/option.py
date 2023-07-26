import argparse

def init():
    parser = argparse.ArgumentParser(description="PyTorch")
    parser.add_argument('--path_to_images', type=str, default='/fast_dataset/shuai/my_scene/',
                        help='directory to images')
    parser.add_argument('--path_to_save_csv', type=str,default="./dataset/TAD66K/",
                        help='directory to csv_folder')
    parser.add_argument('--experiment_dir_name', type=str, default='.',
                        help='directory to project')
    parser.add_argument('--path_to_model_weight', type=str, default='TAD66K_AOT_vacc_0.6882_srcc_0.5171_vlcc_0.5460.pth',
                        help='directory to pretrain model')
    parser.add_argument('--init_lr', type=int, default=0.00001, help='learning_rate'
                        )
    parser.add_argument('--num_epoch', type=int, default=25, help='epoch num for train'
                        )
    parser.add_argument('--batch_size', type=int,default=16,help='16how many pictures to process one time'
                        )
    parser.add_argument('--num_workers', type=int, default=6, help ='num_workers',
                        )
    parser.add_argument('--gpu_id', type=str, default='0', help='which gpu to use')

    args = parser.parse_args()
    return args