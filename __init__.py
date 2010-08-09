class ArkUtils
  XDIGITS = %w( 0 1 2 3 4 5 6 7 8 9 b c d f g h j k m n p q r s t v w x z )
  DIGITS = XDIGITS[0..9]

  class << self
    def mint( options={ :authority => nil, :template => 'dddddddd' } )
      # mint a unique ARK within the given authority
      # random template: eeddeeddk
      #   e is an xdigit: 0123456789bcdfghjkmnpqrstvwxz
      #   d is a digit:   0123456789
      #   k is checkchar: special xdigit
 
      # first generate a name based on given template
      name = generate_name( options[:template] )

      # then prepend authority.number and the '/' character e.g., "11111/id"
      ark = options[:authority].number.to_s + '/' + name 

      # then generate a check character, if specified in template
      name << generate_check( ark ) if options[:template][-1].chr == 'k'

      # return identifier w/ check char to caller
      name
    end

    def generate_name( template )
      name = ''
      template.split( '' ).each do |char|
        next unless ['d', 'e'].include? char
        digit_array = (char == 'e') ? XDIGITS : DIGITS
        name << digit_array[rand(digit_array.length)]
      end
      name
    end

    def generate_check( ark )
      sum = position = 0
      ark.split( '' ).each do |char|
        ordinal = XDIGITS.index( char ) || 0
        position += 1
        sum += ordinal * position
      end
      XDIGITS[sum % XDIGITS.length]
    end

    def validate( ark )
      generate_check( ark[0...-1] ) == ark[-1].chr 
    end

    private :generate_check, :generate_name
  end
end 
