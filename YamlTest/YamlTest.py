import yaml
import os
import argparse
import subprocess
import sys

#設定ファイル(config.yaml)のパスを作る
#config.yamlはこのファイルと同じ階層に置くルールとする
config_path = os.path.dirname(__file__) + '\\config.yaml'

def parser():
  argparser = argparse.ArgumentParser(usage="{} [--lpath <file>] [--rpath <file>] [--cpath <file>] [--mode <diff|merge>] [--help]".format(__file__))
  argparser.add_argument('-l', '--lpath', help="左側のファイルパス")
  argparser.add_argument('-r', '--rpath', help="右側のファイルパス")
  argparser.add_argument('-c', '--cpath', help="中央のファイルパス")
  argparser.add_argument('-m', '--mode', help="差分またはマージモードを指定する")
  args = argparser.parse_args()
  return args

def DiffFunc(extstr, args, extlist, toollist):
  ext = extlist[extstr]
  diff = ext['diff']
  tool = toollist[diff]
  opt = tool['diff']
  #lpathとrpathを実パスに置換する
  opt = opt.replace('$(lpath)', '\"' + args.lpath + '\"')
  opt = opt.replace('$(rpath)', '\"' + args.rpath + '\"')
  cmd = ('\"' + tool['path'] + '\"', opt)
  result = subprocess.run(cmd)
  return result.returncode

args = parser()

if __name__ == '__main__':
  exit_code = -1
  try:
    with open(config_path) as file:
      obj = yaml.load(file)

      obj_toollist = obj['toollist']
      toollist = {}
      for x in obj_toollist:
        tool = obj_toollist[x]
        path = tool['path']
        diff = tool['diff']
        merge = tool['merge']
        toollist[x] = { 'path': path, 'diff': diff, 'merge': merge }

      obj_extlist = obj['extlist']
      extlist = {}
      for x in obj_extlist:
        exts = x.split(',')
        for ext in exts:
          diff = obj_extlist[x]['diff']
          merge = obj_extlist[x]['merge']
          extlist.setdefault('.' + ext, {'diff': diff, 'merge': merge})

      if False:
        print('')
      elif args.mode == 'merge':
        print('')
      elif args.mode == 'diff':
        assert os.path.exists(args.lpath), '{0}が存在しません'.format(args.lpath)
        assert os.path.exists(args.rpath), '{0}が存在しません'.format(args.rpath)
        lroot, lext = os.path.splitext(args.lpath)
        rroot, rext = os.path.splitext(args.rpath)
        if (lext in extlist):
          exit_code = DiffFunc(lext, args, extlist, toollist)
        elif (rext in extlist):
          exit_code = DiffFunc(rext, args, extlist, toollist)
        elif ('.other' in extlist):
          exit_code = DiffFunc('.other', args, extlist, toollist)
  except Exception as e:
    print(e.args)
  finally:
    sys.exit(exit_code)