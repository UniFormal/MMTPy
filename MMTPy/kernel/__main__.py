
from ipykernel.kernelapp import IPKernelApp
from .kernel import MMTKernel
IPKernelApp.launch_instance(kernel_class=MMTKernel)
