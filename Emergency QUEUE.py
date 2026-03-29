import heapq

class EmergencyQueue:
    def __init__(self):
        self.queue = []
    def add_patient(self, name, priority):
        heapq.heappush(self.queue, (priority, name))
    def process_patient(self):
        if not self.is_empty():
            return heapq.heappop (self.queue)[1]
        else:
            return "Antrian Kosong"
    def display_queue(self):
        sorted_queue = sorted(self.queue)
        print([patient[1] for patient in sorted_queue])
    def is_empty(self):
        return len (self.queue) == 0
    
if __name__ == "__main__":
    queue = EmergencyQueue()
    queue.add_patient("Andi", 2)
    queue.add_patient("Budi", 1)
    queue.add_patient("Citra", 3)
    queue.add_patient("Dewi", 1)  
    print("Antrian saat ini: ")
    queue.display_queue()
    print("Pasien diproses: ", queue.process_patient())
    print("Antiran setelah pemrosesan: ")
    queue.display_queue()