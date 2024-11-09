import hashlib
from supabase import create_client, Client

#supabase data connection: url, api key

SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh4amlrYmh2dGhxZmlwdWFjbXhiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxNjY2MjEsImV4cCI6MjA0NTc0MjYyMX0.mOZBSgGzTDBSuWSo26sEIpIdQDhfU1RlFRT_B7-8q1A"
SUPABASE_URL="https://hxjikbhvthqfipuacmxb.supabase.co"

#Connect to SupaBase Client
supabase: Client = create_client(SUPABASE_URL,SUPABASE_KEY)

#get and save data function
def save_data(e, p):
    # Insert Into  users model
    enc_pass=hashlib.sha256(p.encode()).hexdigest()

    response=supabase.table('users').insert({"email":e, "password":enc_pass}).execute()
    
    
    if response.data:
        print(f"User has been have succesfully {response.data}")
    elif response.error:
        print(f" error saving user{response.error}")

#Main
email=input("User email: ")
passwd=input("User password: ")
save_data(email,passwd)