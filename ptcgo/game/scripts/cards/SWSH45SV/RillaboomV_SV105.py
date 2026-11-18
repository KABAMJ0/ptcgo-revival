from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="79fad5f4-8a5a-5cb1-b8c4-784612ef9e18",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomV.Name",
    display_name="Rillaboom V",
    searchable_by=["Rillaboom V", "Basic", "V", "RillaboomV"],
    subtypes=["Basic", "V"],
    collector_number=105,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=812,
    abilities=[
        Attack(
            title="Forest Feast",
            game_text="Search your deck for up to 2 Basic Grass Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Wood Hammer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=recoil_attack(30),
        ),
    ],
)