import os
from opentok import MediaModes, OpenTok, Roles

class OpentokService():
  @classmethod
  def opentok(cls):
    return  OpenTok(
              os.getenv("OPENTOK_API_KEY"),
              os.getenv("OPENTOK_SECRET")
            )
  @classmethod
  def gen_opentok_session_id(cls):
    session = cls.opentok().create_session(media_mode=MediaModes.routed)
    return session.session_id