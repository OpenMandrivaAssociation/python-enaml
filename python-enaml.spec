%define module	enaml

%define debug_package %{nil}

Summary:	ETS declarative language for building dynamic user interfaces
Name:		python-%{module}
Version:	0.6.8
Release:	1
Source0:	http://pypi.python.org/packages/source/e/%{module}/%{module}-%{version}.tar.gz
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
%_bindir/enaml-run
%py_platsitedir/%{module}*


%changelog
* Tue Aug 14 2012 Lev Givon <lev@mandriva.org> 0.2.0-1
+ Revision: 814738
- imported package python-enaml

