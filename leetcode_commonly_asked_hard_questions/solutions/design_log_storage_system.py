class LogSystem:

    def __init__(self):
        self.id_to_timestamps = []

    def put(self, id: int, timestamp: str) -> None:
        self.id_to_timestamps.append((id, timestamp))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        gran_to_idx = {
          "Year": 5,
          "Month": 8,
          "Day": 11,
          "Hour": 14,
          "Minute": 17,
          "Second": 20,
        }
        index = gran_to_idx[gra]
        return [
        	id for id, ts in self.id_to_timestamps if s[:index] <= ts[:index] <= e[:index]
        ]




# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
