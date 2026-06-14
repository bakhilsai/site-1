f = open(r'C:\Users\akhil\.gemini\antigravity\scratch\portfolio_final\index.html', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

# Keep lines 1..996 and 1247..end (1-indexed → 0-indexed: 0..995 and 1246..end)
clean = lines[:996] + lines[1246:]

f = open(r'C:\Users\akhil\.gemini\antigravity\scratch\portfolio_final\index.html', 'w', encoding='utf-8')
f.writelines(clean)
f.close()
print(f"Done. File now has {len(clean)} lines.")
