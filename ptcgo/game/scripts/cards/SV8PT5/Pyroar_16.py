from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8fe81015-82e4-506d-80ab-ca446d600f77",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name",
    display_name="Pyroar",
    searchable_by=["Pyroar", "Stage 1", "Pyroar"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=667,
    abilities=[
        Attack(
            title="Fire Mane",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Flame Tackle",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)