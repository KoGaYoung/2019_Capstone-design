import struct
from struct import unpack
import matplotlib.pyplot as plt
from matplotlib import transforms
import sys
import os
import errno
import multiprocessing
from mpl_toolkits.mplot3d import axes3d


def unpack_drawing(file_handle):
    key_id, = unpack('Q', file_handle.read(8))
    countrycode, = unpack('2s', file_handle.read(2))
    recognized, = unpack('b', file_handle.read(1))
    timestamp, = unpack('I', file_handle.read(4))
    n_strokes, = unpack('H', file_handle.read(2))
    image = []
    for i in range(n_strokes):
        n_points, = unpack('H', file_handle.read(2))
        fmt = str(n_points) + 'B'
        x = unpack(fmt, file_handle.read(n_points))
        y = unpack(fmt, file_handle.read(n_points))
        image.append((x, y))

    return {
        'key_id': key_id,
        'countrycode': countrycode,
        'recognized': recognized,
        'timestamp': timestamp,
        'image': image
    }


def unpack_drawings(filename):
    with open(filename, 'rb') as f:
        while True:
            try:
                yield unpack_drawing(f)
            except struct.error:
                break


def data_preprocessing(filename, path):
    _dpi = 100
    count = 0
    data_file_name = filename + ".bin"
    for drawing in unpack_drawings(data_file_name):
        image_array = drawing['image']
        plt.clf()
        plt.figure(figsize=(331 / _dpi, 333 / _dpi), dpi=_dpi)
        for x in range(len(image_array)):
            x1, y1 = image_array[x][0], image_array[x][1]
            plt.plot(x1, y1, color='k')

        save_path = path + str(count) + ".png"
        plt.axis('off')
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0, dpi=_dpi)
        plt.close()
        print("save png:", save_path)
        count += 1


def is_list(files):
    if type(files) == str:
        load_binfile(files)
    else:
        for i in range(len(files)):
            load_binfile(files[i])


def load_binfile(file_name):
    data_folder_name = file_name
    data_file_name = file_name + ".bin"
    data_folder_path = "./" + data_folder_name + "/"
    try:
        os.makedirs(data_folder_path)
        print('mkdir -p', data_folder_path)
        data_processing(file_name, data_folder_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(data_folder_path + "/" + data_folder_name + "/"):
            print('already exist folder')
            data_processing(data_file_name)
            pass
        else:
            raise


def get_process_schedule():
    process_count = 4
    data_count = len(sys.argv) - 1
    list = []
    if data_count < 5:
        for i in range(data_count):
            list.append(sys.argv[i + 1])
        return list
    else:
        for i in range(process_count):
            list.append([])
        for i in range(data_count):
            list[i % 4].append(sys.argv[i + 1])
        return list


if __name__ == "__main__":
    process = []
    for files in get_process_schedule():
        p = multiprocessing.Process(target=load_binfile, args=(files,))
        process.append(p)
        p.start()

    for p in process:
        p.join()

