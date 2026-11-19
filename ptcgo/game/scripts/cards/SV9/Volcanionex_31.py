from ptcgo.game.card_effects.attacks_common import energy_move_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc5d25ea-f20d-51b2-9980-958c953acb5b",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanionex.Name",
    display_name="Volcanion ex",
    searchable_by=["Volcanion ex", "Basic", "ex", "Volcanionex"],
    subtypes=["Basic", "ex"],
    collector_number=31,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Ability(
            title="Scalding Steam",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may make your opponent's Active Pok\u00e9mon Burned.",
            effect=unimplemented,
        ),
        Attack(
            title="Scorching Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=energy_move_attack(1),
        ),
    ],
)