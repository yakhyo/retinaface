# Copyright 2024 Yakhyokhuja Valikhujaev
#
# Licensed under the MIT License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from .retinaface import RetinaFace
from .log import Logger
from .version import __version__, __author__

__all__ = [
    "__version__",
    "__author__"
    "RetinaFace",
    "Logger"
]
