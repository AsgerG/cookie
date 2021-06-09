import sys
sys.path.insert(0,'C:/Users/Bruger/Desktop/DTU/MLOps/Thomas/mlops/cookiecutter_project/src/data/')

from make_dataset import load_mnist
#from cookiecutter_project.src.data.make_dataset import load_mnist



def test_mytest():
    trainset, testset = load_mnist() 
    assert len(trainset) == 60000 
    assert len(testset) == 10000
    #assert that each datapoint has shape [1,28,28] or [728] depending on how you choose to format
    #assert that all labels are represented
