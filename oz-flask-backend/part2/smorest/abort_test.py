from flask_smorest import abort

# 오류 상황에서 abort 호출
abort(404, message="Resource not found")