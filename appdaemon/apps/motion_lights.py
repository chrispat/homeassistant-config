import appdaemon.plugins.hass.hassapi as hass

class SimpleMotionLight(hass.Hass):
  def initialize(self):
    self.timer_handle = None
    if "light" not in self.args:
      self.log("argument 'light' not provided")
      return

    if "binary_sensor" in self.args:
      self.log("watching {}".format(self.args['binary_sensor']))
      self.listen_state(self.state_change_handler, self.args["binary_sensor"], new="on")
    else:
      self.log("argument 'binary_sensor' not provided", level = "ERROR")
  
  def state_change_handler(self, entity, attribute, old, new, kwargs):
    self.log("{} state changed (old: {}, new: {})".format(entity, old, new))
    self.turn_on(self.args['light'])

    if "off_delay" in self.args:
      delay = self.args["off_delay"]
    else:
      delay = 60
    
    self.cancel_timer(self.timer_handle)

    self.log("scheduling off in {} seconds".format(delay))
    self.timer_handle = self.run_in(self.turn_off_callback, delay)

  def turn_off_callback(self, kwargs):
    self.log("turning off")
    self.turn_off(self.args['light'])