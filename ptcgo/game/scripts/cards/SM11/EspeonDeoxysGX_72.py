from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16c40fac-a578-5dfb-b04e-8a987097dddc",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EspeonDeoxysGX.Name",
    display_name="Espeon & Deoxys-GX",
    searchable_by=["Espeon & Deoxys-GX", "Basic", "TAG TEAM", "GX", "EspeonDeoxysGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=72,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=196,
    abilities=[
        Attack(
            title="Psychic Club",
            game_text="This attack does 30 more damage for each of your Benched Psychic Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Cross Division-GX",
            game_text="Put 10 damage counters on your opponent's Pok\u00e9mon in any way you like. If this Pok\u00e9mon has at least 3 extra Energy attached to it (in addition to this attack's cost), put 20 damage counters on them instead. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)