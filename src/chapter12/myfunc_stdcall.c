/* myfunc_stdcall.c */
#define EXPORT __declspec(dllexport) __stdcall

EXPORT int myadd(int x, int y) {
	return x + y;
}
