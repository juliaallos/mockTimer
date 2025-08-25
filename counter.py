# Julia Allos
# 8/24/25
# Mock Trial Timer using classes (no GUI, with logging)

import sys
import select
import time

class Counter:
    def __init__(self, name, total_time):
        self.name = name
        self.total_time = total_time
        self.time_left = total_time

    def __str__(self):
        mins = self.time_left // 60
        secs = self.time_left % 60
        return f"{self.name}: {mins:02d}:{secs:02d}"

    def tick(self):
        if self.time_left > 0:
            self.time_left -= 1
            return True
        return False

    def reset(self):
        self.time_left = self.total_time

    def get_time_left(self):
        return self.time_left


class TimerApp:
    def __init__(self, segment_order):
        self.segments = [Counter(name, time) for name, time in segment_order]
        self.current = 0
        self.running = False

    def start(self):
        self.running = True

        # Clear the log file at the start
        open("timer_log.txt", "w").close()

        while self.running and 0 <= self.current < len(self.segments):
            current_segment = self.segments[self.current]
            print(f"\n--- Starting: {current_segment.name} ---")

            while current_segment.tick():
                # Live countdown (overwrites one line)
                print(current_segment, end="\r")

                # Log each second to file
                with open("timer_log.txt", "a") as f:
                    f.write(str(current_segment) + "\n")

                time.sleep(1)

                # 🔹 Check keyboard input
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    user_input = sys.stdin.readline().strip()
                    if user_input == "":   # Enter → skip forward
                        print(f"\nSkipped {current_segment.name} early.")
                        break
                    elif user_input.lower() == "b":  # go back
                        print(f"\nGoing back from {current_segment.name}.")
                        self.current = max(0, self.current - 1)
                        break
                    elif user_input.lower() == "q":  # quit
                        print("\nQuitting timer.")
                        self.running = False
                        return

            else:  # finished without skipping
                print(f"\n*** {current_segment.name} finished! ***")

            # Handle next step
            if self.running:
                if 'user_input' in locals() and user_input.lower() == "b":
                    continue  # restart loop at previous segment
                self.current += 1

    def show_final_times(self):
        print("\nFinal Times Remaining:")
        for seg in self.segments:
            print(seg)


def main():
    segment_order = [
        ("P Statements", 14),   # testing: 14 seconds (change back to *60 for minutes)
        ("D Statements", 10),
        ("P Directs", 12),
        ("D Crosses", 8),
        ("D Directs", 6),
        ("P Crosses", 5)
    ]

    app = TimerApp(segment_order)
    app.start()
    app.show_final_times()


if __name__ == "__main__":
    main()
