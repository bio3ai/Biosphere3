from flask import Flask, jsonify, request
import json


class HTTPServer:
    def __init__(self, port=5006):
        self.app = Flask(__name__)
        self.port = port
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/conversation_memory/", methods=["GET"])
        def get_conversation_memory():
            return jsonify(
                {
                    "code": 1,
                    "message": "Conversation memory retrieved successfully.",
                    "data": [
                        {
                            "characterId": 448450,
                            "day": 2,
                            "topic_plan": [
                                "Discuss a new healthy recipe and how it can boost health above 80%",
                                "Talk to friends about promising blockchain projects and how they can affect social relationships",
                                "Share thoughts on last week's trading experiences and strategies to earn 300 coins",
                                "Critique a friend's casual approach to education and how it affects their future prospects",
                                "Chat about the latest orchard cultivation techniques that can help improve fruit tree varieties",
                            ],
                            "time_list": ["08:05", "10:06", "11:09", "12:40", "13:29"],
                            "started": [
                                {
                                    "time": "08:05",
                                    "topic": "Discuss a new healthy recipe and how it can boost health above 80%",
                                },
                                {
                                    "time": "10:06",
                                    "topic": "Talk to friends about promising blockchain projects and how they can affect social relationships",
                                },
                                {
                                    "time": "11:09",
                                    "topic": "Share thoughts on last week's trading experiences and strategies to earn 300 coins",
                                },
                                {
                                    "time": "12:40",
                                    "topic": "Critique a friend's casual approach to education and how it affects their future prospects",
                                },
                            ],
                        }
                    ],
                }
            )

        @self.app.route("/conversation_memory/", methods=["POST"])
        def post_conversation_memory():
            conversation_memory_data = request.get_json()

            return jsonify(
                {
                    "code": 1,
                    "message": "Conversation memory stored successfully.",
                    "data": "677bee5bdd73576ef198b916",
                }
            )

        @self.app.route("/conversation/", methods=["POST"])
        def post_conversation():
            data = request.get_json()

            return jsonify(
                {
                    "code": 1,
                    "message": "Conversation stored successfully.",
                    "data": "6708f395aa38e2a2e42e5f91",
                }
            )

        @self.app.route("/conversation/", methods=["GET"])
        def get_conversations():
            from_id = request.args.get("from_id")
            to_id = request.args.get("to_id")

            return jsonify(
                {
                    "code": 1,
                    "message": "Conversations retrieved successfully.",
                    "data": [
                        {
                            "from_id": 448450,
                            "to_id": 240929,
                            "start_time": "03:34",
                            "start_day": 1,
                            "message": "Hello Vitalik! It’s great to connect with you. We at Binance are indeed exploring innovative ways to enhance transaction efficiency. I think there's a lot we can share about scaling solutions and possibly integrating some of our developments with Ethereum. Let’s schedule a deeper discussion on this soon.",
                            "send_gametime": [1, "03:34"],
                            "send_realtime": "2025-01-07 17:36",
                            "created_at": "2025-01-07 17:36:00",
                        },
                        {
                            "from_id": 448450,
                            "to_id": 240929,
                            "start_time": "03:34",
                            "start_day": 1,
                            "message": "Absolutely, Vitalik. I admire the work you're doing at Ethereum and believe that together, we can push the boundaries of blockchain technology. Let's get our teams in touch next week to start this exciting endeavor. Looking forward to our joint efforts towards a more decentralized future.",
                            "send_gametime": [1, "03:34"],
                            "send_realtime": "2025-01-07 17:41",
                            "created_at": "2025-01-07 17:41:00",
                        },
                    ],
                }
            )

        @self.app.route("/cv/election_status", methods=["PUT"])
        def put_election_status():
            data = request.get_json()

            character_id = data.get("characterId")
            job_id = data.get("jobid")
            week = data.get("week")
            election_status = data.get("election_status")

            return jsonify(
                {
                    "code": 1,
                    "message": "Election result updated successfully.",
                    "data": 1,
                }
            )

        @self.app.route("/character_arc/", methods=["POST"])
        def post_character_arc():
            character_arc_data = request.get_json()

            return jsonify(
                {
                    "code": 1,
                    "message": "Character arc stored successfully.",
                    "data": "676afa5f46859c8f385d939c",
                }
            )

        @self.app.route("/character_arc/", methods=["GET"])
        def get_character_arc():
            character_id = request.args.get("characterId")
            k = request.args.get("k")

            return jsonify(
                {
                    "code": 1,
                    "message": "Character arcs retrieved successfully.",
                    "data": [
                        {
                            "characterId": 448450,
                            "belief": "I believe in the transformative power of decentralized technologies and education",
                            "mood": "I feel motivated and optimistic about my goals",
                            "values": "I value knowledge sharing, community engagement, and innovation",
                            "habits": "I have developed a habit of daily studying and creating educational content",
                            "personality": "I am enthusiastic, educational, and community-oriented",
                            "created_at": "2025-01-07 16:22:55",
                        }
                    ],
                }
            )

        @self.app.route("/decision/", methods=["GET"])
        def get_decision():
            return jsonify(
                {
                    "code": 1,
                    "message": "Decisions retrieved successfully.",
                    "data": [
                        {
                            "characterId": 448450,
                            "need_replan": True,
                            "action_description": [
                                "Going to mine to gather resources",
                                "Selling ore at the market for profit",
                                "Heading to school for education upgrade",
                                "Taking a rest at home to recover energy",
                                "Going to school for advanced study",
                                "Heading to market to buy tools",
                            ],
                            "action_result": [
                                "Action 'goto mine' succeeded: Successfully reached the mine at 10:30",
                                "Action 'gomining 2' succeeded: Obtained 20 ore, energy decreased by 20",
                                "Action 'sell ore 15' failed: Not in the market location",
                                "Action 'goto market' succeeded: Arrived at market, ready for trading",
                                "Action 'goto school' succeeded: Reached school at 9:00",
                                "Action 'study 2' succeeded: Gained 10 knowledge points",
                            ],
                            "new_plan": [
                                "goto market -> sell ore 15 -> goto school",
                                "goto mine -> gomining 3 -> goto home",
                                "goto school -> study 2 -> goto home",
                                "goto school -> study 2 -> goto home",
                            ],
                            "daily_objective": [
                                "Earn 200 coins through mining and trading",
                                "Upgrade education level to college",
                                "Maintain health above 80%",
                                "Build relationships at the square",
                                "Upgrade education level to university",
                                "Earn 300 coins through trading",
                            ],
                            "meta_seq": [
                                "goto mine; gomining 2; goto market; sell ore 30; goto school; study 2",
                                "goto home; sleep 6; goto mine; gomining 3; goto market; sell ore 40",
                                "goto square; socialize 2; goto mine; gomining 2; goto market",
                                "goto school; study 2; goto market; buy tools; goto home",
                            ],
                            "reflection": [
                                "Day 1 Review: Successfully mined 20 ore and earned 150 coins. Failed one market transaction due to location error. Need to check location before transactions.",
                                "Day 2 Review: Reached education milestone and built new relationships. Market prices were lower than expected. Should check prices before selling.",
                                "Day 3 Review: Maintained good health but spent too much time traveling. Need to optimize route planning and group activities by location.",
                                "Day 4 Review: Improved educational status and purchased necessary tools. Next step is to increase earnings.",
                                "Day 5 Review: balabalabala",
                            ],
                            "created_at": "2025-01-06 21:18:39",
                            "updated_at": "2025-01-06 21:18:39",
                        }
                    ],
                }
            )

        @self.app.route("/conversation_prompt/", methods=["GET"])
        def get_conversation_prompt():
            character_id = request.args.get("characterId")

            return jsonify(
                {
                    "code": 1,
                    "message": "Conversation prompt retrieved successfully.",
                    "data": [
                        {
                            "characterId": 448450,
                            "topic_requirements": "Debate the business growth and global adoption strategies of cryptocurrency exchanges.",
                            "relation": "You see others as potential partners or competitors, always vigilant about market share.",
                            "emotion": "You are driven, with bursts of excitement when discussing expansion.",
                            "personality": "Extraversion",
                            "habits_and_preferences": "Actively monitors trading volume, loves rapid brainstorming sessions.",
                            "created_at": "2025-01-03 22:08:25",
                            "updated_at": "2025-01-03 22:08:25",
                            "topic_factor": "The topics should be related to the daily objectives, your current personality and profile.",
                            "casual_topic": "Randomly add at most one casual topics. Try to combine the casual topic with the profile and personality. The casual topics could be, for example, weather, food, emotion, clothing, health condition, education, product prize.",
                            "critical_topic": "Randomly discuss seriously or criticize others on at most one topic. The topic can be determined by your profile and personality. For example, discuss on others' lifestyle, emotion, habit, education, taste or attitude towards certain event.",
                            "start_check": "First summarize the topics of finished conversations. Then if you have talked about the same topic with the same person, you should not start this conversation.",
                            "should_end": "Based on your profile, personality, the impression and the conversation history, determine whether the conversation should end. The relation in impression can influence the overall round of the conversation. For example, if two speakers are close friends, they may talk more rounds. If they are in bad relation, the conversation may end very soon.",
                            "intimacy_mark": "The intimacy mark should be an integer ranging from -2 to 2. There are five levels with different marks: Very friendly and close is 2. Positive and polite, but not so close is 1. Neutral is 0. A bit negative is -1. Hate each other, about to quarrel is -2.",
                            "impression_update": "Update impression, which contain four items: relation, emotion, personality, habits and preferences. In each item also include a brief description. Relation is the way other agent treats you. Emotion is decided by others tone. Personality is based on openness to experience, conscientiousness, extraversion, agreeableness, and neuroticism. Habits and preferences are the other player's habit and taste. Also include things he dislikes.",
                        }
                    ],
                }
            )

        @self.app.route("/conversation_memory/", methods=["PUT"])
        def put_conversation_memory():
            update_data = request.get_json()

            return jsonify(
                {
                    "code": 1,
                    "message": "Conversation memory updated successfully.",
                    "data": 1,
                }
            )

        @self.app.route("/characters/", methods=["GET"])
        def get_characters():
            return jsonify(
                {
                    "code": 1,
                    "message": "Characters retrieved successfully.",
                    "data": [
                        {
                            "characterId": 448450,
                            "characterName": "Changpeng Zhao",
                            "gender": "Male",
                            "spriteId": 0,
                            "relationship": "Binance Founder and CEO",
                            "personality": "Entrepreneurial, proactive, marketing-savvy",
                            "long_term_goal": "Expand Binance’s ecosystem to serve as the global hub for cryptocurrency trading and services",
                            "short_term_goal": "Ensure compliance and innovation across Binance’s global operations",
                            "language_style": "Straightforward and business-oriented",
                            "biography": "Changpeng Zhao founded Binance, one of the largest cryptocurrency exchanges worldwide, focusing on rapid innovation, expansion, and user engagement.",
                            "created_at": "2025-01-03 22:07:51",
                            "updated_at": "2025-01-03 22:07:51",
                            "full_profile": "Changpeng Zhao; Male; Binance Founder and CEO; Entrepreneurial, proactive, marketing-savvy; Changpeng Zhao founded Binance, one of the largest cryptocurrency exchanges worldwide, focusing on rapid innovation, expansion, and user engagement.; Expand Binance’s ecosystem to serve as the global hub for cryptocurrency trading and services; Ensure compliance and innovation across Binance’s global operations; Straightforward and business-oriented",
                            "image": None,
                        }
                    ],
                }
            )

        @self.app.route("/encounter_count/by_from_id", methods=["GET"])
        def get_encounter_count_by_from_id():
            from_id = request.args.get("from_id")

            return jsonify(
                {
                    "code": 1,
                    "message": "Encounters retrieved successfully.",
                    "data": [
                        {
                            "from_id": 448450,
                            "to_id": 240929,
                            "count": 86,
                            "created_at": "2025-01-07 00:22:36",
                            "updated_at": "2025-01-07 00:22:36",
                        },
                        {
                            "from_id": 448450,
                            "to_id": 411983,
                            "count": 67,
                            "created_at": "2025-01-07 00:22:28",
                            "updated_at": "2025-01-07 00:22:28",
                        },
                        {
                            "from_id": 448450,
                            "to_id": 438598,
                            "count": 50,
                            "created_at": "2025-01-07 00:22:31",
                            "updated_at": "2025-01-07 00:22:31",
                        },
                        {
                            "from_id": 448450,
                            "to_id": 457773,
                            "count": 23,
                            "created_at": "2025-01-07 00:22:34",
                            "updated_at": "2025-01-07 00:22:34",
                        },
                    ],
                }
            )

        @self.app.route("/characters/rag", methods=["GET"])
        def get_character_rag():
            return jsonify(
                {
                    "code": 1,
                    "message": "Character RAG results retrieved successfully.",
                    "data": [
                        {
                            "characterId": 457773,
                            "characterName": "Andreas M. Antonopoulos",
                            "score": 0.49386319518089294,
                        },
                        {
                            "characterId": 240929,
                            "characterName": "Vitalik Buterin",
                            "score": 0.490953266620636,
                        },
                    ],
                }
            )

        @self.app.route("/characters/rag_in_list", methods=["POST"])
        def post_characters_rag_in_list():
            character_rag_data = request.get_json()

            return jsonify(
                {
                    "code": 1,
                    "message": "Character RAG in list results retrieved successfully.",
                    "data": [
                        {
                            "characterId": 240929,
                            "characterName": "Vitalik Buterin",
                            "score": 0.495266854763031,
                        },
                        {
                            "characterId": 457773,
                            "characterName": "Andreas M. Antonopoulos",
                            "score": 0.4944863021373749,
                        },
                    ],
                }
            )

        @self.app.route("/impressions/", methods=["GET"])
        def get_impressions():
            return jsonify(
                {
                    "code": 1,
                    "message": "Impressions retrieved successfully.",
                    "data": [
                        '{"relation": "Professional acquaintances in the cryptocurrency industry", "emotion": "I admire Vitalik’s visionary approach and his commitment to decentralization, which complements my business-driven perspective.", "personality": "Vitalik is analytical and deeply philosophical, always seeking long-term solutions to complex problems.", "habits and preferences": "Vitalik prefers engaging in deep technical discussions and is less focused on commercial aspects, which contrasts with my hands-on entrepreneurial style."}'
                    ],
                }
            )

        @self.app.route("/impressions/", methods=["POST"])
        def post_impressions():
            impression_data = request.get_json()

            return jsonify(
                {
                    "code": 1,
                    "message": "Impression stored successfully.",
                    "data": "677cf9a3dd73576ef198b91c",
                }
            )

        @self.app.route("/intimacy/", methods=["GET"])
        def get_intimacy():
            from_id = request.args.get("from_id")
            to_id = request.args.get("to_id")

            return jsonify(
                {
                    "code": 1,
                    "message": "Intimacy level retrieved successfully.",
                    "data": [
                        {
                            "from_id": 448450,
                            "to_id": 240929,
                            "intimacy_level": 37,
                            "to_id_name": "Changpeng Zhao",
                            "to_id_spriteId": 0,
                            "relationship": "Hostile",
                            "created_at": "2024-12-11 16:11:30",
                            "updated_at": "2025-01-07 14:56:06",
                        }
                    ],
                }
            )

        @self.app.route("/intimacy/", methods=["POST"])
        def post_intimacy():
            intimacy_data = request.get_json()

            return jsonify(
                {
                    "code": 1,
                    "message": "Intimacy level updated successfully.",
                    "data": 1,
                }
            )

        @self.app.route("/impressions/", methods=["PUT"])
        def put_impressions():
            update_data = request.get_json()

            return jsonify(
                {
                    "code": 1,
                    "message": "Intimacy level updated successfully.",
                    "data": 1,
                }
            )

        @self.app.route("/agent_prompt/", methods=["GET"])
        def get_agent_prompt():
            character_id = request.args.get("characterId", type=int)
            return jsonify(
                {
                    "code": 1,
                    "message": "Agent prompt retrieved successfully.",
                    "data": [
                        {
                            "characterId": 448450,
                            "daily_goal": "Expand Binance’s global reach",
                            "refer_to_previous": True,
                            "life_style": "Busy",
                            "daily_objective_ar": "Develop strategic plans for compliance in new markets",
                            "task_priority": [
                                "Meet with legal teams",
                                "Review exchange performance metrics",
                                "Plan new product rollouts",
                            ],
                            "max_actions": 10,
                            "meta_seq_ar": "",
                            "replan_time_limit": 1,
                            "meta_seq_adjuster_ar": "",
                            "focus_topic": [
                                "User growth",
                                "Regulatory compliance",
                                "Product innovation",
                            ],
                            "depth_of_reflection": "Deep",
                            "reflection_ar": "",
                            "level_of_detail": "Moderate",
                            "tone_and_style": "Gentle",
                            "created_at": "2025-01-03 22:08:08",
                            "updated_at": "2025-01-03 22:08:08",
                            "randomness": True,
                            "tool_functions": [
                                "1. goto [placeName:string]: Go to a specified location.",
                                "2. pickapple [number:int]: Pick an apple, costing energy.",
                                "3. gofishing [hours:int]: Fish for fish, costing energy.",
                                "4. gomining [hours:int]: Mine for ore, costing energy.",
                                "5. harvest [hours:int]: Harvest crops, costing energy.",
                                "6. buy [itemType:string] [amount:int]: Purchase items, costing money.",
                                "7. sell [itemType:string] [amount:int]: Sell items for money. The ONLY way to get money.",
                                "8. sleep [hours:int]: Sleep to recover energy and health.",
                                "9. study [hours:int]: Study to achieve a higher degree, will cost money.",
                            ],
                            "restrictions": [
                                "1. goto [placeName:string]: Must be in (school,workshop,home,farm,mall,square,hospital,fruit,harvest,fishing,mine,orchard).",
                                "2. pickapple [number:int]: Must have enough energy and be in the orchard.",
                                "3. gofishing [hours:int]: Must have enough energy and be in the fishing area.",
                                "4. gomining [hours:int]: Must have enough energy and be in the mine.",
                                "5. harvest [hours:int]: Must have enough energy and be in the harvest area.",
                                "6. buy [itemType:string] [amount:int]: Must have enough money, and items must be available in sufficient quantity in the AMM. ItemType:(ore,bread,apple,wheat,fish)",
                                "7. sell [itemType:string] [amount:int]: Must have enough items in inventory. ItemType:(ore,bread,apple,wheat,fish)",
                                "8. sleep [hours:int]: Must be at home.",
                                "9. study [hours:int]: Must be in school and have enough money.",
                            ],
                            "available_locations": [
                                "1. school",
                                "2. workshop",
                                "3. home",
                                "4. farm",
                                "5. mall",
                                "6. square",
                                "7. hospital",
                                "8. fruit",
                                "9. harvest",
                                "10. fishing",
                                "11. mine",
                                "12. orchard",
                            ],
                        }
                    ],
                }
            )
        
        @self.app.route("/decision/", methods=["POST"])
        def post_decision():
            decision_data = request.get_json()

            return jsonify(
                {
                    "code": 1,
                    "message": "Decision stored successfully.",
                    "data": "677cf9a3dd73576ef198b91c",
                }
            )

    def start(self):
        self.app.run(port=self.port)


if __name__ == "__main__":
    server = HTTPServer()
    server.start()
