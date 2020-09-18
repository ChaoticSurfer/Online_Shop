# import json
# from .models import *
# from itertools import chain
# from authentication.models import *
#
#
# def cookieCart(request):
# 	#Create empty cart for now for non-logged in user
#
# 	try:
# 		cart = json.loads(request.COOKIES['cart'])
# 		# cart.clear['cart']
# 	except:
# 		cart = {}
# 		print('CART:', cart)
#
# 	items = []
# 	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
# 	cartItems = order['get_cart_items']
#
# 	for i in cart:
# 		#We use try block to prevent items in cart that may have been removed from causing error
# 		try:
# 			product = Product.objects.get(id=i)
# 			cartItems += cart[i]['quantity']
# 			# product = paints1 | paints2 | paints3 | paints4 | paints5 | pastels1 | pastels2 | pastels3 | pastels4 | pencils | accessories1 | accessories2 | accessories3 | accessories4 | canvas_rectangle_frame | canvas_circular_frame | canvas_with_rectangle_frame | canvas_with_circular_frame | drawing_canvas | tree_drawing_board | water_color_sheet | canvas_with_carton
# 			# product = Product.objects.get(id=i)
# 			# paints1 = Paint_Oil_Color_Product.objects.get(id=i)
# 			# paints2 = Paint_Acrylic_Color_Product.objects.get(id=i)
# 			# paints3 = Paint_Gouache_Color_Product.objects.get(id=i)
# 			# paints4 = Paint_Water_Color_Product.objects.get(id=i)
# 			# paints5 = Paint_Other_Color_Product.objects.get(id=i)
# 			# pastels1 = Pastel_Oil_Color_Product.objects.get(id=i)
# 			# pastels2 = Pastel_Soft_Color_Product.objects.get(id=i)
# 			# pastels3 = Pastel_Water_Color_Product.objects.get(id=i)
# 			# pastels4 = Pastel_Dry_Color_Product.objects.get(id=i)
# 			# pencils = Pencil.objects.get(id=i)
# 			# accessories1 = Accessories_Molbert.objects.get(id=i)
# 			# accessories2 = Accessories_Auxiliary_Fluids.objects.get(id=i)
# 			# accessories3 = Accessories_Palette.objects.get(id=i)
# 			# accessories4 = Accessories_Mastehin.objects.get(id=i)
# 			# # drawing_boards = Drawing_boards.objects.all()
# 			# canvas_rectangle_frame = Canvas_rectangle_frame.objects.get(id=i)
# 			# canvas_circular_frame = Canvas_circular_frame.objects.get(id=i)
# 			# canvas_with_rectangle_frame = Canvas_with_rectangle_frame.objects.get(id=i)
# 			# canvas_with_circular_frame = Canvas_with_circular_frame.objects.get(id=i)
# 			# tree_drawing_board = Tree_drawing_board.objects.get(id=i)
# 			# water_color_sheet = Water_color_sheet.objects.get(id=i)
# 			# canvas_with_carton = Canvas_with_carton.objects.get(id=i)
# 			# product_list = list(
# 			# 	chain(paints1, paints2, paints3, paints4, paints5, pastels1, pastels2, pastels3, pastels4, pencils,
# 			# 		  accessories1,
# 			# 		  accessories2, accessories3, accessories4, canvas_rectangle_frame, canvas_circular_frame,
# 			# 		  canvas_with_rectangle_frame,
# 			# 		  canvas_with_circular_frame, drawing_canvas, tree_drawing_board, water_color_sheet,
# 			# 		  canvas_with_carton))
# 			# for product in product_list:
#
# 			total = (product.price * cart[i]['quantity'])
#
# 			order['get_cart_total'] += total
# 			order['get_cart_items'] += cart[i]['quantity']
#
# 			item = {
# 				'id':product.id,
# 				'product':{'id':product.id,'name_geo':product.product_name_geo, 'name_eng':product.product_name_eng, 'name_rus':product.product_name_rus, 'product_id':product.product_id, 'price':product.price,
# 				'image':product.imageURL}, 'quantity':cart[i]['quantity'],
# 				'get_total':total,
# 				# 'digital': product.digital,
# 				}
# 			items.append(item)
#
# 			# if product.digital == False:
# 			# 	order['shipping'] = True
# 		except:
# 			pass
#
# 	return {'cartItems':cartItems ,'order':order, 'items':items}
#
# def cartData(request):
# 	if request.user.is_authenticated:
# 		customer = request.user.email
# 		order, created = Order.objects.get_or_create(customer=customer, complete=False)
# 		items = order.orderitem_set.all()
# 		cartItems = order.get_cart_items
# 	else:
# 		cookieData = cookieCart(request)
# 		cartItems = cookieData['cartItems']
# 		order = cookieData['order']
# 		items = cookieData['items']
#
# 	return {'cartItems':cartItems ,'order':order, 'items':items}
#
#
# # def guestOrder(request, data):
# # 	name = data['form']['name']
# # 	email = data['form']['email']
# #
# # 	cookieData = cookieCart(request)
# # 	items = cookieData['items']
# #
# # 	customer, created = Customer.objects.get_or_create(
# # 			email=email,
# # 			)
# # 	customer.name = name
# # 	customer.save()
# #
# # 	order = Order.objects.create(
# # 		customer=customer,
# # 		complete=False,
# # 		)
# #
# # 	for item in items:
# # 		product = Product.objects.get(id=item['id'])
# # 		orderItem = OrderItem.objects.create(
# # 			product=product,
# # 			order=order,
# # 			quantity=item['quantity'],
# # 		)
# # 	return customer, order
# #
