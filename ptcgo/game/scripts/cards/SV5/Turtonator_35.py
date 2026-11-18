from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="47ee0056-dc82-59aa-af73-fe54dbff3adf",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic", "Turtonator"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Attack(
            title="Spit-Out Shot",
            game_text="This attack does 40 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Steam Artillery",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)