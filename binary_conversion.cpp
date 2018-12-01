unsigned int mac(byte *a1, DWORD *a2, int a3)
{
	byte *i;
	byte *v8;
	DWORD *v3;
	int v4;
	int v6; 
	long v7;
	int v9;
	int v14; // r1
	unsigned __int8 v11;
	unsigned int v12;
	unsigned int v13;	
	unsigned int v15; // r2
	unsigned int result;
	bool v16;
	unsigned int unknown(unsigned int result1, unsigned int a21);

	v3 = a2;
	v4 = a3;
	for (i = a1; ; ++i)
	{
		v6 = (unsigned __int8)*i;    // 获取i的字母，i开始为首字母
		v7 =(2 * v6)& 0x20; //& 0x20);
		if (!v7)                                  // v7=0 break，当为字母时v7=0，为数字是v7！=0
			break;
	}

	if (v6 != 43)                               // v6 ！= ‘+’
	{
		if (v6 != 45)                             // v6 ！= ‘-’
			goto LABEL_8;
		v7 = 1;
	}
	++i;
LABEL_8:
	if (a3 & 0xFFFFFFEF)                        // a3=16 a3 & 0xFFFFFFEF = 0,为假
	{
		v8 = a1;                                    // v8 = a1
	}
	else
	{
		v4 = a3 + 10;
		if (*i == 48)                             // i==0
		{
			v9 = (unsigned __int8)(i++)[1];           // 获取后面一个字母，然后再加一位
			v4 = a3 + 8;                              // v4 = 24
			v8 = i;                                   // v8 = i的后一位
			if ((v9 | 0x20) == 120)                 // ？？？为什么会出现x v9='x'
			{
				v4 *= 2;                                // v4 = 48
				++i;
			}
		}
		else                                        // i != 0 
		{
			v8 = a1;
		}
		if (v4 >= 16)                             // v4无论如何都>=16,故v4 = 16
			v4 = 16;
	}
	if ((unsigned int)(v4 - 2) <= 0x22)
	{
		/*此处有一部忽略，无法判断sub_4581E0(0xFFFFFFFF, v4);*/
		v12 = 0;//v11未赋值
		
		v13 = 0;//unknown(0xFFFFFFFF, v4);//不知道v13为多少,如果不为0则result只能等于0
		result = 0;
		while (1)
		{
			v14 = (unsigned __int8)*i;                // 0 的ascii为48
			v15 = (unsigned __int8)(v14 - 48);
			if (v15 > 9)                            // 是字母
			{
				v15 = (v14 | 0x20u) <= 0x60 ? 40 : (v14 | 0x20) - 87;// | 0x20 = ascii 并且把大写转为小写 ‘a’=>97-87 =10 以此类推
				if ((v14 | 0x20u) > 0x60)             //  0x60 = 96 v14>='a'
					v15 = (unsigned __int8)v15;           // 到‘a'的差+10
			}
			if ((signed int)v15 >= v4)  // v4 = 16，如果i是数字则不进入if，如果i是字母<g也不进入if，i>=g进入循环if
				break;                                  // 正常情况下，不会break
			++i;
			if (result > v13)                       // 不知道v13是啥，v13非负数
				goto LABEL_38;
			v16 = v15 > v12;
			if (result != v13)                      // result ！= v13的时候 v16 =0 导致跳出循环
				v16 = 0;
			if (v16)
		LABEL_38:
			/*此处有一部忽略，无法判断sub_81C0(result);*/
			result = v15 + v4 * result;
			v8 = i;
		}
	}
	else
	{
		result = 0;
	}
	if (v3)
		*v3 = (unsigned long)v8;
	if (v7)
		result = result;
	return result;
}
