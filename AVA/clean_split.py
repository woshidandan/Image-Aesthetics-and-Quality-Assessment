import os
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
import numpy as np
from tqdm import tqdm
from torchvision.datasets.folder import default_loader
from sklearn.model_selection import train_test_split
import option


def remove_all_not_found(df, path_to_images):
    clean_rows = []
    for _, row in df.iterrows():
        image_id = row['image_id']
        try:
            _ = default_loader(os.path.join(path_to_images, f"{image_id}.jpg"))
        except (FileNotFoundError, OSError):
            pass
        else:
            clean_rows.append(row)
    df_clean = pd.DataFrame(clean_rows)
    return df_clean

# 多线程操作
def remove_all_not_found_image(df, path_to_images, num_workers = 64):
    futures = []
    results = []
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for df_batch in np.array_split(df, num_workers):
            future = executor.submit(remove_all_not_found, df=df_batch, path_to_images=path_to_images)
            futures.append(future)
        for future in tqdm(as_completed(futures)):
            results.append(future.result())
    new_df = pd.concat(results)
    return new_df


# 对标签做重新处理
def read_ava_txt(path_to_ava):
    df = pd.read_csv(path_to_ava, header=None, sep=' ')
    del df[0]
    scores_names = [f'score{i}' for i in range(2,12)]
    tag_names = [f'tag{i}' for i in range(1, 4)]
    df.columns = ['image_id'] + scores_names + tag_names
    return df


def clean_and_split(opt):
    df = read_ava_txt(opt.path_to_ava_txt)
    df = remove_all_not_found_image(df, opt.path_to_images)

    df_train, df_val_test = train_test_split(df, train_size=0.9)
    df_val, df_test = train_test_split(df_val_test, train_size=0.5)
    if not os.path.exists(opt.path_to_save_csv):
        os.makedirs(opt.path_to_save_csv)

    df_train.to_csv(os.path.join(opt.path_to_save_csv, 'train.csv'), index=False)
    df_val.to_csv(os.path.join(opt.path_to_save_csv, 'val.csv'), index=False)
    df_test.to_csv(os.path.join(opt.path_to_save_csv, 'test.csv'), index=False)


if __name__ == '__main__':
     opt = option.init()
     clean_and_split(opt)