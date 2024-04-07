import { useFormik } from 'formik';
import React from 'react';
import * as Yup from 'yup';

const CalculateForm = () => {
  const formSchema = Yup.object().shape({
    number: Yup.number().min(0, 'يجب ان تكون القيمة اعلى من الصفر'),
  });

  const formik = useFormik({
    initialValues: {
      number: '',
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      console.log(values);
    },
  });

  const Result = () => (
    <div className='w-full'>
      <h1 dir='rtl' className='text-xl text-green-300'>
        النتيجة
      </h1>
      <div className='bg-gray-200 text-slate-900 color-slate-900 py-2 rounded-md h-full'>
        <p dir='rtl' className='text-xl '>
          {/* display the value rended from the backend dinar_number_to_arabic_words */}
          {formik.values.number}
        </p>
      </div>
    </div>
  );

  return (
    <section className='bg-opacity-60 lg:w-4/5 w-4/5 bg-black p-8 rounded-xl '>
      <h1 dir='rtl' className='text-3xl text-white'>
      تحويل الأعداد العربية إلى ما يقابلها كتابة
      </h1>
      <div className='flex  justify-center gap-10 flex-row'>
        <div className='flex flex-col gap-10 w-full '>
          <form className='flex flex-col gap-2' onSubmit={formik.handleSubmit}>
            <label dir='rtl' htmlFor='number' className='text-xl '>
              القيمة بالارقام
            </label>
            <input
              dir='rtl'
              name='number'
              type='number'
              className='bg-gray-200 text-slate-900 color-slate-900 px-4 py-2 rounded-md outline-none'
              placeholder='أدخل الرقم'
              onChange={formik.handleChange}
              value={formik.values.number}
              onBlur={formik.handleBlur}
            />
            {formik.errors.number && (
              <p dir='rtl' className='text-red-500 text-sm'>
                {formik.errors.number}
              </p>
            )}
          </form>
          <button dir='rtl' className='bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-400 transition-colors'>
            تحويل
          </button>
        </div>
        <Result />
      </div>
    </section>
  );
};

export default CalculateForm;
