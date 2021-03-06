# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ublox_msgs/CfgUSB.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CfgUSB(genpy.Message):
  _md5sum = "d1797a4ed330d6193bc42a443c001b03"
  _type = "ublox_msgs/CfgUSB"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# UBX-CFG-USB (0x06 0x1B)
# USB Configuration
#

uint8 CLASS_ID = 6
uint8 MESSAGE_ID = 27 

uint16 vendorID             # Only set to registered Vendor IDs.                     
                            # Changing this field requires special Host drivers.

uint16 productID            # Product ID. Changing this field requires special  
                            # Host drivers.

uint8[2] reserved1          # Reserved
uint8[2] reserved2          # Reserved

uint16 powerConsumption     # Power consumed by the device [mA]

uint16 flags                # various configuration flags (see graphic below)
uint16 FLAGS_RE_ENUM = 0       # force re-enumeration
uint16 FLAGS_POWER_MODE = 2    # self-powered (1), bus-powered (0)

int8[32] vendorString      # String containing the vendor name. 
                           # 32 ASCII bytes including 0-termination.
int8[32] productString     # String containing the product name. 
                           # 32 ASCII bytes including 0-termination.
int8[32] serialNumber      # String containing the serial number. 
                           # 32 ASCII bytes including 0-termination. 
                           # Changing the String fields requires special Host 
                           # drivers."""
  # Pseudo-constants
  CLASS_ID = 6
  MESSAGE_ID = 27
  FLAGS_RE_ENUM = 0
  FLAGS_POWER_MODE = 2

  __slots__ = ['vendorID','productID','reserved1','reserved2','powerConsumption','flags','vendorString','productString','serialNumber']
  _slot_types = ['uint16','uint16','uint8[2]','uint8[2]','uint16','uint16','int8[32]','int8[32]','int8[32]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       vendorID,productID,reserved1,reserved2,powerConsumption,flags,vendorString,productString,serialNumber

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CfgUSB, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.vendorID is None:
        self.vendorID = 0
      if self.productID is None:
        self.productID = 0
      if self.reserved1 is None:
        self.reserved1 = b'\0'*2
      if self.reserved2 is None:
        self.reserved2 = b'\0'*2
      if self.powerConsumption is None:
        self.powerConsumption = 0
      if self.flags is None:
        self.flags = 0
      if self.vendorString is None:
        self.vendorString = [0] * 32
      if self.productString is None:
        self.productString = [0] * 32
      if self.serialNumber is None:
        self.serialNumber = [0] * 32
    else:
      self.vendorID = 0
      self.productID = 0
      self.reserved1 = b'\0'*2
      self.reserved2 = b'\0'*2
      self.powerConsumption = 0
      self.flags = 0
      self.vendorString = [0] * 32
      self.productString = [0] * 32
      self.serialNumber = [0] * 32

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2H().pack(_x.vendorID, _x.productID))
      _x = self.reserved1
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_2B().pack(*_x))
      else:
        buff.write(_get_struct_2s().pack(_x))
      _x = self.reserved2
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_2B().pack(*_x))
      else:
        buff.write(_get_struct_2s().pack(_x))
      _x = self
      buff.write(_get_struct_2H().pack(_x.powerConsumption, _x.flags))
      buff.write(_get_struct_32b().pack(*self.vendorString))
      buff.write(_get_struct_32b().pack(*self.productString))
      buff.write(_get_struct_32b().pack(*self.serialNumber))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 4
      (_x.vendorID, _x.productID,) = _get_struct_2H().unpack(str[start:end])
      start = end
      end += 2
      self.reserved1 = str[start:end]
      start = end
      end += 2
      self.reserved2 = str[start:end]
      _x = self
      start = end
      end += 4
      (_x.powerConsumption, _x.flags,) = _get_struct_2H().unpack(str[start:end])
      start = end
      end += 32
      self.vendorString = _get_struct_32b().unpack(str[start:end])
      start = end
      end += 32
      self.productString = _get_struct_32b().unpack(str[start:end])
      start = end
      end += 32
      self.serialNumber = _get_struct_32b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2H().pack(_x.vendorID, _x.productID))
      _x = self.reserved1
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_2B().pack(*_x))
      else:
        buff.write(_get_struct_2s().pack(_x))
      _x = self.reserved2
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_2B().pack(*_x))
      else:
        buff.write(_get_struct_2s().pack(_x))
      _x = self
      buff.write(_get_struct_2H().pack(_x.powerConsumption, _x.flags))
      buff.write(self.vendorString.tostring())
      buff.write(self.productString.tostring())
      buff.write(self.serialNumber.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 4
      (_x.vendorID, _x.productID,) = _get_struct_2H().unpack(str[start:end])
      start = end
      end += 2
      self.reserved1 = str[start:end]
      start = end
      end += 2
      self.reserved2 = str[start:end]
      _x = self
      start = end
      end += 4
      (_x.powerConsumption, _x.flags,) = _get_struct_2H().unpack(str[start:end])
      start = end
      end += 32
      self.vendorString = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=32)
      start = end
      end += 32
      self.productString = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=32)
      start = end
      end += 32
      self.serialNumber = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=32)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B
_struct_2H = None
def _get_struct_2H():
    global _struct_2H
    if _struct_2H is None:
        _struct_2H = struct.Struct("<2H")
    return _struct_2H
_struct_2s = None
def _get_struct_2s():
    global _struct_2s
    if _struct_2s is None:
        _struct_2s = struct.Struct("<2s")
    return _struct_2s
_struct_32b = None
def _get_struct_32b():
    global _struct_32b
    if _struct_32b is None:
        _struct_32b = struct.Struct("<32b")
    return _struct_32b
