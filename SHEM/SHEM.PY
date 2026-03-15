class SmartEnergyAgent:

    def __init__(self):
        self.price_threshold = 0.30
        self.room_occupied = True

    def perceive(self, price, occupancy):
        self.current_price = price
        self.room_occupied = occupancy

    def decide(self):
        if not self.room_occupied:
            return "TURN_OFF_LIGHT"

        if self.current_price > self.price_threshold:
            return "DIM_LIGHTS"

        return "NORMAL_OPERATION"

    def act(self, action):
        if action == "TURN_OFF_LIGHT":
            print("Action: Turning off lights")

        elif action == "DIM_LIGHTS":
            print("Action: Dimming lights to 50%")

        else:
            print("Action: No change")

agent = SmartEnergyAgent()

agent.perceive(price=0.40, occupancy=False)
decision = agent.decide()
agent.act(decision)