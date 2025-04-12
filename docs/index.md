# Welcome to CODERTOOLS

![](<work.png>)

## 本工具的主要目标是让大模型可以丝滑的使用和理解第三方的工具包
这是一个偏项目级别的工具包了
我们大致的思路是: 大模型可以达到理解并使用第三方包的程度
而我们开发的私有包则通过标准化和规范化,进而使大模型理解

在大模型可以完美使用一个三方包时, 可以开始拓展到多个包的配合使用
框架级别的包的使用等.为最终的调度赋能.


```python
!pip install codertools


import codertools

from codertools.packager import process_github_repo,process_github_issues

process_github_repo('./test2_md2','pydantic/pydantic')

```