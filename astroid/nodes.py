# copyright 2003-2013 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of astroid.
#
# astroid is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 2.1 of the License, or (at your
# option) any later version.
#
# astroid is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with astroid. If not, see <http://www.gnu.org/licenses/>.
"""
on all nodes :
 .is_statement, returning true if the node should be considered as a
  statement node
 .root(), returning the root node of the tree (i.e. a Module)
 .previous_sibling(), returning previous sibling statement node
 .next_sibling(), returning next sibling statement node
 .statement(), returning the first parent node marked as statement node
 .frame(), returning the first node defining a new local scope (i.e.
  Module, FunctionDef or ClassDef)
 .set_local(name, node), define an identifier <name> on the first parent frame,
  with the node defining it. This is used by the astroid builder and should not
  be used from out there.

on ImportFrom and Import :
 .real_name(name),


"""
# pylint: disable=unused-import,redefined-builtin

from astroid.tree.node_classes import (
    Arguments, AssignAttr, Assert, Assign,
    AssignName, AugAssign, Repr, BinOp, BoolOp, Break, Call, Compare,
    Comprehension, Const, Continue, Decorators, DelAttr, DelName, Delete,
    Dict, Empty, Expr, Ellipsis, ExceptHandler, Exec, ExtSlice, For,
    ImportFrom, Attribute, Global, If, IfExp, Import, Index, Keyword,
    List, Name, NameConstant, Nonlocal, Pass, Param, Print, Raise, Return, Set, Slice,
    Starred, Subscript, TryExcept, TryFinally, Tuple, UnaryOp, While, With,
    WithItem, Yield, YieldFrom, AsyncFor, Await, AsyncWith,
    # Node not present in the builtin ast module.
    DictUnpack,
    # Special nodes for building from live objects.
    InterpreterObject, ReservedName, Unknown
)
from astroid.tree.scoped_nodes import (
    Module, GeneratorExp, Lambda, DictComp,
    ListComp, SetComp, FunctionDef, ClassDef,
    AsyncFunctionDef,
)



ALL_NODE_CLASSES = (
    AsyncFunctionDef, AsyncFor, AsyncWith, Await,

    Arguments, AssignAttr, Assert, Assign, AssignName, AugAssign,
    Repr, BinOp, BoolOp, Break,
    Call, ClassDef, Compare, Comprehension, Const, Continue,
    Decorators, DelAttr, DelName, Delete,
    Dict, DictComp, DictUnpack, Expr,
    Ellipsis, Empty, ExceptHandler, Exec, ExtSlice,
    For, ImportFrom, FunctionDef,
    Attribute, GeneratorExp, Global,
    If, IfExp, Import, Index, InterpreterObject,
    Keyword,
    Lambda, List, ListComp,
    Name, NameConstant, Nonlocal,
    Module,
    Param, Pass, Print,
    Raise, ReservedName, Return,
    Set, SetComp, Slice, Starred, Subscript,
    TryExcept, TryFinally, Tuple,
    UnaryOp, Unknown,
    While, With, WithItem,
    Yield, YieldFrom,
    )
