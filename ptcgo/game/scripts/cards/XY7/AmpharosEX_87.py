from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="2988501b-19c3-5491-a1bc-4dc6ecef3aa7",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AmpharosEX.Name",
    display_name="Ampharos-EX",
    searchable_by=["Ampharos-EX", "Basic", "EX", "AmpharosEX"],
    subtypes=["Basic", "EX"],
    collector_number=87,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=181,
    abilities=[
        Attack(
            title="Thunder Rod",
            game_text="Look at the top 4 cards of your deck and attach as many Lightning Energy cards you find there as you like to this Pok\u00e9mon. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Sparkling Tail",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)