#pragma once

#ifdef DLL_MACRO
#define DLL_INEX dllexport
#else
#define DLL_INEX dllimport
#endif


extern "C" __declspec(DLL_INEX) unsigned long sum_square(unsigned int n);