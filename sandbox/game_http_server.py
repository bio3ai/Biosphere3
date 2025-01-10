from flask import Flask, jsonify, request
import json


class HTTPServer:
    def __init__(self, port=5003):
        self.app = Flask(__name__)
        self.port = port
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/characters/getById/<int:id>", methods=["GET"])
        def get_characters_getById(id):
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": {
                        "id": id,
                        "characterName": "Adam Back",
                        "isMale": 1,
                        "spriteId": 1,
                        "controlType": 0,
                        "workType": 0,
                        "jobId": 0,
                        "subjectId": 0,
                        "health": 100,
                        "energy": 100,
                        "hungry": 100,
                        "experience": 10,
                        "education": "PrimarySchool",
                        "money": 110,
                        "createTime": "2025-01-03 22:01:33",
                        "updateTime": "2025-01-06 17:15:17",
                    },
                }
            )

        @self.app.route(
            "/characterDormitory/getByCharacterIdNew/<int:id>", methods=["GET"]
        )
        def get_characterDomitory_getByCharacterIdNew(id):
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": {
                        "id": 47,
                        "characterId": id,
                        "dormitoryId": 2,
                        "dormitoryType": "CapsuleApartment",
                        "startDate": 1,
                        "endDate": 14,
                        "leaseWeeks": 2,
                        "weeklyRent": 20,
                        "totalRent": 40,
                        "createTime": "2025-01-06 15:24:54",
                        "updateTime": "2025-01-06 15:24:54",
                    },
                }
            )

        @self.app.route("/dormitory/getAll", methods=["GET"])
        def get_dormitory_getAll():
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": [
                        {
                            "id": 1,
                            "type": "Shelter",
                            "rentMultiplier": 0,
                            "averageIncome": 80,
                            "weeklyRent": 0,
                            "energyRecovery": 6,
                            "maxEnergy": 60,
                            "maxHealth": 60,
                            "maxHungry": 60,
                            "createTime": "2024-12-31 17:05:42",
                            "updateTime": "2024-12-31 17:05:42",
                        },
                        {
                            "id": 2,
                            "type": "CapsuleApartment",
                            "rentMultiplier": 0.05,
                            "averageIncome": 80,
                            "weeklyRent": 20,
                            "energyRecovery": 10,
                            "maxEnergy": 100,
                            "maxHealth": 100,
                            "maxHungry": 100,
                            "createTime": "2024-12-31 17:05:42",
                            "updateTime": "2024-12-31 17:05:42",
                        },
                        {
                            "id": 3,
                            "type": "BasicApartment",
                            "rentMultiplier": 0.1,
                            "averageIncome": 80,
                            "weeklyRent": 40,
                            "energyRecovery": 12,
                            "maxEnergy": 120,
                            "maxHealth": 120,
                            "maxHungry": 120,
                            "createTime": "2024-12-31 17:05:42",
                            "updateTime": "2024-12-31 17:05:42",
                        },
                        {
                            "id": 4,
                            "type": "StandardApartment",
                            "rentMultiplier": 0.2,
                            "averageIncome": 80,
                            "weeklyRent": 80,
                            "energyRecovery": 14,
                            "maxEnergy": 140,
                            "maxHealth": 140,
                            "maxHungry": 140,
                            "createTime": "2024-12-31 17:05:42",
                            "updateTime": "2024-12-31 17:05:42",
                        },
                        {
                            "id": 5,
                            "type": "LuxuryApartment",
                            "rentMultiplier": 0.4,
                            "averageIncome": 80,
                            "weeklyRent": 160,
                            "energyRecovery": 16,
                            "maxEnergy": 160,
                            "maxHealth": 160,
                            "maxHungry": 160,
                            "createTime": "2024-12-31 17:05:42",
                            "updateTime": "2024-12-31 17:05:42",
                        },
                        {
                            "id": 6,
                            "type": "Suite",
                            "rentMultiplier": 0.6,
                            "averageIncome": 80,
                            "weeklyRent": 240,
                            "energyRecovery": 17,
                            "maxEnergy": 170,
                            "maxHealth": 170,
                            "maxHungry": 170,
                            "createTime": "2024-12-31 17:05:42",
                            "updateTime": "2024-12-31 17:05:42",
                        },
                        {
                            "id": 7,
                            "type": "LuxurySuite",
                            "rentMultiplier": 1.2,
                            "averageIncome": 80,
                            "weeklyRent": 480,
                            "energyRecovery": 18,
                            "maxEnergy": 180,
                            "maxHealth": 180,
                            "maxHungry": 180,
                            "createTime": "2024-12-31 17:05:42",
                            "updateTime": "2024-12-31 17:05:42",
                        },
                        {
                            "id": 8,
                            "type": "Villa",
                            "rentMultiplier": 3,
                            "averageIncome": 80,
                            "weeklyRent": 1200,
                            "energyRecovery": 20,
                            "maxEnergy": 200,
                            "maxHealth": 200,
                            "maxHungry": 200,
                            "createTime": "2024-12-31 17:05:42",
                            "updateTime": "2024-12-31 17:05:42",
                        },
                    ],
                }
            )

        @self.app.route("/characters/getByIdS/<int:id>", methods=["GET"])
        def get_characters_getByIdS(id):
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": {
                        "id": 448450,
                        "characterName": "Adam Back",
                        "isMale": 1,
                        "spriteId": 1,
                        "controlType": 0,
                        "workType": 0,
                        "jobId": 0,
                        "subjectId": 0,
                        "health": 100,
                        "energy": 100,
                        "hungry": 100,
                        "experience": 10,
                        "education": "PrimarySchool",
                        "money": 110,
                        "skillList": [
                            {"skillId": 1, "skillName": "Farmer"},
                            {"skillId": 4, "skillName": "FactoryOwner"},
                            {"skillId": 2, "skillName": "FoodFactoryOwner"},
                            {"skillId": 3, "skillName": "MineOwner"},
                            {"skillId": 5, "skillName": "Scientist"},
                        ],
                    },
                }
            )

        @self.app.route("/publicWork/getAll", methods=["GET"])
        def get_publicWork_getAll():
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": [
                        {
                            "id": 1,
                            "jobType": "AcademicProfession",
                            "jobName": "Intern",
                            "jobPlace": "school",
                            "dailyWages": 80,
                            "education": "SecondarySchool",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 10,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.08,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 2,
                            "jobType": "AcademicProfession",
                            "jobName": "Trainee",
                            "jobPlace": "school",
                            "dailyWages": 120,
                            "education": "University",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 15,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.12,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 3,
                            "jobType": "AcademicProfession",
                            "jobName": "Assistant",
                            "jobPlace": "school",
                            "dailyWages": 200,
                            "education": "Doctorate",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 25,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.12,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 4,
                            "jobType": "AcademicProfession",
                            "jobName": "Programmer",
                            "jobPlace": "school",
                            "dailyWages": 150,
                            "education": "Master",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 18.75,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.16,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 5,
                            "jobType": "AcademicProfession",
                            "jobName": "Researcher",
                            "jobPlace": "school",
                            "dailyWages": 200,
                            "education": "Doctorate",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 25,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.08,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 6,
                            "jobType": "AcademicProfession",
                            "jobName": "Manager",
                            "jobPlace": "school",
                            "dailyWages": 300,
                            "education": "Doctorate",
                            "experience": 1200,
                            "workHours": 8,
                            "wagePerHour": 37.5,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.08,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 7,
                            "jobType": "AcademicProfession",
                            "jobName": "Director",
                            "jobPlace": "school",
                            "dailyWages": 400,
                            "education": "Doctorate",
                            "experience": 1500,
                            "workHours": 8,
                            "wagePerHour": 50,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.06,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 8,
                            "jobType": "AcademicProfession",
                            "jobName": "ChiefOfficer",
                            "jobPlace": "school",
                            "dailyWages": 600,
                            "education": "Doctorate",
                            "experience": 2000,
                            "workHours": 8,
                            "wagePerHour": 75,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.04,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 9,
                            "jobType": "AcademicProfession",
                            "jobName": "President",
                            "jobPlace": "school",
                            "dailyWages": 800,
                            "education": "Doctorate",
                            "experience": 3000,
                            "workHours": 8,
                            "wagePerHour": 100,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.02,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 10,
                            "jobType": "AcademicProfession",
                            "jobName": "Chairman",
                            "jobPlace": "school",
                            "dailyWages": 1000,
                            "education": "Doctorate",
                            "experience": 5000,
                            "workHours": 8,
                            "wagePerHour": 125,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.01,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 11,
                            "jobType": "LogisticsProfession",
                            "jobName": "Guard",
                            "jobPlace": "school",
                            "dailyWages": 80,
                            "education": "PrimarySchool",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 10,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.15,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 12,
                            "jobType": "LogisticsProfession",
                            "jobName": "Cleaner",
                            "jobPlace": "school",
                            "dailyWages": 80,
                            "education": "PrimarySchool",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 10,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.1,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 13,
                            "jobType": "LogisticsProfession",
                            "jobName": "Gardener",
                            "jobPlace": "garden",
                            "dailyWages": 100,
                            "education": "SecondarySchool",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 12.5,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.1,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 14,
                            "jobType": "LogisticsProfession",
                            "jobName": "Police",
                            "jobPlace": "PoliceStations",
                            "dailyWages": 150,
                            "education": "University",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 18.75,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.15,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 15,
                            "jobType": "LogisticsProfession",
                            "jobName": "Cook",
                            "jobPlace": "canteen",
                            "dailyWages": 100,
                            "education": "SecondarySchool",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 12.5,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.1,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 16,
                            "jobType": "LogisticsProfession",
                            "jobName": "Librarian",
                            "jobPlace": "library",
                            "dailyWages": 150,
                            "education": "University",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 18.75,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.1,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                        {
                            "id": 17,
                            "jobType": "LogisticsProfession",
                            "jobName": "StoreClerk",
                            "jobPlace": "supermarket",
                            "dailyWages": 100,
                            "education": "SecondarySchool",
                            "experience": 0,
                            "workHours": 8,
                            "wagePerHour": 12.5,
                            "cvDay": "1,2,3,4,5,6,7",
                            "voteDay": "1,2,3,4,5,6,7",
                            "jobAvailable": 5,
                            "populationRatioCap": 0.1,
                            "createTime": "2024-12-31 16:13:56",
                            "updateTime": "2024-12-31 16:13:56",
                        },
                    ],
                }
            )

        @self.app.route("/publicWork/getById/<int:id>", methods=["GET"])
        def get_publicWork_getById(id):
            all_work_info = get_publicWork_getAll().get_json()
            work_data = all_work_info["data"]
            work_info = next((work for work in work_data if work["id"] == id), None)

            if work_info:
                return jsonify(
                    {
                        "code": 1,
                        "message": "Query successful.",
                        "data": work_info,
                    }
                )
            else:
                return jsonify(
                    {
                        "code": 0,
                        "message": "Work not found.",
                        "data": None,
                    }
                )

        @self.app.route("/publicWork/checkWork", methods=["POST"])
        def post_publicWork_checkWork():
            data = request.get_json()
            character_id = data.get("characterId")
            new_job_id = data.get("newJobId")
            experience = data.get("experience")
            education = data.get("education")

            if character_id and new_job_id and experience is not None and education:
                return jsonify(
                    {"code": 1, "message": "Work verification passed.", "data": None}
                )
            else:
                return jsonify(
                    {"code": 0, "message": "Invalid input data.", "data": None}
                )

        @self.app.route("/characterPower/getAll", methods=["GET"])
        def get_characterPower_getAll():
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": [
                        {
                            "id": 1,
                            "characterId": 448450,
                            "coinCount": 0,
                            "currentPower": 200,
                            "totalPower": 200,
                            "maxStorageDuration": 200,
                            "clickCount": 200,
                            "minutesPerClick": 1,
                            "createTime": "2025-01-04 23:46:06",
                            "updateTime": "2025-01-04 23:46:06",
                        },
                        {
                            "id": 23,
                            "characterId": 438598,
                            "coinCount": 0,
                            "currentPower": 200,
                            "totalPower": 200,
                            "maxStorageDuration": 200,
                            "clickCount": 200,
                            "minutesPerClick": 1,
                            "createTime": "2025-01-04 23:46:50",
                            "updateTime": "2025-01-04 23:46:50",
                        },
                        {
                            "id": 34,
                            "characterId": 411983,
                            "coinCount": 0,
                            "currentPower": 200,
                            "totalPower": 200,
                            "maxStorageDuration": 200,
                            "clickCount": 200,
                            "minutesPerClick": 1,
                            "createTime": "2025-01-04 23:47:12",
                            "updateTime": "2025-01-04 23:47:12",
                        },
                        {
                            "id": 2,
                            "characterId": 457773,
                            "coinCount": 0,
                            "currentPower": 200,
                            "totalPower": 200,
                            "maxStorageDuration": 200,
                            "clickCount": 200,
                            "minutesPerClick": 1,
                            "createTime": "2025-01-04 23:46:08",
                            "updateTime": "2025-01-04 23:46:08",
                        },
                        {
                            "id": 49,
                            "characterId": 240929,
                            "coinCount": 0,
                            "currentPower": 200,
                            "totalPower": 200,
                            "maxStorageDuration": 200,
                            "clickCount": 200,
                            "minutesPerClick": 1,
                            "createTime": "2025-01-04 23:47:42",
                            "updateTime": "2025-01-04 23:47:42",
                        },
                    ],
                }
            )

        @self.app.route("/bag/getByCharacterId/<int:id>", methods=["GET"])
        def get_bag_getByCharacterId(id):
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": [
                        {
                            "id": 2,
                            "characterId": 448450,
                            "itemName": "Bread",
                            "itemQuantity": 1,
                            "createTime": "2025-01-06 17:12:22",
                            "updateTime": "2025-01-06 17:12:22",
                        }
                    ],
                }
            )

        @self.app.route("/ammPool/getAveragePrice", methods=["GET"])
        def get_ammPool_getAveragePrice():
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": [
                        {"name": "apple", "averagePrice": 5},
                        {"name": "wheat", "averagePrice": 1.5},
                        {"name": "pear", "averagePrice": 7},
                        {"name": "rice", "averagePrice": 2},
                        {"name": "chicken", "averagePrice": 10},
                        {"name": "beef", "averagePrice": 50},
                        {"name": "fish", "averagePrice": 7},
                        {"name": "feed", "averagePrice": 4},
                        {"name": "flour", "averagePrice": 7.5},
                        {"name": "bread", "averagePrice": 15.61849},
                        {"name": "apple_pie", "averagePrice": 20},
                        {"name": "fruit_salad", "averagePrice": 12},
                        {"name": "chicken_salad", "averagePrice": 40},
                        {"name": "beef_rice", "averagePrice": 60},
                        {"name": "sushi", "averagePrice": 10},
                        {"name": "iron_ore", "averagePrice": 2},
                        {"name": "wood", "averagePrice": 1.5},
                        {"name": "copper_ore", "averagePrice": 2},
                        {"name": "silica_ore", "averagePrice": 2},
                        {"name": "iron_ingot", "averagePrice": 10},
                        {"name": "wooden_board", "averagePrice": 7.5},
                        {"name": "copper_ingot", "averagePrice": 10},
                        {"name": "pure_silicon", "averagePrice": 10},
                        {"name": "tools", "averagePrice": 30},
                        {"name": "iron_plate", "averagePrice": 25},
                        {"name": "pulp", "averagePrice": 20},
                        {"name": "books", "averagePrice": 120},
                        {"name": "copper_wire", "averagePrice": 25},
                        {"name": "transistor", "averagePrice": 25},
                        {"name": "circuit_board", "averagePrice": 150},
                        {"name": "A100", "averagePrice": 750},
                        {"name": "H100", "averagePrice": 3000},
                        {"name": "H200", "averagePrice": 15000},
                        {"name": "B200", "averagePrice": 80000},
                    ],
                }
            )

        @self.app.route("/CharacterModel/getByCharacterId/<int:id>", methods=["GET"])
        def get_characterModel_getByCharacterId(id):
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": {
                        "id": 47,
                        "characterId": 448450,
                        "modelType": "gpt-4o-mini",
                        "createTime": "2025-01-03 22:05:32",
                    },
                }
            )

        @self.app.route("/characterPower/getByCharacterId/<int:id>", methods=["GET"])
        def get_characterPower_getByCharacterId(id):
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": {
                        "id": 1,
                        "characterId": 448450,
                        "coinCount": 0,
                        "currentPower": 200,
                        "totalPower": 200,
                        "maxStorageDuration": 200,
                        "clickCount": 200,
                        "minutesPerClick": 1,
                        "createTime": "2025-01-04 23:46:06",
                        "updateTime": "2025-01-04 23:46:06",
                    },
                }
            )

        @self.app.route(
            "/characterDormitory/getByCharacterIdNew/<int:id>", methods=["GET"]
        )
        def get_characterDormitory_getByCharacterIdNew(id):
            return jsonify(
                {
                    "code": 1,
                    "message": "Query successful.",
                    "data": {
                        "id": 47,
                        "characterId": 448450,
                        "dormitoryId": 2,
                        "dormitoryType": "CapsuleApartment",
                        "startDate": 1,
                        "endDate": 14,
                        "leaseWeeks": 2,
                        "weeklyRent": 20,
                        "totalRent": 40,
                        "createTime": "2025-01-06 15:24:54",
                        "updateTime": "2025-01-06 15:24:54",
                    },
                }
            )
        
        @self.app.route("/modelToken/add", methods=["POST"])
        def post_modelToken_add():
            data = request.get_json()
            modelType = data.get("modelType")
            prompt = data.get("prompt")
            completion = data.get("completion")
            total = data.get("total")
            return jsonify(
                {
                    "code": 1,
                    "message": "Successfully.",
                    "data": {
                        "id": 9,
                        "modelType": modelType,
                        "prompt": prompt,
                        "completion": completion,
                        "total": total,
                        "createTime": None,
                    },
                }
            )

    def start(self):
        self.app.run(port=self.port)


if __name__ == "__main__":
    server = HTTPServer()
    server.start()
