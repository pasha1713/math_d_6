import configparser
import os
import math
from datetime import datetime, timedelta

# Функция расчета расстояния между двумя точками (в метрах)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # радиус Земли в метрах
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi / 2.0) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def parse_ini_file(ini_path):
    config = configparser.ConfigParser()
    config.read(ini_path)
    
    # Чтение параметров из ini
    limits = config['limits']
    camera = config['camera']
    files = config['files']
    
    delta_time = int(limits['delta_time'])
    camera_max_distance = int(limits['camera_max_distance'])
    speed_limit = int(limits['speed_limit'])
    
    camera_lat = float(camera['lat'])
    camera_lon = float(camera['lon'])
    
    in_path = files['in_path']
    in_file_mask = files['in_file_mask']
    out_file_full = files['out_file_full']
    
    return {
        'delta_time': delta_time,
        'camera_max_distance': camera_max_distance,
        'speed_limit': speed_limit,
        'camera_coords': (camera_lat, camera_lon),
        'paths': {
            'in_path': in_path,
            'in_file_mask': in_file_mask,
            'out_file': out_file_full
        }
    }

def process_files(params):
    camera_lat, camera_lon = params['camera_coords']
    out_file_path = params['paths']['out_file']
    
    with open(out_file_path, 'w') as out_file:
        # Здесь должен быть код обработки файлов
        # Для примера просто выведем заголовок отчета
        out_file.write("Отчет о проездах под камерой\n")
        out_file.write(f"Максимальная дистанция: {params['camera_max_distance']} м\n")
        out_file.write(f"Ограничение скорости: {params['speed_limit']} км/ч\n")
        
        # Пример структуры записи в файл
        # call go.cmd list [имя_файла] [время] [дата_начала] [дата_конца] [скорость] [расстояние]
        
        # TODO: Добавить реальную обработку файлов
        # for file in files:
        #     process_single_file(file, out_file, params)

def main():
    ini_path = 'input.ini'
    params = parse_ini_file(ini_path)
    
    print("Параметры конфигурации:")
    print(f"Путь к файлам: {params['paths']['in_path']}")
    print(f"Маска файлов: {params['paths']['in_file_mask']}")
    print(f"Координаты камеры: {params['camera_coords']}")
    
    process_files(params)
    print("Обработка завершена")

if __name__ == "__main__":
    main()
