import os
import time

full_img: str = r'''
             @m@,.                                 .@
            .@m%nm@,.                            .@m@
           .@nvv%vnmm@,.                      .@mn%n@
          .@mnvvv%vvnnmm@,.                .@mmnv%vn@,
          @mmnnvvv%vvvvvnnmm@,.        .@mmnnvvv%vvnm@
          @mmnnvvvvv%vvvvvvnnmm@, ;;;@mmnnvvvvv%vvvnm@,
          `@mmnnvvvvvv%vvvvvnnmmm;;@mmnnvvvvvv%vvvvnmm@
           `@mmmnnvvvvvv%vvvnnmmm;%mmnnvvvvvv%vvvvnnmm@
             `@m%v%v%v%v%v;%;%;%;%;%;%;%%%vv%vvvvnnnmm@
             .,mm@@@@@mm%;;@@m@m@@m@@m@mm;;%%vvvnnnmm@;@,.
          .,@mmmmmmvv%%;;@@vmvvvvvvvvvmvm@@;;%%vvnnm@;%mmm@,
       .,@mmnnvvvvv%%;;@@vvvvv%%%%%%%vvvvmm@@;;%%mm@;%%nnnnm@,
    .,@mnnvv%v%v%v%%;;@mmvvvv%%;*;*;%%vvvvmmm@;;%m;%%v%v%v%vmm@,.
,@mnnvv%v%v%v%v%v%v%;;@@vvvv%%;*;*;*;%%vvvvm@@;;m%%%v%v%v%v%v%vnnm@,
`    `@mnnvv%v%v%v%%;;@mvvvvv%%;;*;;%%vvvmmmm@;;%m;%%v%v%v%vmm@'   '
        `@mmnnvvvvv%%;;@@mvvvv%%%%%%%vvvvmm@@;;%%mm@;%%nnnnm@'
           `@mmmmmmvv%%;;@@mvvvvvvvvvvmmm@@;;%%mmnmm@;%mmm@'
              `mm@@@@@mm%;;@m@@m@m@m@@m@@;;%%vvvvvnmm@;@'
             ,@m%v%v%v%v%v;%;%;%;%;%;%;%;%vv%vvvvvnnmm@
           .@mmnnvvvvvvv%vvvvnnmm%mmnnvvvvvvv%vvvvnnmm@
          .@mmnnvvvvvv%vvvvvvnnmm'`@mmnnvvvvvv%vvvnnmm@
          @mmnnvvvvv%vvvvvvnnmm@':%::`@mmnnvvvv%vvvnm@'
          @mmnnvvv%vvvvvnnmm@'`:::%%:::'`@mmnnvv%vvmm@
          `@mnvvv%vvnnmm@'                  `@mvv%vm@'
           `@mnv%vnnm@'                        `@n%n@
            `@m%mm@'                            `@m@
             @m@'                                 `@
             `@'                                    '
              `
'''


quad_one: str = r'''
           
             v%v;%;%;%;%;%;%;%%%vv
             m%;;@@m@m@@m@@m@mm;;%%
          .,@mmmmmmvv%%;;@@vmvvvvvvvvv
       .,@mm;@@vvvvv%%%%%%%vvvvmm@@;;%
    .,@mnnv;@mmvvvv%%;*;*;%%vvvvmmm@;;%
,@mnnvv%v%v;@@vvvv%%;*;*;*;%%vvvvm@@;;
`    `@mnn;;@mvvvvv%%;;*;;%%vvvmmmm@;;
        `%;;@@mvvvv%%%%%%%vvvvmm@@;;%
           `mmmvv%%;;@@mvvvvvvvvvvmmm@
              `mm@m@m@m@@m@@;;%%'
'''

quad_two: str = r'''
|----------||----------|
|##########||##########|
|##########||##########|
|##########||##########|
|##########||##########|
|----------||----------|
'''

quad_three: str = r'''
|----------||----------|
|##########||##########|
|##########||##########|
|##########||##########|
|##########||##########|
|----------||----------|
|##########|
|##########|
|##########|
|##########|
|----------|
'''
quad_four: str = r'''
|----------||----------|
|##########||##########|
|##########||##########|
|##########||##########|
|##########||##########|
|----------||----------|
|##########||##########|
|##########||##########|
|##########||##########|
|##########||##########|
|----------||----------|
'''

def loader(time_delay=1) -> None:
    os.system('clear')
    progress: list[str] = [quad_one, quad_two, quad_three, quad_four]
    for p in progress:
        print(p.center(40))
        time.sleep(time_delay)
        os.system('clear')

# Test the loader
if __name__ == '__main__':
    loader()