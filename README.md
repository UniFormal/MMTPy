# Install

```
python setup.py install
```
Note: If you want to use it with Sage, use
```
sage -python setup.py install
```
instead.

## Installing the Jupyter Kernel
```
python -m MMTPy.kernel.install
```
## Installing the Jupyter Kernel in Sage
```
sage -python -c 'from MMTPy.kernel.install import main; main()'
```

## License
```
MMTPy is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

MMTPy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with MMTPy. If not, see http://www.gnu.org/licenses/.
```