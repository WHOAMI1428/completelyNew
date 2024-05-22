from flask import Flask, render_template, jsonify
from state_machine import StateMachine 
app = Flask(__name__)

# Global variables to keep track of the state
sm=StateMachine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_black_workpiece', methods=['GET'])
def create_black_workpiece():
    workpiece_html = '<div class="workpiece" style="left: 0px; top: 100px;"></div>'
    return workpiece_html

@app.route('/create_metallic_workpiece', methods=['GET'])
def create_metallic_workpiece():

    workpiece_html = '<div class="workpiece" style="left: 0px; top: 100px;"></div>'
    return workpiece_html

@app.route('/create_red_workpiece', methods=['GET'])
def create_red_workpiece():
    workpiece_html = '<div class="workpiece" style="left: 0px; top: 100px;"></div>'
    return workpiece_html

@app.route('/move_workpiece', methods=['POST'])
def move_workpiece():
    workpiece_distance += 20  # 每次移动 20px
    return jsonify(success=True)

@app.route('/move_to_chute3', methods=['POST'])
def move_to_chute3():
    global workpiece_state
    workpiece_state = "at chute"  # 更新工件状态为在分拣槽位置
    return jsonify(success=True)

@app.route('/move_to_barrier', methods=['POST'])
def move_to_barrier():
    global workpiece_state
    workpiece_state = "at barrier"  # 更新工件状态为在分拣槽位置
    return jsonify(success=True)

@app.route('/retract_barrier_arm', methods=['POST'])
def retract_barrier_arm():
    global barrier_arm_state
    barrier_arm_state = 'retracted'
    return jsonify(success=True)

@app.route('/extend_barrier_arm', methods=['POST'])
def extend_barrier_arm():
    global barrier_arm_state
    barrier_arm_state = 'extended'
    return jsonify(success=True)

@app.route('/retract_sorting_arm1', methods=['POST'])
def retract_sorting_arm1():
    global sorting_arm1_state
    sorting_arm1_state = 'retracted'
    return jsonify(success=True)

@app.route('/extend_sorting_arm1', methods=['POST'])
def extend_sorting_arm1():
    global sorting_arm1_state
    sorting_arm1_state = 'extended'
    return jsonify(success=True)

@app.route('/retract_sorting_arm2', methods=['POST'])
def retract_sorting_arm2():
    global sorting_arm2_state
    sorting_arm2_state = 'retracted'
    return jsonify(success=True)

@app.route('/extend_sorting_arm2', methods=['POST'])
def extend_sorting_arm2():
    global sorting_arm2_state
    sorting_arm2_state = 'extended'
    return jsonify(success=True)


app.run(debug=True)