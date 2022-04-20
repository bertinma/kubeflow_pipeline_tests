import kfp
from kfp import dsl 

@dsl.pipeline(name='First Pipeline')
def first_pipeline(input, sum):
    step1 = kfp.components.load_component_from_file('step1/component.yaml')
    step2 = kfp.components.load_component_from_file('step2/component.yaml')

    step1_task = step1(input, sum)
    step2(step1_task.output)


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(first_pipeline, "first_pipeline.yaml")