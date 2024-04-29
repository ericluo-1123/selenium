
import os
import sys

from normal import method
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path_current_dir = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    pass

    try:       
  
        method.FileDelete(method.PathJoin(path_current_dir, 'PASS'))
        method.FileDelete(method.PathJoin(path_current_dir, 'FAIL'))
        method.FileDelete(method.PathJoin(path_current_dir, 'STOP'))
        
        config_data = method.PyConfigParser()
        config = method.PyConfigParser()
        config.read(method.PathJoin(path_current_dir, 'config.ini'))
        #[env]
        output_file_name = method.ConfigGet(config, 'env', 'output_file_name', 'output.txt')
        method.FileDelete(method.PathJoin(path_current_dir, output_file_name))
        #[logger]
        # loggers = method.ConfigGet(config, 'logger', 'loggers', 'all')
        logger_file_name = method.ConfigGet(config, 'logger', 'file_name', 'sys.log')
        # logger_level = method.ConfigGet(config, 'logger', 'level', 'INFO')
        method.FileDelete(method.PathJoin(path_current_dir, logger_file_name))
        # logger = method.LoggerLoad(loggers, logger_file_name, logger_level)
        # if logger == None: raise RuntimeError("LoggerLoad Fail."
      
        
    except Exception as e:
        method.Logging(config, path_current_dir, 'ERROR', '{}'.format(e))
    
    finally:
        method.Logging(config, path_current_dir, 'INFO', 'Finish.')
    
        
        