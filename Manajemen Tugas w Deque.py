from collections import deque

class TaskManajer:
    def __init__(self):
        self.tasks = deque()
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self):
        if not self.is_empty():
            return self.tasks.popleft()
        else:
            return"Tidak ada tugas dalam antrian"
    def add_urgent_taks(self, task):
        self.tasks.appendleft(task)
    def display_task(self):
        print(list(self.tasks))
    def is_empty(self):
        return len(self.tasks) == 0

if __name__ == "__main__":
    tasks = TaskManajer()
    tasks.add_task("Tugas Struktur Data")
    tasks.add_task("Tugas Logika dan Himpunan")
    tasks.add_urgent_taks("Laporan praktikum")
    print("Daftar Tugas:")
    tasks.display_task()
    print("Tugas dikerjakan: ", tasks.remove_task())
    print("Daftar Tugas setelah pemrosesan:")
    tasks.display_task()