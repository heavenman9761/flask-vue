from json import encoder
from flask import request, jsonify
from flask_restx import Resource, Namespace
import json
from models.database import db_session
from models.Model import TbPeeDetectorData, TbBandData, TbIaqData
from datetime import datetime
from set_logger.set_logger import logger
import requests

BuildIt = Namespace('BuildIt')

@BuildIt.route('/data')
class getData(Resource):
    def post(self):
        post_data = request.get_json()
        data=json.dumps(post_data)
        try:
            res = requests.post('http://127.0.0.1:5001/receiver', data)
        except Exception as e:
            logger.error("request error: " + str(e))
            
        # print(json.dumps(post_data, indent=2))
        if post_data['type'] == 'Band':
            devices = post_data['devices']
            parse_band(post_data['id'], devices)
            # print_devices(devices)

        elif post_data['type'] == 'Pee Detector':
            devices = post_data['devices']
            parse_pee(post_data['id'], devices)
            # print_devices(devices)

        elif post_data['type'] == 'IAQ':
            devices = post_data['devices']
            parse_iaq(post_data['id'], devices)
            # print_devices(devices)

        return {}, 200

@BuildIt.route('/attr')
class getAttr(Resource):
    def post(self):
        # post_data = request.get_json()
        # print(json.dumps(post_data, indent=2))
        return {}, 200

def print_devices(devices):
    for d in devices:
        print(d)

def parse_pee(gatewayMac, devices):
    for d in devices:
        name = d['name']
        packet = d['advertising']
        # print(packet)
        buff = []
        for i in range(0, int(len(packet) / 2)):
            buff.append(int(packet[i * 2: i * 2 + 2], 16))

        offset = 2
        x = buff[offset + 9]
        y = buff[offset + 10]
        z = buff[offset + 11]
        sConnect = ''
        if buff[offset + 12] == 0x00:
            sConnect = 'D'
        elif buff[offset + 12] == 0x01:
            sConnect = 'C'
        elif buff[offset + 12] == 0x03:
            sConnect = 'X'
        wetness = (buff[offset + 14] << 8) + buff[offset + 13]
        battery = buff[offset + 15] * 0.01 + 2.0
        temperature = 0.0
        if buff[offset + 16] == 0xFF:
            temperature = 50.0
        elif buff[offset + 16] == 0xFE:
            temperature = 0.0
        else:
            temperature = buff[offset + 16] * 0.5

        isFall = '1' if buff[19] >= 128 else '0'
        pose = ''
        inverted = ''
        if (isFall == '0'):
            if buff[offset + 17] >> 5 == 0x01:
                inverted = '■'
            else:
                inverted = "□"
            if buff[offset + 17] >> 4 == 0x01:
                pose = "┃"
            if buff[offset + 17] >> 3 == 0x01:
                pose = "┫"
            if buff[offset + 17] >> 2 == 0x01:
                pose = "┻"
            if buff[offset + 17] >> 1 == 0x01:
                pose = "┠"
            if buff[offset + 17] == 0x00:
                pose = "┯"
        isActive = '0' if buff[offset + 18] == 0xFF else '1'
        dt_now = datetime.now()
        date = dt_now.strftime('%Y-%m-%d %H:%M:%S')

        if isFall == '1':
            print(d['id'], date, '========================= 낙상')
            try:
                data = {"msg": "fall", "id": d['id']}
                res = requests.post('http://127.0.0.1:5000/iotdata', json.dumps(data))
            except Exception as e:
                logger.error("request error: " + str(e))

        try:
            t = TbPeeDetectorData(date, name, gatewayMac, d['id'], int(d['rssi']), float(x), float(y), float(z), sConnect, wetness, float(battery), float(temperature), inverted, pose, isFall, isActive)
            db_session.add(t) 
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            logger.error("error in commit to db===" + str(e))
        # else:
            # logger.info("=========success commit data to db==============")
        finally:
            db_session.close()

def parse_band(gatewayMac, devices):
    for d in devices:
        name = d['name']
        packet = d['scanresponse']
        buff = []
        for i in range(0, int(len(packet) / 2)):
            buff.append(int(packet[i * 2: i * 2 + 2], 16))

        activeDuration = buff[16] * 65535 + buff[17] * 256 + buff[18]
        steps = buff[19] * 65535 + buff[20] * 256 + buff[21]
        calories = buff[22] * 256 + buff[23]
        distance = buff[24] * 256 + buff[25]
        heart_rate = buff[26]
        sleep_time = buff[27] * 256 + buff[28]

        dt_now = datetime.now()
        date = dt_now.strftime('%Y-%m-%d %H:%M:%S')

        try:
            t = TbBandData(date, name, gatewayMac, d['id'], int(d['rssi']), activeDuration, steps, calories, distance, heart_rate, sleep_time)
            db_session.add(t) 
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            logger.error("error in query from db===" + str(e))
        # else:
            # logger.info("=========success commit data to db==============")
        finally:
            db_session.close()

def parse_iaq(gatewayMac, devices):
    for d in devices:
        dt_now = datetime.now()
        date = dt_now.strftime('%Y-%m-%d %H:%M:%S')
        try:
            t = TbIaqData(date, d['name'], gatewayMac, d['id'], int(d['rssi']), 
                float(d['pm_1_0']), float(d['pm_2_5']), float(d['pm_10_0']), float(d['temp_c']), float(d['temp_f']), 
                float(d['humi']), float(d['co_2']), float(d['tvoc']), float(d['score']))
            db_session.add(t) 
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            logger.error("error in query from db===" + str(e))
        # else:
            # logger.info("=========success commit data to db==============")
        finally:
            db_session.close()
