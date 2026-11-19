from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import heal_dealt_attack

card = PokemonCardDef(
    guid="c00cece1-4af6-5c09-ac9f-e778a0c9feba",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name",
    display_name="Gardevoir-EX",
    searchable_by=["Gardevoir-EX", "Basic", "EX", "GardevoirEX"],
    subtypes=["Basic", "EX"],
    collector_number=10030,
    set_code="TwentiethAnn",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=282,
    abilities=[
        Attack(
            title="Life Leap",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            effect=heal_dealt_attack(),
        ),
        Attack(
            title="Shining Wind",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no Weakness.",
            cost={PokemonTypes.FAIRY: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)