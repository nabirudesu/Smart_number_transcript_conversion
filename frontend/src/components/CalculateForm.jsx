import { useFormik } from 'formik';
import { useState,useEffect } from 'react';
import React from 'react';
import * as Yup from 'yup';

const CalculateForm = () => {
  const [currency, setCurrency] = useState("Dinar")
  const [dinarWords, setDinarWords] = useState('')
  const formSchema = Yup.object().shape({
    number: Yup.number().when('currency',{
      is : (value)=> value ==='Dinar',
      then: (schema) => schema.min(0, 'يجب ان تكون القيمة اعلى من الصفر').max(9999999,"المبلغ تعدى المسموح به").required("*"), 
      otherwise: (schema) => schema.min(100, 'يجب ان تكون القيمة اعلى من المئة سنتيم').max(999999999,"المبلغ تعدى المسموح به").required("*")}),
    currency: Yup.string()
    });
  const formik = useFormik({
    initialValues: {
      number: undefined,
      currency :"Dinar"
    },
    validationSchema: formSchema,
    onSubmit: async (values) => {
      let NumberSubmitted = 0
      let currencySubmitted= ""
      // here we return the dinarTextValue
      NumberSubmitted= values.number
      currencySubmitted = values.currency
      const response =  await fetch('http://127.0.0.1:5000/number_to_words',{
      method: 'POST',
      mode:'cors',
      body: JSON.stringify({
        'number': NumberSubmitted,
        'currency': currencySubmitted,
      }),
      headers:{'content-type':'application/json; charset=UTF-8'},
      }).then((response) => response.json()).then((data) => data.transcription)
      setDinarWords(response)
      console.log(response)
    }
  });

  const Result = () => (
    <div className='w-full'>
      <h1 dir='rtl' className='text-xl text-green-300'>
        النتيجة
      </h1>
      <div className='bg-gray-200 text-slate-900 color-slate-900 py-2 rounded-md h-full'>
        <p dir='rtl' className='text-xl'>
          {/* display the value rended from the backend dinar_number_to_arabic_words */}
          {dinarWords}
        </p>
      </div>
    </div>
  );
  return (
    <section className='bg-opacity-60 lg:w-4/5 w-4/5 bg-black p-8 rounded-xl '>
      <h1 dir='rtl' className='text-3xl text-white'>
      تحويل الأعداد العربية إلى ما يقابلها كتابة
      </h1>
      <div className='flex justify-center gap-10 flex-col'>
        <div className='flex flex-col gap-10 w-full '>
          <form className='flex flex-row-reverse gap-2' onSubmit={formik.handleSubmit}>
            <div className='flex flex-col gap-2'>
              <label dir='rtl' htmlFor='number' className='text-l '>
                القيمة بالارقام
              </label>
              <input
                dir='rtl'
                id='number'
                type='number'
                className='bg-gray-200 text-slate-900 color-slate-900 px-4 py-2 rounded-md outline-none'
                placeholder='أدخل الرقم'
                onChange={formik.handleChange}
                value={formik.values.number}
                onBlur={formik.handleBlur}
                />
            </div>
            <div className='flex flex-col gap-2'>
              <label dir='rtl' htmlFor='number' className='text-l '>
                العملة المستعملة
              </label>
              <select 
                dir='rtl'
                id='Currency'
                name = 'currency'
                type='number'
                className='bg-gray-200 text-slate-900 color-slate-900 px-4 py-2 rounded-md outline-none'
                value={formik.values.currency}
                onChange={formik.handleChange}
                >
                <option value="Dinar">الدينار الجزائري</option>
                <option value="Centime">السنتيم</option>
              </select>
            </div>
              {formik.errors.number && (
                <p dir='rtl' className='text-red-500 text-sm'>
                  {formik.errors.number}
                </p>
              )}
            <button dir='rtl' type="submit" className='bg-blue-500 text-white px-2 py-1 rounded-md hover:bg-blue-400 transition-colors'>
              تحويل
            </button>
          </form>
        </div>
        <Result />
      </div>
    </section>
  );
};

export default CalculateForm;
