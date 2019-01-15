import appdaemon.plugins.hass.hassapi as hass

class SensorTriggeredLight(hass.Hass):
  """
  Monitors a list of binary_sensors
    when any turn on
      turn on all specified lights
    after a configurable delay
      turn them off.
  
  Retriggering during the delay period will extend the delay.

  Arguments:
    - binary_sensors    - (list) which binary_sensors to monitor for state change
    - lights            - (list) which lights to turn on/off
    - turn_off_delay    - (int) how many seconds before turning off
  """

  def initialize(self):
    self.timer_handle = None

    if "binary_sensors" in self.args:
      self.log("watching {}".format(self.args['binary_sensors']))
      for entity in self.args['binary_sensors']:
        self.listen_state(self.state_change_handler, entity, old="off", new="on")
    else:
      self.log("argument 'binary_sensor' not provided", level = "ERROR")
      return

    if "lights" in self.args:
      self.log("will turn on/off these lights: {}".format(self.args['lights']))
    else:
      self.log("argument 'lights' not provided")
      return

  def state_change_handler(self, entity, attribute, old, new, kwargs):

    self.log("turning on {}".format(self.args['lights']))
    for entity in self.args['lights']:
      self.turn_on(entity)

    if "turn_off_delay" in self.args:
      delay = self.args["turn_off_delay"]
    else:
      delay = 60
    
    self.cancel_timer(self.timer_handle)

    self.log("scheduling off in {} seconds".format(delay))
    self.timer_handle = self.run_in(self.turn_off_callback, delay)

  def turn_off_callback(self, kwargs):
    self.log("turning off {}".format(self.args['lights']))
    for entity in self.args['lights']:
      self.turn_on(entity)
