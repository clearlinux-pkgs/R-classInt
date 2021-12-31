#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-classInt
Version  : 0.4.3
Release  : 48
URL      : https://cran.r-project.org/src/contrib/classInt_0.4-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/classInt_0.4-3.tar.gz
Summary  : Choose Univariate Class Intervals
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-classInt-lib = %{version}-%{release}
Requires: R-e1071
BuildRequires : R-e1071
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-classInt package.
Group: Libraries

%description lib
lib components for the R-classInt package.


%prep
%setup -q -c -n classInt
cd %{_builddir}/classInt

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640988802

%install
export SOURCE_DATE_EPOCH=1640988802
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library classInt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library classInt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library classInt
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc classInt || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/classInt/ChangeLog
/usr/lib64/R/library/classInt/DESCRIPTION
/usr/lib64/R/library/classInt/INDEX
/usr/lib64/R/library/classInt/Meta/Rd.rds
/usr/lib64/R/library/classInt/Meta/features.rds
/usr/lib64/R/library/classInt/Meta/hsearch.rds
/usr/lib64/R/library/classInt/Meta/links.rds
/usr/lib64/R/library/classInt/Meta/nsInfo.rds
/usr/lib64/R/library/classInt/Meta/package.rds
/usr/lib64/R/library/classInt/Meta/vignette.rds
/usr/lib64/R/library/classInt/NAMESPACE
/usr/lib64/R/library/classInt/R/classInt
/usr/lib64/R/library/classInt/R/classInt.rdb
/usr/lib64/R/library/classInt/R/classInt.rdx
/usr/lib64/R/library/classInt/doc/headtailsR.R
/usr/lib64/R/library/classInt/doc/headtailsR.Rmd
/usr/lib64/R/library/classInt/doc/headtailsR.html
/usr/lib64/R/library/classInt/doc/index.html
/usr/lib64/R/library/classInt/help/AnIndex
/usr/lib64/R/library/classInt/help/aliases.rds
/usr/lib64/R/library/classInt/help/classInt.rdb
/usr/lib64/R/library/classInt/help/classInt.rdx
/usr/lib64/R/library/classInt/help/paths.rds
/usr/lib64/R/library/classInt/html/00Index.html
/usr/lib64/R/library/classInt/html/R.css
/usr/lib64/R/library/classInt/tests/test_Unique.R
/usr/lib64/R/library/classInt/tests/test_Unique.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/classInt/libs/classInt.so
/usr/lib64/R/library/classInt/libs/classInt.so.avx2
/usr/lib64/R/library/classInt/libs/classInt.so.avx512
