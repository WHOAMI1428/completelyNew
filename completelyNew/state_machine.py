class workpiece:
    def __init__(self, color):
        self.color = color
        self.state = "at front"
        
# TODO:        
# 我感觉还要改。可视化的时候要考虑物块位置先后排列。chute要加一个各location占据情况
# chute满的情况还要考虑


class StateMachine:
    def __init__(self):
        self.conveyor_belt_state = "stopped"
        self.barrier_arm_state = "extended"
        self.sorting_arm1_state = "retracted"
        self.sorting_arm2_state = "retracted"
        self.chute1_state = "not full"
        self.chute1_num = 0
        self.chute2_state = "not full"
        self.chute2_num = 0
        self.chute3_state = "not full"
        self.chute3_num = 0
        self.workpiece_list=[]
        # self.workpiece_state = "at front"
        # self.workpiece_color = "black"
        # self.workpiece_state = workpiece.state
        # self.workpiece_color = workpiece.color
        
    def add_workpiece(self, workpiece):
        self.workpiece_list.append(workpiece(self.workpiece_color))
        
    def start_conveyor_belt(self):
        # if self.conveyor_belt_state == "stopped":
        self.workpiece_state =self.workpiece_list[0].state
        self.workpiece_color = self.workpiece_list[0].color
        self.conveyor_belt_state = "running"
        print("Conveyor belt started.")
        # else:
        #     print("Conveyor belt is already running.")

    def stop_conveyor_belt(self):
        self.conveyor_belt_state = "stopped"
        print("Conveyor belt stopped.")

    def extend_barrier_arm(self):
        # if self.conveyor_belt_state == "stopped":
        self.barrier_arm_state = "extended"
        print("Barrier arm extended.")
        # else:
        #     print("Cannot extend barrier arm. Conveyor belt is running.")

    def retract_barrier_arm(self):
        self.barrier_arm_state = "retracted"
        print("Barrier arm retracted.")

    def extend_sorting_arm1(self):
        # if self.conveyor_belt_state == "stopped":
        self.sorting_arm1_state = "extended"
        print("Sorting arm1 extended.")
        # else:
        #     print("Cannot extend sorting arm1. Conveyor belt is running.")

    def retract_sorting_arm1(self):
        self.sorting_arm1_state = "retracted"
        print("Sorting arm1 retracted.")

    def extend_sorting_arm2(self):
        # if self.conveyor_belt_state == "stopped":
        self.sorting_arm2_state = "extended"
        print("Sorting arm2 extended.")
        # else:
        #     print("Cannot extend sorting arm2. Conveyor belt is running.")

    def retract_sorting_arm2(self):
        self.sorting_arm2_state = "retracted"
        print("Sorting arm2 retracted.")

    def fill_chute1(self):
        if self.chute1_num != 3:
            self.chute1_num += 1
            print("Chute1 num + 1. Now num: " + str(self.chute1_num))
            if self.chute1_num == 3:
                self.chute1_state = "full"
                print("Chute1 is full.")
        

    def empty_chute1(self):
        self.chute1_state = "not full"
        self.chute1_num = 0
        print("Chute1 emptied.")

    def fill_chute2(self):
        if self.chute2_num != 3:
            self.chute2_num += 1
            print("Chute2 num + 1. Now num: " + str(self.chute2_num))
            if self.chute2_num == 3:
                self.chute2_state = "full"
                print("Chute2 is full.")

    def empty_chute2(self):
        self.chute2_state = "not full"
        self.chute2_num = 0
        print("Chute2 emptied.")

    def fill_chute3(self):
        if self.chute3_num != 3:
            self.chute3_num += 1
            print("Chute3 num + 1. Now num: " + str(self.chute3_num))
            if self.chute3_num == 3:
                self.chute3_state = "full"
                print("Chute3 is full.")

    def empty_chute3(self):
        self.chute3_state = "not full"
        self.chute3_num = 0
        print("Chute3 emptied.")

    def move_workpiece(self, location):
        if location == "at front":
            self.workpiece_state = "at detection"
            print("Move workpiece from front to detection")
        elif location == "at detection":
            self.workpiece_state = "at chute"
            print("Move workpiece from detection to chute")

    def transition_from_initial_to_detection(self):
        self.start_conveyor_belt()
        # time.sleep(1)  # Placeholder for running the conveyor belt for some time
        self.move_workpiece("at front")
        self.workpiece_list.pop(0)
        # time.sleep(1)  # Placeholder for the workpiece to reach the color detection device
        

    def transition_from_detection_to_chute(self):
        if self.workpiece_color == "black":
            self.retract_barrier_arm()
            self.move_workpiece("at detection")
            # time.sleep(1)
            self.fill_chute3()
        elif self.workpiece_color == "metallic":
            self.extend_sorting_arm2()
            self.retract_barrier_arm()
            self.move_workpiece("at detection")
            self.fill_chute2()
            self.retract_sorting_arm2()
        elif self.workpiece_color == "red":
            self.extend_sorting_arm1()
            self.retract_barrier_arm()
            self.move_workpiece("at detection")
            self.fill_chute1()
            self.retract_sorting_arm1()

    def transition_from_chute_to_beginning(self):
        self.stop_conveyor_belt()
        self.extend_barrier_arm()
        

