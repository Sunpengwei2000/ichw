1.解释作业、进程、线程的概念，进程和线程概念的提出分别解决了什么问题？    
作业：用户向系统提交的一项工作的基本单位，是用户在一次事务处理或计算过程中要求计算机所作的工作的和。    
  进程：进程是正在运行的程序的实例，程序执行的每一个新状态都可以称作一个进程，是资源分配和调度的单位，是操作系统描述计算机并发活动的一种模型。    
  线程：程序中一个单一的顺序控制流程，程序执行流的最小单元，一个可独立调度和指派的执行单元。    
·进程的引入有利于在一个系统中运行多个程序。为了提高CPU的利用率，多批道处理系统一次性载入多个作业到内存中让程序并发执行，与此同时出现了许多问题：①间断性，执行A时，B因为其他原因没有执行完毕，则A对应的那个程序也无法继续执行，必须等待B执行完毕。②不封闭性，对于并发执行的程序，系统中的资源是共享的，资源状态也由这些程序来改变，致使其中一个程序运行时，环境必然受到其他程序影响。引入进程后，以上问题均得到了很好的解决。    
·曾经在操作系统中能拥有资源和独立运行的基本单位是进程，然而随着计算机技术的发展，进程不在能够满足人们的需要：一方面进程是资源拥有着，创建、撤销与切换存在较大的时间与空间上的开销，因此需要引入轻型进程；另一方面，对称多处理机的出现，可以满足多个运行单位同时进行，而多个进程并行多样开销过大。
    
2.调研虚拟存储器的概念，描述其工作原理和作用。    
虚拟存储器又称为虚拟内存。计算机中的程序均需经由内存执行，若执行程序所占用的内存很多，导致随机存储器不足时，系统将会将一部分硬盘空间充当内存使用。虚拟存储器在硬盘上的存在形式就是PageFile.Sys这个文件。其工作原理如下：CPU需要从主存中存取数据，其访问主存的逻辑地址分为逻辑组号a和组内地址b，需要查地址变换表，如果该信息在主存内，则从地址变换表中读出与逻辑组号a对应的物理组号a，配合组内地址b得到数据的物理地址，在主存中存取即可。而如果并没有在主存中找到该数据，则需要将该数据从虚拟存储器中调入主存，若主存中有空闲区，则可直接数据调入；若主存中没有空闲区，则需要按照算法将一些数据组调出至虚拟存储器，再将数据调入。调入数据后，将地址变换表中的物理组号和逻辑组号更新。之后CPU便可从主存中存取数据了。虚拟存储器可以简化共享：利用虚拟地址来映射物理地址，使得可以让多个进程的不同虚拟地址映射同一块物理地址。虚拟存储器还可以作为存储器的保护工具。再虚拟存储器里面可以设计PTE时可读，可写，还是可执行的。如果出现只读的PTE被写入的情况，CPU便会通知出现段错误，但并不会影响实际存放数据的物理内存。
