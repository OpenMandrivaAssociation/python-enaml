%define module	enaml

Summary:	ETS declarative language for building dynamic user interfaces

Name:		python-%{module}
Version:	0.9.1
Release:	1
Source0:	http://pypi.python.org/packages/source/e/enaml/enaml-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/enaml/
Requires:	python-traits >= 4.2.0
Requires:	python-casuarius
Requires:	pyside, wxPython
Requires:	python-ply
BuildRequires:	python-cython
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-sphinx
BuildArch: noarch

%description
Enaml is a framework for writing declarative user interfaces in
Python. It provides a Yaml-ish/Pythonic syntax language for declaring
a ui that binds and reacts to changes in the user's models. Code can
freely call back and forth between Python and Enaml.

Enaml is heavily inspired by Qt's QML system, but Enaml uses native
widgets (as opposed to drawing on a 2D canvas) and is toolkit
independent. Currently supported/in-development toolkits include Wx
and Qt4 via PySide.

Enaml is extensible and makes it extremely easy for the user to define
their own widgets, override existing widgets, create a new backend
toolkit, or even hook the runtime to apply their own expression
dependency behavior. Indeed, about the only thing not hookable is the
Enaml langauge syntax itself.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
%__python setup.py build_docs

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%doc *.txt *.rst licenses/ examples/ build/docs/html
%{_bindir}/enaml-run
%{py_puresitedir}/%{module}*
%{_libdir}/debug/.build-id/07/8a81ccacdd15713d102031ccee32c6b91fdb35
%{_libdir}/debug/.build-id/07/8a81ccacdd15713d102031ccee32c6b91fdb35.debug
%{_libdir}/debug/.build-id/44/1169d3d495a80a43ac7ac2707d7368b0c50dbe
%{_libdir}/debug/.build-id/44/1169d3d495a80a43ac7ac2707d7368b0c50dbe.debug
%{_libdir}/debug/.build-id/45/855bdb6828c6b5e9838d518b887113198f46ab
%{_libdir}/debug/.build-id/45/855bdb6828c6b5e9838d518b887113198f46ab.debug
%{_libdir}/debug/.build-id/57/0602ca669eea0826b125b66a07a00023ec7b74
%{_libdir}/debug/.build-id/57/0602ca669eea0826b125b66a07a00023ec7b74.debug
%{_libdir}/debug/.build-id/a4/d43f7fe44bf81358edda56bff3412126594083
%{_libdir}/debug/.build-id/a4/d43f7fe44bf81358edda56bff3412126594083.debug
%{_libdir}/debug/.build-id/c6/b98ed79cfc82089c9e1c219c7050c2d844f057
%{_libdir}/debug/.build-id/c6/b98ed79cfc82089c9e1c219c7050c2d844f057.debug
%{_libdir}/debug/.build-id/f8/e2b7ae2d0ab9c80f2043d06bd672f5e9026c42
%{_libdir}/debug/.build-id/f8/e2b7ae2d0ab9c80f2043d06bd672f5e9026c42.debug
%{_libdir}/debug/.build-id/f9/42275b87c818c48f6792cdf26c37d60b267dc2
%{_libdir}/debug/.build-id/f9/42275b87c818c48f6792cdf26c37d60b267dc2.debug
%{_libdir}/debug%{py_puresitedir}/enaml/callableref.so.debug
%{_libdir}/debug%{py_puresitedir}/enaml/colorext.so.debug
%{_libdir}/debug%{py_puresitedir}/enaml/core/alias.so.debug
%{_libdir}/debug%{py_puresitedir}/enaml/core/dynamicscope.so.debug
%{_libdir}/debug%{py_puresitedir}/enaml/core/funchelper.so.debug
%{_libdir}/debug%{py_puresitedir}/enaml/fontext.so.debug
%{_libdir}/debug%{py_puresitedir}/enaml/signaling.so.debug
%{_libdir}/debug%{py_puresitedir}/enaml/weakmethod.so.debug
/usr/src/debug/enaml-0.9.1/enaml/src/alias.cpp
/usr/src/debug/enaml-0.9.1/enaml/src/callableref.cpp
/usr/src/debug/enaml-0.9.1/enaml/src/colorext.cpp
/usr/src/debug/enaml-0.9.1/enaml/src/dynamicscope.cpp
/usr/src/debug/enaml-0.9.1/enaml/src/fontext.cpp
/usr/src/debug/enaml-0.9.1/enaml/src/funchelper.cpp
/usr/src/debug/enaml-0.9.1/enaml/src/pythonhelpers.h
/usr/src/debug/enaml-0.9.1/enaml/src/pythonhelpersex.h
/usr/src/debug/enaml-0.9.1/enaml/src/signaling.cpp
/usr/src/debug/enaml-0.9.1/enaml/src/weakmethod.cpp



